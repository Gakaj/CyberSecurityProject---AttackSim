import hashlib, os

password = "Password"

def simpleHash(password):
  password = list(password)
  
  for i in range(len(password)):
    password[i] = str(ord(password[i]) % len(password))
  
  hashed = "".join(password)
  return hashed
  

path = input("Enter path to wordlist: ").strip().strip('""') # remove whitespace and other
def read_hash_wordlist(path):

  #validate path
  if not os.path.isfile(path):
    print(ValueError("Incorrect path"))
    quit()
  

  with open(path, "r", encoding="utf-8", errors="ignore") as file:
    for line in file:
      original = line.strip() # remove whitepsace and other problems
      if not original: # skip if empty/errors to continue
        continue






