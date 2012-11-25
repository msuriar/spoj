#!/usr/bin/env python

import math
import sys

# Find all primes up to sqrt(n)
# For each prime p
## Find largest multiple of p smaller than m (m/p*p)
## Increment up through array by increments of p, setting "prime" to false

# Return list of items which still have prime=trueo


def main():
  sieves = gen_primes(32768)
  input = sys.stdin
  records = int(input.next().strip())
  for x in xrange(records):
    line = input.next().strip()
    start,stop = ( int(n) for n in line.split(' ') )
    primes(start, stop, sieves)
    if x < records-1:
      print ''


def primes(m, n, filters):
  """Print all primes between m and n.
  Args:
    m, n integers
    filters, list of primes
  Returns:
    Nothing
  Outputs:
    A single prime per line.
  """
  if m<2:
    m = 2

  largest_prime = int(math.sqrt(n))
  sieves = [ prime for prime in filters if prime <= largest_prime ]
  num_candidates = n-m+1
  candidates = [ True ] * num_candidates
  for sieve in sieves:
    floor = m / sieve * sieve
    start = floor + sieve
    index = start - m
    if index + m == sieve:
      index +=sieve

    while index  < num_candidates:
      candidates[index] = False
      index += sieve
  for candidate in range(num_candidates):
    if candidates[candidate]:
      print candidate+m

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


if __name__ == "__main__":
  main()
