import os
import sys
#!/usr/bin/python
import time
from collections import OrderedDict

print "Start : %s" % time.ctime()
time.sleep( 2 )
print "End : %s" % time.ctime()

todo={}
country=[]
capitals=[]

def question():
    limpiar()
    val3=raw_input("You want to re- enter the data again and y/n: " )
    val3=val3.lower()
    if val3 == "y":
        Country()
    elif val3== "n":
        menu()
    else:
        print "your data is not valid"
        
        question()

def Country():
    var=True
    while var == True:
        val1 =raw_input("<<<Enter to Country>>>: ")
        if str(val1).isalpha() == True or " " in val1:
            val1 = val1.title()
            country.append(val1)
            var = False
        else:
            print "your data is not valid"
            var = True
    vor = True
    while vor==True:
        val2 =raw_input("<<<Enter to Capitals>>>: ")
        if str(val2).isalpha() == True or " " in val2:
            val2 =  val2.title()
            capitals.append(val2)
            vor = False
        else:
            print "your data is not valid"
            vor = True
    todo [val1] = val2
    limpiar
    question()    
    menu()


def Countries_List():
    limpiar()
    print "==================="
    print "#####COUNTRIES#####"
    print "==================="

    for i in country:
        print i.title() 
    raw_input("<<<Enter to Continue>>>")
    
    menu()

def Capitals_List():
    limpiar()
    print "================"
    print "####CAPITALS####"
    print "================"

    for i in capitals:
        print i.title() 
    raw_input("<<<Enter to Continue>>>")
    menu()

def Capitals_and_Countries():
    limpiar()
    print "==================================="
    print "#COUNTRIES#".center(15)+"#CAPITALS#".center(15)
    print "==================================="
    for i in todo:
        print i.center(15),todo[i].center(15)

    raw_input("<<<Enter to Continue>>>")
    
    menu()

def All_Ordered():
    limpiar()
    print "          --All Ordered--          "
    print "==================================="
    print "#COUNTRIES#".center(15)+"#CAPITALS#".center(15)
    print "==================================="
    ordered = OrderedDict(sorted(todo.items(), key=lambda x: x[1:]))
    for key, value in ordered.items():
        print key.center(20) + value.center(10)
    raw_input("Press Enter to Continue")    
    
    menu()
   
def All_Mail():
    print "dsfa"



def limpiar():
    os.system("reset")
def salir():
    sys.exit()
    

def menu():
    limpiar()
    print "========================================================"                   
    print "$                  Countries and Capitals              $"
    print "$                  What go do you                      $"
    print "$                  1.) Country                         $"
    print "$                  2.) Countries List                  $"
    print "$                  3.) Capitals List                   $"
    print "$                  4.) Capitals and Countries          $"
    print "$                  5.) All Ordered                     $"
    print "$                  6.) All Mail                        $"
    print "$                  7.) exit                            $"
    print "========================================================"

    menu = raw_input("Insert to opcion: ")

    if menu == "1" or menu == "country":
        Country()
    elif menu == "2" or menu == "countries list":
        Countries_List()
    elif menu == "3" or menu == "capitals list":
        Capitals_List()
    elif menu == "4" or menu == "capitals and countries":
        Capitals_and_Countries()
    elif menu == "5" or menu == "all ordered":
        All_Ordered()
    elif menu == "6" or menu == "all mail":
        All_Mail
    elif menu == "7":
        salir()
       
menu()