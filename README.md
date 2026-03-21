# CyberSecurityProject---AttackSim
<!-- no official site warning -->
> [!CAUTION]
> WORK IN PROGRESS

This project consists of files: "Attack.py", "Entropy.py", "Hashing.py" and a txt file - common_passwords.txt 
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# WHAT EACH MODULE MEANS:: Defined inside scope ( research folder )

entropy.py → calculate password entropy
hashing.py → hash + verify passwords
attack.py → simulate brute force + dictionary attack
main.py → "glue" everything together ( calls 3 modules before ) 
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
User password
      ↓
Entropy module
      ↓
Hashing module
      ↓
Attack module
      ↓
    Results
------------------------------------------------------------------------------------------------------------------------------------------------------------------------ # Standard English:

1.User enters password

2.Calculate entropy

3.Hash password

4.Pass hash to attack simulation

5.Output results

