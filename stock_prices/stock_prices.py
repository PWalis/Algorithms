#!/usr/bin/python

import argparse

def find_max_profit(prices):
  dif_list = []
  for subtract in range(len(prices)):
    for price in prices[subtract+1:]:
      dif_list.append(price - prices[subtract])
  return max(dif_list)

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))