#!/python
# CREATE_MY_PASS.py was created by DECKCARD23 (JORGE ALEJANDRO ESCLAPEZ BONET)
# TWITTER: @rickdeckard23
# That script made a password with your selection options.

import os
import string
import secrets
import random

# COLORS

amarillo = chr(27)+"[0;33m"
rojo = chr(27)+"[0;31m"
azul_N = chr(27)+"[1;34m"
blanco = chr(27)+"[0;37m"
cian = chr(27)+"[0;36m"
morado_N = chr(27)+"[1;35m"

# FUNCTIONS

def ARROW_COLOR():
    numero = random.randint(1, 6)
    if numero == 1:
        print(amarillo + "=>", end="")
    elif numero == 2:
        print(rojo + "=>", end="")
    elif numero == 3:
        print(azul_N + "=>", end="")
    elif numero == 4:
        print(blanco + "=>", end="")
    elif numero == 5:
        print(cian + "=>", end="")
    elif numero == 6:
        print(morado_N + "=>", end="")

def MY_PASS():
    entropy = 0
    entro = 0
    barra = 0
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    alphabet = letters + digits + special_chars
    minus = int(input(amarillo + "How many LOWERCASE caracteres will your password have?: " + blanco))
    mayus = int(input(amarillo + "How many UPPERCASE caracteres will your password have?: " + blanco))
    symbo = int(input(amarillo + "How many SYMBOLS caracteres will your password have?: " + blanco))
    numer = int(input(amarillo + "How many NUMBERS caracteres will your password have?: " + blanco))
    pwd_length = minus + mayus + symbo + numer
    print(amarillo + "\nYour password will be " + morado_N + str(pwd_length) + amarillo + " length.")
    if pwd_length < 8:
        print(rojo + "[!] Ufff, your password will be very weak.\n")
    else:
        print(azul_N + "[x] Good, your password will be very strong.\n")
    print(amarillo + "If you want a very very strong password then select your own entropy")
    print(rojo + "[!] If you select a very higher entropy, perhaps the computer crash.")
    my_entropy = input(amarillo + "Do you want [A]utomatic entropy or [S]elect my own entropy? Choose [A] or [S]: " + blanco)
    if my_entropy == "A" or my_entropy == "a":
        print(cian + "\nAutomatic entropy selected.")
    elif my_entropy == "S" or my_entropy == "s":
        entro = int(input(amarillo + "\nPut a number to your entropy: " + blanco))
    else:
        print(rojo + "\nBad election, automatic entropy by default.")
    while True:
        minusculas = 0
        mayusculas = 0
        simbolos = 0
        numeros = 0
        pwd = ''
        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))
            ARROW_COLOR()
        # Contador de letras
        for letra in pwd:
            if letra in "abcdefghijklmnñopqrstuvwxyz":
                minusculas += 1
            if letra in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ":
                mayusculas += 1
            if letra in "!\"·$%&/()=?¿¡'ºª\\|@#~¬<>,;.:-_´¨çÇ`^+*[]{}":
                simbolos += 1
            if letra in "1234567890":
                numeros += 1
            entropy += 1
        #barra += 1
        if (minus >= minusculas and mayus >= mayusculas and symbo >= simbolos and numer >= numeros) and (entropy > entro):
            print(amarillo + "\nYour random password is: " + azul_N, pwd)
            print(amarillo + "The entropy of this password is: " + cian, entropy)
            option = input(blanco + "[ENTER] to continue | [Y]+[ENTER] to exit: ")
            if option == "Y" or option == "y":
                print(azul_N + "\nThanks to use my script. Remember, " + rojo + "don´t forget your passwords.")
                print(azul_N + "Follow me in " + morado_N + "@rickdeckard23" + blanco + ". Have a nice day.")
                break
            else:
                entropy = 0
                barra = 0
                continue

os.system('cls')
print(azul_N + "----------------------------------------------------")
print(azul_N + "   Wellcome to Create my password" + morado_N + " by Deckcard23")
print(azul_N + "----------------------------------------------------\n")


MY_PASS()
