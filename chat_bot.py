import sys
from datetime import datetime

# Making Time stemped File name
dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y_(%H-%M-%S)")
write_to_text=open("CH_"+timestampStr+".txt","w+")
write_to_text.write("Time: "+ timestampStr + " \n ")

#Trucks brand names
Brands_Name=["Scania","MAN","PACCAR","Iveco","Hino","Volvo","Navistar","Dongfeng","TATA","Daimler"]


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

#if the input is empty ask question again
def Check_isEmpty(Question, C_input):
    while (True):
        if(C_input==""):
            print(Question)
            C_input = input("Customer: ")
        else:
            break
    return C_input

#Getting Information about the trucks and their models
def Truck_Information(Number):
    write_to_text.write("Chatbot: What is the "+Number+" brand Name?" + " \n ")
    print("Chatbot: What is the "+Number+" brand Name?")
    Brand_Name = Check_isEmpty("Chatbot: What is the "+Number+" brand Name?",input("Customer: "))
    write_to_text.write("Customer: "+ Brand_Name + " \n ")
    while(not any(Brand_Name.lower() in s.lower() for s in Brands_Name)):
        write_to_text.write("Chatbot: What is the " + Number + " brand Name?[Entered Brand Not Found]" + " \n ")
        print("Chatbot: What is the " + Number + " brand Name?[Entered Brand Not Found]")
        Brand_Name = input("Customer: ")
        write_to_text.write("Customer: " + Brand_Name + " \n ")

    write_to_text.write("Chatbot: How Many Trucks in " + Brand_Name + "? (IN NUMBER)" + " \n ")
    print("Chatbot: How Many Trucks in " + Brand_Name + "? (IN NUMBER)")
    C_input = Check_isEmpty("Chatbot: How Many Trucks in " + Brand_Name + "? (IN NUMBER)",input("Customer: "))
    write_to_text.write("Customer: " + C_input + " \n ")
    Truck_Quantity = Ask_Question("Chatbot: How Many Trucks in " + Brand_Name + " (IN NUMBER only)", C_input)

    if(Truck_Quantity!=1):
        write_to_text.write("Chatbot: Are They of the same Model?[Yes/No]" + " \n ")
        print("Chatbot: Are They of the same Model?[Yes/No]")
        C_input = Check_isEmpty("Chatbot: Are They of the same Model?[Yes/No]",input("Customer: "))
        write_to_text.write("Customer: " + C_input + " \n ")
    else:
        write_to_text.write("Chatbot: What model is it?" + " \n ")
        print("Chatbot: What model is it?")
        C_input = Check_isEmpty("Chatbot: What model is it?",input("Customer: "))
        write_to_text.write("Customer: " + C_input + " \n ")

    if ("no" in C_input.lower() or "n" in C_input.lower()):
        j = 1
        while (j <= Truck_Quantity):
            if (j == 1):
                write_to_text.write("Chatbot: what is the 1st Truck model?" + " \n ")
                print("Chatbot: what is the 1st Truck model?")
                C_input =Check_isEmpty("Chatbot: what is the 1st Truck model?",input("Customer: "))
                write_to_text.write("Customer: " + C_input + " \n ")
            elif (j == 2):
                write_to_text.write("Chatbot: what is the 2nd Truck model?" + " \n ")
                print("Chatbot: what is the 2nd Truck model?")
                C_input = input("Customer: ")
                write_to_text.write("Customer: " + C_input + " \n ")
            elif (j == 3):
                write_to_text.write("Chatbot: what is the 3nrd Truck model?" + " \n ")
                print("Chatbot: what is the 3nrd Truck model?")
                C_input = Check_isEmpty("Chatbot: what is the 3nrd Truck model?",input("Customer: "))
                write_to_text.write("Customer: " + C_input + " \n ")
            elif (i > 3):
                write_to_text.write("Chatbot: what is the " + str(j) + "th Truck model?" + " \n ")
                print("Chatbot: what is the " + str(j) + "th Truck model?")
                C_input = Check_isEmpty("Chatbot: what is the " + str(j) + "th Truck model?",input("Customer: "))
                write_to_text.write("Customer: " + C_input + " \n ")
            j = j + 1
    elif("yes" in C_input.lower() or "y" in C_input.lower()):
        if(Truck_Quantity==1):
            write_to_text.write("Chatbot: What model is it?" + " \n ")
            print("Chatbot: What model is it?")
            C_input = Check_isEmpty("Chatbot: What model is it?",input("Customer: "))
            write_to_text.write("Customer: " + C_input + " \n ")
        else:
            write_to_text.write("Chatbot: What model are they?" + " \n ")
            print("Chatbot: What model are they?")
            C_input =Check_isEmpty("Chatbot: What model are they?",input("Customer: "))
            write_to_text.write("Customer: " + C_input + " \n ")

#Starting Point of the Program
write_to_text.write("Chatbot: Hello, Your Full Name Please " + " \n ")
print("Chatbot: Hello, Your Full Name Please")
Customer_Name =Check_isEmpty( "Chatbot: Hello, Your Full Name Please",input("Customer: "))
write_to_text.write("Customer: " + Customer_Name + " \n ")

write_to_text.write("Chatbot: Hi " + Customer_Name + " what\'s the name of your company?" + " \n ")
print("Chatbot: Hi " + Customer_Name + " what\'s the name of your company?")
C_input = Check_isEmpty("Chatbot: Hi " + Customer_Name + " what\'s the name of your company?",input("Customer: "))
write_to_text.write("Customer: " + C_input + " \n ")

write_to_text.write("Chatbot: Do you own Trucks?[Yes/No]" + " \n ")
print("Chatbot: Do you own Trucks?[Yes/No]")
C_input = Check_isEmpty("Chatbot: Do you own Trucks?[Yes/No]",input("Customer: "))
write_to_text.write("Customer: " + C_input + " \n ")
if("no" in C_input.lower() or "n" in C_input.lower()):
    write_to_text.write("Please contact to one of our Colleague For more information "+ " \n ")
    print('Please contact to one of our colleague for more information ')
    write_to_text.close()
    sys.exit()

write_to_text.write("Chatbot: How many truck's brand do you have? (IN NUMBER)" + " \n ")
print("Chatbot: How many truck's brand do you have? (IN NUMBER)")
C_input =Check_isEmpty("Chatbot: How many truck's brand do you have? (IN NUMBER)", input("Customer: "))
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
