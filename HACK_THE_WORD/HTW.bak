#!/bin/python3

# AUTHOR: DECKCARD23 (JORGE ALEJANDRO ESCLAPEZ BONET)
# Started: 02/08/2022
# Tested in Windows 10 system with: python 3.9.10




###############
## LIBRARIES ##
###############

import os, time
import itertools
import secrets
import string
import base64
import hashlib
import codecs



                                                                                              
# COLORS

menu = chr(27)+"[1;33;44m"
c_col = chr(27)+"[0;m"
yellow = chr(27)+"[0;33m"
yellow_B = chr(27)+"[1;33m"
red = chr(27)+"[0;31m"
red_B = chr(27)+"[1;31m"
green = chr(27)+"[0;32m"
green_B = chr(27)+"[1;32m"
blue = chr(27)+"[0;34m"
blue_B = chr(27)+"[1;34m"
purple = chr(27)+"[0;35m"
purple_B = chr(27)+"[1;35m"
cian = chr(27)+"[0;36m"
cian_B = chr(27)+"[1;36m"
white = chr(27)+"[0;37m"
white_B = chr(27)+"[1;37m"




# VARIABLES, LISTS, TUPLES, DICTIONARIES

file_dont_exist = 0
words=[]
dates=[]
uniq_list=[]
vocals=["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
symbols=["@", "#", "º", "!", "\"", "·", "$", "%", "&", "/", "(", ")", "=", "?", "¿", "¡", "'", "¬", "~", "|", "\\", "ª", "<", ">", ",", ".", "-", ";", ":", "_", "´", "ç", "¨", "Ç", "{", "}", "]", "[", "+", "`", "^", "*"]
new_list=""
hacker_wordlist=""
hacker_long={"L":"1","l":"1","i":"1","I":"1","E":"3","e":"3","A":"4","a":"4","S":"5","s":"5","T":"7","t":"7","B":"8","b":"8","O":"0","o":"0"}
hacker_short={"L":"1","l":"1","i":"1","I":"1","E":"3","e":"3","A":"4","a":"4","S":"5","s":"5","O":"0","o":"0"}
hacker_long_plus={"L":"1","l":"1","i":"1","I":"1","T":"7","t":"7","B":"8","b":"8","O":"0","o":"0","A":"@","a":"@","S":"$","s":"$","E":"€","e":"€"}
hacker_short_plus={"L":"1","l":"1","i":"1","I":"1","O":"0","o":"0","A":"@","a":"@","S":"$","s":"$","E":"€","e":"€"}
months={"01":"Enero","02":"Febrero","03":"Marzo","04":"Abril","05":"Mayo","06":"Junio","07":"Julio","08":"Agosto","09":"Septiembre","10":"Octubre","11":"Noviembre","12":"Diciembre"}
date_var_open=["[","(","[ ","( ","{","{ "]
date_var_close=["]",")"," ]"," )","}"," }"]
card_dict={'card_dict0':{"a":"EE", "b":"EE", "c":"EE", "d":"EE", "e":"EE", "f":"EE", "g":"EE", "h":"EE", "i":"EE", "j":"EE", "k":"EE", "l":"EE", "m":"EE","n":"Kj", "o":"Kj", "p":"Kj", "q":"12", "r":"12", "s":"12", "t":"12", "u":"12", "v":"12", "w":"12", "y":"12", "z":"12",".":"34"},
'card_dict1': {"a":"dk", "b":"dk", "c":"dk", "d":"dk", "e":"dk", "f":"dk", "g":"dk", "h":"dk", "i":"dk", "j":"dk", "k":"dk", "l":"dk", "m":"dk", "n":"mn", "o":"mn", "p":"mn", "q":"33", "r":"33", "s":"33", "t":"33", "u":"33", "v":"33", "w":"33", "y":"33", "z":"33", ".":"3?"},
'card_dict2': {"a":"pp", "b":"pp", "c":"pp", "d":"pp", "e":"pp", "f":"pp", "g":"pp", "h":"pp", "i":"pp", "j":"pp", "k":"pp", "l":"pp", "m":"pp", "n":"k=", "o":"k=", "p":"k=", "q":"3?", "r":"3?", "s":"3?", "t":"3?", "u":"3?", "v":"3?", "w":"3?", "y":"3?", "z":"3?", ".":"2!"},
'card_dict3': {"a":"ii", "b":"ii", "c":"ii", "d":"ii", "e":"ii", "f":"ii", "g":"ii", "h":"ii", "i":"ii", "j":"ii", "k":"ii", "l":"ii", "m":"ii", "n":"iI", "o":"iI", "p":"iI", "q":"I!", "r":"I!", "s":"I!", "t":"I!", "u":"I!", "v":"I!", "w":"I!", "y":"I!", "z":"I!", ".":"))"},
'card_dict4': {"a":"kK", "b":"kK", "c":"kK", "d":"kK", "e":"kK", "f":"kK", "g":"kK", "h":"kK", "i":"kK", "j":"kK", "k":"kK", "l":"kK", "m":"kK", "n":"CA", "o":"CA", "p":"CA", "q":"iw", "r":"iw", "s":"iw", "t":"iw", "u":"iw", "v":"iw", "w":"iw", "y":"iw", "z":"iw", ".":"?U"}}
locker_words=["w","x","y","h","W","X","Y","H"]
locker_list = {"h":"*","t":"1","d":"1","n":"2","ñ":"2","m":"3","c":"4","k":"4","q":"4","l":"5","s":"6","z":"6","f":"7","ch":"8","j":"8","g":"8","v":"9","b":"9","p":"9","r":"0"}




#######################
#######################
## GENERAL FUNCTIONS ##
#######################
#######################




# Main menu
def MENU():
    os.system("cls")
    print(white)
    print(""" ██╗  ██╗ █████╗  ██████╗██╗  ██╗    ████████╗██╗  ██╗███████╗    ██╗    ██╗ ██████╗ ██████╗ ██████╗ 
 ██║  ██║██╔══██╗██╔════╝██║ ██╔╝    ╚══██╔══╝██║  ██║██╔════╝    ██║    ██║██╔═══██╗██╔══██╗██╔══██╗
 ███████║███████║██║     █████╔╝        ██║   ███████║█████╗      ██║ █╗ ██║██║   ██║██████╔╝██║  ██║
 ██╔══██║██╔══██║██║     ██╔═██╗        ██║   ██╔══██║██╔══╝      ██║███╗██║██║   ██║██╔══██╗██║  ██║
 ██║  ██║██║  ██║╚██████╗██║  ██╗       ██║   ██║  ██║███████╗    ╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝
 ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝       ╚═╝   ╚═╝  ╚═╝╚══════╝     ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ """)
    print(menu + "\n ------- M A I N   M E N U ------- " + c_col)
    print(green_B + "\n 1. " + yellow + "Generate wordlist.")
    print(green_B + " 2. " + yellow + "Set relevants dates or numbers.")
    print(green_B + " 3. " + yellow + "DICEWARE.")
    print(green_B + " 4. " + yellow + "H4ck3r W0rd1i5t5.")
    print(green_B + " 5. " + yellow + "Suffix and Preffix.")
    print(green_B + " 6. " + yellow + "Sudoku.")
    print(green_B + " 7. " + yellow + "Emojis.")
    print(green_B + " 8. " + yellow + "KeyBoard patterns.")
    print(green_B + " 9. " + yellow + "Password card.")
    print(green_B + " 10. " + yellow + "Phonetic Muscle Memory.")
    print(green_B + " 11. " + yellow + "Phone Alphanumeric System.")
    print(green_B + " 12. " + yellow + "Relevant dates variants.")
    print(green_B + " 13. " + yellow + "Are you superstitioning?.")
    print(green_B + " 14. " + yellow + "Mental lockers.")
    print(green_B + " 15. " + yellow + "Ethereum method.")
    print(green_B + " 16. " + yellow + "Words and numbers mixing.")
    print(green_B + " 17. " + yellow + "Password ciphers.")
    print(blue_B + "\n 0. " + red_B + "Exit/Quit.\n")
    global option
    print(white_B + " Choose your option: " + green, end="")
    option=input()




# Wait a moment
def WAIT():
    print(white + " Press" + white_B + " [ENTER]" + white + " to continue...", end="")
    input()




# PAUSE
def PAUSE():
    time.sleep(2)


# UNIQ

def UNIQ():
    print(green_B + "Debug wordlist and cleaning duplicate words if existing...")
    # initialize a null list
    unique_list = []
  
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)



# BASIC CHECK FILE
def CHECK_BASIC():
    print(green + " Checking if file exist...")
    if selection_new == selection_folder:
        print(red + "No has elegido ningún fichero.")
        global file_dont_exist
        file_dont_exist = 1
    elif os.path.exists(selection_new) == False:
        print(red + " The file {} don´t exist.".format(selection_new))
        PAUSE()
        file_dont_exist = 1
    else:
        file_dont_exist = 0


    

# CHECK IF FILE EXIST
def CHECK_FILE():
    print(green + " Checking if file exist...")
    if os.path.exists(filecheck) == True:
        print(red + " The file {} exist. Do you want to add that new wordlist? (Y/N): ".format(filecheck), end="")
        option = input()
        if option == "y" or option == "Y":
            print(green + " Adding information...")
        elif option == "N" or option == "n":
            print(green + " Deleting old file...")
            os_order = "del " + filecheck
            os.system(os_order)
    else:
        print(green + " Checking file...")



# Read the file name data.txt with the OSINT information about the PENTESTING CUSTOMER
def READ():
    global words
    words=[]
    print(green + " Reading DATA.txt file...")
    PAUSE()
    file=open("data.txt","r")
    while True:
        line=file.readline()
        reduce_line=line.find(":")
        reduce_line=int(reduce_line+1)
        line=line[reduce_line:]
        line=str(line)
        line=line.removesuffix("\n")
        words.append(line)
        if not line:
            break
    del words[-1]
    file.close()
    print(green + " Datos leidos de DATA.txt: " + green_B + str(words))


# Read dates or number in option 2
def READ_DATES():
    if not dates:
        print(white + " No dates numbers...")
    else:
        file=open("..\\OUTPUTS\\HTC_wordlist.txt","a")
        global password_symbols
        for date in dates:
            if password_symbols+date not in uniq_list:
                file.write(password_symbols+date+"\n")
                uniq_list.append(password_symbols+date)
            if password_symbols.upper()+date not in uniq_list:    
                file.write(password_symbols.upper()+date+"\n")
                uniq_list.append(password_symbols.upper()+date)
            if password_symbols.lower()+date not in uniq_list:
                file.write(password_symbols.lower()+date+"\n")
                uniq_list.append(password_symbols.lower()+date)
            if date+password_symbols not in uniq_list:
                file.write(date+password_symbols+"\n")
                uniq_list.append(date+password_symbols)
            if date+password_symbols.upper() not in uniq_list:
                file.write(date+password_symbols.upper()+"\n")
                uniq_list.append(date+password_symbols.upper())
            if date+password_symbols.lower() not in uniq_list:
                file.write(date+password_symbols.lower()+"\n")
                uniq_list.append(date+password_symbols.lower())
            
            date=date[::-1]

            if password_symbols+date not in uniq_list:
                file.write(password_symbols+date+"\n")
                uniq_list.append(password_symbols+date)
            if password_symbols.upper()+date not in uniq_list:    
                file.write(password_symbols.upper()+date+"\n")
                uniq_list.append(password_symbols.upper()+date)
            if password_symbols.lower()+date not in uniq_list:
                file.write(password_symbols.lower()+date+"\n")
                uniq_list.append(password_symbols.lower()+date)
            if date+password_symbols not in uniq_list:
                file.write(date+password_symbols+"\n")
                uniq_list.append(date+password_symbols)
            if date+password_symbols.upper() not in uniq_list:
                file.write(date+password_symbols.upper()+"\n")
                uniq_list.append(date+password_symbols.upper())
            if date+password_symbols.lower() not in uniq_list:
                file.write(date+password_symbols.lower()+"\n")
                uniq_list.append(date+password_symbols.lower())


        file.close()


            
# Read dates or number introduced in option 2 and mix with passwords simple mode
def READ_DATES_PASS():
    if not dates:
        print(white + " No dates numbers...")
    else:
        file=open("..\\OUTPUTS\\HTC_wordlist.txt","a")
        global password
        for date in dates:
            # Dates at the end
            if password+date not in uniq_list:
                file.write(password+date+"\n")
                uniq_list.append(password+date)
            if password.upper()+date not in uniq_list:
                file.write(password.upper()+date+"\n")
                uniq_list.append(password.upper()+date)
            if password.lower()+date not in uniq_list:
                file.write(password.lower()+date+"\n")
                uniq_list.append(password.lower()+date)
            # Dates at the beggining
            if date+password not in uniq_list:
                file.write(date+password+"\n")
                uniq_list.append(date+password)
            if date+password.upper() not in uniq_list:
                file.write(date+password.upper()+"\n")
                uniq_list.append(date+password.upper())
            if date+password.lower() not in uniq_list:
                file.write(date+password.lower()+"\n")
                uniq_list.append(date+password.lower())
            # Dates reverse at the end
            date=date[::-1]
            
            if password+date not in uniq_list:
                file.write(password+date+"\n")
                uniq_list.append(password+date)
            if password.upper()+date not in uniq_list:
                file.write(password.upper()+date+"\n")
                uniq_list.append(password.upper()+date)
            if password.lower()+date not in uniq_list:
                file.write(password.lower()+date+"\n")
                uniq_list.append(password.lower()+date)
            # Dates reverse at the beggining
            if date+password not in uniq_list:
                file.write(date+password+"\n")
                uniq_list.append(date+password)
            if date+password.upper() not in uniq_list:
                file.write(date+password.upper()+"\n")
                uniq_list.append(date+password.upper())
            if date+password.lower() not in uniq_list:
                file.write(date+password.lower()+"\n")
                uniq_list.append(date+password.lower())

            
        file.close()




########################
## WORDLIST FUNCTIONS ##
########################



            
def MAIN_LETTER():
    #take the first letter in the line to make the password
    global filecheck
    filecheck="..\\OUTPUTS\\HTC_wordlist.txt"
    CHECK_FILE()
    print(green + " Generate main letter passwords...")
    PAUSE()
    global password
    password=""
    global password_symbols
    password_symbols=""
    global file
    file=open("..\\OUTPUTS\\HTC_wordlist.txt","a")
    # CREA WORDLIST CON VARIACIONES BÁSICAS
    for symbol in range(len(symbols)):
        for item in range(len(words)): # Aqui suma el primer caracter de cada palabra de la lista words (DATA.txt)
            password=words[item][0]
            password_symbols=words[item][0] # password_symbols[words[item][0]] (lo que ponia antes)
                                                
            for i in range(len(words[item])):
                if words[item][i] == " ": # Aquí gestiona los espacios y suma la primera letra de cada palabra
                    password=password+(words[item][i+1])
                    password_symbols=password_symbols+symbols[symbol]+(words[item][i+1]) # Aquí suma simbolo 0

            
            if password not in uniq_list:    
                file.write(password+"\n")
                uniq_list.append(password)
            if password.upper() not in uniq_list:
                file.write(password.upper()+"\n")
                uniq_list.append(password.upper())
            if password.lower() not in uniq_list:
                file.write(password.lower()+"\n")
                uniq_list.append(password.lower())
            READ_DATES_PASS()
    
            password = password[::-1] # aquí las inversiones de la palabra
            
            if password not in uniq_list:
                file.write(password+"\n")
                uniq_list.append(password)
            if password.upper() not in uniq_list:
                file.write(password.upper()+"\n")
                uniq_list.append(password.upper())
            if password.lower() not in uniq_list:    
                file.write(password.lower()+"\n")
                uniq_list.append(password.lower())
            READ_DATES_PASS()

            
            if password_symbols not in uniq_list:            
                file.write(password_symbols+"\n")
                uniq_list.append(password_symbols)
            if password_symbols.upper() not in uniq_list:
                file.write(password_symbols.upper()+"\n")
                uniq_list.append(password_symbols.upper())
            if password_symbols.lower() not in uniq_list:
                file.write(password_symbols.lower()+"\n")
                uniq_list.append(password_symbols.lower())
            READ_DATES()

            password_symbols = password_symbols[::-1]
            
            if password_symbols not in uniq_list:
                file.write(password_symbols+"\n")
                uniq_list.append(password_symbols)
            if password_symbols.upper() not in uniq_list:
                file.write(password_symbols.upper()+"\n")
                uniq_list.append(password_symbols.upper())
            if password_symbols.lower() not in uniq_list:
                file.write(password_symbols.lower()+"\n")
                uniq_list.append(password_symbols.lower())
            READ_DATES()
        
    file.close()   




def BRUCE_SCHNEIER():
    #take the first letter in the line to make the password
    print(green + " Generate Bruce Schneier passwords...")
    PAUSE()
    global password
    global password_symbols
    password=""
    password_symbols=""
    file=open("..\\OUTPUTS\\HTC_wordlist.txt","a")
    for item in words:
        for symbol in range(len(symbols)):
            password=item[0]+item[1]
            password_symbols=item[0]+item[1]
        
            for i in range(len(item)):
                if item[i] == " ":
                    password=password+(item[i+1]+item[i+2])
                    password_symbols=password_symbols+symbols[symbol]+(item[i+1]+item[i+2])
            if password_symbols.upper() not in uniq_list:
                file.write(password_symbols.upper()+"\n")
                uniq_list.append(password_symbols.upper())
            if password_symbols.lower() not in uniq_list:
                file.write(password_symbols.lower()+"\n")
                uniq_list.append(password_symbols.lower())    
            if password_symbols not in uniq_list:
                file.write(password_symbols+"\n")
                uniq_list.append(password_symbols)
            READ_DATES()
            
            password_symbols = password_symbols[::-1]
            if password_symbols.upper() not in uniq_list:
                file.write(password_symbols.upper()+"\n")
                uniq_list.append(password_symbols.upper())
            if password_symbols.lower() not in uniq_list:
                file.write(password_symbols.lower()+"\n")
                uniq_list.append(password_symbols.lower())    
            if password_symbols not in uniq_list:
                file.write(password_symbols+"\n")
                uniq_list.append(password_symbols)
            READ_DATES()
            
        if password not in uniq_list:    
            file.write(password+"\n")
            uniq_list.append(password)
        if password.upper() not in uniq_list:
            file.write(password.upper()+"\n")
            uniq_list.append(password.upper())
        if password.lower() not in uniq_list:
            file.write(password.lower()+"\n")
            uniq_list.append(password.lower())
        READ_DATES_PASS()
    
        password = password[::-1] # aquí las inversiones de la palabra

        if password not in uniq_list:
            file.write(password+"\n")
            uniq_list.append(password)
        if password.upper() not in uniq_list:
            file.write(password.upper()+"\n")
            uniq_list.append(password.upper())
        if password.lower() not in uniq_list:    
            file.write(password.lower()+"\n")
            uniq_list.append(password.lower())
        READ_DATES_PASS()
        
    file.close()




def ONLY_CONSONANTS():
    #take only the consonants to creat the password
    print(green + " Generate only consonants passwords...")
    PAUSE()
    global password
    password=""
    global vocales
    vocales=0
    global password_symbols
    password_symbols=""
    # Fichero que crea solo consonantes
    file=open("..\\OUTPUTS\\HTC_wordlist.txt","a")
    for item in range(len(words)):
        for symbol in range(len(symbols)):
            password=""
            for i in range(len(words[item])):
        
                for vowel in vocals:
             
                    if words[item][i] == vowel:
                        vocales+=1

                if vocales != 1 and words[item][i] != " ":        
                    password=password+(words[item][i])
                    password_symbols=password_symbols+(words[item][i])+(symbols[symbol])
                vocales=0

            if password_symbols not in uniq_list:
                file.write(password_symbols+"\n")
                uniq_list.append(password_symbols)
            if password_symbols.upper() not in uniq_list:    
                file.write(password_symbols.upper()+"\n")
                uniq_list.append(password_symbols.upper())
            if password_symbols.lower not in uniq_list:
                file.write(password_symbols.lower()+"\n")
                uniq_list.append(password_symbols.lower())
            READ_DATES()
            
            password_symbols = password_symbols[::-1]

            if password_symbols not in uniq_list:
                file.write(password_symbols+"\n")
                uniq_list.append(password_symbols)
            if password_symbols.upper() not in uniq_list:
                file.write(password_symbols.upper()+"\n")
                uniq_list.append(password_symbols.upper())
            if password_symbols.lower not in uniq_list:
                file.write(password_symbols.lower()+"\n")
                uniq_list.append(password_symbols.lower())
            READ_DATES()
            password_symbols=""
        
        if password not in uniq_list:        
            file.write(password+"\n")
            uniq_list.append(password)
        if password.upper() not in uniq_list:
            file.write(password.upper()+"\n")
            uniq_list.append(password.upper())
        if password.lower() not in uniq_list:
            file.write(password.lower()+"\n")
            uniq_list.append(password.lower())
        READ_DATES_PASS()
    
        password = password[::-1]
        
        if password not in uniq_list:
            file.write(password+"\n")
            uniq_list.append(password)
        if password.upper() not in uniq_list:
            file.write(password.upper()+"\n")
            uniq_list.append(password.upper())
        if password.lower() not in uniq_list:
            file.write(password.lower()+"\n")
            uniq_list.append(password.lower())
        READ_DATES_PASS()
    
    file.close()



    
def H4CK3R():
    print(green + " Generating H4CK3R W0RD1I5T5, wait a moment...")
    PAUSE()
    p_hacker_w=[]
    global filecheck
    filecheck = "..\\OUTPUTS\\H4CK3R_w_" + selection
    CHECK_FILE()
    # Crea una lista (p_hacker_w) con las palabras del diccionario elegido
    file=open(selection_new,"r")
    while True:
        line=file.readline()
        line=str(line)
        line=line.removesuffix("\n")
        p_hacker_w.append(line)

        if not line:
            break
    file.close()
    del p_hacker_w[-1]
    # Lee la lista y va cambiado letras por números
    filename="..\\OUTPUTS\\H4CK3R_w_" + selection
    resultado="" # valor de la variable modificada
    
    file=open(filename,"a")
    for item in range(len(p_hacker_w)):
        for x,y in hacker_wordlist.items():
            letra_buscada = x
            letra_reemplazo = y
            palabra = p_hacker_w[item]
            for letra in palabra:
                if letra == letra_buscada:
                    resultado += letra_reemplazo
                else:
                    resultado += letra
        
            p_hacker_w[item] = resultado
            resultado=""
        file.write(p_hacker_w[item]+"\n")
    file.close()
    print(cian + filename + " wordlists was created.")





def SUF_PREF():
    print(green + " Creating a Suffix and Prefix wordlist...\n")
    PAUSE()
    suf_pref = []
    wlist_suf = []
    # Lee los sufijos y prefijos y los guarda en la lista suf_pref
    global filecheck
    filecheck = "..\\OUTPUTS\\Suf_Pref_wordlist_" + selection
    CHECK_FILE()
    file=open("suf_and_pref.txt","r")
    while True:
        line=file.readline()
        line=str(line)
        line=line.removesuffix("\n")
        suf_pref.append(line)

        if not line:
            break
    file.close()
    del suf_pref[-1]
    # Lee diccionario elegido y lo guarda en la lista wlist_suf
    file=open(selection_new,"r")
    while True:
        line=file.readline()
        line=str(line)
        line=line.removesuffix("\n")
        wlist_suf.append(line)

        if not line:
            break
    file.close()
    del wlist_suf[-1]
    # Crea nuevo diccionario con sufijo y prefijo (suf_pref) añadido a wordlist elegida (wlist_suf)
    filename="..\\OUTPUTS\\Suf_Pref_wordlist_" + selection
    file=open(filename,"a")
    for item in range(len(wlist_suf)):
        for suf in range(len(suf_pref)):
            file.write(wlist_suf[item] + suf_pref[suf] + "\n")
            file.write(suf_pref[suf] + wlist_suf[item] + "\n")
    file.close()





def SUDOKU():
    print(green + " Creating SUDOKU wordlist...")
    PAUSE()
    global filecheck
    filecheck="..\\OUTPUTS\\Sudoku_wordlist_" + selection
    CHECK_FILE()
    sudoku=[]
    # Lee el Sudoku elegido de la carpeta SUDOKU y lo añade a la lista "sudoku"
    file=open(selection_new,"r")
    while True:
        line=file.readline()
        line=str(line)
        line=line.removesuffix("\n")
        sub_list = []
        for number in range(len(line)):
            sub_list.append(line[number])
        sudoku.append(sub_list)
        if not line:
            break
    file.close()
    del sudoku[-1]
    # Lee el patron (pattern) y lo mete en las listas "rows" and "colums"
    rows = []
    colums = []
    file=open("..\\SUDOKU\\patrones\\pattern_u.txt","r")
    while True:
        line=file.readline()
        line=str(line)
        line=line.removesuffix("\n")
        for coordenates in range(len(line)):
            if coordenates == 0:
                colums.append(line[coordenates])
            elif coordenates == 2:
                rows.append(line[coordenates])

        if line == "#":
            del colums[-1]
            # Lee la lista "sudoku" utilizando listas "rows" and "colums" y extrae el password que copia en wordlist
            filename="..\\OUTPUTS\\Sudoku_wordlist_" + selection
            file2=open(filename,"a")
            for item in range(len(colums)):
                col = int(colums[item])
                row = int(rows[item])
                file2.write(sudoku[col][row])
            rows = []
            colums = []
            file2.write("\n")
            file2.close()
            

        if not line:
            break
        
    file.close()





def EMOJIS():
    print(green + " Creating a EMOJIS wordlist...\n")
    PAUSE()
    global filecheck
    filecheck = "..\\OUTPUTS\\Emojis_wordlist_" + selection
    CHECK_FILE()
    emojis=[]
    wlist_suf=[]
    # Lee los sufijos y prefijos y los guarda en la lista emojis
    file=open("emojis.txt","r")
    while True:
        line=file.readline()
        line=str(line)
        line=line.removesuffix("\n")
        emojis.append(line)
        if not line:
            break
    file.close()
    del emojis[-1]
    # Lee diccionario elegido y lo guarda en la lista wlist_suf
    file=open(selection_new,"r")
    while True:
        line=file.readline()
        line=str(line)
        line=line.removesuffix("\n")
        wlist_suf.append(line)
        
        if not line:
            break
    file.close()
    del wlist_suf[-1]
    print(yellow + " wlist_suf total: " + white + ', '.join(wlist_suf))
    # Crea nuevo diccionario con emojis añadido a wordlist elegida (wlist_suf)
    filename="..\\OUTPUTS\\Emojis_wordlist_" + selection
    file=open(filename,"a")
    for item in range(len(wlist_suf)):
        for suf in range(len(emojis)):
            file.write(wlist_suf[item] + emojis[suf] + "\n")
            file.write(emojis[suf] + wlist_suf[item] + "\n")
    file.close()




def PASSWORD_CARD():
    print(green + " Creating a PASSWORD CARD wordlist...\n")
    PAUSE()
    websites=[]
    # Lee los sitios webs del fichero elegido y los guarda en la lista passwords_sites
    file=open(selection_new,"r")
    while True:
        line=file.readline()
        line=str(line)
        line=line.removesuffix("\n")
        websites.append(line)
        if not line:
            break
    file.close()
    del websites[-1]
    # Lee websites y crea wordlist de equivalencias
    global filecheck
    filecheck = "..\\OUTPUTS\\Passwordcard_wordlist_" + selection + ".txt"
    CHECK_FILE()
    pass_card = ""
    file=open(filecheck, "a")
    for web in range(len(websites)):
        if len(websites[web]) <= 5:
            for caracter in range(len(websites[web])):
                num_dict = "card_dict"+str(caracter)
                key_dict = str(websites[web][caracter])
                pass_card += card_dict[num_dict][key_dict]
            file.write(pass_card + "\n")
            pass_card = ""
        else:
            print(purple + " La web " + purple_B + websites[web] + purple + " tiene más de 5 caracteres y es inválida.")
    file.close()
    
    

    
def MUSCLE():
    print(green + " Creating a PHONETIC MUSCLE PASSWORD\n")
    PAUSE()
    # Debes elegir el tamaño de la contraseña y dar a [ENTER] hasta que aparezca la que te guste siempre que tenga un sentido fonético
    contador = 0
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    alphabet = letters + digits + special_chars
    print(yellow + " Select you password length: " + white, end="")
    pwd_length = int(input())
    if muscle_list == 1:
        global filecheck
        filecheck = "..\\OUTPUTS\\Muscle_wordlist_" + str(pwd_length) + "_" + str(muscle_words) + ".txt"
        CHECK_FILE()
    while True:
        vocales = 0
        pwd = ''
        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))
        # Contador de vocales
        for letra in pwd:
            if letra.lower() in "aeiou":
                vocales += 1
            if letra.upper() in "AEIOU":
                vocales += 1
        if muscle_list == 0: # Imprime password por pantalla
            if vocales >= (pwd_length + ((pwd_length/2)/2)):
                print(yellow + " Your random password is: " + cian + pwd + white)
                print(white_B + " [ENTER]" + white + " to continue or" + white_B + " Y+[ENTER]" + white + " to exit: ", end="")
                option = input()
                if option == "Y" or option == "y":
                    break
                else:
                    continue
                
        elif muscle_list == 1: # Crea lista de passwords
            if vocales >= (pwd_length + ((pwd_length/2)/2)):
                filename="..\\OUTPUTS\\Muscle_wordlist_" + str(pwd_length) + "_" + str(muscle_words) + ".txt"
                file=open(filename,"a")
                file.write(pwd + "\n")
                file.close()
                contador += 1
                print(purple + " Add password: " + white + str(contador))
                if muscle_words == contador:
                    print (cian + " Your wordlist was created. " + str(muscle_words) + " passwords added.")
                    break




def PHONE():
    print(green + " Creating a ALPHANUMERIC PHONE wordlist from dates or numbers.\n")
    PAUSE()
    # Comprueba si hay datos en la opcion 2 de fechas relevantes
    if str(bool(dates)) == "False" :
        print(red + " [!] Sorry but your dates list are empty. Select the option 2 and add relevants dates")
        time.sleep(3)
    else:
        print(green + " Your relevant dates or numbers are the next: " + white + str(dates))
        global filecheck
        filecheck="..\\OUTPUTS\\Phone_Alphabetic_Wordlist.txt"
        CHECK_FILE()
        phone_pass = ""
        for date in range(len(dates)):
            for caracter in range(len(dates[date])):
                alpha = str(dates[date][caracter])
                if alpha == "1":
                    phone_pass += "1"
                elif alpha == "2":
                    phone_pass += "A"
                elif alpha == "3":
                    phone_pass += "D"
                elif alpha == "4":
                    phone_pass += "G"
                elif alpha == "5":
                    phone_pass += "J"
                elif alpha == "6":
                    phone_pass += "M"
                elif alpha == "7":
                    phone_pass += "P"
                elif alpha == "8":
                    phone_pass += "T"
                elif alpha == "9":
                    phone_pass += "W"
                elif alpha == "0":
                    phone_pass += "+"
            # Copia phone_pass en wordlist de las fechas 
            print(green + " Saving password number: " + white + str(date + 1))
            filename = "..\\OUTPUTS\\Phone_Alphabetic_Wordlist.txt"
            file = open(filename,"a")
            file.write(phone_pass + "\n")
            file.close()
            phone_pass = ""
        print(cian + " Your wordlist relevants dates or numbers have been created.")

    print(green + " Creating a ALPHANUMERIC PHONE wordlist from words DATA.txt\n")
    PAUSE()
    # Comprueba si hay datos en la opcion 1 palabras de DATA.txt
    if str(bool(words)) == "False" :
        print(red + " [!] Sorry but your words list are empty. Select the option 1 and create the main wordlist.")
        time.sleep(3)
    else:
        print(green + " Your main words are the next: " + white + str(words))
        filecheck="..\\OUTPUTS\\Phone_Alphabetic_Wordlist_words.txt"
        CHECK_FILE()
        phone_pass = ""
        for word in range(len(words)):
            for caracter in range(len(words[word])):
                alpha = str(words[word][caracter])
                alpha = alpha.lower()
                if alpha == "a":
                    phone_pass += "2"
                elif alpha == "b":
                    phone_pass += "2"
                elif alpha == "c":
                    phone_pass += "2"
                elif alpha == "d":
                    phone_pass += "3"
                elif alpha == "e":
                    phone_pass += "3"
                elif alpha == "f":
                    phone_pass += "3"
                elif alpha == "g":
                    phone_pass += "4"
                elif alpha == "h":
                    phone_pass += "4"
                elif alpha == "i":
                    phone_pass += "4"
                elif alpha == "j":
                    phone_pass += "5"
                elif alpha == "k":
                    phone_pass += "5"
                elif alpha == "l":
                    phone_pass += "5"
                elif alpha == "m":
                    phone_pass += "6"
                elif alpha == "n":
                    phone_pass += "6"
                elif alpha == "o":
                    phone_pass += "6"
                elif alpha == "p":
                    phone_pass += "7"
                elif alpha == "q":
                    phone_pass += "7"
                elif alpha == "r":
                    phone_pass += "7"
                elif alpha == "s":
                    phone_pass += "7"
                elif alpha == "t":
                    phone_pass += "8"
                elif alpha == "u":
                    phone_pass += "8"
                elif alpha == "v":
                    phone_pass += "8"
                elif alpha == "w":
                    phone_pass += "9"
                elif alpha == "x":
                    phone_pass += "9"
                elif alpha == "y":
                    phone_pass += "9"
                elif alpha == "z":
                    phone_pass += "9"
                elif alpha == "+":
                    phone_pass += "0"
                elif alpha == " ":
                    phone_pass += "1"
                else:
                    phone_pass += alpha                    
            # Copia phone_pass en wordlist_words
            print(green + " Saving password number: " + white + str(word + 1))
            filename = "..\\OUTPUTS\\Phone_Alphabetic_Wordlist_words.txt"
            file = open(filename,"a")
            file.write(phone_pass + "\n")
            file.close()
            phone_pass = ""
        print(cian + " Your wordlist main words have been created.")

        


def DATES_CH():
    print(green + " Creating a RELEVANT DATES VARIANTS wordlist\n")
    PAUSE()
    global filecheck
    filecheck="..\\OUTPUTS\\Dates_variants_Wordlist.txt"
    CHECK_FILE()
    # Comprueba si hay datos en la opcion 2 de fechas relevantes
    if str(bool(dates)) == "False" :
        print(red + " [!] Sorry but your dates list are empty. Select the option 2 and add relevants dates")
        time.sleep(3)
    else:
        print(green + " Your dates and number list are the next: " + white + str(dates))
        # Crea variantes de las fechas
        print(yellow + " Saving the next password dates numbers: " + white + str(dates))
        filename = "..\\OUTPUTS\\Dates_variants_Wordlist.txt"
        file = open(filename,"a")
        date_var = ""
        # Copia básica de fechas con [] y ()
        for item in range(len(dates)):
            for symbol in range(len(date_var_open)):
                date_var += date_var_open[symbol]
                date_var += dates[item]
                date_var += date_var_close[symbol]
                file.write(date_var + "\n")
                date_var = ""
        file.close()
        # Copia formato [ DD-Mes-AA ] o [ DD-Mes-AAAA ] y ( DD-Mes-AA ) o ( DD-Mes-AAAA )
        date_var = ""
        file = open(filename,"a")
        for item in range(len(dates)):

            if len(dates[item]) < 4:
                print(purple_B + " Skipping: " + purple + dates[item] + ", invalid date format.")
                continue
            suma_mes = str(dates[item][2]) + str(dates[item][3])
            suma_mes = int(suma_mes)
            if suma_mes > 12: # Si es mayor que Diciembre se salta la fecha
                print(purple_B + " Skipping: " + purple + dates[item] + ", invalid month.")
                continue
            
            else:
                month = dates[item][2] + dates[item][3]

                for symbol in range(len(date_var_open)):
            
                    if len(dates[item]) == 6:
                        date_var += date_var_open[symbol]
                        date_var += dates[item][0]
                        date_var += dates[item][1]
                        date_var += "-"
                        date_var += months.get(month)
                        date_var += "-"
                        date_var += dates[item][4]
                        date_var += dates[item][5]
                        date_var += date_var_close[symbol]
                        file.write(date_var + "\n")
                        date_var = ""
                
                    elif len(dates[item]) == 8:
                        date_var += date_var_open[symbol]
                        date_var += dates[item][0]
                        date_var += dates[item][1]
                        date_var += "-"
                        date_var += months.get(month)
                        date_var += "-"
                        date_var += dates[item][4]
                        date_var += dates[item][5]
                        date_var += dates[item][6]
                        date_var += dates[item][7]
                        date_var += date_var_close[symbol]
                        file.write(date_var + "\n")
                        date_var = ""
                
                    else:                
                        print(purple_B + " Skipping: " + purple + dates[item] + " is not a date format.")
                
        file.close()
        print(cian + " Your Relevants Dates and Numbers wordlist was created.")




def LOCKERS():
    words_without_vowels = []
    print(green + " Creating a MENTAL LOCKERS wordlist...\n")
    PAUSE()
    # Lee la lista words (contiene DATA.txt) y comprueba si está vacía.
    if str(bool(words)) == "False" :
        print(red + " [!] Sorry but you must select the option 1 to generate the main wordlist.")
    else:
        print(yellow + " Your words to convert are the next: " + white + str(words))
        global filecheck
        filecheck = "..\\OUTPUTS\\Mental_Lockers_Wordlist.txt"
        CHECK_FILE()
        # Quita las vocales de la lista words.
        for word in range(len(words)): # recorre lista de palabras DATA.txt
            correcto = True
            for word1 in range(len(locker_words)): # recorre lista de palabras que no están en tabla LOCKER
                if (locker_words[word1] in words[word]): 
                    index_words = int(words[word].index(locker_words[word1]))
                    if index_words == 0:
                        print(red + " [!] The word '" + red_B + words[word] + red + "' is not OK. Because contains '{}' letter.".format(locker_words[word1]))
                        correcto = False
                        break
                    else:
                        if str(words[word][index_words-1]) == "c" or str(words[word][index_words-1]) == "C":
                            continue
                        else:
                            print(red + " [!] The word '" + red_B + words[word] + red + "' is not OK. Because contains '{}' letter.".format(locker_words[word1]))
                            correcto = False
                            break
                        
            if correcto == True:
                out_vowel = ""
                for caracter in range(len(words[word])):
                    if words[word][caracter] in vocals:
                        continue
                    elif words[word][caracter] == " ":
                        continue
                    else:
                        out_vowel += words[word][caracter]
                out_vowel = out_vowel.lower()        
                words_without_vowels.append(out_vowel)
                print(purple_B + " Word added: " + purple + words[word])
        # Generando números y guardando en archivo
        print(green + " Saving the wordlist with number passwords...")
        filename = "..\\OUTPUTS\\Mental_Lockers_Wordlist.txt"
        file = open(filename,"a")
        for word in range(len(words_without_vowels)):
            out_number=""
            for caracter in range(len(words_without_vowels[word])):
                if words_without_vowels[word][caracter] == "h" and words_without_vowels[word][caracter-1] == "c":
                    out_number = out_number.removesuffix("4")
                    out_number += "8"
                else:
                    out_number += locker_list[words_without_vowels[word][caracter]]
            file.write(out_number + "\n")
        file.close()
        print(cian + " The Lockers wordlists was created.")




def ETHEREUM():
    print(green + " Creating a ETHEREUM wordlist...\n")
    PAUSE()
    print(yellow + " The wordlist have permutations with " + white + str(option) + yellow + " words.")
    # Lee el diccionario BIP39 en ingles.
    bip39_var=""
    bip39 = []
    filename = "..\\ETHEREUM\\english.txt"
    file = open(filename,"r")
    for word in file:
        bip39_var = word
        bip39_var = bip39_var.removesuffix("\n")
        bip39.append(bip39_var)
    file.close()
    # Creamos las permutaciones elegidas y las guardamos en wordlist
    permutations = list(itertools.permutations(bip39, option))
    print(green + " Generando permutaciones de " + white + str(option) + green + " words...")
    # Guardando permutations en wordlist txt file
    output_name = "Ethereum_Wordlist_" + str(option) + "_words.txt"
    filename = "..\\OUTPUTS\\" + output_name
    global filecheck
    filecheck = "..\\OUTPUTS\\" + output_name
    CHECK_FILE()
    file = open(filename, "a")
    for permuta in permutations:
        permuta_var = ""
        for subpermuta in permuta:
            permuta_var += subpermuta + "-"
        permuta_var = permuta_var[:-1]
        file.write(permuta_var + "\n")
    file.close()





def MIXING():
    print(green + " Creating a WORDS & DATES MIXING wordlist...\n")
    PAUSE()
    # Lee la lista words (contiene DATA.txt) y comprueba si está vacía.
    if str(bool(words)) == "False" or str(bool(dates)) == "False" :
        print(red + " [!] Sorry but you must select the option 1 to generate the main wordlist and afther that introduce relevants dates in option 2")
        time.sleep(3)
    else:
        global filecheck
        filecheck="..\\OUTPUTS\\Mixing_wordlist.txt"
        CHECK_FILE()
        print(yellow + " Your words to mixing are the next: " + white + '-'.join(words))
        print(yellow + " Your dates to mixing are the next: " + white + '-'.join(dates))
        #Creando el diccionario mezclado y guardando en wordlist
        filename="..\\OUTPUTS\\Mixing_wordlist.txt"
        file=open(filename, "a")
        print(green + " Creating mixing wordlist...")
        PAUSE()
        for word in range(len(words)):
            for date in range(len(dates)):
                mixing = ""
                if len(words[word]) > len(dates[date]):
                    for count in range(len(words[word])):
                        mixing += words[word][count]
                        if count < len(dates[date]):
                            mixing += dates[date][count]
                    file.write(mixing + "\n")
                
                if len(words[word]) < len(dates[date]):
                    for count in range(len(dates[date])):
                        mixing += dates[date][count]
                        if count < len(words[word]):
                            mixing += words[word][count]
                    file.write(mixing + "\n")
        file.close()
        print(cian + " The Mixing wordlist was created.")



        
def LE_CIFRE():
    print(green + " Creating CIPHER wordlist...\n")
    PAUSE()
    # Lee la lista words (contiene DATA.txt) y comprueba si está vacía.
    if str(bool(words)) == "False" :
        print(red + " [!] Sorry but you must select the option 1 to generate the main wordlist.")
    else:
        global filecheck
        filecheck=filename = "..\\OUTPUTS\\Le_cifre_wordlist.txt"
        CHECK_FILE()
        filename = "..\\OUTPUTS\\Le_cifre_wordlist.txt"
        file = open(filename, "a")
        # BASE64, MD5, SHA1, SHA224, SHA256, SHA384, SHA512, BLAKE2B, BLAKE2S, HEXADECIMAL, ROT13
        for word in range(len(words)):
            txt_string = words[word]
            txt_bytes = txt_string.encode('utf-8')
            txt_md5 = hashlib.md5(txt_bytes)
            txt_sha1 = hashlib.sha1(txt_bytes)
            txt_sha224 = hashlib.sha224(txt_bytes)
            txt_sha256 = hashlib.sha256(txt_bytes)
            txt_sha384 = hashlib.sha384(txt_bytes)
            txt_sha512 = hashlib.sha512(txt_bytes)
            txt_blake2b = hashlib.blake2b(txt_bytes)
            txt_blake2s = hashlib.blake2s(txt_bytes)
            txt_b64 = base64.b64encode(txt_bytes)
            txt_hex = codecs.encode(txt_bytes, "hex")
            txt_hex = txt_hex.decode()
            txt_rot13 = codecs.encode(txt_string, 'rot_13')
            txt_b64_string = txt_b64.decode('utf-8')
            file.write(txt_b64_string + "\n")
            file.write(txt_md5.hexdigest() + "\n")
            file.write(txt_sha1.hexdigest() + "\n")
            file.write(txt_sha256.hexdigest() + "\n")
            file.write(txt_sha224.hexdigest() + "\n")
            file.write(txt_sha384.hexdigest() + "\n")
            file.write(txt_sha512.hexdigest() + "\n")
            file.write(txt_blake2b.hexdigest() + "\n")
            file.write(txt_blake2s.hexdigest() + "\n")
            file.write(txt_hex + "\n")
            file.write(txt_rot13 + "\n")
        file.close()
        print(cian + " The Cipher wordlist was created.")





        
#################
## MAIN SOURCE ##
#################




counter=0
while counter == 0:
    MENU()
    if option == "1":
        print(blue + "\n Main Letter, Bruce Schneier and Only Consonants wordlists.")
        print(blue + " ----------------------------------------------------------\n")
        print(yellow + """ This is the most important part from HTW. Here we created a wordlists using DATA.txt file like the next information: """ + yellow_B + """
 Main Letter: """ + white + """ The first letter in the word or phrase. And the reverse mode.""" + yellow_B + """
 Bruce Schneier: """ + white + """ The 2 first letters in a word or passphrase. And the reverse mode.""" + yellow_B + """
 Only Consonant: """ + white + """ Only the consonants in the word or phrase. And reverse mode.""" + yellow_B + """
 Plus Symbols: """ + white + """ Main, Only and Bruce with symbols in the list symbols. Mixing system. And reverse mode.""" + yellow_B + """
 Plus Dates or Numbers: """ + white + """ Main, Only, Bruce and symbols plus option 2 dates. Mixing system. And reverse mode.""")
        WAIT()
        READ()
        MAIN_LETTER()
        BRUCE_SCHNEIER()
        ONLY_CONSONANTS()
        print (cian + " The wordlist HTC_wordlist have been created successfully with " + cian_B + str(len(uniq_list)) + cian + " words.")
        WAIT()




    elif option == "2":
        print(blue + "\n INSERT RELEVANTS DATES or NUMBERS.")
        print(blue + " ----------------------------------\n")
        print(white + " You must set the relevants dates from Pentesting attact customer.")
        print(white + " For example: Birth dates, married or other anniversary, saints dates...")
        print(white + " Some special dates appear authomatically togheter the passwor.\n")
        print(yellow + " How many dates or numbers do you want to introduce?: " + white, end="")
        dates_number=int(input())
        dates=[]
        for i in range(dates_number):
            print(purple + f"   Add the date or number {i+1}: " + white, end="")
            date=input()
            dates.append(date)
        print (cian + " The list of dates and numbers are the next: ", ', '.join(dates))
        WAIT()




    elif option == "3":
        print(blue + "\n WELLCOME TO DICEWARE WORDLIST CREATOR.")
        print(" --------------------------------------\n")
        print(white + " DiceWare is a method to create passwords. It´s very simple. You must create a wordlist. If the wordlist is big, then better, more strong will be your password.")
        print(yellow_B + """ For example:""" + yellow + """ If you create a list like the next:\n
            1. John
            2. hello
            3. Peter
            4. home
            5. ant
            6. easy\n""")

        print(white + """ Then you throw a dice. How many times do you throw the dice? If you want a password with 3 words then 3 times, if you want a password with 8 words then 8 times.
 If you throw a dice 3 times and the numbers are 1, 4, 5 then password will be Johnhomeant.""")
        WAIT()
        diceware=[]
        diceware_fussion=[]
        contador=0
        while contador == 0:
            # Lee DICEWARE wordlists y realiza permutaciones elegidas
            print(green + " Availables DiceWare wordlists..\n")
            os.system('dir ..\DICEWARE /b')
            print(yellow + " Select your DICEWARE wordlists (example: spanish.txt): " + white, end="")
            selection=str(input()) # Elige el diccionario
            selection_folder="..\\DICEWARE\\"
            selection_new="..\\DICEWARE\\" + selection
            CHECK_BASIC()
            if file_dont_exist == 0:
                print(yellow + " Select the permutations number: " + white, end="")
                r=int(input()) # Elige las permutaciones
                filecheck = "..\\OUTPUTS\\HTC_wordlist_DICEWARE_" + selection + "_" + str(r) + ".txt"
                CHECK_FILE()
                # Pasa el diccionario a la lista diceware
                my_file = open(selection_new, "r")
                data = my_file.read()
                diceware = data.split('\n')
                my_file.close()

                # Crea wordlist con permutaciones dadas
                permutations = list(itertools.permutations(diceware, r))

                # Fusionamos permutaciones de DICEWARE list
                for item_a in range (len(permutations)):
                    for item_b in range (len(permutations[item_a])):
                        new_list+=permutations[item_a][item_b]
                    diceware_fussion.append(new_list)
                    new_list=""
                    
                # Guardamos fusiones de lista diceware_fussion en fichero
                selection="..\\OUTPUTS\\HTC_wordlist_DICEWARE_" + selection + "_" + str(r) + ".txt"
                file=open(selection,"a")
                for item in range(len(diceware_fussion)):
                    file.write(diceware_fussion[item]+"\n")
                file.close()
                print(cian + " The wordlist " + selection + " have been created successfully.")
                contador=1
            WAIT()




    # CREACION DE WORDLISTS AL ESTILO HACKER        
    elif option == "4":                  
        print(blue + "\n WELLCOME to H4CK3R W0RD1I5T5 creator.")
        print(" -------------------------------------\n")
        print(white + " Here you can create your" + white_B + " Hacker Wordlist" + white + ". You must select a wordlist in your directory and choose the method to convert that normal wordlist in a H4CK3R password to your Pentesting Brute Force.\n")
        print(yellow + """    A. Select the wordlist.
    B. Select type [letter:change]

    1. hacker_long:""" + white + """ L:1, l:1 , i:1 , I:1, E:3, e:3, A:4 ,a:4, S:5, s:5, T:7, t:7, B:8, b:8, O:0, o:0 """ + yellow + """
    2. hacker_short:""" + white + """ L:1, l:1 , i:1 , I:1, E:3, e:3, A:4 ,a:4, S:5, s:5, O:0, o:0 """ + yellow + """
    3. hacker_long_plus:""" + white + """ Same that 1 but changuing ==> A:@, a:@. S:$, s:$, E:€, e:€ """ + yellow + """
    4. hacker_short_plus:""" + white + """ Same that 2 but changuing ==> A:@, a:@. S:$, s:$, E:€, e:€ """ + yellow + """
""")
        # Lee wordlists de la carpeta H4CK3RS
        print(green + " Availables wordlists to convert it.\n")
        os.system('dir ..\H4CK3RS /b')
        print(yellow + " STEP A. Select your wordlists to convert (example: spanish.txt): " + white, end="")
        selection=str(input()) # Elige el diccionario
        selection_folder="..\\H4CK3RS\\"
        selection_new="..\\H4CK3RS\\" + selection
        CHECK_BASIC()
        if file_dont_exist == 0:
            print(yellow + " STEP B. Select the type (1 to 4): " + white, end="")
            selection_type=int(input()) # Elige diccionario largo o corto
            if selection_type == 1:
                hacker_wordlist = hacker_long
            elif selection_type == 2:
                hacker_wordlist = hacker_short
            elif selection_type == 3:
                hacker_wordlist = hacker_long_plus
            elif selection_type == 4:
                hacker_wordlist = hacker_short_plus
            H4CK3R()
            contador=1
        WAIT()





    elif option == "5":                  
        print(blue + "\n WELLCOME to wordlist prefix and sufix creator.")
        print(blue + " ----------------------------------------------\n")
        print(yellow + """ In that option you must select any of your wordlist in your hard disk. Then you can created a suffix or preffix new wordlist. For example,
 if the wordlist selected have the password """ + yellow_B + """P@assw0rd""" + yellow + """ the script will create a new password named """ + yellow_B + """P@ssw0rdFB""" + yellow + """. """ + yellow_B + """FB""" + yellow +  """ is a suffix that mean """ + yellow_B + """FaceBook""" + yellow + """ and
 the script will create other new password name """ + yellow_B + """FBP@ssw0rd""" + yellow + """ with the same words but like a suffix.

 You can edit and add new suffix and preffix in the file """ + yellow_B + """suf_and_pref.txt""" + yellow + """ in the folder """ + yellow_B + """SUF_AND_PREF. """)
        print(green + " Availables wordlists to convert it.\n")
        print(green_B)
        os.system('dir ..\SUF_AND_PREF /b')
        print(yellow + " Select your wordlists to convert (example: spanish.txt): " + white, end="")
        selection=str(input()) # Elige el diccionario
        selection_folder="..\\SUF_AND_PREF\\"
        selection_new="..\\SUF_AND_PREF\\" + selection
        CHECK_BASIC()
        if file_dont_exist == 0:
            SUF_PREF()
            print(cian + " The SUF_AND_PREF wordlist have been created.")
        WAIT()




    elif option == "6":
        print(blue + "\n WELLCOME to Sudoku wordlist creator.")
        print(blue + " ------------------------------------\n")
        print(yellow + """ You must have a SUDOKU complete and save it in the folder """ + yellow_B + """SUDOKU""" + yellow + """. We have the file """ + yellow_B + """sudoku_test.txt""" + yellow + """ like a example. That SUDOKU is
 the wikipedia example (https://es.wikipedia.org/wiki/Sudoku): """ + white + """

                                                colums  | 012345678
                                                --------------------
                                                rows  0 | 534678912
                                                      1 | 672195348
                                                      2 | 198342567
                                                      3 | 859761423
                                                      4 | 426853791
                                                      5 | 713924856
                                                      6 | 961537284
                                                      7 | 287419635
                                                      8 | 345286179

""" + yellow + """ Then you must select a file inside the folder """ + yellow_B + """patrones""" + yellow + """ with a pattern like used in mobile phones. We have the example named """ + yellow_B + """pattern_u.txt""" + yellow + """ to test that
 SUDOKU. The content of that pattern file is:""" + white + """

                                                            [COLUM:ROW]
                """ + purple + """--> Here start the pattern                                                 Here end the pattern -->""" + white + """
                0:0 1:0 2:0 3:0 4:0 5:0 6:0 7:0 8:0 8:1 8:2 8:3 8:4 8:5 8:6 8:7 8:8 7:8 6:8 5:8 4:8 3:8 2:8 1:8 0:8

    PASSWORD:    5   6   1   8   4   7   9   2   3   4   5   2   8   6   1   7   9   5   4   6   1   3   7   8   2 \n""")
        # Lee wordlists de la SUDOKU
        print(green + " Availables wordlists to convert it.\n")
        print(green_B)
        os.system('dir ..\SUDOKU /b')
        print(yellow + " Select your wordlists to convert (example: spanish.txt): " + white, end="")
        selection=str(input()) # Elige el diccionario
        selection_folder="..\\SUDOKU\\"
        selection_new="..\\SUDOKU\\" + selection
        CHECK_BASIC()
        if file_dont_exist == 0:
            SUDOKU()
            print(cian + " Your SUDOKU wordlist was created.")
        WAIT()





    elif option == "7":
        print(blue + "\n WELLCOME to Emojis wordlist creator.")
        print(blue + " ------------------------------------\n")
        print(white + """ A lot of users use emojis to create your passwords. Some typicals emojis are:""" + yellow + """

                                            :) to smile or happy
                                            :( to sad
                                            :O to amazed
                                            :| to serious""" + white + """
                                            
  If any people have a password like """ + white_B + """p4ssw0r""" + white + """ with a emoji the password could be """ + white_B + """p4ssw0r:)""" + white + """
  Now you can select a wordlist and add suffix and preffix emojis.
""")
        print(green + " Availables wordlists to convert it.\n")
        os.system('dir ..\\EMOJIS\\ /b')
        print(yellow + " Select your wordlists to convert (example: spanish.txt): " + white, end="")
        selection=str(input()) # Elige el diccionario
        selection_folder="..\\EMOJIS\\"
        selection_new="..\\EMOJIS\\" + selection
        CHECK_BASIC()
        if file_dont_exist == 0:
            EMOJIS()
            print(cian + " Your Emoji wordlists was created.")
        WAIT()





    elif option == "8":
        print(blue + "\n WELLCOME to KEYBOARD PATTERNS wordlist creator.")
        print(blue + " -----------------------------------------------\n")
        print(white + """ To create KEYBOARD PATTERNS like """ + white_B + """qwerty""" + white + """ i recommend the tool """ + white_B + """Keyboard Walk Generators""" + white + """ by Rich5

""" + yellow + """ You can download from the next repository:""" + yellow_B + """ https://github.com/Rich5/Keyboard-Walk-Generators
""")
        
        WAIT()





    elif option == "9":
        print(blue + "\n WELLCOME to PASSWORD CARD wordlist creator.")
        print(blue + " -------------------------------------------\n")
        print(white + """ If you have a website like """ + white_B + """ebay.com""" + white + """ if you want to find the password if the user have a """ + white_B + """password card""" + white + """ then you must search the
 position and the word, like coordenates. Here a example with a little """ + white_B + """password card""" + white + """ and the website """ + white_B + """hi.es""" + white + """:""" + yellow + """

                            -------------------------------------
                            |   | A to M | N to P | Q to Z | .  |
                            -------------------------------------
                            | 1 |  EE    |   Kj   |   12   | 34 |
                            -------------------------------------
                            | 2 |  dk    |  mn    |   33   | 3? |
                            -------------------------------------
                            | 3 |  pp    |  k=    |   3?   | 2! |
                            -------------------------------------
                            | 4 |  ii    |  iI    |   I!   | )) |
                            -------------------------------------
                            | 5 |  kK    |  CA    |   iw   | ?U |
                            -------------------------------------
                            
""" + yellow + """ The password is: """ + yellow_B + """EEdk2!iiiw   (h = 1 = EE, i = 2 = dk, . = 3 = 2!, e = 4 = ii, s = 5 = iw)""")
        # Seleccionar listado de paginas webs en el disco duro
        print(green + " Availables wordlists to convert it.\n")
        os.system('dir ..\\PASSWORD_CARD\\ /b')
        print(yellow + " Select your wordlists to convert (example: spanish.txt): " + white, end="")
        selection=str(input()) # Elige el diccionario
        selection_folder="..\\PASSWORD_CARD\\"
        selection_new="..\\PASSWORD_CARD\\" + selection
        CHECK_BASIC()
        if file_dont_exist == 0:
            PASSWORD_CARD()
            print(cian + " Your Password Card wordlist was created.")
        WAIT()




    
    elif option == "10":
        print(blue + "\n WELLCOME to PHONETIC MUSCLE MEMORY creator.")
        print(blue + " -------------------------------------------\n")
        print(white + """ Click [ENTER] to generate a random password and when appear a password that have a "phonetic sense" then you click [Y] + [ENTER] to exit
 For example: The password "9938:Kmd?=8((" dont have any sense, it is strong but difficult to memorize. However the password "RakpuuKzien33==>"
 have a phonetic sense and then it is more easy to memorize.

 Sometimes you must wait because the random password search that have some vowels in the password generate.""")

        print(yellow + " 1. Create a PHONETIC MUSCLE MEMORY random word.")
        print(" 2. Create a PHONETIC MUSCLE MEMORY random list to brute force attack.")
        print("\n Choose 1 or 2: " + white, end="")
        option = input()
        if option == "1":
            muscle_list = 0
            MUSCLE()
        elif option == "2":
            muscle_list = 1
            print(purple + " How many words do you have your wordlists? " + white, end="")
            muscle_words = int(input())
            MUSCLE()
        else:
            muscle_list = 0
            MUSCLE()
        WAIT()

    elif option == "11":
        print(blue + "\n WELLCOME to ALPHANUMERIC PHONE creator.")
        print(blue + " ---------------------------------------\n")        
        print(yellow + """ Do you remember your Alphanumeric Phone? Here is it. """ + white + """

                            =======================
                            ||  1  ||  2  ||  3  ||
                            ||     || ABC || DEF ||
                            =======================
                            ||  4  ||  5  ||  6  ||
                            || GHI || JKL || MNO ||
                            =======================
                            ||  7  ||  8  ||  9  ||
                            || PQRS|| TUV || WXYZ||
                            =======================
                            ||  *  ||  0  ||  #  ||
                            ||     ||  +  ||     ||
                            ======================= """ + yellow + """
\n Then if you have a important date like""" + yellow_B + """ 30/10/1978""" + yellow + """ you can convert it using the Alphanumeric Phone in """ + yellow_B + """D+1+1WPT.
""" + yellow + """
 If you have a password from DATA.txt (option 1) too. For example, the password """ + yellow_B + """ Pubdlfdlqf """ + yellow + """ the conversion will be """ + yellow_B + """7823533573""" 
+ red + """\n [!] You must add in the option number 2 relevant dates.""")
        PHONE()
        WAIT()





    elif option == "12":
        print(blue + "\n WELLCOME to RELEVANTS DATES wordlist creator.")
        print(blue + " ---------------------------------------------\n")
        print(yellow + """ To use that option you need to put relevants dates in the option number 2. Then that dates are converted like the example:
""" + white + """
                    EXAMPLE DATE: 22101990  (DDMMAAAA 22 de Octubre de 1990)

                                    [22-Octubre-1990]
                                    [22-Octubre-90]
                                    (22-Octubre-1990)
                                    (22-Octubre-90)\n""")
        DATES_CH()
        WAIT()




        
    elif option == "13" or option == "12+1":
        print(blue + "\n WELLCOME to the information about the number 13.")
        print(blue + " ------------------------------------------------\n")
        print(yellow + """ 1. Number 13 is the Alfred Hitchcock film name that never premiere.
 2. Paraskevidekatriaphobia
 3. Friday 13th fallen the Knights Templars
 4. Superstitions or Divine number?
 5. Hammurabi code ommited 13 rule
 6. 12 is the perfect number (Sumerians)
 7. Judas, 13, betray Jesus
 8. 13 is connecting with the Universes and it´s so divine
 9. Major arcana in tarot
 10. The connection to your guardian angel
 11. Tuesday, 13, married? embark?
 12. Bet 13 in the casino
 13. Hindi, Terah, soul
 14. 13 represented feminity in some cultures
 15. In the Coperos religion (Brazil) is the God number\n""")

        WAIT()






    elif option == "14":
        print(blue + "\n WELLCOME to MENTAL LOCKERS wordlist creator.")
        print(blue + " --------------------------------------------\n")
        print(yellow + """ MENTAL LOCKERS wordlist take the""" + yellow_B + """ DATA.txt""" + yellow + """ information and delete all the vowels and chage the others with the next table conversion:
""" + white + """
            =================================================================================
            |  t,d  |  n,ñ  |  m  |  c,k,q  |   L  |  s,z  |  f  |  ch,j,g  |  v,b,p  |  r  |
            =================================================================================
            |   1   |   2   |  3  |    4    |   5  |   6   |  7  |     8    |    9    |  0  |
            =================================================================================
""" + yellow + """
            Example: Frankenstein ==> Frnknstn ==> """ + yellow_B + """70242612

""")
        LOCKERS()
        WAIT()





    elif option == "15":
        print(blue + "\n WELLCOME to ETHEREUM wordlist creator.")
        print(blue + " --------------------------------------\n")
        print(yellow + """ That method to create passwords is """ + yellow_B + """using a wordlist with 2048 words""" + yellow + """. Then you can choose the number of words that you want to your password
 and appear separated from "-". The normal password seed in cryptocurrencies wallets are 12 or 24 but to create a password you can created the
 combinations that you want.
""" + white + """
 Example: if you choose 3 words then the wordlist will have all the permutations with 3 words "entry-magic-horse" "entry-blast-hollow" ...
""" + red + """
 [!] if you select a lot of number of words, perhaps the computer crash because there are a lot of number of permutations.""" + red_B + """ I recomended start
 with 2 words and if you try 3 or more CLOSE ALL YOUR PROGRAMS BEFORE.
""")
        print(yellow + " Select the words to permutations: " + white, end="")
        option = int(input())
        ETHEREUM()
        print(cian + " The wordlist Ethereum was created.")
        WAIT()





    elif option == "16":
        print(blue + "\n WELLCOME to WORDS & NUMBERS MIXING wordlist creator.")
        print(blue + " ----------------------------------------------------\n")
        print(yellow + """ Mix numbers and words, simple. If a possible password is """ + yellow_B + """John""" + yellow + """ and a relevant date is """ + yellow_B + """230975""" + yellow + """ the result is: """ + yellow_B + """J2o3h0n975 """)
        MIXING()
        WAIT()





    elif option == "17":
        print(blue + "\n WELLCOME to CIPHER PASSWORD wordlist creator.")
        print(blue + " ---------------------------------------------\n")
        print(yellow + """ If you want to create an strong password using a weak password with the cipher method it is possible. Here you have some examples
 using the password """ + yellow_B + """Juan23:
""" + white + """                 
                    Base64 ==> SnVhbjIz
                    ROT13 o cifrado Cesar ==>  Whna23
                    MD5 ==> bbd537d497f86dacd245fdb10b55231
                    SHA1 ==> 06e22539003f130cbb447af6994c9066ab327303
                    HEXADECIMAL ==> 4a75616e3233
""")

        LE_CIFRE()
        WAIT()





    elif option == "0" or option == "exit" or option == "EXIT" or option == "quit" or option == "QUIT":
        print(purple + " \n Thanks to use" + purple_B + " Hack The Word " + purple + "by " + cian + "Deckcard23")
        print(purple + " Follow me in Twitter " + blue_B + "@rickdeckard23" + white)
        counter=1
        break
    
    else:
        print(red + " [!] The option isn´t correct, try again." + white)
        time.sleep(3)
