#Author: ALGEN MALAZARTE JR.
#Section: CPE - 2C
#Date: 11/4/19
#Description: THIS CODE IS CREATED FOR THE COMPLETION OF CAPSTONE PROJECT IN OBJECT ORIENTED PROGRAMMING
#Refactored and revised: 12/14/2022

import os

#formula functions
def boyle_pressure(V1, V2, P2):
    """
    Parameters:
        P2 -> 2nd Pressure
        V1 -> 1st Volume
        V2 -> 2nd Volume
    
    Returns:
        P1 -> 1st Pressure or the pressure that we are going to find :)
            
    """
    return (P2*V2)/V1

def boyle_volume(P1, P2, V2):
    """  
    Parameters:
        P1 -> 1st Pressure
        P2 -> 2nd Pressure
        V2 -> 2nd Volume
        
    Returns:
        V1 -> 1st Volume or the volume that we are going to find.
        
    """
    return (P2*V2)/P1

def charles_volume(T1, T2, V2):
    """
    Parameters:
        T1 -> 1st Temperature
        T2 -> 2nd Temperature
        V2 -> 2nd Volume
        
    Returns:
        V1 -> 1st Volume or the volume that we are going to find.
    
    """
    return (T1*V2)/T2

def charles_temp(V1, V2, T2):
    """  
    Parameters:
        V1 -> 1st Volume
        V2 -> 2nd Volume
        T2 -> 2nd Temperature
        
    Returns:
        T1 -> 1st Temperature or the temperature that we are going to find.
            
    """
    return (V1*T2)/V2

def lussac_pressure(T1, T2, P2):
    """
     Parameters:
        P2 -> 2nd Pressure
        T1 -> 1st Temperature
        T2 -> 2nd Temperature
    
    Returns:
        P1 -> 1st Pressure or the pressure that we are going to find.
           
    """
    return (P2*T1)/T2

def lussac_temp(P1, P2, T2):
    """
    Parameters:
        P1 -> 1st Pressure
        P2 -> 2nd Pressure
        T2 -> 2nd Temperature
        
    Returns:
        T1 -> 1st Temperature or the temperature that we are going to find.
            
    """
    return (P1*T2)/P2

def combined_volume(P1, P2, T1, T2, V2):
    """
    Parameters:
        P1 -> 1st Pressure
        P2 -> 2nd Pressure
        T1 -> 1st Temperature
        T2 -> 2nd Temperature
        V2 -> 2nd Volume
        
    Returns:
        V1 -> 1st Volume or the volume that we are going to find.
                
    """
    return (V2*P2*T1)/(P1*T2)

def combined_pressure(V1, V2, T1, T2, P2):
    """
    Parameters:
        V1 -> 1st Volume
        V2 -> 2nd Volume
        T1 -> 1st Temperature
        T2 -> 2nd Temperature
        P2 -> 2nd Pressure
    Returns:
        P1 -> 1st Pressure or the pressure that we are going to find.
    """
    return (V2*P2*T1)/(V1*T2)

def combined_temp(V1, V2, P1, P2, T2):
    """
    Parameters:
        V1 -> 1st Volume
        V2 -> 2nd Volume
        P1 -> 1st Pressure
        P2 -> 2nd Pressure
        T2 -> 2nd Temperature
        
    Returns:
        P1 -> 1st Pressure or the pressure that we are going to find.
               
    """
    return (V1*P1*T2)/(V2*P2)

#function for boyle's law
def boyle_law():
    os.system('cls')
    print("BOYLE'S LAW\n\n")
    print('WHAT DO YOU WANT TO FIND?')
    print('\n1.PRESSURE\n2.VOLUME\n')
    error_loop = 1 #This will loop through the try and except statements until the appropriate choice is made.
    while (error_loop!=0):
        try:
            choice = int(input('\nENTER THE NUMBER OF YOUR CHOICE: '))
            error_loop = 0
        except ValueError:
            print('ENTER THE NUMBER ONLY')
            error_loop += 1
        else:
            if ((choice>2) or (choice<1)):
                print('ENTER THE NUMBER FROM 1 TO 2 ONLY')
                error_loop +=1
    if (choice == 1):
        error_loop_pressure = 1
        while (error_loop_pressure!=0):
            os.system('cls')
            print("THE FORMULA FOR PRESSURE IN BOYLE'S LAW IS P1=(P2*V2)/V1\n\nPLEASE NOTE THAT V1 IS THE VOLUME FOR PRESSURE P1 AND V2 IS THE VOLUME FOR PRESSURE P2\n\n")
            first_num_loop = 1 
            while (first_num_loop!=0):
                try:
                    V1=float(input('ENTER YOUR V1: '))
                    first_num_loop = 0
                except ValueError:
                    print ('ENTER NUMBERS ONLY\n')
                    first_num_loop += 1
            second_num_loop = 1
            while (second_num_loop!=0):
                try:
                    V2=float(input('ENTER YOUR V2: '))
                    second_num_loop = 0
                except ValueError:
                    print ('ENTER NUMBERS ONLY\n')
                    second_num_loop += 1
            third_num_loop = 1
            while (third_num_loop!=0):
                try:
                    P2=float(input('ENTER YOUR P2: '))
                    third_num_loop = 0
                except ValueError:
                    print ('ENTER NUMBERS ONLY\n')
                    third_num_loop += 1
            try:
                sum="{:.2f}".format(boyle_pressure(V1, V2, P2))
                print ('\nTHE ANSWER IS', sum)
                error_loop_pressure = 0
            except ZeroDivisionError:
                print ("\nYOU CAN'T DIVIDE BY ZERO!")
                input('PRESS THE ENTER KEY TO TRY AGAIN')
                error_loop_pressure += 1
    elif (choice == 2):
        error_loop_volume = 1
        while (error_loop_volume!=0):
            os.system('cls')
            print("THE FORMULA FOR VOLUME IN BOYLE'S LAW IS V1=(P2*V2)/P1\n\nPLEASE NOTE THAT V1 IS THE VOLUME FOR PRESSURE P1 AND V2 IS THE VOLUME FOR PRESSURE P2\n\n")
            first_num_loop = 1 
            while (first_num_loop!=0):
                try:
                    P1=float(input('ENTER YOUR P1: '))
                    first_num_loop = 0
                except ValueError:
                    print ('ENTER NUMBERS ONLY\n')
                    first_num_loop += 1
            second_num_loop = 1
            while (second_num_loop!=0):
                try:
                    P2=float(input('ENTER YOUR P2: '))
                    second_num_loop = 0
                except ValueError:
                    print ('ENTER NUMBERS ONLY\n')
                    second_num_loop += 1
            third_num_loop = 1
            while (third_num_loop!=0):
                try:
                    V2=float(input('ENTER YOUR V2: '))
                    third_num_loop = 0
                except ValueError:
                    print ('ENTER NUMBERS ONLY\n')
                    third_num_loop += 1
            try:
                sum="{:.2f}".format(boyle_volume(P1, P2, V2))
                print ('\nTHE ANSWER IS', sum)
                error_loop_volume = 0
            except ZeroDivisionError:
                print ("\nYOU CAN'T DIVIDE BY ZERO!")
                input('PRESS THE ENTER KEY TO TRY AGAIN')
                error_loop_volume += 1

#function for charles' law
def charles_law():
    os.system('cls')
    print("CHARLES' LAW\n\n")
    print('WHAT DO YOU WANT TO FIND?')
    print('\n1.VOLUME\n2.TEMPERATURE\n')
    error_loop = 1 #This will loop through the try and except statements until the appropriate choice is made.
    while (error_loop!=0):
        try:
            choice = int(input('\nENTER THE NUMBER OF YOUR CHOICE: '))
            error_loop = 0
        except ValueError:
            print('ENTER THE NUMBER ONLY')
            error_loop += 1
        else:
            if ((choice>2) or (choice<1)):
                print('ENTER THE NUMBER FROM 1 TO 2 ONLY')
                error_loop +=1
    if (choice == 1):
        error_loop_volume = 1
        while (error_loop_volume!=0):
            os.system('cls')
            print("THE FORMULA FOR VOLUME IN CHARLES' LAW IS V1=(T1*V2)/T2\n\nPLEASE NOTE THAT T1 IS THE TEMPERATURE FOR VOLUME V1 AND T2 IS THE TEMPERATURE FOR VOLUME V2\n\n")
            first_num_loop = 1 
            while (first_num_loop!=0):
                try:
                    T1=float(input('ENTER YOUR T1: '))
                    first_num_loop = 0
                except ValueError:
                    print ('ENTER NUMBERS ONLY\n')
                    first_num_loop += 1
            second_num_loop = 1
            while (second_num_loop!=0):
                try:
                    T2=float(input('ENTER YOUR T2: '))
                    second_num_loop = 0
                except ValueError:
                    print ('ENTER NUMBERS ONLY\n')
                    second_num_loop += 1
            third_num_loop = 1
            while (third_num_loop!=0):
                try:
                    V2=float(input('ENTER YOUR V2: '))
                    third_num_loop = 0
                except ValueError:
                    print ('ENTER NUMBERS ONLY\n')
                    third_num_loop += 1
            try:
                sum="{:.2f}".format(charles_volume(T1, T2, V2))
                print ('\nTHE ANSWER IS', sum)
                error_loop_volume = 0
            except ZeroDivisionError:
                print ("\nYOU CAN'T DIVIDE BY ZERO!")
                input('PRESS THE ENTER KEY TO TRY AGAIN')
                error_loop_volume += 1
    elif (choice == 2):
        error_loop_temp = 1
        while (error_loop_temp!=0):
            os.system('cls')
            print("THE FORMULA FOR TEMPERATURE IN CHARLES' LAW IS T1=(V1*T2)/V2\n\nPLEASE NOTE THAT T1 IS THE TEMPERATURE FOR VOLUME V1 AND T2 IS THE TEMPERATUR FOR VOLUME V2\n\n")
            first_num_loop = 1 
            while (first_num_loop!=0):
                try:
                    V1=float(input('ENTER YOUR V1: '))
                    first_num_loop = 0
                except ValueError:
                    print ('ENTER NUMBERS ONLY\n')
                    first_num_loop += 1
            second_num_loop = 1
            while (second_num_loop!=0):
                try:
                    V2=float(input('ENTER YOUR V2: '))
                    second_num_loop = 0
                except ValueError:
                    print ('ENTER NUMBERS ONLY\n')
                    second_num_loop += 1
            third_num_loop = 1
            while (third_num_loop!=0):
                try:
                    T2=float(input('ENTER YOUR T2: '))
                    third_num_loop = 0
                except ValueError:
                    print ('ENTER NUMBERS ONLY\n')
                    third_num_loop += 1
            try:
                sum="{:.2f}".format(charles_temp(V1, V2, T2))
                print ('\nTHE ANSWER IS', sum)
                error_loop_temp = 0
            except ZeroDivisionError:
                print ("\nYOU CAN'T DIVIDE BY ZERO!")
                input('PRESS THE ENTER KEY TO TRY AGAIN')
                error_loop_temp += 1

#function for gay-lussac's law                
def lussac_law():
    os.system('cls')
    print("GAY-LUSSAC'S LAW\n\n")
    print('WHAT DO YOU WANT TO FIND?')
    print('\n1.PRESSURE\n2.TEMPERATURE\n')
    error_loop = 1 #This will loop through the try and except statements until the appropriate choice is made.
    while (error_loop!=0):
        try:
            choice = int(input('\nENTER THE NUMBER OF YOUR CHOICE: '))
            error_loop = 0
        except ValueError:
            print('ENTER THE NUMBER ONLY')
            error_loop += 1
        else:
            if ((choice>2) or (choice<1)):
                print('ENTER THE NUMBER FROM 1 TO 2 ONLY')
                error_loop +=1
    if (choice == 1):
        error_loop_pressure = 1
        while (error_loop_pressure!=0):
            os.system('cls')
            print("THE FORMULA FOR PRESSURE IN GAY-LUSSAC'S LAW IS P1=(P2*T1)/T2\n\nPLEASE NOTE THAT T1 IS THE TEMPERATURE FOR PRESSURE P1 AND T2 IS THE TEMPERATURE FOR PRESSURE P2\n\n")
            first_num_loop = 1 
            while (first_num_loop!=0):
                try:
                    T1=float(input('ENTER YOUR T1: '))
                    first_num_loop = 0
                except ValueError:
                    print ('ENTER NUMBERS ONLY\n')
                    first_num_loop += 1
            second_num_loop = 1
            while (second_num_loop!=0):
                try:
                    T2=float(input('ENTER YOUR T2: '))
                    second_num_loop = 0
                except ValueError:
                    print ('ENTER NUMBERS ONLY\n')
                    second_num_loop += 1
            third_num_loop = 1
            while (third_num_loop!=0):
                try:
                    P2=float(input('ENTER YOUR P2: '))
                    third_num_loop = 0
                except ValueError:
                    print ('ENTER NUMBERS ONLY\n')
                    third_num_loop += 1
            try:
                sum="{:.2f}".format(lussac_pressure(T1, T2, P2))
                print ('\nTHE ANSWER IS', sum)
                error_loop_pressure = 0
            except ZeroDivisionError:
                print ("\nYOU CAN'T DIVIDE BY ZERO!")
                input('PRESS THE ENTER KEY TO TRY AGAIN')
                error_loop_pressure += 1
    elif (choice == 2):
        error_loop_temp = 1
        while (error_loop_temp!=0):
            os.system('cls')
            print("THE FORMULA FOR TEMPERATURE IN GAY-LUSSAC'S LAW IS T1=(P1*T2)/P2\n\nPLEASE NOTE THAT T1 IS THE TEMPERATURE FOR PRESSURE P1 AND T2 IS THE TEMPERATURE FOR PRESSURE P2\n\n")
            first_num_loop = 1 
            while (first_num_loop!=0):
                try:
                    P1=float(input('ENTER YOUR P1: '))
                    first_num_loop = 0
                except ValueError:
                    print ('ENTER NUMBERS ONLY\n')
                    first_num_loop += 1
            second_num_loop = 1
            while (second_num_loop!=0):
                try:
                    P2=float(input('ENTER YOUR P2: '))
                    second_num_loop = 0
                except ValueError:
                    print ('ENTER NUMBERS ONLY\n')
                    second_num_loop += 1
            third_num_loop = 1
            while (third_num_loop!=0):
                try:
                    T2=float(input('ENTER YOUR T2: '))
                    third_num_loop = 0
                except ValueError:
                    print ('ENTER NUMBERS ONLY\n')
                    third_num_loop += 1
            try:
                sum="{:.2f}".format(lussac_temp(P1, P2, T2))
                print ('\nTHE ANSWER IS', sum)
                error_loop_temp = 0
            except ZeroDivisionError:
                print ("\nYOU CAN'T DIVIDE BY ZERO!")
                input('PRESS THE ENTER KEY TO TRY AGAIN')
                error_loop_temp += 1

#function for combined gas law
def combined_gas_law():
    os.system('cls')
    print("COMBINE GAS LAW\n\n")
    print('WHAT DO YOU WANT TO FIND?')
    print('\n1.VOLUME\n2.PRESSURE\n3.TEMPERATURE\n')
    error_loop = 1 #This will loop through the try and except statements until the appropriate choice is made.
    while (error_loop!=0):
        try:
            choice = int(input('\nENTER THE NUMBER OF YOUR CHOICE: '))
            error_loop = 0
        except ValueError:
            print('ENTER THE NUMBER ONLY')
            error_loop += 1
        else:
            if ((choice>2) or (choice<1)):
                print('ENTER THE NUMBER FROM 1 TO 2 ONLY')
                error_loop +=1
    if (choice == 1):
        error_loop_volume = 1
        while (error_loop_volume!=0):
            os.system('cls')
            print("THE FORMULA FOR VOLUME IN COMBINED GAS LAW IS V1=(V2*P2*T1)/(P1*T2)\n\nPLEASE NOTE THAT V1,P1, AND T1 ARE THE VOLUME, PRESSURE AND TEMPERATURE OF THE SAME GAS. THE SAME APPLIES TO V2, P2 AND T2\n\n")
            first_num_loop = 1 
            while (first_num_loop!=0):
                try:
                    T1=float(input('ENTER YOUR T1: '))
                    first_num_loop = 0
                except ValueError:
                    print ('ENTER NUMBERS ONLY\n')
                    first_num_loop += 1
            second_num_loop = 1
            while (second_num_loop!=0):
                try:
                    T2=float(input('ENTER YOUR T2: '))
                    second_num_loop = 0
                except ValueError:
                    print ('ENTER NUMBERS ONLY\n')
                    second_num_loop += 1
            third_num_loop = 1
            while (third_num_loop!=0):
                try:
                    P1=float(input('ENTER YOUR P1: '))
                    third_num_loop = 0
                except ValueError:
                    print ('ENTER NUMBERS ONLY\n')
                    third_num_loop += 1
            fourth_num_loop = 1
            while (fourth_num_loop!=0):
                try:
                    P2=float(input('ENTER YOUR P2: '))
                    fourth_num_loop = 0
                except ValueError:
                    print ('ENTER NUMBERS ONLY\n')
                    fourth_num_loop += 1
            fifth_num_loop = 1
            while (fifth_num_loop!=0):
                try:
                    V2=float(input('ENTER YOUR V2: '))
                    fifth_num_loop = 0
                except ValueError:
                    print ('ENTER NUMBERS ONLY\n')
                    fifth_num_loop += 1
            try:
                sum="{:.2f}".format(combined_volume(P1, P2, T1, T2, V2))
                print ('\nTHE ANSWER IS', sum)
                error_loop_volume = 0
            except ZeroDivisionError:
                print ("\nYOU CAN'T DIVIDE BY ZERO!")
                input('PRESS THE ENTER KEY TO TRY AGAIN')
                error_loop_volume += 1
    elif (choice == 2):
        error_loop_pressure = 1
        while (error_loop_pressure!=0):
            os.system('cls')
            print("THE FORMULA FOR PRESSURE IN COMBINED GAS LAW IS P1=(V2*P2*T1)/(V1*T2)\n\nPLEASE NOTE THAT V1,P1, AND T1 ARE THE VOLUME, PRESSURE AND TEMPERATURE OF THE SAME GAS. THE SAME APPLIES TO V2, P2 AND T2\n\n")
            first_num_loop = 1 
            while (first_num_loop!=0):
                try:
                    V1=float(input('ENTER YOUR V1: '))
                    first_num_loop = 0
                except ValueError:
                    print ('ENTER NUMBERS ONLY\n')
                    first_num_loop += 1
            second_num_loop = 1
            while (second_num_loop!=0):
                try:
                    V2=float(input('ENTER YOUR V2: '))
                    second_num_loop = 0
                except ValueError:
                    print ('ENTER NUMBERS ONLY\n')
                    second_num_loop += 1
            third_num_loop = 1
            while (third_num_loop!=0):
                try:
                    T1=float(input('ENTER YOUR T1: '))
                    third_num_loop = 0
                except ValueError:
                    print ('ENTER NUMBERS ONLY\n')
                    third_num_loop += 1
            fourth_num_loop = 1
            while (fourth_num_loop!=0):
                try:
                    T2=float(input('ENTER YOUR T2: '))
                    fourth_num_loop = 0
                except ValueError:
                    print ('ENTER NUMBERS ONLY\n')
                    fourth_num_loop += 1
            fifth_num_loop = 1
            while (fifth_num_loop!=0):
                try:
                    P2=float(input('ENTER YOUR P2: '))
                    fifth_num_loop = 0
                except ValueError:
                    print ('ENTER NUMBERS ONLY\n')
                    fifth_num_loop += 1
            try:
                sum="{:.2f}".format(combined_pressure(V1, V2, T1, T2, P2))
                print ('\nTHE ANSWER IS', sum)
                error_loop_pressure = 0
            except ZeroDivisionError:
                print ("\nYOU CAN'T DIVIDE BY ZERO!")
                input('PRESS THE ENTER KEY TO TRY AGAIN')
                error_loop_pressure += 1
    elif (choice == 3):
        error_loop_temp = 1
        while (error_loop_temp!=0):
            os.system('cls')
            print("THE FORMULA FOR TEMPERATURE IN COMBINED GAS LAW IS T1=(V1*P1*T2)/(V2*P2)\n\nPLEASE NOTE THAT V1,P1, AND T1 ARE THE VOLUME, PRESSURE AND TEMPERATURE OF THE SAME GAS. THE SAME APPLIES TO V2, P2 AND T2\n\n")
            first_num_loop = 1 
            while (first_num_loop!=0):
                try:
                    V1=float(input('ENTER YOUR V1: '))
                    first_num_loop = 0
                except ValueError:
                    print ('ENTER NUMBERS ONLY\n')
                    first_num_loop += 1
            second_num_loop = 1
            while (second_num_loop!=0):
                try:
                    V2=float(input('ENTER YOUR V2: '))
                    second_num_loop = 0
                except ValueError:
                    print ('ENTER NUMBERS ONLY\n')
                    second_num_loop += 1
            third_num_loop = 1
            while (third_num_loop!=0):
                try:
                    P1=float(input('ENTER YOUR P1: '))
                    third_num_loop = 0
                except ValueError:
                    print ('ENTER NUMBERS ONLY\n')
                    third_num_loop += 1
            fourth_num_loop = 1
            while (fourth_num_loop!=0):
                try:
                    P2=float(input('ENTER YOUR P2: '))
                    fourth_num_loop = 0
                except ValueError:
                    print ('ENTER NUMBERS ONLY\n')
                    fourth_num_loop += 1
            fifth_num_loop = 1
            while (fifth_num_loop!=0):
                try:
                    T2=float(input('ENTER YOUR T2: '))
                    fifth_num_loop = 0
                except ValueError:
                    print ('ENTER NUMBERS ONLY\n')
                    fifth_num_loop += 1
            try:
                sum="{:.2f}".format(combined_temp(V1, V2, P1, P2, T2))
                print ('\nTHE ANSWER IS', sum)
                error_loop_pressure = 0
            except ZeroDivisionError:
                print ("\nYOU CAN'T DIVIDE BY ZERO!")
                input('PRESS THE ENTER KEY TO TRY AGAIN')
                error_loop_pressure += 1

#main function               
def main():
    os.system('cls')
    print ('WELCOME TO GAS LAW CALCULATOR.\nPLEASE PICK WHICH LAW YOU WANT TO USE:')
    print ("\n1.BOYLE'S LAW\n2.CHARLES' LAW\n3.GAY-LUSSAC'S LAW\n4.COMBINED GAS LAW\n")
    error_loop = 1 #This will loop through the try and except statements until the appropriate choice is made.
    while (error_loop!=0):
        try:
            choice = int(input('\nENTER THE NUMBER OF YOUR CHOICE: '))
            error_loop = 0
        except ValueError:
            print('ENTER THE NUMBER ONLY')
            error_loop += 1
        else:
            if ((choice>4) or (choice<1)):
                print('ENTER THE NUMBER FROM 1 TO 4 ONLY')
                error_loop +=1
    if (choice == 1):
        boyle_law()
    elif (choice == 2):
        charles_law()
    elif (choice == 3):
        lussac_law()
    elif (choice == 4):
        combined_gas_law()
        
#calling main function in a reset loop
reset = 'y'
while (reset==('y'or'Y')):
    main()
    reset=input('DO YOU WANT TO TRY AGAIN? (Y/N): ')
else:
    quit()