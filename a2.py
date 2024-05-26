cards={'AH':100,'JH':90,'KH':80,'QH':70,'H2':60,'H3':50,'H4':40,'H5':30,'H6':20,'H7':10,'H8':5,'H9':2,'H10':0}
round=0

player1=" "
player2=" "
while True:
	round=round+1
	print("round",round)
	player1=str(input("player1 enter your card: "))
	player2=str(input("player2 enter your card: "))
	
	

	if round==6:
		break
score_p1=0
score_p2=0
if player1 in cards and player2 in cards:
    if(cards[player1]>cards[player2]):
       score_p1+=10
    if(cards[player1]<cards[player2]):
        score_p2+=10
else:
    print("invalid card")
print("player1 score is",score_p1)
print("player2 score is",score_p2)
