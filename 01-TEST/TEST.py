#!/usr/bin/env python

import sys

def main():
  for line in sys.stdin:
    number = line.strip()
    if number == '42':
      break
    else:
      print number

if __name__ == "__main__":
  main()
