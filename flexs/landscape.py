import abc

from typing import List, Union
import numpy as np

SEQUENCES_TYPE = Union[List[str], np.ndarray]


class Landscape(abc.ABC):
    def __init__(self, name: str):
        self.cost = 0
        self.name = name

    @abc.abstractmethod
    def _fitness_function(self, sequences: SEQUENCES_TYPE) -> np.ndarray:
        pass

    def get_fitness(self, sequences: SEQUENCES_TYPE) -> np.ndarray:
        """
        Args:
            sequences: A list/numpy array of sequence strings to be scored

        Returns:
            np.ndarray(float): Scores for each sequence
        """

        self.cost += len(sequences)
        return self._fitness_function(sequences)
