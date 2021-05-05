from uuid import uuid4

import numpy
import onnx

from onnx_model_maker import omm


def _add_input(target, inputs):
  if target is None:
    return
  if type(target) == numpy.ndarray:
    t = onnx.numpy_helper.from_array(target, f"_t_{uuid4().hex[:4]}")
    omm.model.graph.initializer.append(t)
    inputs.append(t.name)
  elif type(target) == str:
    inputs.append(target)
  elif type(target) == list:
    _add_list(target, inputs)
  elif type(target) == onnx.NodeProto:
    inputs.append(target.output[0])


def _add_list(target, inputs):
  for t in target:
    _add_input(t, inputs)
