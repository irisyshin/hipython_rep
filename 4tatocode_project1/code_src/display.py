from . import menu 
from . import payment_membership
import time

# 첫 화면 + 메뉴판 
def display_menu():
    print('*' * 40)
    print('어서오세요, ‘요렇게’에 오신 것을 환영합니다:)')
    print("Menu\t\t\t\tPrice")
    print("-" * 30)
    print("요거트 아이스크림(250g)\t3,000")
    print("-" * 30)
    print("\nNo. Topping\t\tPrice")
    print("-" * 30)
    for idx, item in enumerate(menu.menu_list, start=1):
        print(f"{idx:<5} {item['name']:<10}\t{item['price']:,}")
    print("-" * 30)
    print("*" * 40)

#현재 장바구니에 있는 물품, 가격, total price display
def display_cart(cart, total_price):
    print("\n" + "=" * 40)
    print("현재 장바구니")
    for i, item in enumerate(cart, start=1):
        print(f"{i}. {item['name']} x {item['quantity']} = {item['price'] * item['quantity']:,}원")
    print("-" * 40)
    print(f"Total = {total_price:,}원")

#back to main display w. 5 sec timers
def end_screen_delay():
    print("초기화면으로 돌아갑니다.")
    for i in range(5, 0, -1):
        print(f"{i} ", end='\r', flush=True)
        time.sleep(1)
    print(" ", end='\r')