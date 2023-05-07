def component_wise_mean(v1:list, v2:list)->list:
  return[(v_i+w_i)//2 for v_i,w_i in zip(v1,v2)]

v1 = [int(x) for x in input("Enter first vector: ").split()]
v2 = [int(x) for x in input("Enter second vector: ").split()]
assert len(v1)==len(v2) , "the length of vectors must be equal"

print(component_wise_mean(v1,v2))

