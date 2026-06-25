import hashlib, os, sys, argparse


def hashing():
  parser = argparse.ArgumentParser(
    description= "Hash a wordlist using sha-256"
  )


  parser.add_argument(
      "-w",
      "--wordlist",
      required=True,
      help="Path to wordlist"  
  )


    

  # -- >  """" Sha 256 program starts here """
  def read_hash_wordlist(path):
      path = args.wordlist

      with open(path, "r", encoding="utf-8", errors="ignore") as file:
        for line in file:
          original = line.strip() # remove whitepsace and other problems
          if not original: # skip if empty/errors to continue
            continue #go to next iteration


          hashed = hashlib.sha256(original.encode()).hexdigest() # encode data and transform into sha256 hash
          # as well as making it a hex NOT a byte and not output object.
          yield hashed # makes the function a generator by returning an iterable - makes it more efficient as no longer held in RAM


  args = parser.parse_args()
  for line in read_hash_wordlist(args.wordlist): #print every hashed line
    print(line)

if __name__ == "__main__":
  hashing()
else:
  pass