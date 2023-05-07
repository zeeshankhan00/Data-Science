from typing import Callable
from typing import List
Matrix = List[List[float]]
def make_matrix(num_rows:int, num_cols: int, entry_fn: Callable[[int,int],float])->Matrix:
  return [[entry_fn(i,j) for j in range(num_cols)] for i in range(num_rows)]

rows = int(input("Enter the number of rows:"))
cols = int(input("Enter the number of cols:"))
print(make_matrix(rows,cols,lambda i,j:i+j))
