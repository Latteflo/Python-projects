import re 

def check_password_strength(password):
     if len(password) < 8:
         return "Password is too short man, what the heck! You know better than that! Come on! It should be at least 16 characters long!"
     if not re.search("[a-z]", password):
         return "Password must contain at least one lowercase letter! You know that right? Come on!"  
     if not re.search("[A-Z]", password):
         return "Password must contain at least one uppercase letter! Show some respect!"
     if not re.search("[0-9]", password):
         return "Password must contain at least one number! You know math right? We're not asking for much!"
     if not re.search("[_@$]", password):
         return "Password must contain at least one special character! At this point you're just... special right?!"
     return "Password is strong! You're good to go! Here's a cookie 🍪! Now move along." 
 
 
if __name__ == "__main__":
     password = input("Feel free to feed me your secrets (just the password, gee): ")
     result = check_password_strength(password) 
     print(result)