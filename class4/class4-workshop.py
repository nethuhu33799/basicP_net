# ฟังก์ชันแสดงรายชื่อหนังทั้งหมดในระบบ
def show_movies(movie_list):
    for movie_list in movie_list:
        print(movie_list['movie_name'], "-", movie_list['ticket_price'], "Baht")

# ฟังก์ชันตรวจสอบอายุตามข้อจำกัดของหนัง
def check_age(user_age,age_restriction,choioce,movie_list):
    if user_age>=movie_list[choioce]['age_restriction'] or 'G'== movie_list[choioce]['age_restriction']:
        check = ("Order seccese")
    else:
        check = ("อายุน้อยเกินไป ต้องมากกว่า "+ age_restriction) 
        main()
    return check
# ฟังก์ชันคำนวณราคาตั๋วโดยขึ้นกับประเภทหนัง
def calculate_price(base_price, genre):
    # TODO: ถ้า genre เป็น 'Sci-Fi' บวกเพิ่ม 50 บาท
    # ถ้าไม่ใช่ คืนราคาเดิม
    if genre  == 'Sci-Fi':
        base_price  += 50
    else:
        show_movies_oder()
    return base_price

def soundtrack():
    sound = int(input("เลือกเสียงพากย์ (1 = พากย์ไทย, 2 = Soundtrack) : "))
    return sound

# ฟังก์ชันสำหรับการซื้อบัตรชมหนัง
def buy_ticket(movie_list):
    
    # 1. เรียก show_movies เพื่อแสดงรายชื่อหนัง
    show_movies(movie_list)
    # 2. รับค่าตัวเลือกหนังจากผู้ใช้ (1-5)
    chioce = int(input("เลือกหนังจาก (1-5) : "))
    # 3. รับอายุผู้ใช้
    age_restriction = movie_list[chioce-1]['age_restriction']
    age = int(input("อายุ : "))
    # 4. ตรวจสอบอายุผ่าน check_age
    #    - ถ้าไม่ผ่าน ให้แสดงข้อความว่าอายุน้อยเกินไปและ return ออกจากฟังก์ชัน

    check_age(age,age_restriction,chioce,movie_list)
    # 5. ให้ผู้ใช้เลือกเสียงพากย์ (1 = พากย์ไทย, 2 = Soundtrack)

    soundtrack()
    sound = int(input("เลือกเสียงพากย์ (1 = พากย์ไทย, 2 = Soundtrack) : "))
    # 6. คำนวณราคาตั๋วโดยใช้ calculate_price
    calculate_price(base_price,genre)
    base_price = movies[chioce]['ticket_price']
    genre = movies[chioce]['genre']
    # 7. แสดงผลการซื้อบัตร พร้อมชื่อหนัง, เสียงที่เลือก, ราคาตั๋ว
def show_movies_oder(sound,base_price):
    print(movies[chioce]['movie_name']+"is"+ check + sound + base_price)
    


def main():
    # TODO: สร้างรายการหนังเป็น list ของ dict โดยเก็บข้อมูล movie_name, ticket_price, genre, age_restriction
    movies = [
        {'movie_name': 'Avengers Endgame', 'ticket_price': 300, 'genre': 'Action', 'age_restriction': '13'},
        {'movie_name': 'Inception', 'ticket_price': 280, 'genre': 'Sci-Fi', 'age_restriction': '13'},
        {'movie_name': 'It', 'ticket_price': 180, 'genre': 'Horror', 'age_restriction': '18'},
        {'movie_name': 'The Notebook', 'ticket_price': 250, 'genre': 'Romantic', 'age_restriction': '13'},
        {'movie_name': 'Harry Potter and the Sorcerer\'s Stone', 'ticket_price': 260, 'genre': 'Fantasy', 'age_restriction': 'G'}
    ]
    # TODO: แสดงเมนูให้ผู้ใช้เลือก
    # 1. แสดงหนังทั้งหมด===
    # 2. ซื้อตั๋วหนัง

    # รับค่าตัวเลือกเมนูจากผู้ใช้
    print("1. แสดงหนังทั้งหมด 2. ซื้อตั๋วหนัง")
    menu = int(input("เลือกเมนู: "))
    if menu == 1:
        show_movies(movies)
        return
    if menu == 2:
        buy_ticket(movies)
        
    else : print("ไม่อยู่ในตัวเลือก")
    # TODO: ตรวจสอบเมนูที่เลือก
    # ถ้าเลือก 1 ให้เรียก show_movies พร้อมส่ง movies
    # ถ้าเลือก 2 ให้เรียก buy_ticket พร้อมส่ง movies
    # ถ้าเลือกอื่น ให้แสดงข้อความว่าเมนูไม่ถูกต้อง

# เรียก main เพื่อเริ่มโปรแกรม
main()
