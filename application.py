import os
import sys
#!/usr/bin/python
import time

print "Start : %s" % time.ctime()
time.sleep( 2 )
print "End : %s" % time.ctime()

todo={}
country=[]
capitals=[]

def question():
    val3=raw_input("desea volver a ingrear los datos otra vez y/n: " )
    val3=val3.lower()
    if val3 == "y":
        Insert_Country()
    elif val3== "n":
        menu()
    else:
        print "no es valido"
        limpiar()
        question()

def Insert_Country():
    var=True
    while var == True:
        val1 =raw_input("enter to Country: ")
        if str(val1).isalpha() == True or " " in val1:
            country.append(val1)
            var = False
        else:
            print "su dato no es valido"
            var = True
    vor = True
    while vor==True:
        val2 =raw_input("enter to Capitals: ")
        if str(val2).isalpha() == True or " " in val2:
            capitals.append(val2)
            vor = False
        else:
            print "su dato no es valido"
            vor = True
    todo [val1] = val2
    limpiar
    question()    
    menu()


def Countries_List():
    limpiar()
    for i in country:
        print i 
    raw_input("presione enter")
    
    menu()

def Capitals_List():
    print "Here shows the Capitals and Countries"
    for i in capitals:
        print i 
    raw_input("presione enter")
    menu()

def Capitals_and_Countries():
  
    for i in todo:
        print i, todo[i]
    raw_input("enter to continue")
    limpiar()
    menu()
   

def limpiar():
    os.system("reset")


def salir():
    sys.exit()
    

def menu():
    limpiar()
    print "Countries and Capitals"
    print "What go do you"
    print "1.) Insert Country"
    print "2.) Countries List"
    print "3.) Capitals List"
    print "4.) Capitals and Countries"
    print "5.) Exit"
    menu = raw_input("Insert to opcion: ")

    if menu == "1":
        Insert_Country()
    elif menu == "2":
        Countries_List()
    elif menu == "3":
        Capitals_List()
    elif menu == "4":
        Capitals_and_Countries()
    elif menu == "5":
        salir()
       
menu()