from . import menu 
from . import display 

membership_dict = {}
def pay_deci():
    while True:
        answer = input("주문이 확정되었습니다. 결제를 하시겠습니까? (y/n): ").lower().strip()
        if answer in ['y', 'n']:
            return answer
        else:
            print("잘못된 입력입니다. 'y' 또는 'n'을 입력해주세요.")
            
def pay_screen(total_price, num_order):
    print(f"{total_price:,}원 결제하겠습니다. 카드를 삽입해주세요.")
    print("결제가 완료되었습니다.")
    
    while True:
        mem = input("적립 하시겠습니까? (y/n): ").lower().strip()
        if mem == 'y':
            membership_point_save(total_price)
            break
        elif mem == 'n':
            break
        else:
            print("잘못된 입력입니다. 'y' 또는 'n'을 입력해주세요.")
    
    print(f"주문번호는 {num_order}번 입니다.")
    
def membership_point_save(total_price):
    while True:
        phone_input = input("전화번호를 입력해주세요 (- 없이): ").strip()
    
        try:
            phone = int(phone_input)
            if len(phone_input) != 11:  # 길이 체크
                    print("전화번호는 반드시 11자리여야 합니다.")
                    continue
            break
        except (ValueError,TypeError):
            print("입력이 올바르지 않습니다. 다시 시도해주세요.")
        
    points = int(total_price * 0.1)
    
    if phone in membership_dict:
        membership_dict[phone] += points
        print(f"{phone} 번호에 {points}포인트가 추가되어, 총 {membership_dict[phone]}포인트가 있습니다.")
    else:
        membership_dict[phone] = points
        print(f"{phone} 번호로 {points}포인트가 새로 적립되었습니다.")