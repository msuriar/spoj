#!/usr/bin/env python

import math
import sys

def main():
  input = sys.stdin
  records = int(input.next().strip())
  for _ in xrange(records):
    line = input.next().strip()
    start,stop = [int(n) for n in  line.split(' ')]
    output_primes(start, stop)

def output_filter_primes(start,stop):
  for n in [x for x in FILTER_PRIMES if start <= x <= stop]:
    print n

def output_primes(start,stop):
  if (stop <= UPPER_FACTOR_LIMIT):
    output_filter_primes(start,stop)
  elif (start < LAST_FILTER_PRIME):
    output_filter_primes(start,stop)
    candidates = xrange(LAST_FILTER_PRIME+2, stop+1, 2)
    for n in candidates:
      for factor in FILTER_PRIMES:
        if n % factor == 0: break
      else: print n
  elif (LAST_FILTER_PRIME < start):
    if start % 2  == 0: start = start+1
    candidates = xrange(start, stop+1, 2)
    for n in candidates:
      for factor in FILTER_PRIMES:
        if n % factor == 0: break
      else: print n
  print ''
      
    

def slow_primes(n):
  """Uses sieve of eratosthenes. Use to calculate primes up to limit of
  possible square roots of primes, then use this list as a base to factor
  larger data sets."""
  factor_limit = int(math.ceil(math.sqrt(n)))
  current = 2
  data = range(2, n)
  while current < factor_limit:
    idx = data.index(current) + 1
    data = data[:idx] + [x for x in data[idx:] if x % current != 0]
    current = data[idx]
  return data

if __name__ == "__main__":
  UPPER_FACTOR_LIMIT = int(math.ceil(math.sqrt(1E9)))
  FILTER_PRIMES = slow_primes(UPPER_FACTOR_LIMIT)
  LAST_FILTER_PRIME = FILTER_PRIMES[-1]
  main()
