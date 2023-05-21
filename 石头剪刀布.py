import random
choices = ["石头", "布", "剪刀"]
computer = random.choice(choices)
player = False
cpu_score = 0
player_score = 0
while True:
    player = input("石头, 剪刀 或 布?").capitalize()
    # 判断游戏者和电脑的选择
    if player == computer:
        print("平局!")
    elif player == "石头":
        if computer == "布":
            print("你输了!", computer, "包住", player)
            cpu_score+=1
        else:
            print("你赢了!", player, "砸了", computer)
            player_score+=1
    elif player == "布":
        if computer == "剪刀":
            print("你输了!", computer, "剪了", player)
            cpu_score+=1
        else:
            print("你赢了!", player, "包住", computer)
            player_score+=1
    elif player == "剪刀":
        if computer == "石头":
            print("你输了!", computer, "砸了", player)
            cpu_score+=1
        else:
            print("你赢了!", player, "剪了", computer)
            player_score+=1
    elif player=='结束':
        print("最终分数:")
        print(f"输:{cpu_score}")
        print(f"赢:{player_score}")
        break
    else:
        print("这不是一个有效的输入，请重新输入!")
    computer = random.choice(choices)
