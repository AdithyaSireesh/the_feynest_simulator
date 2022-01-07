import numpy as np
import math

class Qubit:
  """The simplest abstraction for the Quantum Equivalent of a bit"""
  def __init__(self, a, b):
    a_probability = np.absolute(a)
    b_probability = np.absolute(b)
    total_probability = a_probability**2 + b_probability**2
    print(total_probability, a_probability, b_probability, a, b)
    if math.isclose(total_probability, 1):
      self.a = a
      self.b = b
      
    
  def display(self):
    "display the qubit"
    print(f"{self.a}|0> + {self.b}|1>")