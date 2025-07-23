while True :
    HP = 200
    character = ["1.Nobi Nobita","2.Gon Furikusu","3.Kurapika"]
    print("Character : ",character[0:3])
    Chioice_character = int(input("Enter your Chioice : "))
    print("Your Character is : ",character[Chioice_character-1])
    
    chioice = int(input("พิมพ์ 1 เพื่อต่อสู้ , พิพม์ 2 เพื่อหนี!!! : "))
    if chioice==1:
        num = int(input("ต้องการสู้กี่รอบ : "))
        for i in range (num):
            print("----HP monster = ",HP,"----")
            if(HP==0):print("***********  ตาย  ***********")
            if(HP<0):print("ยังไม่ตาย")
            print("-----------------------------")
            print("1.ไม้จิ้มฟัน : atk 100")
            print("2.เช็ดชู่ : atk 50")
            print("3.ดินสอ : atk 200")
            print("-----------------------------")
            item = int(input("เลือกอาวุทธ 1 ชิ้น ในรอบนี้ "))
            if item == 1:
                HP-=100
            elif item == 2:
                HP-=50
            elif item == 3:
                HP-=200
            if HP < 0:
                HP = 20
                print("HP monster = ",HP)
            print("////////////////////////////////////////////////////")
        print("คุณตาย เนื่องจาก จัดการมอนไม่ได้")
        print("เริ่มเกมใหม่ เริ่มเกมใหม่ เริ่มเกมใหม่")
        print(".....................................................")
            
            
