#def User_input():
#    user_pass = input("Please , Enter Your Password ")

def Password_logic(user_pass):
    score = 0

    if(length_checker(user_pass)):
        score += 1
    if(Upper_checker(user_pass)):
        score += 1
    if(lower_checker(user_pass)):
        score += 1 
    if(Num_checker(user_pass)):
        score += 1
    if(special_checker(user_pass)):
        score += 1
    return score

def length_checker(user_pass):
    if(len(user_pass) >= 8):
    
        return True
    else:
        print("Password length must be at least 8 letters ")
        return False      

def Upper_checker(user_pass):
    upp = 0
    for each in user_pass:
        if(each.isupper()):
            upp +=1
    if(upp):
        
        return True
    else:
        print("missing uppercase letters")
        return False  

    
def lower_checker(user_pass):
    low = 0
    for each in user_pass:
        if(each.islower()):
            low += 1

    if(low):
        
        return True
    else:
        print("missing lowercase letters")
        return False

    

def Num_checker(user_pass):
    num = 0
    for each in user_pass:
        if(each.isdigit()):
            num += 1
    
    if(num):
        
        return True
    else:
        print("password must contain atleast 1 number")
        return False

def special_checker(user_pass):
    spe = 0
    for each in user_pass:
        #print(each)
        if not each.isalnum():
            spe += 1
        else:
            pass
            
    if(spe):
        
        return True
    else:
        print("password must contain atleast 1 special character")
        return False

def main():
    User_pass = input("Please , Enter Your Password")
    
    final_score = Password_logic(User_pass)

    if final_score == 5:
        print("strong")
    elif( 3<= final_score < 5):
        print("medium")
    else:
        print("Weak")

if __name__ == "__main__":
    main()
