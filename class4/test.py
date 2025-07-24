movies = [
    {'movie_name': 'Avengers Endgame', 'ticket_price': 300, 'genre': 'Action', 'age_restriction': '13'},
    {'movie_name': 'Inception', 'ticket_price': 280, 'genre': 'Sci-Fi', 'age_restriction': '13'},
    {'movie_name': 'It', 'ticket_price': 180, 'genre': 'Horror', 'age_restriction': '18'},
    {'movie_name': 'The Notebook', 'ticket_price': 250, 'genre': 'Romantic', 'age_restriction': '13'},
    {'movie_name': 'Harry Potter and the Sorcerer\'s Stone', 'ticket_price': 260, 'genre': 'Fantasy', 'age_restriction': 'G'}
]

def show_movies():
    for movi in movies:
        print(movi['movie_name'], "-", movi['ticket_price'], "Baht")


    print("1. แสดงหนังทั้งหมด 2. ซื้อตั๋วหนัง")
    menu = input("เลือกเมนู: ")
    if menu == 1:how_movies()
    if menu == 2:buy_ticket()
    print("ไม่อยู่ในตัวเลือก")

for i in movie_list:
    print (i+show_movies())
