import random
import json
from tkinter import *
from tkinter import messagebox

window = Tk()
# window.config(width=800, height=600)
window.title("Blackjack")
window.configure(bg="#0c7741",padx=10, pady=10)
window.iconbitmap("icon.ico")

logo = PhotoImage(file="logo.png")
logo_label = Label(image=logo, bg="#0c7741")
logo_label.grid(row=0, column=1, columnspan=3, padx=10, pady=10)

dealer_img = PhotoImage(file="dealer.png")
dealer_label = Label(image=dealer_img, bg="#0c7741")
dealer_label.grid(row=1, column=0, padx=10, pady=10)

player_img = PhotoImage(file="player.png")
player_label = Label(image=player_img, bg="#0c7741")
player_label.grid(row=2, column=0, padx=10, pady=10)

hit_button = Button(text="HIT", padx=5, pady=5)
hit_button.grid(row=3, column=1, columnspan=3, padx=5, pady=5)

pass_button = Button(text="PASS", padx=5, pady=5)
pass_button.grid(row=3, column=2, columnspan=3, padx=5, pady=5)

player_cards = []
dealer_cards = []

def card_generate():
    f = open("cards_dict.json")
    data = json.load(f)

    card = random.choice(data)
    return card


def starting_position():
    player_cards.append(card_generate()["value"])
    dealer_cards.append(card_generate()["value"])
    player_cards.append(card_generate()["value"])
    dealer_cards.append(card_generate()["value"])

starting_position()

print(player_cards, dealer_cards)


window.mainloop()


# def blackjack(user_cards, user_score, delaer_cards, dealer_score):  
#     global win
#     if user_score > 21 and 11 in user_cards:
#         for i in range(0, user_cards):
#             if user_cards[i] == 11:
#                 user_cards[i] = 1
#     if dealer_score > 21 and 11 in delaer_cards:
#         for i in delaer_cards:
#             if delaer_cards[i] == 11:
#                 delaer_cards[i] = 1

#     if 11 in user_cards and 10 in user_cards and 11 not in delaer_cards and 10 not in delaer_cards:
#         print("You win with Blackjack!")
#         win = True
#     if 11 in delaer_cards and 10 in delaer_cards:
#         print("The dealer wins with Blackjack!")
#         print(f"Dealer cards: {delaer_cards}, dealer score: {dealer_score}")
#         win = False


# if start == "start":
#     user_cards = [random.choice(cards), random.choice(cards)]
#     delaer_cards = [random.choice(cards), random.choice(cards)]

#     user_score = sum(user_cards)
#     dealer_score = sum(delaer_cards)
  
#     print(f"Your cards: {user_cards}, your score: {user_score}") 
#     print(f"Dealer's first card: {delaer_cards[0]}")
    
#     blackjack(user_cards, user_score, delaer_cards, dealer_score)

    
#     while win != True and win != False:
#         get_or_pass = input("Type 'y' to get antoher card, type 'n' to pass:  ")

#         if get_or_pass == "y":
#             user_cards.append(random.choice(cards))
#             user_score = sum(user_cards)
#             print(f"Your cards: {user_cards}, your score: {user_score}") 
#             print(f"Dealer's first card: {delaer_cards[0]}")

#             blackjack(user_cards, user_score, delaer_cards, dealer_score)
#             if user_score > 21:
#                 win = False
#                 print("The Dealer wins!")
#                 print(f"Dealer cards: {delaer_cards}, dealer score: {dealer_score}")

#         else:
#             while dealer_score < 16:
#                 delaer_cards.append(random.choice(cards))
#                 dealer_score = sum(delaer_cards)
#             print(f"Your cards: {user_cards}, your score: {user_score}") 
#             user_score = sum(user_cards)
#             if user_score > 21:
#                 win = False
#                 print("The Dealer wins!")
#                 print(f"Dealer cards: {delaer_cards}, dealer score: {dealer_score}")
#             else:
#                 blackjack(user_cards, user_score, delaer_cards, dealer_score)
#                 if (21-user_score) < (21-dealer_score) or dealer_score > 21:
#                     win = True
#                     print("You win!")
#                     print(f"Dealer cards: {delaer_cards}, dealer score: {dealer_score}")
#                 elif user_score == dealer_score:
#                     win = False
#                     print("Draft!")
#                 else:
#                     win = False
#                     print("The dealer wins!")
#                     print(f"Dealer cards: {delaer_cards}, dealer score: {dealer_score}")

            
            
            
           

            
            



    

    








