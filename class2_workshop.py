distance = int(input("Enter your distance : "))

if distance < 0:
    print("Wtf !?")
elif distance < 5:
    print("Not sending items")
elif distance <= 50:
    print("price = 10 Bath")
elif distance <= 100:
    print("price = 15 Bath")
elif distance <= 300:
    print("price = 25 Bath")
elif distance <= 500:
    print("price = 35 Bath")
else:
    print("price = 45 Bath")