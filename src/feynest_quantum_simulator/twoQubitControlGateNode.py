import numpy as np

class TwoQubitControlGateNode:
  def __init__(self, gate, q1, q2, operation_number=0, gate_mat=np.eye(2)):
#     GateNode.__init__(self, gate_type=2, operation_number=operation_number)
    self.gate_type=2
    self.operation_number=operation_number
    self.gate = gate
    self.gate_mat = gate_mat
    self.control_qubit = q1
    self.target_qubit = q2
    self.next_gate_node = None