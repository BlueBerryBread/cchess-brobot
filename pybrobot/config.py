

'''''''''''''''运动信息'''''''''''''''''
# 机械臂参数
SPEEDRATE = 1

# 按键位置/准备位置
POS_READY = (-192.48, -146.13, 132.58)

'''''''''''''''内置参数'''''''''''''''''
# 控制信号
CTRL_BEGIN    = 0x01  # (开始) BB BB 03 41 03 01 BB
CTRL_PAUSE    = 0x02  # (暂停) BB BB 03 41 03 02 BA
CTRL_CONTINUE = 0x03  # (继续) BB BB 03 41 03 03 B9
CTRL_CANCEL   = 0x04  # (取消) BB BB 03 41 03 04 B8
CTRL_END      = 0x05  # (结束) BB BB 03 41 03 05 B7

# 气泵
PUMP_SUCK = 0x01 # (吸气) BB BB 03 BF 04 01 3C
PUMP_STOP = 0x00 # (停)   BB BB 03 BF 04 00 3D
PUMP_BLOW = 0x02 # (吹气) BB BB 03 BF 04 02 3B




'''''''''''''''位置信息'''''''''''''''''
# 0. 取夹具，定标定杆，位置校准
# 1. 采集棋盘四角位置信息(x, y), 更新 # 棋盘区域
# 2. 采集存放区四角位置信息(x, y), 更新 # 存子区域
# 3. 运行计算并更新CHESSBOARD 和 PIECEBOARD

# 棋盘区域
POS_BOARD_LEFTDOWN  = ( 132, -163)
POS_BOARD_RIGHTDOWN = (-132, -163)
POS_BOARD_LEFTUP    = ( 132, -433)
POS_BOARD_RIGHTUP   = (-132, -433)  
# 存子区域
POS_STORE_LEFTDOWN  = (-170, -186)
POS_STORE_RIGHTDOWN = (-200, -213)
POS_STORE_LEFTUP    = (-170, -412)
POS_STORE_RIGHTUP   = (-200, -384)

# CHESSBOARD
#   81  . . . .  88 89
#   . .     .
#   . .   .
#   . . .
#   9 . . . . .  
#   0 1 2 3 4 5 6 7 8
CHESSBOARD = ((132, -163), (99, -163), (66, -163), (33, -163), (0, -163), (-33, -163), (-66, -163), (-99, -163), (-132, -163), (132, -193), (99, -193), (66, -193), (33, -193), (0, -193), (-33, -193), (-66, -193), (-99, -193), (-132, -193), (132, -223), (99, -223), (66, -223), (33, -223), (0, -223), (-33, -223), (-66, -223), (-99, -223), (-132, -223), (132, -253), (99, -253), (66, -253), (33, -253), (0, -253), (-33, -253), (-66, -253), (-99, -253), (-132, -253), (132, -283), (99, -283), (66, -283), (33, -283), (0, -283), (-33, -283), (-66, -283), (-99, -283), (-132, -283), (132, -313), (99, -313), (66, -313), (33, -313), (0, -313), (-33, -313), (-66, -313), (-99, -313), (-132, -313), (132, -343), (99, -343), (66, -343), (33, -343), (0, -343), (-33, -343), (-66, -343), (-99, -343), (-132, -343), (132, -373), (99, -373), (66, -373), (33, -373), (0, -373), (-33, -373), (-66, -373), (-99, -373), (-132, -373), (132, -403), (99, -403), (66, -403), (33, -403), (0, -403), (-33, -403), (-66, -403), (-99, -403), (-132, -403), (132, -433), (99, -433), (66, -433), (33, -433), (0, -433), (-33, -433), (-66, -433), (-99, -433), (-132, -433))
# PIECEBOARD
#   8 
#   . 15
#   . . 
#   . . 
#   2 10
#   1 9   
#   0
PIECEBOARD = ((-170, -186), (-170, -214), (-170, -242), (-170, -270), (-170, -298), (-170, -326), (-170, -354), (-170, -382), (-170, -410), (-200, -213), (-200, -241), (-200, -269),(-200, -297), (-200, -325), (-200, -353), (-200, -381))


if __name__ == "__main__":
    
    # 计算棋盘位置列表
    print("********************************************计算棋盘位置矩阵CHESSBOARD*********************************************")
    chessboard = []
    detal_x = round((POS_BOARD_LEFTDOWN[0] - POS_BOARD_RIGHTDOWN[0]) / 8 )
    detal_y = round((POS_BOARD_RIGHTDOWN[1] - POS_BOARD_RIGHTUP[1])  / 9)
    zero_x, zero_y =  POS_BOARD_LEFTDOWN[0], POS_BOARD_LEFTDOWN[1]
    print("datl_x, datl_y: ", detal_x, detal_y)
    print("zero_x, zero_y: ", zero_x, zero_y)
    print("chessboard:")
    for y in range(10):
        for x in range(9):
            pos = (zero_x - x*detal_x, zero_y - y*detal_y)
            print(pos, end = " ")
            chessboard.append(pos)
        print()
    print("CHESSBOARD: ", chessboard)

    # 计算存子区域位置列表
    print("********************************************计算吃子存储矩阵PIECEBOARD********************************************")
    pieceboard = []
    detal_y = round((POS_STORE_RIGHTDOWN[1] - POS_STORE_RIGHTUP[1])  / 6)
    zero_x_1, zero_y_1 = POS_STORE_LEFTDOWN[0], POS_STORE_LEFTDOWN[1]
    zero_x_2, zero_y_2 = POS_STORE_RIGHTDOWN[0], POS_STORE_RIGHTDOWN[1] 
    print("datl_y: ", detal_y)
    print("zero_x_1, zero_y_1: ", zero_x_1, zero_y_2)
    print("zero_x_2, zero_y_2: ", zero_x_2, zero_y_2)
    print("pieceboard:")
    for y in range(9):
        pos = (zero_x_1, zero_y_1 - y*detal_y)
        print(pos, end = " ")
        pieceboard.append(pos)
    print()
    for y in range(7):
        pos = (zero_x_2, zero_y_2 - y*detal_y)
        print(pos, end = " ")
        pieceboard.append(pos)
    print()
    print("PIECEBOARD: ", pieceboard)
