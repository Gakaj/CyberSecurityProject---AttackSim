import hashlib, os

password = "Password"

def simpleHash(password):
  password = list(password)
  
  for i in range(len(password)):
    password[i] = str(ord(password[i]) % len(password))
  
  hashed = "".join(password)
  return hashed
  


def read_hash_wordlist():
  path = input("Enter path to wordlist: ").strip().strip('""') # remove whitespace and other

  #validate path
  if not os.path.isfile(path):
    print(ValueError("Incorrect path"))
    read_hash_wordlist()
  
  elif os.path.isfile(path):
    print("TRUE")

read_hash_wordlist()
  






