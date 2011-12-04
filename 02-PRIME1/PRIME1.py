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
    return tuple(data)

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
    if stop <= self.factor_limit:
      return self._gen_static_output(start, stop)
    elif start < self.last_filter_prime:
      first = self._gen_static_output(start,stop)
      candidates = xrange(self.last_filter_prime+2, stop+1, 2)
      second = self._gen_upper_output(candidates)
      return '\n'.join((first, second))
    elif self.last_filter_prime < start:
      if start % 2 == 0: start = start+1
      candidates = xrange(start, stop+1, 2)
      return self._gen_upper_output(candidates)
    else:
      raise Exception("Should not have got here!")

  def _gen_static_output(self, start, stop):
    return '\n'.join([str(x) for x in self.filter_primes if start <= x <= stop])

  def _gen_upper_output(self, candidates):
    return '\n'.join([str(x) for x in candidates if self.isprime(x)])

if __name__ == "__main__":
  main()
