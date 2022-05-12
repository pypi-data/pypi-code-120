"""Implementation of the `Space` metaclass."""
from __future__ import annotations

from typing import Generic, Iterable, Mapping, Optional, Sequence, Type, TypeVar

import numpy as np

from dishpill.utils import seeding

T_cov = TypeVar("T_cov", covariant=True)


class Space(Generic[T_cov]):
    """Superclass that is used to define observation and action spaces.

    Spaces are crucially used in dishpill to define the format of valid actions and observations.
    They serve various purposes:

    * They clearly define how to interact with environments, i.e. they specify what actions need to look like and what observations will look like
    * They allow us to work with highly structured data (e.g. in the form of elements of :class:`Dict` spaces) and painlessly transform them into flat arrays that can be used in learning code
    * They provide a method to sample random elements. This is especially useful for exploration and debugging.
    """

    def __init__(
        self,
        shape: Optional[Sequence[int]] = None,
        dtype: Optional[Type | str] = None,
        seed: Optional[int | seeding.RandomNumberGenerator] = None,
    ):
        """Constructor of :class:`Space`.

        Args:
            shape (Optional[Sequence[int]]): If elements of the space are numpy arrays, this should specify their shape.
            dtype (Optional[Type | str]): If elements of the space are numpy arrays, this should specify their dtype.
            seed: Optionally, you can use this argument to seed the RNG that is used to sample from the space
        """
        self._shape = None if shape is None else tuple(shape)
        self.dtype = None if dtype is None else np.dtype(dtype)
        self._np_random = None
        if seed is not None:
            if isinstance(seed, seeding.RandomNumberGenerator):
                self._np_random = seed
            else:
                self.seed(seed)

    @property
    def np_random(self) -> seeding.RandomNumberGenerator:
        """Lazily seed the PRNG since this is expensive and only needed if sampling from this space."""
        if self._np_random is None:
            self.seed()

        return self._np_random  # type: ignore  ## self.seed() call guarantees right type.

    @property
    def shape(self) -> Optional[tuple[int, ...]]:
        """Return the shape of the space as an immutable property."""
        return self._shape

    def sample(self) -> T_cov:
        """Randomly sample an element of this space. Can be uniform or non-uniform sampling based on boundedness of space."""
        raise NotImplementedError

    def seed(self, seed: Optional[int] = None) -> list:
        """Seed the PRNG of this space and possibly the PRNGs of subspaces."""
        self._np_random, seed = seeding.np_random(seed)
        return [seed]

    def contains(self, x) -> bool:
        """Return boolean specifying if x is a valid member of this space."""
        raise NotImplementedError

    def __contains__(self, x) -> bool:
        """Return boolean specifying if x is a valid member of this space."""
        return self.contains(x)

    def __setstate__(self, state: Iterable | Mapping):
        """Used when loading a pickled space.

        This method was implemented explicitly to allow for loading of legacy states.
        """
        # Don't mutate the original state
        state = dict(state)

        # Allow for loading of legacy states.
        if "shape" in state:
            state["_shape"] = state["shape"]
            del state["shape"]
        if "np_random" in state:
            state["_np_random"] = state["np_random"]
            del state["np_random"]

        # Update our state
        self.__dict__.update(state)

    def to_jsonable(self, sample_n: Sequence[T_cov]) -> list:
        """Convert a batch of samples from this space to a JSONable data type."""
        # By default, assume identity is JSONable
        return list(sample_n)

    def from_jsonable(self, sample_n: list) -> list[T_cov]:
        """Convert a JSONable data type to a batch of samples from this space."""
        # By default, assume identity is JSONable
        return sample_n
