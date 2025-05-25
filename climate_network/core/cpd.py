"""Conditional probability distributions for linear-Gaussian nodes."""

from typing import Sequence

import numpy as np


class LinearGaussianCPD:
    """Conditional probability distribution for a linear-Gaussian node.

    Attributes
    ----------
    beta : ndarray, shape (k+1,)
        Regression coefficients, where beta[0] is the intercept and
        beta[1:] correspond to the node's parents in order.
    sigma : float
        Standard deviation of the Gaussian noise term.

    """

    def __init__(self, beta: Sequence[float], sigma: float) -> None:
        """Initialize a LinearGaussianCPD with regression coeffs and noise std.

        Parameters
        ----------
        beta : Sequence[float]
            Regression coefficients.
        sigma : float
            Standard deviation of the Gaussian noise term (must be positive).

        """
        # Convert beta to a NumPy array and validate that it is one-dimensional
        self.beta = np.asarray(beta, dtype=float)
        if self.beta.ndim != 1:
            error_msg = "`beta` must be a 1-D sequence of floats."
            raise ValueError(error_msg)
        # Validate that sigma is a positive number
        if sigma <= 0:
            error_msg = "`sigma` must be positive."
            raise ValueError(error_msg)
        self.sigma = float(sigma)
