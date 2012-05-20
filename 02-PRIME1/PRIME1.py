#!/usr/bin/env python

import math
import sys

def main():
  p = Prime()

  input = sys.stdin
  records = int(input.next().strip())
  for x in xrange(records):
    line = input.next().strip()
    start,stop = [int(n) for n in  line.split(' ')]
    print p.gen_output(start, stop)
    if x+1 != records:
      print ''

class Prime(object):
  def __init__(self):
    self.prime = {}
    self.filter_primes = [2,3,5,7]
    self.max_prime = self.filter_primes[-1]
    for n in self.filter_primes:
      self._insert_number(n)

  def max_filter_prime(self):
    return self.filter_primes[-1]

  def extend_filter_primes(self, new_limit):
    current = self.filter_primes[-1] + 2
    data = self.filter_primes + range(current, new_limit)
    while current < data[-1]:
      idx = data.index(current) + 1
      data = data[:idx] + [x for x in data[idx:] if x % current != 0]
      current = data[idx]
    self.filter_primes = data

  def isprime(self, n):
    if n in self.prime:
      return self.prime[n]
    else:
      self._insert_number(n)
      return self.prime[n]

  def _insert_number(self, n):
    is_prime = False
    for factor in self.filter_primes:
      if n % factor == 0: break
    else:
      is_prime = True
    self.prime[n] = is_prime

  def gen_output(self, start, stop):
    filter_upper_limit = int(math.ceil(math.sqrt(stop)))
    if filter_upper_limit > self.filter_primes[-1]:
      self.extend_filter_primes(filter_upper_limit)
    candidates = xrange(start, stop+1)
    return '\n'.join([str(x) for x in candidates if self.isprime(x)])

if __name__ == "__main__":
  main()
