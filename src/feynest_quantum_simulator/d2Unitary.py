import numpy as np
import math

class d2Unitary:
  """The simplest abstraction for the Quantum Equivalent of a bit"""
  def i(self):
    return np.eye(2)

  def x(self):
    pauli_x = np.array([[0, 1],
                        [1, 0]])
    return pauli_x
  
  def y(self):
    pauli_y = np.array([[0, -1j],
                        [1j, 0]])
    return pauli_y
    
  def z(self):
    pauli_z = np.array([[1, 0],
                        [0, -1]])
    return pauli_z
  
  def r_theta(self, theta):
    e = np.e**(1j*theta)
    r = np.array([[1, 0],
                  [0, e]])
    return r
  
  def control_u(self, u):
    c_u = np.eye(4, dtype=np.complex128)
    c_u[2:, 2:]
    c_u[2:, 2:] = np.copy(u)
    return c_u

  def tensor_product(self, u1, u2):
    if self.checkunitary(u1) and self.checkunitary(u2):
      return np.kron(u1, u2)
    else:
      raise ValueError(f"Oops! either {u1} or {u2} is not a aunitary matrix")
    
  def adjoint(self, operator):
    """The transpose conjugate of the operator"""
    operator_transpose = np.copy(operator.T)
    return np.real(operator_transpose) + (-1j)*np.imag(operator_transpose)
  
  def checkunitary(self, operator):
    """Check if the operator is a unitary matrix"""
    size = np.shape(operator)[0]
    UU_T = operator.dot(self.adjoint(operator))
    print(f"operator\n {operator},\n adjoint\n {self.adjoint(operator)}")
    return np.allclose(UU_T,np.eye(size))