amount = float(input("enter the amount")) 
if amount <= 1000 :
    print(amount*(10/100))
elif amount <=5000 and amount >1000 :
    print(amount*(20/100))
elif amouny>5000 and amount<=1000 :
    print(amount*(30/100))
elif amount>10000 :
    print(amount*(50/100))
