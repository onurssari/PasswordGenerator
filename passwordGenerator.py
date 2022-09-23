import random
import string

lengt=int(input("Enter your password lenght....:"))
lover_Case=string.ascii_lowercase
upper_Case=string.ascii_uppercase
numbers=string.digits
symbols=string.punctuation
all= lover_Case+upper_Case+numbers+symbols
temp=random.sample(all,lengt)
password="".join(temp)
print(password)