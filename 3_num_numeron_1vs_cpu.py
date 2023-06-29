# 3桁数字当てゲーム(シングルプレイ)(数字被りなし)

import random  
import time

com_ans = []

kaisu = 0
    
while len(com_ans) < 3:
    num = random.randint(0,9)
    if (len(com_ans) > 0) and (num not in com_ans) :
        com_ans.append(num)
    elif (len(com_ans) == 0) and (num != 0):
        com_ans.append(num)
# print(com_ans) #この文頭の♯を消すと、数字が出てきます


time.sleep(1)
print("コンピューターによる三桁の数字が決定しました！")
print("3桁の数字(被りなし)を予想して入力してください")
while True :
    player_ans = []
    kaisu += 1
    eat = 0
    bite = 0
    ask = str(input())
    for i in range(3):
        ask_num = int(ask[i])
        player_ans.append(ask_num)
    for l in range(3):
        if player_ans[l] in com_ans:
            if player_ans[l] == com_ans[l]:
                eat += 1
            else:
                bite += 1
    if eat == 3:
        break
    print(f"・・・EAT:{eat} BITE:{bite}")

time.sleep(1)
print(f"当たり、{kaisu}回目で当たりました！答えは「{ask}」です。")
time.sleep(2)
