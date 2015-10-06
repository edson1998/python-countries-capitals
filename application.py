#!/usr/bin/python

import os
import sys
import smtplib
import getpass
import time
from collections import OrderedDict
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


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
   print "Send email by gmail"

   fromaddr = raw_input("Count from gmail: ")
   password = getpass.getpass("Password: ")
   toaddrs = raw_input("to: ")
   #asunto = raw_input("subject, from message: ")
   body = "Countries\t===========\tCapitals\n"
   for msg in todo:
        body = body + str(msg).center(20) +str(todo[msg]).center(20) + "\n" 
   msg = MIMEMultipart()
   msg['From'] = fromaddr #This saves the mail of the sender
   msg['To'] = toaddrs  #This saves the mail of the receiver
   msg['Subject'] = "Countries and Capitals"  #This saves the subject
   msg.attach(MIMEText(body, 'plain')) #This saves the message

   try:
       server = smtplib.SMTP('smtp.gmail.com:587')
       server.starttls()
       server.login(fromaddr,password)
       text = msg.as_string()
       server.sendmail(fromaddr, toaddrs, text)
       server.quit()
       print "yes"
       raw_input("press enter")
   except ValueError:
       print "No se envio nada"



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
    option = raw_input("Insert to opcion: ")

    if option == "1" or option == "country":
        Country()
    elif option == "2" or option == "countries list":
        Countries_List()
    elif option == "3" or option == "capitals list":
        Capitals_List()
    elif option == "4" or option == "capitals and countries":
        Capitals_and_Countries()
    elif option == "5" or option == "all ordered":
        All_Ordered()
    elif option == "6" or option == "all mail":
        All_Mail()
    elif option == "7"or option == "exit":
        salir()
    else:
        print "vuelva a intertarlo"
        raw_input("press enter to continue")
        menu()
menu()