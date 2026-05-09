
password = "Password"

def simpleHash(password):
  password = list(password)
  
  for i in range(len(password)):
    password[i] = str(ord(password[i]) % len(password))
  
  hashed = "".join(password)
  return hashed
  
User_password = {
  "user123" : simpleHash(password)
  #"User1234" : sha256Hash(password)
}




