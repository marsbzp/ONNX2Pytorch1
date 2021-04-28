import logging

import onnx
import onnx.numpy_helper
import torch

import glob
import os

modules = glob.glob(os.path.join(os.path.dirname(__file__), "*.py"))
__all__ = [
    os.path.basename(f)[:-3]
    for f in modules
    if os.path.isfile(f) and not f.endswith('__init__.py')
] + ["get_op_code_generator"]


class OpCodeGenerator:

  def __init__(self,
               onnx_ver=onnx.defs.onnx_opset_version(),
               torch_ver=torch.__version__):
    self.onnx_ver = onnx_ver
    self.torch_ver = torch_ver
    self.onnx_op = self.__class__.__name__.replace("OpCodeGenerator", "")
    self.schema = onnx.defs.get_schema(self.onnx_op,
                                       max_inclusive_version=onnx_ver)
    if self.schema is not None:
      self.attr_default = {}
      for a, i in self.schema.attributes.items():
        try:
          default_value = onnx.helper.get_attribute_value(i.default_value)
          self.attr_default[a] = default_value
        except Exception as e:
          logging.warning(
              f"Cannot get default value for {a} of {self.onnx_op}.")

  def gen(self, node, value_infos, initializers):
    raise Exception

  def get_attr_value_dict(self, node):
    attr_value_dict = {}
    for a in node.attribute:
      attr_value_dict[a.name] = onnx.helper.get_attribute_value(a)
    attr_value_dict = dict(
        list(self.attr_default.items()) + list(attr_value_dict.items()))
    return attr_value_dict

  def gen_input_output_string(self,
                              node,
                              initializers,
                              input_num=None,
                              output_num=None):
    inputs_str, outputs_str = [], []
    input_num, output_num = input_num or len(node.input), output_num or len(
        node.output)
    for n, f, ls in ((input_num, node.input, inputs_str),
                     (output_num, node.output, outputs_str)):
      for i in range(n):
        ls.append("self.{}".format(f[i]) if f[i] not in
                  initializers else "self.__variables[\"{}\"]".format(f[i]))
    return inputs_str, outputs_str

  def gen_params_str(self, **kwargs):
    params = []
    for k, v in kwargs.items():
      v_str = v if type(v) == str else v.__repr__()
      params.append(f"'{k}': {v_str}")
    return ', '.join(params).__repr__()[1:-1]


__op_gen_dict = {}


def get_op_code_generator(op, **kwargs):
  op_code_gen_name = "{}OpCodeGenerator".format(op)
  if op_code_gen_name in __op_gen_dict:
    return __op_gen_dict[op_code_gen_name]
  mod = globals().get(op, None)
  if mod is None:
    return None
  __op_gen_dict[op_code_gen_name] = getattr(mod, op_code_gen_name)(**kwargs)
  return __op_gen_dict[op_code_gen_name]
