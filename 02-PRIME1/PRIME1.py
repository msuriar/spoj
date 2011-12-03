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
    p.print_range(start, stop)
    if x+1 != records:
      print ''


class Prime(object):
  def __init__(self, upper_limit=1000000000):
    self.prime = {}
    self.upper_limit = upper_limit
    self.factor_limit = int(math.ceil(math.sqrt(upper_limit)))
    self._populate_filter_primes()

  def _populate_filter_primes(self):
    self.filter_primes = self._primes(self.factor_limit)
    self.last_filter_prime = self.filter_primes[-1]

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

  def print_range(self, start, stop):
    if stop <= self.factor_limit:
      self._print_static_range(start, stop)
    elif start < self.last_filter_prime:
      self._print_static_range(start,stop)
      candidates = xrange(self.last_filter_prime+2, stop+1, 2)
      self._print_upper_range(candidates)
    elif self.last_filter_prime < start:
      if start % 2 == 0: start = start+1
      candidates = xrange(start, stop+1, 2)
      self._print_upper_range(candidates)
    else:
      raise Exception("Should not have got here!")


  def _print_static_range(self, start, stop):
    for n in [ x for x in self.filter_primes if start <= x <= stop]:
        print n

  def _print_upper_range(self, candidates):
    for n in candidates:
      if self.isprime(n):
        print n

if __name__ == "__main__":
  main()
