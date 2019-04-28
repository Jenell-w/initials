def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    inits = ""
    for i in fullname.split():
        inits += i[0]
    return "The initials of " + fullname + " are " + inits.upper() 
 


