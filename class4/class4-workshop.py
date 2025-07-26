def dot():
    print("-----------------------------------")
def dot2():
    print("==================================================================================================")
def show_movies(movie_list):
    for mov in movie_list:
        print(f"{mov['movie_name']} - {mov['ticket_price']}")
    dot()
def check_age(user_age, age_restriction):
    if age_restriction == 'G':
        return True
    elif user_age >= int(age_restriction):
        return True
    else: return False
def calculate_price(base_price, genre):
    if genre == 'Sci-Fi':
        base_price+=50
        return base_price
    else : return base_price
def buy_ticket(movie_list):
    chioce = int(input("เลือกหนังจาก (1-5) : "))
    user_age = int(input("กรอกอายุ : "))
    movie = movie_list[chioce-1]
    if check_age(user_age,movie['age_restriction']) == True:
        pass
    if check_age(user_age,movie['age_restriction']) == False: 
        print("ไม่ผ่านข้อกำหนด โปรดเลือกใหม่") 
        return
    dot()
    sound = int(input("(1 = พากย์ไทย, 2 = Soundtrack) : "))
    if sound == 1:
        sound = "พากย์ไทย"
    elif sound == 2:
        sound = "Soundtrack"
    else:
        print("ไม่อยู่ในตัวเลือก")
        main()
    fianl_base_price = calculate_price(movie['ticket_price'],movie['movie_name'])
    dot2()
    print("✅ รายละเอียดการสั่งซื้อ:")
    print(f"🎬 เรื่อง: {movie['movie_name']}")
    print(f"🔊 เสียง: {sound}")
    print(f"💵 ราคาตั๋ว: {fianl_base_price} บาท")
    dot2()
def main():
    movies = [
        {'movie_name': 'Avengers Endgame', 'ticket_price': 300, 'genre': 'Action', 'age_restriction': '13'},
        {'movie_name': 'Inception', 'ticket_price': 280, 'genre': 'Sci-Fi', 'age_restriction': '13'},
        {'movie_name': 'It', 'ticket_price': 180, 'genre': 'Horror', 'age_restriction': '18'},
        {'movie_name': 'The Notebook', 'ticket_price': 250, 'genre': 'Romantic', 'age_restriction': '13'},
        {'movie_name': 'Harry Potter and the Sorcerer\'s Stone', 'ticket_price': 260, 'genre': 'Fantasy', 'age_restriction': 'G'}
    ]
    while True:
        print("1. แสดงตั๋วหนังทั้งหมด \n2. ซื้อตัวหนัง")
        menu = int(input("เลือกเมนู: "))
        dot()
        if menu == 1:
            show_movies(movies)
        elif menu == 2:
            show_movies(movies)
            buy_ticket(movies)
        else : print("ไม่อยู่ในตัวเลือก โปรดใส่ใหม่")
main()