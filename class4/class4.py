# def Doo_Grade(x): # X คือ พารามิเตอ์ Doo_Grade อากิวเมน
#     if x < 0:
#         print("กาก")
#     elif x < 50:
#         print("F")
#     elif x <= 60:
#         print("D")
#     elif x <= 70:
#         print("E")
#     elif x <= 80:
#         print("B")
#     elif x <= 100:
#         print("A")
#     elif x > 100:
#         print("God")
        
# grade = int(input("Enter your distance : "))
# Doo_Grade(grade)


# # # # --------------------------------------------------------------------
# # # # def my_sum(a,b):
# # # #     return a+b

# # # # result = my_sum(5,5)
# # # # print(result)
# # # # --------------------------------------------------------------------
# # # def menu():
# # #     while True :
# # #         n = int(input("1.เลือกคำนวณราคาสินค้า 2.ออก"))
# # #         if n==1:
# # #             Mony1 = int(input("สินค้าอันชิ้น :"))
# # #             mony2 = int(input("จำนวนสินค้า :"))
# # #             print(price(Mony1,mony2))
# # #         elif n == 2 :
# # #                 print("out")
# # #                 break
# # # def price(Mony1,mony2):
# # #     Vatb = ((Mony1*mony2)*(0.07))
# # #     resule = Vatb + (mony2*Mony1)
# # #     return resule

# # # menu()

# # my_list = ["net",'A',13]
# # print (my_list[0:3])
# # print (my_list[-3:3])

# # my_list[0]=1111
# # print(my_list[0])
# # print(my_list[0:3])
# # my_list.append("new")
# # print(my_list)

# # print(my_list)
# # print(my_list.pop(1))
# # print(my_list)

# # print("----------------------------------------------------------------]")
# # for i in my_list:
# #     print(i)
# # print("===================================================================")
# # my_dice = {
# #     "name":"tanaphon",
# #     "age":20,
# #     "No":26
# # }
# # print("Age : ",my_dice["age"])
# # my_dice["age"]=18
# # print("Age : ",my_dice["age"])


# print("========================================================================")

# students = [
#     {"name":"net","id":26,"score":88},
#     {"name":"sua","id":11,"score":98},
#     {"name":"zodz","id":65,"score":89}
# ]
# for i in students:
#     print(i["name"])

print("==========================================================================")
for students in students:
    if (students["score"] >= 90):
        students["score"]='A'
    else : students["score"]='B'
    print(students)