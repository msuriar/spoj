#!/usr/bin/env python

import math
import sys

# Find all primes up to sqrt(n)
# For each prime p
## Find largest multiple of p smaller than m (m/p*p)
## Increment up through array by increments of p, setting "prime" to false

# Return list of items which still have prime=trueo


def main():
  FILTER_PRIMES = gen_primes(100000)
  input = sys.stdin
  records = int(input.next().strip())

def primes(m, n):
  """Return all primes between m and n.

  Args:
    m, n integers
  Returns:
    A list of integers
  """
  num_candidates = n-m
  candidates = [ True ] * num_candidates
  largest_prime = int(math.sqrt(n))

def gen_primes(limit):
  """Generate a list of primes up to the limit specified."""
  candidates = [ True ] * (limit+1)
  candidates[0] = candidates[1] = False

  marker = 0

  while marker <= limit:
    if candidates[marker] == True:
      sieve = marker
      sieve += marker
      while sieve <= limit:
        candidates[sieve] = False
        sieve += marker
      marker += 1
    else:
      marker += 1
  return [ x for x in range(limit+1) if candidates[x] ]


if __name__ == "__main__": main()
