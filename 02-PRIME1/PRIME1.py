#!/usr/bin/env python

import math
import sys

def main():
  p = Prime()
  input = sys.stdin
  records = int(input.next().strip())
  for _ in xrange(records):
    line = input.next().strip()
    start,stop = [int(n) for n in  line.split(' ')]
    p.print_range(start, stop)

class Prime(object):
  def __init__(self, upper_limit=1000000000):
    self.prime = {}
    self.upper_limit = upper_limit
    self.factor_limit = int(math.ceil(math.sqrt(upper_limit)))
    self._populate_filter_primes()

  def _populate_filter_primes(self):

    self.filter_primes = self._primes(self.factor_limit)

    for num in range(self.factor_limit):
      self.prime[num] = False

    for num in self.filter_primes:
      self.prime[num] = True

  @staticmethod
  def _primes(n):
    factor_limit = int(math.ceil(math.sqrt(n)))
    current = 2
    data = range(2, n)
    while current < factor_limit:
      idx = data.index(current) + 1
      data = data[:idx] + [x for x in data[idx:] if x % current != 0]
      current = data[idx]
    return data

  def isprime(self, n):
    if n not in self.prime:
      self._insert_number(n)
    return self.prime[n]

  def _insert_number(self, n):
    is_prime = False
    for factor in self.filter_primes:
      if n % factor == 0: break
    else:
      is_prime = True
    self.prime[n] = is_prime

  def print_range(self, start, stop):
    for n in xrange(start, stop+1):
      if self.isprime(n):
        print n
    print ''

if __name__ == "__main__":
  main()
