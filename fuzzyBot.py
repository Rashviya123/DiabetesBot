# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 22:57:49 2023

@author: Mohamed Mustafa

"""
import numpy as np
import time
import pandas as pd
import sys
from fuzzywuzzy import fuzz
import docx
import sqlite3 as db

time_limit = 300
start_time=time.time()
end_time=start_time+time_limit
print("Hai, My name is Ria, your diabetes assistant!")
print("I'm here to answer your doubts, Let's start!")
name = input("What's your name?")
print('Hi '+name+' How are you?')
s = input()

def moreQueries():
    a = input('\nDo you have any queries? Y|N: ')
    
    if(a.lower()=='y'):
        main()
    elif(a.lower()=='n'):
        print('Thank you, Have a nice day!')
        sys.exit()
    else:
        print('Invalid option')
        sys.exit()
        
        
def is_valid_mobile_number(mobile_number):
    if len(mobile_number) == 10 and mobile_number.isdigit():
        return True
    else:
        return False

def is_valid_email(email):
    if '@' in email and '.' in email:
        return True
    else:
        return False


'''while not is_valid_mobile_number(mobile_number):
    print("Invalid mobile number. Please enter a 10-digit number.")
    mobile_number = input("\nEnter a mobile number: ")

#Validate the email
while not is_valid_email(email):
    print("Invalid email address. Please enter a valid email.")
    email = input("\nEnter your email id: ")'''



def main():
    while time.time()<end_time:
    
        time.sleep(1)
        print('\nGood, Ask me any question or Enter the given option:\n')
       # image_filenames = ["diabetes.webp","treatmentImage.png", "diet.jpeg","dailylife.webp","preventions.jpeg"]'''
        print("1.Diabetes and diagnosis\n2.Treatment\n3.Diet\n4.Daily-life\n5.Prevention\n")
        ques = input('\n')
        ques = ques.replace('?', ' ')
        
       
       
        c = ['what diabetes']
        d = ['types','categories']
        e = ['diagnosis','tests']
        f = ['treatment','treated']
        g = ['type 1 diabetes','type1 diabetes']
        h = 'symptoms of diabetes'
        i = ['type2 diabetes']
        if fuzz.WRatio(c,ques)>90 or ques==str(1):
             with open("diabetes.txt", "r") as file:
                 file_contents = file.read()
                 print(file_contents)
                 moreQueries()
        elif fuzz.WRatio(d[0], ques)>80 or fuzz.WRatio(d[1],ques)>90:
            with open("types.txt", "r") as file:
                file_contents = file.read()
                print(file_contents)
                moreQueries()
        elif fuzz.WRatio(e[0],ques)>60 or fuzz.WRatio(e[1],ques)>60:
            with open("DiabetesTest.txt", "r") as file:
                file_contents = file.read()
                print(file_contents)
                moreQueries()
        elif fuzz.WRatio(f[0],ques)>60 or  fuzz.WRatio(f[1],ques)>60 or ques==str(2):
            with open("Treatment.txt", "r") as file:
                file_contents = file.read()
                print(file_contents)
                moreQueries()
        elif fuzz.WRatio(g[0],ques)>70 or  fuzz.WRatio(g[1],ques)>70:
             with open("Type1Diabetes.txt", "r") as file:
                 file_contents = file.read()
                 print(file_contents)
                 moreQueries()
        elif fuzz.WRatio(h,ques)>90 :
              with open("Symptoms-diabetes.txt", "r") as file:
                  file_contents = file.read()
                  print(file_contents)
                  moreQueries()
       
         
            
        
            
main()
        
        
        
        
        
        
        
        
        
        
        