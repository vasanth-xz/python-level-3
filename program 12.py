print("Government of Tamilnadu")
print("Electricity Board")
print("-----------------")
print("Bill Receipt")
print("------------")
eno=int(input("Enter the eb.no:"))
Name=input("Enter the customer name:")
pu=int(input("Enter the previous unit:"))
cu=int(input("Enter the current unit:"))
unit=cu-pu
print("Unit consumed:",unit)
if(unit>=1000):
    amt1=unit*10
    print("Amount to be paid:",amt1)
elif(unit>=500):
    amt2=unit*5
    print("Amount to be paid:",amt2)
elif(unit>=100):
    amt3=unit*2
    print("Amount to be paid:",amt3)
else:
    print("Amount to be paid:nil")
