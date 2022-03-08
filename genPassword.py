import imp
from    itertools import chain
from operator import length_hint
import string
import random
from xml.dom.minidom import CharacterData

characters= list(string.ascii_letters+string.digits +"!@#$%&*()^")

def generateRamdomPass():
    length = int(input("Entrez la longueur du mots de passe: "))
    random.shuffle(characters)
    password = []
    for i in range(length):
        password.append(random.choice(characters))
        
    random.shuffle(password)

    print("".join(password))
generateRamdomPass()