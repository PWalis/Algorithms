#!/usr/bin/python

import sys
def list_maker(list0):
  # Create copies of the passed in list and add rock papaer and scissors to them 
  # slice notaion can be used to truly copy lists
  listA, listB, listC = (list0[:] for i in range(3))
  listA.append('rock')
  listB.append('paper')
  listC.append('scissors')
  return [listA, listB, listC]

def rock_paper_scissors(n):
  rps_list = []
  # if n is 0 return empty nested list
  if n == 0:
    return [rps_list]
  # N determines how many times to loop
  for i in range(n):
    # Fist loop populates rps_list
    if i == 0:
      for t in list_maker(rps_list):
        rps_list.append(t)
    # every loop after takes the rps_list and calls list_maker on each item
    else:
      new_list = []
      for t in rps_list:
        for lt in list_maker(t):
          new_list.append(lt)
      rps_list = new_list[:]
  return rps_list


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')