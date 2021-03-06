#!/usr/bin/env python3
import sys


def react(polymer):
    ans = ''
    skip = False
    skips = 0
    for p, r in zip(polymer, polymer[1:] + '_'):
        if skip:
            skip = False
            continue
        if p == r.swapcase():
            skip = True
            skips += 1
            continue
        ans += p
    return ans, skips


def fully_react(polymer):
    skips = 1
    while skips > 0:
        polymer, skips = react(polymer)
    return polymer


def reduce(polymer, unit):
    return polymer.replace(unit.lower(), '').replace(unit.upper(), '')


input = sys.stdin.read().strip()
reacted_input = fully_react(input)
print(len(reacted_input))

unit_types = set(input.lower())
lengths = []
for unit in unit_types:
    lengths.append(len(fully_react(reduce(reacted_input, unit))))

print(min(lengths))
