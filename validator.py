idPassPair = {
    "id" : "",
    "password" : ""
}

#list of already existing ids
idList = ['user1', 'user2', 'user3']

#create and check  user id
def checkId():
    userId = input('Create your username: ')
    
    #check id is not an id that already exists
    if userId not in idList:
        idList.append(userId)
        idPassPair['id'] = userId
        
        #check id meets min length
        if len(userId) < 5:
            print('The username you entered is invalid. ' +
                  'Make sure it\'s at least 5 characters long.')
            checkId()
    else:
        print('This username already exists. Please enter another username choice.')
        checkId()
    return idList
checkId()

#create password
def passwordCheck():
    password = input('Please create a password of minimum 6 characters, ' +
    'of which there must be minimum one digit: ')
    
    #check password includes min one digit
    checkDigit = 0
    for x in password:
        if x.isdigit():
            checkDigit += 1
    #check the password meets requirements (length and digit)
    if len(password) > 5 and checkDigit > 0:
            #retype password to check
            repeatPass = input('Enter your choosen password again: ')
            if repeatPass == password:
                idPassPair['password'] = password
                print('Username and Password have been successfuly created.')
            else: 
                print('The two passwords you entered don\'t match.\n')
                passwordCheck()
    else: 
            print('Your password doesn\'t meet the criteria.\n')
            passwordCheck()
passwordCheck()

#check the program works well and the input data is saved corectly
print (idPassPair)