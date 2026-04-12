import random

balance = 100

def spin_roulette(bet_color, bet_amount):
    global balance
    
    roll = random.randint(1, 100)

    if 1 <= roll <= 49:
        result = "красное"
    elif 50 <= roll <= 98:
        result = "черное"
    else:
        result = "зеленое"
    
    print(f"Выпало: {result}")

    if bet_color == result:
        if result == "красное":
            win = 25
        elif result == "черное":
            win = 50
        else:
            win = 500
        
        balance += win
        print(f"Ты выиграл +{win} монет 🎉")
    else:
        balance -= bet_amount
        print(f"Ты проиграл -{bet_amount} монет ❌")
    
    print(f"Баланс: {balance}\n")


while True:
    print(f"Текущий баланс: {balance}")
    
    bet_color = input("Выбери цвет (красное/черное/зеленое): ").lower()
    if bet_color not in ["красное", "черное", "зеленое"]:
        print("Неверный выбор цвета!\n")
        continue
    
    bet_amount = int(input("Введите сумму ставки: "))
    
    if bet_amount > balance:
        print("Недостаточно монет!\n")
        continue
    
    print("Ставка утверждена ✅")
    
    input("Нажми Enter, чтобы крутить рулетку...")
    spin_roulette(bet_color, bet_amount)