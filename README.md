# CyberSecurityProject---AttackSim
<!-- no official site warning -->
> [!CAUTION]
> WORK IN PROGRESS

This project emulates what an attack would look like. 
Simulating before the attack -> "grading" a password using entropy. Also, hashing algorithm performed on password -> simulate an attack on a hash comparing the hash value to the hashe enumerated password attempts rather than the raw password.

Furthermore, a seperate attack.py module that simulates a dictionary attack enumerating passwords mirroring with less detail like tools like dirbuster(web directories/url) and [Hydra](https://www.kali.org/tools/hydra/)

 This project consists of files: 
 "Attack.py", "Entropy.py", "Hashing.py" and a txt file - common_passwords.txt 

Common_passwords.txt accredited from [SecLists](https://github.com/danielmiessler/SecLists/tree/master) - Compiled by DanielMiessler


<ins>Summary:

| entropy.py | hashing.py | attack.py | main.py   |
|------------|------------|-----------|-----------|
| Uses entropy formula | Uses SHA-256 cryptography | Uses different methods | Glues all files    |
| Collapse entropy formula| hashing.py | View [BFAR.txt](https://github.com/Gakaj/CyberSecurityProject---AttackSim/blob/main/Cybersecurity%20Project/research/BruteForceAttackResearch.txt)  | ***Final Program***|

Accreddited OWASP.org for info on [dictionary attacks](https://owasp.org/www-community/attacks/Brute_force_attack).
Also accredit [account enumeration](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/03-Identity_Management_Testing/04-Testing_for_Account_Enumeration_and_Guessable_User_Account)

<details><summary>Entropy Equation</summary>![download](https://github.com/user-attachments/assets/d7739ee8-4fe3-4f14-ab62-c48526b838b1)
</details>
