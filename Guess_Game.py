import random       #ماژول رندوم را وارد برنامه می‌کند تا بتوانیم عدد تصادفی بسازیم

MIN_NUMBER = 1      #کمترین عدد 
MAX_NUMBER = 100    #بیشترین عدد
MAX_ATTEMPTS = 5    #تعداد فرصت ها
CLOSE_THRESHOLD = 5     # اختلاف تا ۵  => خیلی نزدیک
MEDIUM_THRESHOLD = 15   # اختلاف تا ۱۵ => متوسط، بیشتر از آن => دور

RANKS = {          
    1: "Exemplary",
    2: "Excellent",
    3: "Good",
    4: "Acceptable",
    5: "You won by luck!",    #با توجه بع جزوه شماره تلاش و رتبه
 }



def read_guess():    #گرفتن حدس معتبر
    text = input(f"Enter your guess ({MIN_NUMBER} to {MAX_NUMBER}): ").strip()
    try:
        guess = int(text)
    except ValueError:
        print("Invalid input; please enter a whole number. (No attempt was used)")
        return None
    if guess < MIN_NUMBER or guess > MAX_NUMBER:
        print(f"The number must be between {MIN_NUMBER} and {MAX_NUMBER}. (No attempt was used)")
        return None
    return guess


def closeness_hint(difference):    #راهمما نزدیک بودن#   اختلاف
    if difference <= CLOSE_THRESHOLD:
        return "Very close!"
    elif difference <= MEDIUM_THRESHOLD:
        return "Close, but still some distance away!"
    else:
        return "Very far!"


def play_round():    #یک دور بازی
    secret = random.randint(MIN_NUMBER, MAX_NUMBER)
    attempt = 1    #شمارنده

    while attempt <= MAX_ATTEMPTS:
        print()
        print(f"Attempt {attempt} of {MAX_ATTEMPTS}")
        print(f"Lives left: {MAX_ATTEMPTS - attempt + 1}")
 
        guess = read_guess()
        if guess is None:
            continue  # شمارنده تلاش تغییر نمی‌کند

        if guess == secret:
            print("Congratulations! You guessed it, you win!")
            print(f"Your rank: {RANKS[attempt]}")
            return
 

        direction = "Enter a larger number" if guess < secret else "Enter a smaller number"
        print(f"{direction} - {closeness_hint(abs(guess - secret))}")
        attempt += 1  #یک تلاش مصرف شد

    print()
    print("Sorry, you lost! You have no attempts left.")
    print(f"The secret number was {secret}.")
 

def ask_play_again():  #پرسیدن بازی مجدد
    while True:
        answer = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if answer in ("yes", "y", "بله", "بلی"):
            return True
        if answer in ("no", "n", "خیر", "نه"):
            return False
        print('Please enter only "yes" or "no".')
 

def main():  #اجرای برنامه
    print("Welcome to the Number Guessing Game!")
    play_again = True
    while play_again:
        play_round()
        play_again = ask_play_again()
    print("Goodbye!")


if __name__ == '__main__':
    main()