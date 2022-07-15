# -*- coding: utf-8 -*-
"""
Created on Wed May 27 14:35:28 2020

@author: Kevin
studente nr: 32368984

The property of the program is to analyse if a student number is valid or not, and to provide  datafiles of valid and invalid
student numbers. The program also display the valid and invalid student numbers with their status when it runs. 
In the program you take a data file that has to be devided in to a list per line.

"""

# Deel 1
def AnalyseStudents(StudenteNommer) :
    status = 0 # define veranderlike
    if len(StudenteNommer) == 8 : #  if lus om te kyk of die nommer presies 8 (agt) karakters lank is.
        try: # probeer om die studente nommer as 'n integer in die lys te voeg
            snl = [] 
            i = 0
            for i in range(0,8):# verdeel die getal in 'n lys in
                snl.append(int(StudenteNommer[i]))# toets veranderlike
                status = 1 # opdateur status

            som = 0 # define veranderlike
            tel = 8 # define veranderlike teller
            j = 0 # define veranderlike
            for j in range(len(snl)):
                som += (snl[j] * tel)
                tel -= 1
            result = som % 11 # kry die res waarde van die deel som

            if result != 0 : # kyk of die result wat gekry is uit die vorige veranderlike nie gelyk 
                status = 0 # opdateur status            # aan 0 nie.
            else:
                status = 1 # opdateur status


        except:
            status = 0 # opdateur status
    else:
        status = 0 # opdateur status




    return status

# deel 2

def Read(studentNumbers):
    tel = 0 # define veranderlike teller
    with open("Data.txt", "r") as k :

        for line in k:
            try:# probeer data uit die textfile lees en in 'n lys in verdeel
                studentNumbers.append(line.rstrip())
            except:
                print("File does not exist")
            tel +=1 #teller
        print("Number of lines read: " , tel) #  print die aantal lyne in die teksleêr
        
    #return tel
    #return studentNumbers


# Deel 3
#skryf die resultate van die status in die ooreenstemende teksleêr saam die studente nommer.
# en vertoon die resultate in die program
def Write(studentNumber, status):
    
    
    if status == 1:
        f = open("ValidNumbers.txt", "a") # define veranderlike as die oopmaak van die teksleêr en die opdateuring daarvan 
        print(studentNumber, " is a VALID student number")  
        f.write(studentNumber + "\n") # skryf na die teksleêr
        f.close() # maak die teksleêr toe 
    elif status == 0 :
        g = open("InvalidNumbers.txt", "a")  # define veranderlike as die oopmaak van die teksleêr en die opdateuring daarvan
        print(studentNumber, " is a INVALID student number")
        g.write(studentNumber + "\n") # skryf na die teksleêr
        g.close() # maak die teksleêr toe
    


# Deel 4


studentNumbers = [] # skep 'n lee lys
Read(studentNumbers) # voer deel 2 uit van die program
l = 0 # define veranderlike teller
for l in range((len(studentNumbers))):
    status = AnalyseStudents(studentNumbers[l]) # voer deel 1 van die program uit
    Write(studentNumbers[l], status) # voer deel 3 van die program uit
    

    


# sss = input("Studente Nommer : ")

# print(status)
# read(studentnumbers)
# print(studentnumbers)
