"""Linear Gaussian Bayesian Network implementation."""

from __future__ import annotations

from typing import Bool, Dict, List, Mapping, Sequence, Set

import numpy as np
from cpd import LinearGaussianCPD


class DAGError(Exception):
    """Exception raised when adding an edge creates a cycle in the DAG."""


class LinearGaussianBN:
    """Linear Gaussian Bayesian Network class.

    Public API:
      - add_node(name: str)
      - add_edge(parent: str, child: str)
      - set_cpd(node: str, beta: Sequence[float], sigma: float)
      - sample(n_samples: int, rng: np.random.Generator | None = None) -> Dict[str, ndarray]
      - log_likelihood(data: Mapping[str, ndarray]) -> float
    """

    def __init__(self) -> None:
        """Initialize empty network with no nodes or CPDs."""
        self._parents: Dict[str, List[str]] = {}
        self._children: Dict[str, List[str]] = {}
        self._cpd: Dict[str, LinearGaussianCPD] = {}

    def add_node(self, name: str) -> None:
        """Add a new node to the network."""
        if name in self._parents:
            msg = f"Node '{name}' already exists."
            raise ValueError(msg)
        self._parents[name] = []
        self._children[name] = []

    def add_edge(self, parent: str, child: str) -> None:
        """Add a directed edge parent -> child, ensuring no cycle is created.

        Raises
        ------
        KeyError: if parent or child does not exist.
        ValueError: if the edge already exists.
        DAGError: if adding the edge creates a cycle.

        """
        if parent not in self._parents or child not in self._parents:
            msg = "Both parent and child must be existing nodes."
            raise KeyError(msg)
        if child in self._children[parent]:
            msg = f"Edge {parent}->{child} already exists."
            raise ValueError(msg)
        # Speculative add
        self._parents[child].append(parent)
        self._children[parent].append(child)
        # Check for cycle
        if self._detect_cycle():
            # Rollback
            self._parents[child].remove(parent)
            self._children[parent].remove(child)
            msg = f"Adding edge {parent}->{child} creates a cycle."
            raise DAGError(msg)

    def _detect_cycle(self) -> Bool:
        """Detect if the current graph has a cycle.

        Returns
        -------
        True if a cycle is found, False otherwise.

        """
        visited: set[str] = Set()
        stack: set[str] = Set()

        def dfs(v: str) -> Bool:
            visited.add(v)
            stack.add(v)
            for w in self._children[v]:
                if w not in visited:
                    if dfs(w):
                        return True
                elif w in stack:
                    return True
            stack.remove(v)
            return False

        return any(node not in visited and dfs(node) for node in self._parents)
