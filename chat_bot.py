'''
Author:Umer Rehman
Last Time changed: 09-10-2019

Original file is located at
    https://colab.research.google.com/drive/1GzctgYoZivfNdNv_DQu0VgOM0BC4oXyR
'''

import sys
from datetime import datetime

# Making Time stemped File name
dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y_(%H-%M-%S)")
write_to_text=open("CH_"+timestampStr+".txt","w+")
write_to_text.write("Time: "+ timestampStr + " \n ")

#Check if the Input is Integer or not 
def Ask_Question(Question, C_input):
    while (True):
        try:
            val = int(C_input)
            break
        except ValueError:
            write_to_text.write(Question + " \n ")
            print(Question)
            C_input = input("Customer: ")
            write_to_text.write("Customer: "+ C_input + " \n ")
            continue
    return val

#Getting Information about the trucks and their models 
def Truck_Information(Number):
    write_to_text.write("Chatbot: What is the "+Number+" brand Name?" + " \n ")
    print("Chatbot: What is the "+Number+" brand Name?")
    Brand_Name = input("Customer: ")
    write_to_text.write("Customer: "+ Brand_Name + " \n ")

    write_to_text.write("Chatbot: How Many Trucks in " + Brand_Name + "? (IN NUMBER)" + " \n ")
    print("Chatbot: How Many Trucks in " + Brand_Name + "? (IN NUMBER)")
    C_input = input("Customer: ")
    write_to_text.write("Customer: " + C_input + " \n ")
    Truck_Quantity = Ask_Question("Chatbot: How Many Trucks in " + Brand_Name + " (IN NUMBER only)", C_input)

    write_to_text.write("Chatbot: Are They of the same Model?[Yes/No]" + " \n ")
    print("Chatbot: Are They of the same Model?[Yes/No]")
    C_input = input("Customer: ")
    write_to_text.write("Customer: " + C_input + " \n ")

    if ("no" in C_input):
        j = 1
        while (j <= Truck_Quantity):
            if (j == 1):
                write_to_text.write("Chatbot: what is the 1st Truck model?" + " \n ")
                print("Chatbot: what is the 1st Truck model?")
                C_input = input("Customer: ")
                write_to_text.write("Customer: " + C_input + " \n ")
            elif (j == 2):
                write_to_text.write("Chatbot: what is the 2nd Truck model?" + " \n ")
                print("Chatbot: what is the 2nd Truck model?")
                C_input = input("Customer: ")
                write_to_text.write("Customer: " + C_input + " \n ")
            elif (j == 3):
                write_to_text.write("Chatbot: what is the 3nrd Truck model?" + " \n ")
                print("Chatbot: what is the 3nrd Truck model?")
                C_input = input("Customer: ")
                write_to_text.write("Customer: " + C_input + " \n ")
            elif (i > 3):
                write_to_text.write("Chatbot: what is the " + str(j) + "th Truck model?" + " \n ")
                print("Chatbot: what is the " + str(j) + "th Truck model?")
                C_input = input("Customer: ")
                write_to_text.write("Customer: " + C_input + " \n ")
            j = j + 1
    else:
        write_to_text.write("Chatbot: What model are they?" + " \n ")
        print("Chatbot: What model are they?")
        C_input = input("Customer: ")
        write_to_text.write("Customer: " + C_input + " \n ")

#Starting Point of the Program
write_to_text.write("Chatbot: Hello, Your Full Name Please " + " \n ")
print("Chatbot: Hello, Your Full Name Please")
Customer_Name = input("Customer: ")
write_to_text.write("Customer: " + Customer_Name + " \n ")

write_to_text.write("Chatbot: Hi " + Customer_Name + " what\'s the name of your company?" + " \n ")
print("Chatbot: Hi " + Customer_Name + " what\'s the name of your company?")
C_input = input("Customer: ")
write_to_text.write("Customer: " + C_input + " \n ")

write_to_text.write("Chatbot: Do you own Trucks?[Yes/No]" + " \n ")
print("Chatbot: Do you own Trucks?[Yes/No]")
C_input = input("Customer: ")
write_to_text.write("Customer: " + C_input + " \n ")
if("no" in C_input.lower()):
    write_to_text.write("Please contact to one of our Colleague For more information "+ " \n ")
    print('Please contact to one of our colleague for more information ')
    write_to_text.close()
    sys.exit()

write_to_text.write("Chatbot: How many truck's brand do you have? (IN NUMBER)" + " \n ")
print("Chatbot: How many truck's brand do you have? (IN NUMBER)")
C_input = input("Customer: ")
write_to_text.write("Customer: " + C_input + " \n ")
Brand_Quantity = Ask_Question("Chatbot: How many truck's brand do you have? (IN NUMBER only)", C_input)

i = 1
while i <= Brand_Quantity:
    if (i == 1):
        Truck_Information("1st")
    elif (i == 2):
        Truck_Information("2nd")
    elif (i == 3):
        Truck_Information("3rd")
    elif (i > 3):
        Truck_Information(str(i)+"th")
    i = i + 1

print("Chatbot: Thank you very much for your information \n we are now processing your information and \n we will get back to you soon\n until than have a nice day Bye:) ")
write_to_text.write("Chatbot: Thank you very much for your information \n we are now processing your information and \n we will get back to you soon\n until than have a nice day Bye:)  \n ")
write_to_text.close()

