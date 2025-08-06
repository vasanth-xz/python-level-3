print("Vasanth computer mart")
print("Gandhi nagar,puducherry")
print("-----------------")
print("Bill Receipt")
print("------------")
No=input("Enter the item no:")
Name=input("Enter the particular:")
rate=int(input("Enter the rate:"))
qnty=int(input("Enter the quantity:"))
total=rate*qnty
print("Total amount in rupees:",total)
if(total>=100000):
    GST=total*10/100
elif(total>=50000):
    GST=total*5/100
elif(total>=20000):
    GST=total*3/100
elif(total>=10000):
    GST=total*2/100
else:
    GST=total*1/100
print("GST(Good&Service tax):",GST)
amt=total+GST
print("Amount to be paid:",amt)
