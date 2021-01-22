#Made by A3therium
#import libaries and set variables
import random
import PySimpleGUI as sg

pWin=""
pWins=0
dWins=0
#Set Window
sg.theme('DarkAmber')
layout=[
        [sg.Text("Welcome To Blackjack!")],
        [sg.Button("Start?")]
    ]
window=sg.Window("BlackJack",layout,margins=(300,150), element_justification='c')
event, values = window.read()
while True:

    print()
    print("Welcome to Blackjack!")
    print("Current session wins:")
    print("Your Wins: "+str(pWins))
    print("Dealer Wins: "+str(dWins))
    print()
    print()
    
    #draw cards and store for players
    pCard1 = random.randint(1,13)
    pCard2 = random.randint(1,13)
    pTotal = pCard1 + pCard2
    dCard1 = random.randint(1,13)
    dCard2 = random.randint(1,13)
    dTotal = dCard1 + dCard2
    #display cards
    print()
    print("Your Cards: ")
    print("- "+str(pCard1))
    print("- "+str(pCard2))
    print("Total: "+str(pTotal))
    print("---------")
    print("Dealer's Cards:")
    print("- "+str(dCard1))
    print("- ?")
    print("Total: ?")
    print()
    print()
    print()
    window.close()
    layout=[
            [sg.Text("Current Session Wins :\nYour Wins: "+str(pWins)+"\nDealer Wins: "+str(dWins)+"\n------------------------------------\nYour Cards: \n- "+str(pCard1)+"\n- "+str(pCard2)+"\n Total: "+str(pTotal)+"\n-----------\nDealer's Cards: \n- "+str(dCard1)+"\n- ?\nTotal: ?")],
            [sg.Button("---HIT---")],
            [sg.Button("STAND")]
        ]
    window=sg.Window("BlackJack",layout,margins=(300,150), element_justification='c')
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    #hit or stand
    if pTotal <= 21:
        if event == "---HIT---":
            hitOrStand="hit"
        else:
            hitOrStand="stand"
        firstLoopToggle=0
        pBust=0
        while hitOrStand == "hit":
            pCardTemp = random.randint(1,13)
            pTotal = pTotal + pCardTemp
            print()
            print("You draw "+str(pCardTemp))
            print("Your total is "+str(pTotal))
            
            if pTotal >= 22:
                print("Your BUST !")
                hitOrStand=""
                pBust=1
                window.close()
                layout=[
                    [sg.Text("You are bust!")],
                    [sg.Button("Next ->")]
                ]
                window=sg.Window("BlackJack",layout,margins=(300,150), element_justification='c')
                event, values = window.read()
            else:
                print()
                window.close()
                layout=[
                    [sg.Text("Current Session Wins :\nYour Wins: "+str(pWins)+"\nDealer Wins: "+str(dWins)+"\n------------------------------------\nYou draw "+str(pCardTemp)+"\nYour total is "+str(pTotal)+"\nDealer's Cards: \n- "+str(dCard1)+"\n- ?\nTotal: ?")],
                    [sg.Button("---HIT---")],
                    [sg.Button("STAND")]
                ]
                window=sg.Window("BlackJack",layout,margins=(300,150), element_justification='c')
                event, values = window.read()
                firstLoopToggle=1
                if event == "---HIT---":
                    hitOrStand="hit"
                else:
                    hitOrStand="stand"
        print()
        print("The dealer's hidden card is a "+str(dCard2))
        print("Dealer's total is "+str(dTotal))
        window.close()
        layout=[
            [sg.Text("The dealer's hidden card is a "+str(dCard2)+"\nDealer's total is "+str(dTotal))],
            [sg.Button("Next ->")]
        ]
        window=sg.Window("BlackJack",layout,margins=(300,150), element_justification='c')
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        while dTotal <= 17 and pBust==0:
            dCardTemp = random.randint(1,13)
            dTotal = dTotal + dCardTemp
            print()
            print("The dealer draws "+str(dCardTemp))
            print("The dealer's total is "+str(dTotal))
            window.close()
            layout=[
                [sg.Text("The dealer draws "+str(dCardTemp)+"\nThe dealer's total is "+str(dTotal))],
                [sg.Button("Next ->")]
            ]
            window=sg.Window("BlackJack",layout,margins=(300,150), element_justification='c')
            event, values = window.read()
            if dTotal >= 22:
                print("The dealer is BUST !")
                window.close()
                layout=[
                    [sg.Text("The dealer is bust!")],
                    [sg.Button("Next ->")]
                ]
                window=sg.Window("BlackJack",layout,margins=(300,150), element_justification='c')
                event, values = window.read()
    #calculate the winner
    if pTotal >= 22:
        pWin="The dealer"
        dWins+=1
    elif dTotal >= 22:
        pWin="You"
        pWins+=1
    else:
        if dTotal >= pTotal:
            pWin="The dealer"
            dWins+=1
        else:
            pWin="You"
            pWins+=1
    print()
    print(pWin+" WIN!")
    window.close()
    layout=[
        [sg.Text(pWin+" WIN!")],
        [sg.Button("Next ->")]
    ]
    window=sg.Window("BlackJack",layout,margins=(300,150), element_justification='c')
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break





    
