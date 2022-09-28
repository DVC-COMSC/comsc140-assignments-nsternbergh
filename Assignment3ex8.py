
#create an email
#must meet conditions for a valid email
user_input = input('Enter a user name ')
print (user_input) 
if user_input[0].isalpha():
    print ('true')
if len(user_input) < 5 or len(user_input) > 30:
	print ('true')
print (user_input.find('@')) 
if (user_input.find('@')) > 3:
    print ('true')
if user_input.find('@') == -1:
	print ('false')
at = user_input.find('@') 
if user_input.find(".", at, len(user_input)) > at:
    print('true')
else:
    print('false .')