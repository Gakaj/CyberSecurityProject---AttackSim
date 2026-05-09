import hashlib

password = "Password"

def simpleHash(password):
  password = list(password)
  
  for i in range(len(password)):
    password[i] = str(ord(password[i]) % len(password))
  
  hashed = "".join(password)
  return hashed
  


def sha256Hash(password):
  hashed = hashlib.sha256("password".encode()).hexdigest() #prepare password in byte form, then digest into hex rather than byte form.
  return hashed

User_password = {
  "user123" : simpleHash(password),
  "user1234" : sha256Hash(password)
}


