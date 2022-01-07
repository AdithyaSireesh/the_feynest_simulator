class SingleQubitGateNode:
  def __init__(self, gate, qubit_number, operation_number=0):
#     GateNode.__init__(self, gate_type=1, operation_number=operation_number)
    self.gate_type=1
    self.operation_number=operation_number
    self.gate = gate
    self.qubit_number = qubit_number
    self.next_gate_node = None