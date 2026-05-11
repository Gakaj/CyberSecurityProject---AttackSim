import hashlib, os

def hashing_program():
  password = "Password"

  def simpleHash(password):
    password = list(password)
    
    for i in range(len(password)):
      password[i] = str(ord(password[i]) % len(password))
    
    hashed = "".join(password)
    return hashed
    


  def read_hash_wordlist():
    while True:
      path = input("Enter path to wordlist: ").strip().strip('""') # remove whitespace and other
    #validate path
      if os.path.isfile(path):
        break #stop asking for path

    print(ValueError("Incorrect path")) #if not correct type

    with open(path, "r", encoding="utf-8", errors="ignore") as file:
      for line in file:
        original = line.strip() # remove whitepsace and other problems
        if not original: # skip if empty/errors to continue
          continue #go to next iteration


        hashed = hashlib.sha256(original.encode()).hexdigest() # encode data and transform into sha256 hash
                                                              # as well as making it a hex NOT a byte and not output object.
        yield hashed # makes the function a generator by returning an iterable - makes it more efficient as no longer held in RAM



  for line in read_hash_wordlist(): #print every hashed line
    print(line)

if __name__ == "__main__":
  hashing_program()
else:
  pass