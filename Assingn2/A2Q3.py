from typing import Tuple
from typing import List
Matrix = List[List[float]]

def get_row(A: Matrix, i: int)-> Vector:
  return A[i]
def get_col(A:Matrix, i:int)-> Vector:
  return[A_i[j] for A_i in A]
