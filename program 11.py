print("takshashila university")
print("ongur tindivam")
print("____________")
print("student mark list")
print("______________")
no1=int(input("Enter the python mark:"))
no2=int(input("Enter the DBMS mark:"))
no3=int(input("Enter the indudtry mark:"))
totalmark=no1+no2+no3
print("total mark:",totalmark)
Average=totalmark/3
print("Average mark :",Average)
if (no1>=40 and no2>=40 and no3>=40):
    print("result:pass")
else:
     ("result:fail")         
if (totalmark>=250):
    print("grade:O grade")
elif (totalmark>=200):
    print("grade:A+ grade")
elif (totalmark>=150):
    print("grade:A grade")
else:
    print ("grade:B grade")
