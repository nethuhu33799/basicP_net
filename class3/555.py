while True :
    chioice = int(input("กรอก 1 เพื่อบวกเลข , กรอก 2 เพื่อออก"))
    if chioice == 1:
        num = int(input("จำนวนเลขที่จะบวก : "))
        sumation = 0

        for i in range (num):
            num1 = int(input("กรอกเลข : "))
            sumation = sumation + num1
        print("ผลลัพธ์", sumation)

    if chioice == 2:
        print("บาย บาย")
        break