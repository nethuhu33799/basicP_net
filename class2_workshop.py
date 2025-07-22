distance = input(int("Enter your distance : "))

if distance<5:
    print ("Not sending items")
elif 5<distance<50:
    print ("price = 10 Bath")
elif 51<distance<100:
    print ("price = 15 Bath")
elif 101<distance<300:
    print ("price = 25 Bath")
elif distance<500:
    print ("price = 35 Bath")
else :
    print ("price = 45 Bath")