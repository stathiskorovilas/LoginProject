
p = input("Put the path to txt file : ")

#A bunch of usefull methods
#Opens file and takes every usernames , puts it in a list
def allusernames ():
	people = open( p , "r")
	list = []
	for x in people:
		list.append(x.split(","))

	list2 = []
	for y in list:
		list2.append(y[0])
	people.close()
	return list2
	#comment for fucking git
	
	
 
#Opens the file and puts every password in a txt 
def allpasswords():
	people = open(p , "r")
	list = []
	for x in people:
		list.append(x.split(","))
		
	list2 = []
	for y in list:
		#[:-1] is to remove /n
		list2.append(y[1][:-1])
	people.close()
	return list2

	

#takes a list and a string , returns position in list if string is found, else -1
def findString (List , string):
	counter = 0 
	for x in List:
		if x == string:
			return counter
		counter += 1
	return -1





#takes a string with illegal characters , the input password, returns true if there is illegal char in pass, else false
def CheckPasswordValidity(illegal , password):
	flag = False
	for x in illegal:
		if x in password:
			flag = True
	return flag




#----------------------------------------------------------------

acc = input ("Press C to create account, press L to login to a already existed account, or press X to exit  : ")

while(acc != 'x' and acc != 'X' ):
	if acc == "L" or acc == "l":
		
		print("Log in")
		username = input ("Enter your username  : ")
		password = input ("Enter your password  : ")
		Usernames = allusernames() #Usernames a list full of registered usernames
		Passwords = allpasswords() #Passwords a list full of registered passwords

	
		#find the position of input username 
		x = findString(Usernames , username)
		#if the method returns -1 that means that the input username is not found
		if x == -1:
			print("User , " , username , " is not registered to our database!")
		#if the method returns any number beyond 0 and the input password is equal to the input username's password
		elif(Passwords[x] == password):
			print("Successfully Logged In!")
		#if passwords doesnt match then is wrong
		else:
			print("The password for , " , username , " is wrong!" )
		


	#----------------------------------------------------------------
	#User inputs n or N

	elif acc == "C" or acc == "c":
		
		
		CreateUsername = input("Create Username  : ")
		AllUsernames = allusernames() #AllUsernames is a list with every registered username in our txt file
		
		#if the input name already exists in our txt file then make the user re-enter username
		while (CreateUsername in AllUsernames) :
			CreateUsername = input ("The name you put already exists!\nPlease re-enter a new username  : ")


		CreatePassword = input ("Create password (note: password must have 4-18 characters and no use of symbols) : ")
		
		illegalPassword = "!@#$%^&*()_+}:>{?<,/.;][~ `-=/*-"

		#This method checks if the input password has any illegal character inside
		x = CheckPasswordValidity(illegalPassword , CreatePassword)
		#repeat asking input password until user enters something acceptable
		while (len(CreatePassword) < 4 or len(CreatePassword) > 18 or x):
			CreatePassword = input ("Wrong Password!\nCreate password (note: password must have 4-18 characters and no use of symbols) : ")
			x = CheckPasswordValidity(illegalPassword , CreatePassword)
			
		

		#Append file with username and password, update user
		people = open(p , "a")
		userNpassW = CreateUsername + "," + CreatePassword + "\n"
		people.write(userNpassW)
		people.close()
		print("Account successfully created!")

	
	else:
		print("Wrong input")

	acc = input ("Press C to create account, press L to login to a already existed account, or press X to exit  : ")

