#Author: ALGEN MALAZARTE JR.
#Section: CPE - 2C
#Date: 11/4/19

#main function
def gas_laws():
    #formula functions
	def boyle_pressure(Va, Vb, Pb):
		return (Pb*Vb)/Va
	def boyle_volume(Pa, Pb, Vb):
		return (Pb*Vb)/Pa
	def charles_volume(Ta, Tb, Vb):
		return (Ta*Vb)/Tb
	def charles_temp(Va, Vb, Tb):
		return (Va*Tb)/Vb
	def lussac_pressure(Ta, Tb, Pb):
		return (Pb*Ta)/Tb
	def lussac_temp(Pa, Pb, Tb):
		return (Pa*Tb)/Pb
	def combined_volume(Pa, Pb, Ta, Tb, Vb):
		return (Vb*Pb*Ta)/(Pa*Tb)
	def combined_pressure(Va, Vb, Ta, Tb, Pb):
		return (Vb*Pb*Ta)/(Va*Tb)
	def combined_temp(Va, Vb, Pa, Pb, Tb):
		return (Va*Pa*Tb)/(Vb*Pb)

	#main program loop
	ans='y'
	if (ans==('y'or'Y')):	
		import os
		os.system('cls')
		print ('WELCOME TO GAS LAW CALCULATOR.\nPLEASE PICK WHICH LAW YOU WANT TO USE:')
		print ("\n1.BOYLE'S LAW\n2.CHARLES' LAW\n3.GAY-LUSSAC'S LAW\n4.COMBINED GAS LAW\n")
		m=1
		while (m!=0):
			try:
				x=int(input('ENTER THE NUMBER OF YOUR CHOICE: '))
				m=0
			except ValueError:
				print('\nENTER THE NUMBER ONLY')
				m+=1
			else:
				if (x>4):
					print('\nENTER THE NUMBER FROM 1 TO 4 ONLY')
					m+=1
				elif (x<1):
					print('\nENTER THE NUMBER FROM 1 TO 4 ONLY')
					m+=1
		#boyle's law
		if (x==1):
			os.system('cls')
			print('WHAT DO YOU WANT TO FIND?')
			print('\n1.PRESSURE\n2.VOLUME\n')
			n=1
			while (n!=0):
				try:
					b=int(input('ENTER THE NUMBER OF YOUR CHOICE: '))
					n=0
				except ValueError:
					print('\nENTER THE NUMBER ONLY')
					n+=1
				else:
					if (b>2):
						print('\nENTER THE NUMBER FROM 1 TO 2 ONLY')
						n+=1
					elif (b<1):
						print('\nENTER THE NUMBER FROM 1 TO 2 ONLY')
						n+=1
			if (b==1):
				z=1
				while (z!=0):
					os.system('cls')
					print("THE FORMULA FOR PRESSURE IN BOYLE'S LAW IS P1=(P2*V2)/V1\n\nPLEASE NOTE THAT V1 IS THE VOLUME FOR PRESSURE P1 AND V2 IS THE VOLUME FOR PRESSURE P2\n\n")
					o=1
					while (o!=0):
						try:
							Va=float(input('ENTER YOUR V1: '))
							o=0
						except ValueError:
							print ('ENTER NUMBERS ONLY\n')
							o+=1
					p=1
					while (p!=0):
						try:
							Vb=float(input('ENTER YOUR V2: '))
							p=0
						except ValueError:
							print ('ENTER NUMBERS ONLY\n')
							p+=1
					q=1
					while (q!=0):
						try:
							Pb=float(input('ENTER YOUR P2: '))
							q=0
						except ValueError:
							print ('ENTER NUMBERS ONLY\n')
							q+=1
					try:
						sum="{:.2f}".format(boyle_pressure(Va, Vb, Pb))
						print ('\nTHE ANSWER IS', sum)
						z=0
					except ZeroDivisionError:
						print ("\nYOU CAN'T DIVIDE BY ZERO!")
						input('PRESS THE ENTER KEY TO TRY AGAIN')
						z+=1
			if (b==2):
				z=1
				while (z!=0):
					os.system('cls')
					print("THE FORMULA FOR VOLUME IN BOYLE'S LAW IS V1=(P2*V2)/P1\n\nPLEASE NOTE THAT V1 IS THE VOLUME FOR PRESSURE P1 AND V2 IS THE VOLUME FOR PRESSURE P2\n\n")
					o=1
					while (o!=0):
						try:
							Pa=float(input('ENTER YOUR P1: '))
							o=0
						except ValueError:
							print ('ENTER NUMBERS ONLY\n')
							o+=1
					p=1
					while (p!=0):
						try:
							Pb=float(input('ENTER YOUR P2: '))
							p=0
						except ValueError:
							print ('ENTER NUMBERS ONLY\n')
							p+=1
					q=1
					while (q!=0):
						try:
							Vb=float(input('ENTER YOUR V2: '))
							q=0
						except ValueError:
							print ('ENTER NUMBERS ONLY\n')
							q+=1
					try:
						sum="{:.2f}".format(boyle_volume(Pa, Pb, Vb))
						print ('\nTHE ANSWER IS', sum)
						z=0
					except ZeroDivisionError:
						print ("\nYOU CAN'T DIVIDE BY ZERO!")
						input('PRESS THE ENTER KEY TO TRY AGAIN')
						z+=1
		#charles' law		
		if (x==2):
			os.system('cls')
			print('WHAT DO YOU WANT TO FIND?')
			print('\n1.VOLUME\n2.TEMPERATURE\n')
			n=1
			while (n!=0):
				try:
					b=int(input('ENTER THE NUMBER OF YOUR CHOICE: '))
					n=0
				except ValueError:
					print('\nENTER THE NUMBER ONLY')
					n+=1
				else:
					if (b>2):
						print('\nENTER THE NUMBER FROM 1 TO 2 ONLY')
						n+=1
					elif (b<1):
						print('\nENTER THE NUMBER FROM 1 TO 2 ONLY')
						n+=1
			if (b==1):
				z=1
				while (z!=0):
					os.system('cls')
					print("THE FORMULA FOR VOLUME IN CHARLES' LAW IS V1=(T1*V2)/T2\n\nPLEASE NOTE THAT T1 IS THE TEMPERATURE FOR VOLUME V1 AND T2 IS THE TEMPERATURE FOR VOLUME V2\n\n")
					o=1
					while (o!=0):
						try:
							Ta=float(input('ENTER YOUR T1: '))
							o=0
						except ValueError:
							print ('ENTER NUMBERS ONLY\n')
							o+=1
					p=1
					while (p!=0):
						try:
							Tb=float(input('ENTER YOUR T2: '))
							p=0
						except ValueError:
							print ('ENTER NUMBERS ONLY\n')
							p+=1
					q=1
					while (q!=0):
						try:
							Vb=float(input('ENTER YOUR V2: '))
							q=0
						except ValueError:
							print ('ENTER NUMBERS ONLY\n')
							q+=1
					try:
						sum="{:.2f}".format(charles_volume(Ta, Tb, Vb))
						print ('\nTHE ANSWER IS', sum)
						z=0
					except ZeroDivisionError:
						print ("\nYOU CAN'T DIVIDE BY ZERO!")
						input('PRESS THE ENTER KEY TO TRY AGAIN')
						z+=1
			if (b==2):
				z=1
				while (z!=0):
					os.system('cls')
					print("THE FORMULA FOR TEMPERATURE IN CHARLES' LAW IS T1=(V1*T2)/V2\n\nPLEASE NOTE THAT T1 IS THE TEMPERATURE FOR VOLUME V1 AND T2 IS THE TEMPERATUR FOR VOLUME V2\n\n")
					o=1
					while (o!=0):
						try:
							Va=float(input('ENTER YOUR V1: '))
							o=0
						except ValueError:
							print ('ENTER NUMBERS ONLY\n')
							o+=1
					p=1
					while (p!=0):
						try:
							Vb=float(input('ENTER YOUR V2: '))
							p=0
						except ValueError:
							print ('ENTER NUMBERS ONLY\n')
							p+=1
					q=1
					while (q!=0):
						try:
							Tb=float(input('ENTER YOUR T2: '))
							q=0
						except ValueError:
							print ('ENTER NUMBERS ONLY\n')
							q+=1
					try:
						sum="{:.2f}".format(charles_temp(Va, Vb, Tb))
						print ('\nTHE ANSWER IS', sum)
						z=0
					except ZeroDivisionError:
						print ("\nYOU CAN'T DIVIDE BY ZERO!")
						input('PRESS THE ENTER KEY TO TRY AGAIN')
						z+=1
		#gay-lussac's law
		if (x==3):
			os.system('cls')
			print('WHAT DO YOU WANT TO FIND?')
			print('\n1.PRESSURE\n2.TEMPERATURE\n')
			n=1
			while (n!=0):
				try:
					b=int(input('ENTER THE NUMBER OF YOUR CHOICE: '))
					n=0
				except ValueError:
					print('\nENTER THE NUMBER ONLY')
					n+=1
				else:
					if (b>2):
						print('\nENTER THE NUMBER FROM 1 TO 2 ONLY')
						n+=1
					elif (b<1):
						print('\nENTER THE NUMBER FROM 1 TO 2 ONLY')
						n+=1
			if (b==1):
				z=1
				while (z!=0):
					os.system('cls')
					print("THE FORMULA FOR PRESSURE IN GAY-LUSSAC'S LAW IS P1=(P2*T1)/T2\n\nPLEASE NOTE THAT T1 IS THE TEMPERATURE FOR PRESSURE P1 AND T2 IS THE TEMPERATURE FOR PRESSURE P2\n\n")
					o=1
					while (o!=0):
						try:
							Ta=float(input('ENTER YOUR T1: '))
							o=0
						except ValueError:
							print ('ENTER NUMBERS ONLY\n')
							o+=1
					p=1
					while (p!=0):
						try:
							Tb=float(input('ENTER YOUR T2: '))
							p=0
						except ValueError:
							print ('ENTER NUMBERS ONLY\n')
							p+=1
					q=1
					while (q!=0):
						try:
							Pb=float(input('ENTER YOUR P2: '))
							q=0
						except ValueError:
							print ('ENTER NUMBERS ONLY\n')
							q+=1
					try:
						sum="{:.2f}".format(lussac_pressure(Ta, Tb, Pb))
						print ('\nTHE ANSWER IS', sum)
						z=0
					except ZeroDivisionError:
						print ("\nYOU CAN'T DIVIDE BY ZERO!")
						input('PRESS THE ENTER KEY TO TRY AGAIN')
						z+=1
			if (b==2):
				z=1
				while (z!=0):
					os.system('cls')
					print("THE FORMULA FOR TEMPERATURE IN GAY-LUSSAC'S LAW IS T1=(P1*T2)/P2\n\nPLEASE NOTE THAT T1 IS THE TEMPERATURE FOR PRESSURE P1 AND T2 IS THE TEMPERATURE FOR PRESSURE P2\n\n")
					o=1
					while (o!=0):
						try:
							Pa=float(input('ENTER YOUR P1: '))
							o=0
						except ValueError:
							print ('ENTER NUMBERS ONLY\n')
							o+=1
					p=1
					while (p!=0):
						try:
							Pb=float(input('ENTER YOUR P2: '))
							p=0
						except ValueError:
							print ('ENTER NUMBERS ONLY\n')
							p+=1
					q=1
					while (q!=0):
						try:
							Tb=float(input('ENTER YOUR T2: '))
							q=0
						except ValueError:
							print ('ENTER NUMBERS ONLY\n')
							q+=1
					try:
						sum="{:.2f}".format(lussac_temp(Pa, Pb, Tb))
						print ('\nTHE ANSWER IS', sum)
						z=0
					except ZeroDivisionError:
						print ("\nYOU CAN'T DIVIDE BY ZERO!")
						input('PRESS THE ENTER KEY TO TRY AGAIN')
						z+=1
		#combined gas law
		if (x==4):
			os.system('cls')
			print('WHAT DO YOU WANT TO FIND?')
			print('\n1.VOLUME\n2.PRESSURE\n3.TEMPERATURE\n')
			n=1
			while (n!=0):
				try:
					b=int(input('ENTER THE NUMBER OF YOUR CHOICE: '))
					n=0
				except ValueError:
					print('\nENTER THE NUMBER ONLY')
					n+=1
				else:
					if (b>3):
						print('\nENTER THE NUMBER FROM 1 TO 3 ONLY')
						n+=1
					elif (b<1):
						print('\nENTER THE NUMBER FROM 1 TO 3 ONLY')
						n+=1
			if (b==1):
				z=1
				while (z!=0):
					os.system('cls')
					print("THE FORMULA FOR VOLUME IN COMBINED GAS LAW IS V1=(V2*P2*T1)/(P1*T2)\n\nPLEASE NOTE THAT V1,P1, AND T1 ARE THE VOLUME, PRESSURE AND TEMPERATURE OF THE SAME GAS. THE SAME APPLIES TO V2, P2 AND T2\n\n")
					o=1
					while (o!=0):
						try:
							Ta=float(input('ENTER YOUR T1: '))
							o=0
						except ValueError:
							print ('ENTER NUMBERS ONLY\n')
							o+=1
					p=1
					while (p!=0):
						try:
							Tb=float(input('ENTER YOUR T2: '))
							p=0
						except ValueError:
							print ('ENTER NUMBERS ONLY\n')
							p+=1
					q=1
					while (q!=0):
						try:
							Pa=float(input('ENTER YOUR P1: '))
							q=0
						except ValueError:
							print ('ENTER NUMBERS ONLY\n')
							q+=1
					r=1
					while (r!=0):
						try:
							Pb=float(input('ENTER YOUR P2: '))
							r=0
						except ValueError:
							print ('ENTER NUMBERS ONLY\n')
							r+=1
					s=1
					while (s!=0):
						try:
							Vb=float(input('ENTER YOUR V2: '))
							s=0
						except ValueError:
							print ('ENTER NUMBERS ONLY\n')
							s+=1
					try:
						sum="{:.2f}".format(combined_volume(Pa, Pb, Ta, Tb, Vb))
						print ('\nTHE ANSWER IS', sum)
						z=0
					except ZeroDivisionError:
						print ("\nYOU CAN'T DIVIDE BY ZERO!")
						input('PRESS THE ENTER KEY TO TRY AGAIN')
						z+=1
			if (b==2):
				z=1
				while (z!=0):
					os.system('cls')
					print("THE FORMULA FOR PRESSURE IN COMBINED GAS LAW IS P1=(V2*P2*T1)/(V1*T2)\n\nPLEASE NOTE THAT V1,P1, AND T1 ARE THE VOLUME, PRESSURE AND TEMPERATURE OF THE SAME GAS. THE SAME APPLIES TO V2, P2 AND T2\n\n")
					o=1
					while (o!=0):
						try:
							Ta=float(input('ENTER YOUR T1: '))
							o=0
						except ValueError:
							print ('ENTER NUMBERS ONLY\n')
							o+=1
					p=1
					while (p!=0):
						try:
							Tb=float(input('ENTER YOUR T2: '))
							p=0
						except ValueError:
							print ('ENTER NUMBERS ONLY\n')
							p+=1
					q=1
					while (q!=0):
						try:
							Va=float(input('ENTER YOUR V1: '))
							q=0
						except ValueError:
							print ('ENTER NUMBERS ONLY\n')
							q+=1
					r=1
					while (r!=0):
						try:
							Vb=float(input('ENTER YOUR V2: '))
							r=0
						except ValueError:
							print ('ENTER NUMBERS ONLY\n')
							r+=1
					s=1
					while (s!=0):
						try:
							Pb=float(input('ENTER YOUR P2: '))
							s=0
						except ValueError:
							print ('ENTER NUMBERS ONLY\n')
							s+=1
					try:
						sum="{:.2f}".format(combined_pressure(Va, Vb, Ta, Tb, Pb))
						print ('\nTHE ANSWER IS', sum)
						z=0
					except ZeroDivisionError:
						print ("\nYOU CAN'T DIVIDE BY ZERO!")
						input('PRESS THE ENTER KEY TO TRY AGAIN')
						z+=1
			if (b==3):
				z=1
				while (z!=0):
					os.system('cls')
					print("THE FORMULA FOR TEMPERATURE IN COMBINED GAS LAW IS T1=(V1*P1*T2)/(V2*P2)\n\nPLEASE NOTE THAT V1,P1, AND T1 ARE THE VOLUME, PRESSURE AND TEMPERATURE OF THE SAME GAS. THE SAME APPLIES TO V2, P2 AND T2\n\n")
					o=1
					while (o!=0):
						try:
							Pa=float(input('ENTER YOUR P1: '))
							o=0
						except ValueError:
							print ('ENTER NUMBERS ONLY\n')
							o+=1
					p=1
					while (p!=0):
						try:
							Pb=float(input('ENTER YOUR P2: '))
							p=0
						except ValueError:
							print ('ENTER NUMBERS ONLY\n')
							p+=1
					q=1
					while (q!=0):
						try:
							Va=float(input('ENTER YOUR V1: '))
							q=0
						except ValueError:
							print ('ENTER NUMBERS ONLY\n')
							q+=1
					r=1
					while (r!=0):
						try:
							Vb=float(input('ENTER YOUR V2: '))
							r=0
						except ValueError:
							print ('ENTER NUMBERS ONLY\n')
							r+=1
					s=1
					while (s!=0):
						try:
							Tb=float(input('ENTER YOUR T2: '))
							s=0
						except ValueError:
							print ('ENTER NUMBERS ONLY\n')
							s+=1
					try:
						sum="{:.2f}".format(combined_temp(Va, Vb, Pa, Pb, Tb))
						print ('\nTHE ANSWER IS', sum)
						z=0
					except ZeroDivisionError:
						print ("\nYOU CAN'T DIVIDE BY ZERO!")
						input('PRESS THE ENTER KEY TO TRY AGAIN')
						z+=1
		ans=input('DO YOU WANT TO TRY AGAIN? (Y/N): ')
	else:
		quit()
  
#calling main function
gas_laws()
