# Commonly used type aliases.
# Everything in this module is private for stubs. There is no runtime
# equivalent.

from collections.abc import Mapping, Sequence
from typing import Any, TypeVar
from typing_extensions import TypeAlias

import numpy
import tensorflow as tf

_T1 = TypeVar("_T1")
ContainerGeneric: TypeAlias = Mapping[str, ContainerGeneric[_T1]] | Sequence[ContainerGeneric[_T1]] | _T1

TensorLike: TypeAlias = tf.Tensor | tf.RaggedTensor | tf.SparseTensor
Gradients: TypeAlias = tf.Tensor | tf.IndexedSlices

ContainerTensorsLike: TypeAlias = ContainerGeneric[TensorLike]
ContainerTensors: TypeAlias = ContainerGeneric[tf.Tensor]
ContainerGradients: TypeAlias = ContainerGeneric[Gradients]

AnyArray: TypeAlias = numpy.ndarray[Any, Any]
