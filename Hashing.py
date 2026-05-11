import hashlib

password = "Password"

def simpleHash(password):
  password = list(password)
  
  for i in range(len(password)):
    password[i] = str(ord(password[i]) % len(password))
  
  hashed = "".join(password)
  return hashed
  








