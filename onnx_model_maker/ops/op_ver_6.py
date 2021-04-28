# Autogenerated by onnx-model-maker. Don't modify it manually.

import onnx
import onnx.helper
import onnx.numpy_helper
from onnx_model_maker import omm
from onnx_model_maker import onnx_mm_export
from onnx_model_maker.ops.op_helper import _add_input


@onnx_mm_export("v6.Floor")
def Floor(X, **kwargs):
  _inputs = []
  for i in (X, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Floor"]
  omm.op_counter["Floor"] += 1
  node = onnx.helper.make_node("Floor",
                               _inputs, [f"_t_Floor_{idx}"],
                               name=f"Floor_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v6.Tile")
def Tile(input, repeats, **kwargs):
  _inputs = []
  for i in (input, repeats):
    _add_input(i, _inputs)

  idx = omm.op_counter["Tile"]
  omm.op_counter["Tile"] += 1
  node = onnx.helper.make_node("Tile",
                               _inputs, [f"_t_Tile_{idx}"],
                               name=f"Tile_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v6.Sub")
def Sub(A, B, **kwargs):
  _inputs = []
  for i in (A, B):
    _add_input(i, _inputs)

  idx = omm.op_counter["Sub"]
  omm.op_counter["Sub"] += 1
  node = onnx.helper.make_node("Sub",
                               _inputs, [f"_t_Sub_{idx}"],
                               name=f"Sub_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v6.Sqrt")
def Sqrt(X, **kwargs):
  _inputs = []
  for i in (X, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Sqrt"]
  omm.op_counter["Sqrt"] += 1
  node = onnx.helper.make_node("Sqrt",
                               _inputs, [f"_t_Sqrt_{idx}"],
                               name=f"Sqrt_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v6.Max")
def Max(data_0, **kwargs):
  _inputs = []
  for i in (data_0, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Max"]
  omm.op_counter["Max"] += 1
  node = onnx.helper.make_node("Max",
                               _inputs, [f"_t_Max_{idx}"],
                               name=f"Max_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v6.Tanh")
def Tanh(input, **kwargs):
  _inputs = []
  for i in (input, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Tanh"]
  omm.op_counter["Tanh"] += 1
  node = onnx.helper.make_node("Tanh",
                               _inputs, [f"_t_Tanh_{idx}"],
                               name=f"Tanh_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v6.Selu")
def Selu(X, **kwargs):
  _inputs = []
  for i in (X, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Selu"]
  omm.op_counter["Selu"] += 1
  node = onnx.helper.make_node("Selu",
                               _inputs, [f"_t_Selu_{idx}"],
                               name=f"Selu_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v6.Sum")
def Sum(data_0, **kwargs):
  _inputs = []
  for i in (data_0, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Sum"]
  omm.op_counter["Sum"] += 1
  node = onnx.helper.make_node("Sum",
                               _inputs, [f"_t_Sum_{idx}"],
                               name=f"Sum_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v6.Relu")
def Relu(X, **kwargs):
  _inputs = []
  for i in (X, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Relu"]
  omm.op_counter["Relu"] += 1
  node = onnx.helper.make_node("Relu",
                               _inputs, [f"_t_Relu_{idx}"],
                               name=f"Relu_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v6.Reciprocal")
def Reciprocal(X, **kwargs):
  _inputs = []
  for i in (X, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Reciprocal"]
  omm.op_counter["Reciprocal"] += 1
  node = onnx.helper.make_node("Reciprocal",
                               _inputs, [f"_t_Reciprocal_{idx}"],
                               name=f"Reciprocal_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v6.Mul")
def Mul(A, B, **kwargs):
  _inputs = []
  for i in (A, B):
    _add_input(i, _inputs)

  idx = omm.op_counter["Mul"]
  omm.op_counter["Mul"] += 1
  node = onnx.helper.make_node("Mul",
                               _inputs, [f"_t_Mul_{idx}"],
                               name=f"Mul_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v6.Sigmoid")
def Sigmoid(X, **kwargs):
  _inputs = []
  for i in (X, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Sigmoid"]
  omm.op_counter["Sigmoid"] += 1
  node = onnx.helper.make_node("Sigmoid",
                               _inputs, [f"_t_Sigmoid_{idx}"],
                               name=f"Sigmoid_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v6.Neg")
def Neg(X, **kwargs):
  _inputs = []
  for i in (X, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Neg"]
  omm.op_counter["Neg"] += 1
  node = onnx.helper.make_node("Neg",
                               _inputs, [f"_t_Neg_{idx}"],
                               name=f"Neg_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v6.Mean")
def Mean(data_0, **kwargs):
  _inputs = []
  for i in (data_0, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Mean"]
  omm.op_counter["Mean"] += 1
  node = onnx.helper.make_node("Mean",
                               _inputs, [f"_t_Mean_{idx}"],
                               name=f"Mean_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v6.Log")
def Log(input, **kwargs):
  _inputs = []
  for i in (input, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Log"]
  omm.op_counter["Log"] += 1
  node = onnx.helper.make_node("Log",
                               _inputs, [f"_t_Log_{idx}"],
                               name=f"Log_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v6.LeakyRelu")
def LeakyRelu(X, **kwargs):
  _inputs = []
  for i in (X, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["LeakyRelu"]
  omm.op_counter["LeakyRelu"] += 1
  node = onnx.helper.make_node("LeakyRelu",
                               _inputs, [f"_t_LeakyRelu_{idx}"],
                               name=f"LeakyRelu_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v6.BatchNormalization")
def BatchNormalization(X, scale, B, mean, var, **kwargs):
  _inputs = []
  for i in (X, scale, B, mean, var):
    _add_input(i, _inputs)

  idx = omm.op_counter["BatchNormalization"]
  omm.op_counter["BatchNormalization"] += 1
  node = onnx.helper.make_node("BatchNormalization",
                               _inputs, [f"_t_BatchNormalization_{idx}"],
                               name=f"BatchNormalization_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v6.Cast")
def Cast(input, **kwargs):
  _inputs = []
  for i in (input, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Cast"]
  omm.op_counter["Cast"] += 1
  node = onnx.helper.make_node("Cast",
                               _inputs, [f"_t_Cast_{idx}"],
                               name=f"Cast_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v6.InstanceNormalization")
def InstanceNormalization(input, scale, B, **kwargs):
  _inputs = []
  for i in (input, scale, B):
    _add_input(i, _inputs)

  idx = omm.op_counter["InstanceNormalization"]
  omm.op_counter["InstanceNormalization"] += 1
  node = onnx.helper.make_node("InstanceNormalization",
                               _inputs, [f"_t_InstanceNormalization_{idx}"],
                               name=f"InstanceNormalization_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v6.Clip")
def Clip(input, **kwargs):
  _inputs = []
  for i in (input, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Clip"]
  omm.op_counter["Clip"] += 1
  node = onnx.helper.make_node("Clip",
                               _inputs, [f"_t_Clip_{idx}"],
                               name=f"Clip_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v6.PRelu")
def PRelu(X, slope, **kwargs):
  _inputs = []
  for i in (X, slope):
    _add_input(i, _inputs)

  idx = omm.op_counter["PRelu"]
  omm.op_counter["PRelu"] += 1
  node = onnx.helper.make_node("PRelu",
                               _inputs, [f"_t_PRelu_{idx}"],
                               name=f"PRelu_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v6.HardSigmoid")
def HardSigmoid(X, **kwargs):
  _inputs = []
  for i in (X, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["HardSigmoid"]
  omm.op_counter["HardSigmoid"] += 1
  node = onnx.helper.make_node("HardSigmoid",
                               _inputs, [f"_t_HardSigmoid_{idx}"],
                               name=f"HardSigmoid_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v6.Elu")
def Elu(X, **kwargs):
  _inputs = []
  for i in (X, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Elu"]
  omm.op_counter["Elu"] += 1
  node = onnx.helper.make_node("Elu",
                               _inputs, [f"_t_Elu_{idx}"],
                               name=f"Elu_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v6.Exp")
def Exp(input, **kwargs):
  _inputs = []
  for i in (input, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Exp"]
  omm.op_counter["Exp"] += 1
  node = onnx.helper.make_node("Exp",
                               _inputs, [f"_t_Exp_{idx}"],
                               name=f"Exp_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v6.Add")
def Add(A, B, **kwargs):
  _inputs = []
  for i in (A, B):
    _add_input(i, _inputs)

  idx = omm.op_counter["Add"]
  omm.op_counter["Add"] += 1
  node = onnx.helper.make_node("Add",
                               _inputs, [f"_t_Add_{idx}"],
                               name=f"Add_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v6.Min")
def Min(data_0, **kwargs):
  _inputs = []
  for i in (data_0, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Min"]
  omm.op_counter["Min"] += 1
  node = onnx.helper.make_node("Min",
                               _inputs, [f"_t_Min_{idx}"],
                               name=f"Min_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v6.Div")
def Div(A, B, **kwargs):
  _inputs = []
  for i in (A, B):
    _add_input(i, _inputs)

  idx = omm.op_counter["Div"]
  omm.op_counter["Div"] += 1
  node = onnx.helper.make_node("Div",
                               _inputs, [f"_t_Div_{idx}"],
                               name=f"Div_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v6.Dropout")
def Dropout(data, **kwargs):
  _inputs = []
  for i in (data, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Dropout"]
  omm.op_counter["Dropout"] += 1
  node = onnx.helper.make_node("Dropout",
                               _inputs, [f"_t_Dropout_{idx}"],
                               name=f"Dropout_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v6.Ceil")
def Ceil(X, **kwargs):
  _inputs = []
  for i in (X, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Ceil"]
  omm.op_counter["Ceil"] += 1
  node = onnx.helper.make_node("Ceil",
                               _inputs, [f"_t_Ceil_{idx}"],
                               name=f"Ceil_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v6.Abs")
def Abs(X, **kwargs):
  _inputs = []
  for i in (X, ):
    _add_input(i, _inputs)

  idx = omm.op_counter["Abs"]
  omm.op_counter["Abs"] += 1
  node = onnx.helper.make_node("Abs",
                               _inputs, [f"_t_Abs_{idx}"],
                               name=f"Abs_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node


@onnx_mm_export("v6.Gemm")
def Gemm(A, B, C, **kwargs):
  _inputs = []
  for i in (A, B, C):
    _add_input(i, _inputs)

  idx = omm.op_counter["Gemm"]
  omm.op_counter["Gemm"] += 1
  node = onnx.helper.make_node("Gemm",
                               _inputs, [f"_t_Gemm_{idx}"],
                               name=f"Gemm_{idx}",
                               **kwargs)
  onnx.checker.check_node(node, omm.ctx)
  omm.model.graph.node.append(node)
  return node
