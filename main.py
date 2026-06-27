#this version is before attempting to add salting. I understand passwords would likely be salted before hashing to improve security.
#will think of way to solve this after completing attack simulation. 09.05.2026

import Entropy
import Hashing
import argparse


parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(
    dest="command",
    required=True
)
hash_parser = subparsers.add_parser(
    "hash",
    help="Hash a wordlist"
  )

hash_parser.add_argument(
    "-w",
    "--wordlist",
    required=True,
    help="Path to wordlist"
  )
args = parser.parse_args()
if args.command == "hash":
    print(f"Hashing {args.wordlist}")
    Hashing.hashing(args.wordlist)



