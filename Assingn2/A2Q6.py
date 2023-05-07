import random
num_friends = [random.randint(1,100) for _ in range(50)]

def _median_odd(xs:list)->float:
  # if len is odd median is the middle element
  return sorted(xs)[len(xs)//2]

def _median_even(xs:list)->float:
  # if the length is even the average is middle two elements
  sorted_xs = sorted(xs)
  mid = len(xs)//2
  return (sorted_xs[mid-1]+sorted_xs[mid])/2

if len(num_friends)%2==0:
  print(_median_even(num_friends))
else:
  print(_median_odd(num_friends))
