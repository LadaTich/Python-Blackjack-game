import random
import json
from tkinter import *
from tkinter import messagebox
from PIL import Image



def card_generate():
    f = open("cards_dict.json")
    data = json.load(f)

    card = random.choice(data)
    return card

def starting_position():

    player_cards.append(card_generate())
    dealer_cards.append(card_generate())
    player_cards.append(card_generate())
    dealer_cards.append(card_generate())

    show_cards()
    
    blackjack_check()

    player_ace_check()
    dealer_ace_check()
    
    player_score_increase()
    dealer_score_increased()


def player_ace_check():
    if end == False:

        for card in player_cards:
            if card["value"] == "ace":
                ace = messagebox.askquestion("Blackjack", "Ace in your cards!\nClick on YES to count it as 11 or NO to count it as 1")
                if ace == "yes":
                    card["value"] = 11
                elif ace == "no":
                    card["value"] = 1
    
def dealer_ace_check():
    if end == False:
        for card in dealer_cards:
            if card["value"] == "ace":
                if dealer_score + 11 > 21:
                    card["value"] = 1
                else:
                    card["value"] = 11

def show_cards():

    for card in range(len(player_cards)):
        
        label_name = f"player_card_label{card + 1}"
        
        img = PhotoImage(file=f'cards/{player_cards[card]["path"]}')

        labels[label_name].config(image = img)
        labels[label_name].image = img

    for card in range(len(dealer_cards)):
        
        label_name = f"dealer_card_label{card + 1}"
        if label_name == "dealer_card_label1":
            img = PhotoImage(file=f'cards/{dealer_cards[card]["path"]}')
        else:
            img = PhotoImage(file="bottom.png")

        labels[label_name].config(image = img)
        labels[label_name].image = img

def player_score_increase():
    if end == False:
        for score in player_cards:
            global player_score
            player_score += int(score["value"])
            score_label.config(text=f"Your score: {player_score}")

def dealer_score_increased():
    if end == False:
        for score in dealer_cards:
            global dealer_score
            dealer_score += int(score["value"])

def score_check():
    global end
    if player_score > 21:
        messagebox.showinfo("Blackjack", f"You lose, the dealer wins!\nYour score: {player_score}, Dealer's score: {dealer_score}")
        window.destroy()
        end = True

    else:
        if player_score == dealer_score:
            messagebox.showinfo("Blackjack", f"It's a draft!\nYour score: {player_score}, Dealer's score: {dealer_score}")
            window.destroy()
            end = True
        elif dealer_score > 21:
            messagebox.showinfo("Blackjack", f"You won! the dealer lose.\nYour score: {player_score}, Dealer's score: {dealer_score}")
            window.destroy()
            end = True
        else:
            if (21-player_score) < (21-dealer_score):
                messagebox.showinfo("Blackjack", f"You won! the dealer lose.\nYour score: {player_score}, Dealer's score: {dealer_score}")
                window.destroy()
                end = True
                
            elif (21-player_score) > (21-dealer_score):
                messagebox.showinfo("Blackjack", f"You lose, the dealer wins!\nYour score: {player_score}, Dealer's score: {dealer_score}")
                window.destroy()
                end = True
                
                

def hit_card():
    global end
    card = card_generate()
    player_cards.append(card)

    player_ace_check()

    global player_score
    player_score += int(card["value"])

    score_label.config(text=f"Your score: {player_score}")
    
    show_cards()

    if player_score > 21:
        dealer_cards_show()
        messagebox.showinfo("Blackjack", f"You lose, the dealer wins!\nYour score: {player_score}, Dealer's score: {dealer_score}")
        window.destroy()
        end = True

def dealer_hit_card():

    
    for card in range(len(dealer_cards)):
        label_name = f"dealer_card_label{card + 1}"

        img = PhotoImage(file=f'cards/{dealer_cards[card]["path"]}')

        labels[label_name].config(image = img)
        labels[label_name].image = img

    global dealer_score
    while dealer_score < 17:
        card = card_generate()
        dealer_cards.append(card)
        dealer_ace_check()
        dealer_score += int(card["value"])

        dealer_cards_show()

    else:
        score_check()
    

def blackjack_check():
    global end
    d_blackjack = False
    p_blackjack = False

    if dealer_cards[0]["value"] == 10 and dealer_cards[1]["value"] == "ace":
        d_blackjack = True
    elif dealer_cards[0]["value"] == "ace" and dealer_cards[1]["value"] == 10:
        d_blackjack = True

    if player_cards[0]["value"] == 10 and player_cards[1]["value"] == "ace":
        p_blackjack = True
    elif player_cards[0]["value"] == "ace" and player_cards[1]["value"] == 10:
        p_blackjack = True
            
    if d_blackjack == True and p_blackjack == True:
        dealer_cards_show()
        messagebox.showinfo("Blackjack", f"It's a blackjack draft!")
        window.destroy()
        end = True
    elif d_blackjack == True and p_blackjack == False:
        dealer_cards_show()
        messagebox.showinfo("Blackjack", f"The dealer wins with blackjack!")
        window.destroy()
        end = True
    elif p_blackjack == True and d_blackjack == False:
        dealer_cards_show()
        messagebox.showinfo("Blackjack", f"You won with blackjack!")
        window.destroy()
        end = True


def dealer_cards_show():
    for card in range(len(dealer_cards)):
        
            label_name = f"dealer_card_label{card + 1}"

            img = PhotoImage(file=f'cards/{dealer_cards[card]["path"]}')

            labels[label_name].config(image = img)
            labels[label_name].image = img

end = False

player_cards = []
dealer_cards = []

player_score = 0
dealer_score = 0

window = Tk()
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

score_label = Label(text=f"Your score: {player_score}")
score_label.grid(row=3, column=0)

hit_button = Button(text="HIT", padx=5, pady=5, command=hit_card)
hit_button.grid(row=3, column=1, columnspan=3, padx=5, pady=5)

pass_button = Button(text="PASS", padx=5, pady=5, command=dealer_hit_card)
pass_button.grid(row=3, column=2, columnspan=3, padx=5, pady=5)

player_card_label1 = Label(bg="#0c7741")
player_card_label1.grid(row=2, column=1, padx=10, pady=10)

player_card_label2 = Label(bg="#0c7741")
player_card_label2.grid(row=2, column=2, padx=10, pady=10)

player_card_label3 = Label(bg="#0c7741")
player_card_label3.grid(row=2, column=3, padx=10, pady=10)

player_card_label4 = Label(bg="#0c7741")
player_card_label4.grid(row=2, column=4, padx=10, pady=10)

player_card_label5 = Label(bg="#0c7741")
player_card_label5.grid(row=2, column=5, padx=10, pady=10)

player_card_label6 = Label(bg="#0c7741")
player_card_label6.grid(row=2, column=6, padx=10, pady=10)

dealer_card_label1 = Label(bg="#0c7741")
dealer_card_label1.grid(row=1, column=1, padx=10, pady=10)

dealer_card_label2 = Label(bg="#0c7741")
dealer_card_label2.grid(row=1, column=2, padx=10, pady=10)

dealer_card_label3 = Label(bg="#0c7741")
dealer_card_label3.grid(row=1, column=3, padx=10, pady=10)

dealer_card_label4 = Label(bg="#0c7741")
dealer_card_label4.grid(row=1, column=4, padx=10, pady=10)

dealer_card_label5 = Label(bg="#0c7741")
dealer_card_label5.grid(row=1, column=5, padx=10, pady=10)

dealer_card_label6 = Label(bg="#0c7741")
dealer_card_label6.grid(row=1, column=6, padx=10, pady=10)

labels = {
    "player_card_label1" : player_card_label1,
    "player_card_label2" : player_card_label2,
    "player_card_label3" : player_card_label3,
    "player_card_label4" : player_card_label4,
    "player_card_label5" : player_card_label5,
    "player_card_label6" : player_card_label6,
    "dealer_card_label1" : dealer_card_label1,
    "dealer_card_label2" : dealer_card_label2,
    "dealer_card_label3" : dealer_card_label3,
    "dealer_card_label4" : dealer_card_label4,
    "dealer_card_label5" : dealer_card_label5,
    "dealer_card_label6" : dealer_card_label6
}

starting_position()

window.mainloop()
