#!/usr/bin/env python

import math
import sys

def main():
  fullprimes = [2]
  input = sys.stdin
  records = int(input.next().strip())
  for _ in xrange(records):
    line = input.next().strip()
    start,stop = [int(n) for n in  line.split(' ')]
    output_primes(start, stop, fullprimes)

def output_primes(start, stop, fullprimes):
  """Print out all primes between start and stop from the list fullprimes."""
  prime_limit = int(math.floor(math.sqrt(stop)))
  while (fullprimes[-1] <= prime_limit):
    extend_primes(fullprimes)

  limited_primes = [x for x in fullprimes if x <= prime_limit]

  desired_primes = []

  actual_start = max(start, 2)

  for n in xrange(actual_start, stop+1):
    if n in limited_primes:
      desired_primes.append(n)
    elif not check_factors(n, limited_primes):
      desired_primes.append(n)
    else:
      continue

  for number in desired_primes:
    print number
  print ''

def extend_primes(fullprimes):
  """Given a list of primes, find the next highest prime."""

  # Start with the number above our highest prime.
  candidate = fullprimes[-1] + 1

  while(True):
    # To check the primacy of candidate, we only need primes up to
    # sqrt(candidate)
    prime_limit = int(math.ceil(math.sqrt(candidate)))
    limited_primes = [x for x in fullprimes if x < prime_limit]

    if check_factors(candidate, limited_primes):
      # Candidate has a factor in the existing prime list, try again.
      candidate = candidate + 1
    else:
      # We've found a new prime number. Append and return.
      fullprimes.append(candidate)
      return fullprimes

def check_factors(number, factor_list):
  """Check if factor_list contains a number which is a factor of number.

  Args:
    number, an int, the number being checked.
    factor_list, a list of integers, the possible factors
  """

  for factor in factor_list:
    if (number % factor) == 0:
      return True

  # Haven't found any factors, so false.
  return False

if __name__ == "__main__":
  main()
