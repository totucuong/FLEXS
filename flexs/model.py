import abc
from typing import Any, List

import numpy as np

import flexs
from flexs.landscape import SEQUENCES_TYPE


class Model(flexs.Landscape, abc.ABC):
    """

    Base model class. Inherits from `flexs.Landscape` and adds an additional
    `train` method.

    """

    @abc.abstractmethod
    def train(self, sequences: SEQUENCES_TYPE, labels: List[Any]):
        """
        Train model.

        This function is called whenever you would want your model to update itself
        based on the set of sequences it has measurements for.

        """

        pass


class LandscapeAsModel(flexs.Model):
    """
    This simple class wraps a `flexs.Landscape` in a `flexs.Model` to allow
    running experiments against a perfect model.

    """

    def __init__(self, landscape: flexs.Landscape):
        super().__init__(f"LandscapeAsModel={landscape.name}")
        self.landscape = landscape

    def _fitness_function(self, sequences: SEQUENCES_TYPE) -> np.ndarray:
        return self.landscape._fitness_function(sequences)

    def train(self, sequences: SEQUENCES_TYPE, labels: List[Any]):
        """No-op."""

        pass
