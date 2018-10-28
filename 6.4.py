def new_password(oldpassword, newpassword):
    if newpassword != oldpassword and len(newpassword) >= 6:
        return(True)
    else:
        return(False)

oldpassword ='welkomterug'
newpassword = 'welkomterug123'

print((new_password)(oldpassword,newpassword))