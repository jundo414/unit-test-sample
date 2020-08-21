#!/usr/bin/env bats

@test "sum all numbers 1" {
  result="$(bash ../sum_num.sh abc 12 d e 3 71 z)"
  [ "$result" -eq 86 ]
}

@test "sum all numbers 2" {
  result="$(bash ../sum_num.sh 1 23 1b)"
  [ "$result" -eq 24 ]
}

@test "sum all numbers 3" {
  result="$(bash ../sum_num.sh -2 -9 3 1a)"
  [ "$result" -eq -8 ]
}
