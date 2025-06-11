import time
membership_dict = {}
menu_list = [
    {'name': '바나나', 'price': 4000},
    {'name': '딸기', 'price': 5000},
    {'name': '벌집꿀', 'price': 7000},
    {'name': '그레놀라', 'price': 7000},
    {'name': '초코쉘', 'price': 7000},
    {'name': '요거트 아이스크림', 'price': 3000}
]

def get_valid_number_input(msg, min_no = 1, max_no = 5):
    # 숫자체크
    try:
        number = int(input(msg))
        if number < min_no:
            print(f"{min_no} 이상 숫자를 입력하세요")
            return None
        elif number > max_no:
            print(f"{max_no} 이하 숫자를 입력하세요")
            return None
        else:
            return number
    except ValueError:
        print("숫자를 입력하세요")
        return None

def add_menu(cart, total_price):
    current_total = sum(item['quantity'] for item in cart)
    remaining = 16 - current_total
    
    if remaining <= 0:
        print("장바구니에는 최대 15개까지만 담을 수 있습니다.")
        return total_price

    print("\n메뉴 목록:")
    for i, item in enumerate(menu_list, start=1):
        print(f"{i}. {item['name']} : {item['price']:,}원")
    idx = get_valid_number_input("추가할 토핑 번호를 골라주세요 : ", 1, len(menu_list))
    if idx:
        idx -= 1
        qty = get_valid_number_input(f"수량을 선택해주세요 (남은 수량: {remaining}) : ",1,remaining)
        if qty:
            selected_item = menu_list[idx]
            for item in cart:
                if item['name'] == selected_item['name']:
                    item['quantity'] += qty
                    if item['quantity'] > 15:
                        item['quantity'] = 15
                    break
            else:
                cart.append({'name': selected_item['name'], 'quantity': qty, 'price': selected_item['price']})
    
            total_price += selected_item['price'] * qty
    return total_price

def del_menu(cart, total_price):
    display_cart(cart, total_price)
    idx = get_valid_number_input("삭제할 메뉴의 번호를 골라주세요 : ",1,len(cart))
    if idx:
        idx -= 1
        item = cart[idx]
        print(f"'{item['name']}'의 현재 수량: {item['quantity']}")
        del_qty = get_valid_number_input("몇 개를 삭제하시겠습니까? : ", 1, item['quantity'])
        if del_qty:
            item['quantity'] -= del_qty
            total_price -= item['price'] * del_qty
            print(f"'{item['name']}' {del_qty}개가 삭제되었습니다.")
    return total_price

def select_pro():
    print("메뉴를 확정하려면 o")
    print("메뉴를 삭제하려면 d")
    print("메뉴를 추가하려면 a")
    print("메뉴를 취소하려면 c")
    return input("알파벳을 입력해주세요 : ").lower().strip()
