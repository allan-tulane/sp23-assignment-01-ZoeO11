"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x<= 1:
      return x
    else:
      ra = foo((x-1))
      rb = foo((x-2))
      return ra + rb

def longest_run(mylist, key):
  c1 = 0
  c2 = 0
  for i in mylist:
      if i == key:
        c1 += 1
      if (c1>0) and (i != key) and (c1 > c2):
        c2 = c1
        c1 = 0
  if c1 > c2:
    return c1
  else:
    return c2


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))

def longest_run_recursive_help(mylist, key):
  if len(mylist) == 1:
    if mylist[0] == key:
      return Result(1,1,1,True)
    else:
      return Result(0,0,0,False)
    
  else:
      r = mylist[(len(mylist)//2):]
      l = mylist[:(len(mylist)//2)]
      right = longest_run_recursive_help(r,key)
      left = longest_run_recursive_help(l,key)

      if right.is_entire_range:
        if left.is_entire_range:
          sum = right.longest_size + left.longest_size
          return Result(sum,sum,sum,True)
        else:
          if right.longest_size >= (left.right_size + right.left_size):
            sum = right.longest_size
          else: sum = (left.right_size + right.left_size)
        return Result(left.left_size, right.right_size + left.right_size, sum, False)
      elif left.is_entire_range:
        if left.longest_size < (right.left_size + left.longest_size):
          sum = left.longest_size + right.left_size
        else:
          sum = left.longest_size
        return Result(left.left_size + right.left_size,right.right_size, sum, False)
      else:
        if (left.right_size + right.left_size) < left.longest_size:
          sum = left.longest_size
        elif (left.right_size + right.left_size) < right.longest_size:
          sum = right.longest_size
        else:
          sum = right.left_size + left.right_size
        return Result(left.left_size, right.right_size, sum, False)
  
    
def longest_run_recursive(mylist, key):
  return longest_run_recursive_help(mylist,key).longest_size