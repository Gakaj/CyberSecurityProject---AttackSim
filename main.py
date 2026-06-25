#this version is before attempting to add salting. I understand passwords would likely be salted before hashing to improve security.
#will think of way to solve this after completing attack simulation. 09.05.2026

import Entropy
import Hashing



def validate_email(username):
    pass







# Acting as target 
def target_enter():
    username = input("Enter username of email: ")
    validate_email(username)
    password = input("Enter password to email: ")
    Entropy.entropy_program(password)

target_enter()