## The feynest simulator

The feynest simulator (homage to the great physicist **Richard Feynman**) is a python package for simulating quantum circuits.

I took this project up to self-learn quantum computing within a span of 1 year (alongside my masters degree)

### Steps to create your own circuit using the feynest simulator

****
*Step 1:* Instantiate a GateGraph object. The line of code below creates a 4 qubit circuit.

```python
gg = GateGraph(4)
```

*Step 2*: Add gates. The numbers represent the qubit that you want to apply to gate to.

```python
  gg.insert_single_qubit_gate(1, "X")
  gg.insert_single_qubit_gate(2, "Y")
  gg.insert_two_qubit_gate(1, 0, "CX", np.array([[0, 1], [1, 0]]))
  gg.insert_single_qubit_gate(2, "Z")
  gg.insert_single_qubit_gate(3, "Z")
  gg.insert_single_qubit_gate(0, "Z")
```


*Step 3*: If you want, you can visualise the circuit using the command below.

```
gg.display_circuit()
```

**Output:**

────────────────────────────────────────────────────────────────────────────────────────────────────

|0>------------------Z#3--

|0>--X#1----CU#2---------

|0>--Y#1----Z#2-----------

|0>--Z#1------------------- 

