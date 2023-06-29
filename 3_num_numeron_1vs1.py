# 3桁数字当てゲーム(1 VS 1)(数字被りなし)

import random  
import getpass
import time

player1 = input("player1は名前を決めてください　")
player2 = input("player2は名前を決めてください　")

player1_num = getpass.getpass(prompt = f"「{player1}」 は三桁(被りなし)の数字を入力してください")
player2_num = getpass.getpass(prompt = f"「{player2}」 は三桁(被りなし)の数字を入力してください")
#print(player1_num) #文頭の「#」を外すと打った数字が確認できます。
#print(player2_num)

play1_ans = []
play2_ans = []

for i in range(3):
    play1_ans.append(int(player1_num[i]))
    play2_ans.append(int(player2_num[i]))

while True:
    player1_ans = []
    player2_ans = []
    eat_1 , eat_2 , bite_1 , bite_2 = 0 , 0 , 0 , 0
    ask = str(input(f"{player1}⇒{player2}  "))
    print(ask)
    for i in range(3):
        ask_num = int(ask[i])
        player1_ans.append(ask_num)
    for l in range(3):
        if player1_ans[l] in play2_ans:
            if player1_ans[l] == play2_ans[l]:
                eat_2 += 1
            else:
                bite_2 += 1
    if eat_2 == 3:
        break
    print(f"{ask}・・・EAT:{eat_2} BITE:{bite_2}  ")
    
    ask = input(f"{player2}⇒{player1}  ")
    print(ask)
    for i in range(3):
        ask_num = int(ask[i])
        player2_ans.append(ask_num)
    for l in range(3):
        if player2_ans[l] in play1_ans:
            if player2_ans[l] == play1_ans[l]:
                eat_1 += 1
            else:
                bite_1 += 1
    if eat_1 == 3:
        break
    print(f"{ask}・・・EAT:{eat_1} BITE:{bite_1}  ")

if eat_1 == 3:
    print(f"おめでとう!{player2}の勝利!")
    time.sleep(2)
    print(f"{player1}・・・「{player1_num}」,{player2}・・・「{player2_num}」でした！")    
else:
    print(f"おめでとう!{player1}の勝利!")
    time.sleep(2)
    print(f"{player1}・・・「{player1_num}」,{player2}・・・「{player2_num}」でした！")    