import numpy as np
from singleQubitGateNode import SingleQubitGateNode
from twoQubitControlGateNode import TwoQubitControlGateNode

class GateGraph:
  
  def __init__(self, number_of_qubits):
    self.qubit_gate_nodes = self.fill_circuit(number_of_qubits)
    self.current_qubit_gate_nodes = [node for node in self.qubit_gate_nodes]
    self.operation_number = [0 for _ in range(number_of_qubits)]
    
    
  def fill_circuit(self, number_of_qubits):
    qubit_gate_nodes = []
    operation_number=0
    for i in range(number_of_qubits):
      qubit_gate_nodes.append(SingleQubitGateNode(gate="I", qubit_number=i, operation_number=operation_number))
    return qubit_gate_nodes
      
  def insert_single_qubit_gate(self, qubit_number, gate):
    self.operation_number[qubit_number]+=1
    new_gate_node = SingleQubitGateNode(gate=gate, qubit_number=qubit_number, 
                             operation_number=self.operation_number[qubit_number])    
    self.current_qubit_gate_nodes[qubit_number].next_gate_node = new_gate_node
    self.current_qubit_gate_nodes[qubit_number]=new_gate_node
    return
  
  def insert_two_qubit_gate(self, q1, q2, gate="2Q", gate_mat=np.eye(2)):
    ops_number_q1 = self.operation_number[q1]
    ops_number_q2 = self.operation_number[q2]
    ops_number = max(ops_number_q1, ops_number_q2)
    lower = min(q1, q2)
    upper = max(q1, q2)
    max_ops_number_in_range = ops_number
    for i in range(lower, upper+1, 1):
      max_ops_number_in_range=max(max_ops_number_in_range, self.current_qubit_gate_nodes[i].operation_number)
    for i in range(lower, upper+1, 1):
      self.operation_number[i]=max_ops_number_in_range+1
    new_gate_node = TwoQubitControlGateNode(gate=gate, q1=q1, q2=q2, 
                             operation_number=self.operation_number[q1], gate_mat=gate_mat)
    
    self.current_qubit_gate_nodes[q1].next_gate_node = new_gate_node
    self.current_qubit_gate_nodes[q1]=new_gate_node
    return

  def display_circuit(self):
    print('─' * 100)
    print('─' * 100)
    for idx, qubit_gate in enumerate(self.qubit_gate_nodes):
      print(f"|0>", end="")
      next_gate_for_qubit_i = qubit_gate.next_gate_node
      current_iter_number = 0
      while next_gate_for_qubit_i:
        for i in range(current_iter_number, next_gate_for_qubit_i.operation_number-1):
          print(f"--   --", end="")
        print(f"--{next_gate_for_qubit_i.gate}#{next_gate_for_qubit_i.operation_number}--", end="")
        current_iter_number=next_gate_for_qubit_i.operation_number
        next_gate_for_qubit_i=next_gate_for_qubit_i.next_gate_node
      print("\n") 


def main():
  gg = GateGraph(4)
  gg.insert_single_qubit_gate(1, "X")
  gg.insert_single_qubit_gate(2, "Y")
  gg.insert_two_qubit_gate(1, 0, "CU")
  gg.insert_single_qubit_gate(2, "U")
  gg.insert_single_qubit_gate(3, "U")
  gg.insert_single_qubit_gate(0, "U")
  gg.display_circuit()


  for i in range(4):
    gg.insert_two_qubit_gate(i, 3-i, "CZ")
  gg.display_circuit()

if __name__ == "__main__":
    main()