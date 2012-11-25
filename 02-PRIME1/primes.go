package main

import (
  "flag"
  "fmt"
  "log"
  "math"
)

var verbose bool
var sieve_limit int
func init() {
  flag.BoolVar(&verbose, "verbose", false, "Should I log stuff?")
  flag.IntVar(&sieve_limit, "upper_limit", 1000000000, "Upper limit of " +
  "primes to be sieved")
}

func main() {
  prime_limit := int(math.Sqrt(float64(sieve_limit)))
  l := gen_primes(prime_limit)
  if verbose {
    log.Println("Generated primes below ", prime_limit)
  }

  var rows int
  fmt.Scanln(&rows)
  if verbose {
    log.Println(rows, " rows to come.")
  }

  for i := 1; i <= rows ; i++ {
    if verbose {
      log.Println("Processing line ", i)
    }
    var start, stop int
    fmt.Scanln(&start, &stop)
    if verbose {
      log.Println("Generating primes between ", start, " and ", stop)
    }
    r := range_primes(start, stop, l)

    if verbose {
      log.Println("There are ", len(r), " results.")
    }

    for _, prime := range(r) {
      fmt.Println(prime)
    }
    fmt.Println("")
  }
}

func range_primes(start, stop int, known_primes []int) []int {

  if start < 2 {
    start = 2
  }

  num_candidates := stop-start+1
  candidates := make([]bool, num_candidates)
  for i := range(candidates) {
    candidates[i] = true
  }

  largest_prime_factor := int(math.Sqrt(float64(stop)))
  if verbose {
    log.Println("largest_prime_factor: ", largest_prime_factor)
  }

  prime_index := 0

  for known_primes[prime_index] <= largest_prime_factor {
    if verbose {
      log.Printf("{prime_index: %v ; known_primes[prime_index] :%v}\n",
      prime_index, known_primes[prime_index])
    }

    if verbose {
      log.Println("start: ", start)
    }

    sieve := known_primes[prime_index]
    if verbose {
      log.Println("sieve: ", sieve)
    }

    var first_candidate int

    // TODO: Failure. Not handling case analysis here properly.
    /*
    if start < sieve {
      first_candidate = 2*sieve
    } else {
      first_candidate = start/sieve*sieve + sieve
    }
    */

    first_candidate = start/sieve*sieve
    if first_candidate < start {
      first_candidate += sieve
    }
    if verbose {
      log.Println("first_candidate: ", first_candidate)
    }

    cand_idx := first_candidate - start
    if verbose {
      log.Println("cand_idx: ", cand_idx)
    }
    for cand_idx < len(candidates) {
      if cand_idx+start != sieve {
        candidates[cand_idx] = false
      }
      cand_idx += sieve
    }
    prime_index++
  }

  var primes []int
  for offset, is_prime := range(candidates) {
    if is_prime {
      primes = append(primes, offset+start)
    }
  }

  return primes
}

func gen_primes(limit int) []int {
  // All integers up to limit are candidates.
  candidates := make([]bool, limit+1)
  // Initially everything could be prime, except 0 and 1
  for num := range(candidates) {
    candidates[num] = true
  }
  candidates[0] = false
  candidates[1] = false

  for number, is_prime := range(candidates) {
    // Uncheck set false for all multiple of known primes
    if is_prime == true {
      multiple := number * 2
      for multiple <= limit {
        candidates[multiple] = false
        multiple += number
      }
    }
  }

  var primes []int
  for num, is_prime := range(candidates) {
    if is_prime {
      primes = append(primes, num)
    }
  }
  return primes
}
