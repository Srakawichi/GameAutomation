# import pyautogui as gui
# import sys
# 
# print('中断するにはCrt+Cを入力してください。')
# 
# try:
#     while True:
#        x=input("取得したい箇所にカーソルを当てEnterキー押してください\n")
#        print(gui.position())
# 
#        
# except KeyboardInterrupt:
#     print('\n終了')
#     sys.exit()

from tkinter import *  

import datetime
import schedule
import time
import pyautogui

import pyautogui as pag


def Start():
    print(datetime.datetime.now())
    pyautogui.moveTo(1855, 32)
    #Koordinate erreicht doppel Click
    pyautogui.doubleClick()
    #Ant wird geöffnet
    pyautogui.moveTo(3137, 127, duration = 200)#x=3170, y=129
    pyautogui.click()
    

#     #ファイル記入
#     file = open(r"C:\Users\rebek\OneDrive\Desktop\Programme\Python\TheAntsAuto\TAAEintrag.txt","a")
#     t = datetime.datetime.now()
#     file.write(f"LogInBonus successful: {t}\n" )
# 
#     file = open(r"C:\Users\rebek\OneDrive\Desktop\Programme\Python\TheAntsAuto\TAAEintrag.txt","r")
#     print(file.read())
#     file.close()
    
def Routine():
    #VIP 
    pyautogui.moveTo(2720, 126, duration = 1)
    pyautogui.click()
    #Prüfen
    pyautogui.moveTo(2817, 409, duration = 1)
    pyautogui.click()
    #Sammeln
    pyautogui.moveTo(2917, 693, duration = 1)
    pyautogui.click()
    #Anmeldung 
    pyautogui.moveTo(3154, 136, duration = 1)
    pyautogui.click(clicks = 3, interval = 1.5)
    #Raus auv VIPFenster
    pyautogui.moveTo(2687, 62, duration = 1)
    pyautogui.click()
    #
    #女王蟻巣位置のリセット
    pyautogui.press('space',interval = 10)
    pyautogui.press('space')
    #現在のマウスカーソル位置を取得
    pyautogui.moveTo(2924, 545, duration = 3)
    pyautogui.keyDown('ctrl')
    m_posi_x, m_posi_y = pag.position()
    #スクロール
    pag.scroll(-8000,m_posi_x,m_posi_y)
    pag.scroll(-2000,m_posi_x,m_posi_y)
    pag.scroll(-8000,m_posi_x,m_posi_y)
    pag.scroll(-2000,m_posi_x,m_posi_y)
    pyautogui.keyUp('ctrl')
    #champ1
    pyautogui.moveTo(3078, 642, duration = 1)
    pyautogui.click(clicks = 2, interval = 1)
    #Ausbilden
    pyautogui.moveTo(3116, 649, duration = 1)
    pyautogui.click()
    pyautogui.moveTo(3063, 967, duration = 1)
    pyautogui.click()
    #zurück
    pyautogui.moveTo(2663, 80, duration = 1)
    pyautogui.click()
    #champ2
    pyautogui.moveTo(2909, 576, duration = 1)
    pyautogui.click(clicks = 2, interval = 1)
    #Ausbilden
    pyautogui.moveTo(3001, 653, duration = 1)
    pyautogui.click()
    pyautogui.moveTo(3061, 972, duration = 1)
    pyautogui.click()
    #zurück
    pyautogui.moveTo(2663, 80, duration = 1)
    pyautogui.click()
    #Blattschneiderameise1
    pyautogui.moveTo(2831, 519, duration = 1)
    pyautogui.click()
    #Transportieren
    pyautogui.moveTo(2923, 628, duration = 1)
    pyautogui.click()
    pyautogui.moveTo(2924, 672, duration = 1)
    pyautogui.click()
    #champ3
    pyautogui.moveTo(2779, 520, duration = 1)
    pyautogui.click(clicks = 2, interval = 1)
    #Ausbilden
    pyautogui.moveTo(2900, 651, duration = 1)
    pyautogui.click()
    pyautogui.moveTo(3060, 970, duration = 1)
    pyautogui.click()
    #zurück
    pyautogui.moveTo(2670, 85, duration = 1)
    pyautogui.click()
    #Blattschneiderameise2
    pyautogui.moveTo(2924, 172, duration = 1)
    pyautogui.click()
    pyautogui.moveTo(2999, 286, duration = 1)
    pyautogui.click()
    pyautogui.moveTo(2917, 669, duration = 1)
    pyautogui.click()
    #Blattschneiderameise3
    pyautogui.moveTo(2852, 172, duration = 1)
    pyautogui.click()
    pyautogui.moveTo(2928, 271, duration = 1)
    pyautogui.click()
    pyautogui.moveTo(2914, 667, duration = 1)
    pyautogui.click()
    #Essbereich
    pyautogui.moveTo(2790, 450, duration = 10)
    pyautogui.click()
    #Transportieren
    pyautogui.moveTo(2901, 541, duration = 1)
    pyautogui.click()
    pyautogui.moveTo(2919, 739, duration = 1)
    pyautogui.click()
    #ファイル記入
    file = open(r"C:\Users\rebek\OneDrive\Desktop\Programme\Python\TheAntsAuto\TAAEintrag.txt","a")
    t = datetime.datetime.now()
    file.write(f"Routine successful:  {t}\n" )

    file = open(r"C:\Users\rebek\OneDrive\Desktop\Programme\Python\TheAntsAuto\TAAEintrag.txt","r")
    print(file.read())
    file.close()
        
def Spezial():
    #特化アリ
    pyautogui.moveTo(2733, 517, duration = 1)
    pyautogui.click()
    pyautogui.moveTo(2983, 637, duration = 1)
    pyautogui.click()
    #一セット
    pyautogui.moveTo(2920, 831, duration = 1)
    pyautogui.doubleClick(interval = 1)
    pyautogui.moveTo(3162, 57, duration = 1)
    pyautogui.click()
    #二セット
    pyautogui.moveTo(3115, 951, duration = 1)
    pyautogui.click()
    pyautogui.moveTo(2910, 830, duration = 1)
    pyautogui.doubleClick(interval = 1)
    pyautogui.moveTo(3162, 57, duration = 1)
    pyautogui.click()
    #三セット
    pyautogui.moveTo(3121, 957, duration = 1)
    pyautogui.click()
    pyautogui.moveTo(2910, 830, duration = 1)
    pyautogui.doubleClick(interval = 1)
    pyautogui.moveTo(3162, 57, duration = 1)
    pyautogui.click()
    #raus aus Spezialameisenfenster
    pyautogui.moveTo(2687, 62, duration = 1)
    pyautogui.click()
    
def Plündern():
    pyautogui.moveTo(2858, 816, duration = 1)
    pyautogui.click()
    pyautogui.press('space')
    #Lupe
    pyautogui.moveTo(2678, 677, duration = 2)
    pyautogui.click()
    pyautogui.moveTo(3105, 966, duration = 2)
    pyautogui.click()
    #X-Koordinate
    pyautogui.moveTo(2808, 862, duration = 0.3)
    pyautogui.click()
    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    pyautogui.keyUp('ctrl')
    pyautogui.typewrite('567')
    pyautogui.moveTo(3148, 991, duration = 1)
    pyautogui.click()
    #Y-Koordinate
    pyautogui.moveTo(3026, 863, duration = 0.3)
    pyautogui.click()
    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    pyautogui.keyUp('ctrl')
    pyautogui.typewrite('930')
    pyautogui.moveTo(3148, 991, duration = 1)
    pyautogui.click()
    #Suchen
    pyautogui.moveTo(3113, 864, duration = 1)
    pyautogui.click()
    pyautogui.moveTo(2922, 496, duration = 3)
    pyautogui.click()
    #Angreifen1,pro Einheit wiederholen
    pyautogui.moveTo(2985, 647, duration = 1)
    pyautogui.click()
    #Einheit1
    pyautogui.moveTo(3054, 970, duration = 0.5)
    pyautogui.click()
    pyautogui.moveTo(2914, 618, duration = 0.5)
    pyautogui.click()
    #Einheit2
    pyautogui.moveTo(2985, 647, duration = 0.5)
    pyautogui.click()
    #Einheit2
    pyautogui.moveTo(3054, 970, duration = 0.5)
    pyautogui.click()
    pyautogui.moveTo(2914, 618, duration = 0.5)
    pyautogui.click()
    pyautogui.press('space')
    
def Murmeltier():
    pyautogui.moveTo(2858, 816, duration = 1)
    pyautogui.click()
    pyautogui.press('space')
    #Lupe
    pyautogui.moveTo(2678, 677, duration = 2)
    pyautogui.click()
    pyautogui.moveTo(3105, 966, duration = 0.3)
    pyautogui.click()
    #X-Koordinate
    pyautogui.moveTo(2808, 862, duration = 0.3)
    pyautogui.click()
    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    pyautogui.keyUp('ctrl')
    pyautogui.typewrite('566')
    pyautogui.moveTo(3148, 991, duration = 0.3)
    pyautogui.click()
    #Y-Koordinate
    pyautogui.moveTo(3026, 863, duration = 0.3)
    pyautogui.click()
    pyautogui.keyDown('ctrl')
    pyautogui.press('a')
    pyautogui.keyUp('ctrl')
    pyautogui.typewrite('942')
    pyautogui.moveTo(3148, 991, duration = 0.3)
    pyautogui.click()
    #Suchen
    pyautogui.moveTo(3113, 864, duration = 0.3)
    pyautogui.click()
    pyautogui.moveTo(2922, 496, duration = 3)
    pyautogui.click()
    #Angreifen1,pro Einheit wiederholen
    pyautogui.moveTo(2918, 569, duration = 1)
    pyautogui.click()
    #Einheit1
    pyautogui.moveTo(3054, 970, duration = 0.5)
    pyautogui.click()
    #Einheit2
    pyautogui.moveTo(2918, 569, duration = 0.5)
    pyautogui.click()
    #Einheit2
    pyautogui.moveTo(3054, 970, duration = 1)
    pyautogui.click()
    pyautogui.moveTo(2918, 569, duration = 1)
    pyautogui.press('space')
    
def Sammeln():
    pyautogui.moveTo(2858, 816, duration = 1)
    pyautogui.click()
    pyautogui.press('space')
    #Lupe1
    pyautogui.moveTo(2678, 677, duration = 5)
    pyautogui.click()
    pyautogui.moveTo(2733, 974, duration = 1)
    pyautogui.click()
    #gehen
    pyautogui.moveTo(3110, 882, duration = 0.3)
    pyautogui.click()
    pyautogui.moveTo(2922, 496, duration = 3)
    pyautogui.click()
    pyautogui.moveTo(2911, 684, duration = 1)
    pyautogui.click()
    pyautogui.moveTo(3053, 968, duration = 1)
    pyautogui.click()
    #Lupe2
    pyautogui.moveTo(2678, 677, duration = 2)
    pyautogui.click()
    pyautogui.moveTo(2733, 974, duration = 1)
    pyautogui.click()
    #gehen
    pyautogui.moveTo(3110, 882, duration = 0.3)
    pyautogui.click()
    pyautogui.moveTo(2922, 496, duration = 3)
    pyautogui.click()
    pyautogui.moveTo(2911, 684, duration = 1)
    pyautogui.click()
    pyautogui.moveTo(3053, 968, duration = 1)
    pyautogui.click()
    pyautogui.press('space')

def Schliessen():
    #schließen
    pyautogui.moveTo(3177, 18, duration = 0.5)
    pyautogui.click()
    pyautogui.moveTo(3022, 557, duration = 0.5)
    pyautogui.click()

def Machen():
    #Blattschneiderameise2
    pyautogui.moveTo(2924, 172, duration = 1)#y-10
    pyautogui.click()
    pyautogui.moveTo(2999, 286, duration = 1)#y-10
    pyautogui.click()
    pyautogui.moveTo(2917, 669, duration = 1)
    pyautogui.click()
    #Blattschneiderameise3
    pyautogui.moveTo(2852, 172, duration = 1)#y-10
    pyautogui.click()
    pyautogui.moveTo(2928, 271, duration = 1)#y-10
    pyautogui.click()
    pyautogui.moveTo(2914, 667, duration = 1)
    pyautogui.click()
    #Essbereich
    pyautogui.moveTo(2790, 450, duration = 1)#y+20 noch verbesserungsbedarf?
    pyautogui.click()
    #Transportieren
    pyautogui.moveTo(2901, 541, duration = 1)
    pyautogui.click()
    pyautogui.moveTo(2919, 739, duration = 1)
    pyautogui.click()

def machen2():
    pass
    
#アリの羽化に必要な時間１時間３４分
#Start()
Routine() 
Spezial()
#Plündern()
#Murmeltier()
Sammeln()
#Schliessen() 
#Machen()


##====================1-10=============8:00 - 18:00
# Start()
# LogInBonus()
# Routine()
# Spezial()
# Sammeln()
# schedule.every().day.at("10:00:00").do(Routine)
# schedule.every().day.at("10:10:00").do(Sammeln)
# schedule.every().day.at("12:00:00").do(Routine)
# schedule.every().day.at("12:10:00").do(Sammeln)
# schedule.every().day.at("14:00:00").do(Routine)
# schedule.every().day.at("14:10:00").do(Sammeln)
# schedule.every().day.at("16:00:00").do(Routine)
# schedule.every().day.at("16:10:00").do(Sammeln)
# schedule.every().day.at("18:00:00").do(Routine)
# schedule.every().day.at("18:10:00").do(Sammeln)
# schedule.every().day.at("20:00:00").do(Routine)
# schedule.every().day.at("20:05:00").do(Sammeln)
# #=============2-6=====================7:00 - 14:30    
# Start()
# LogInBonus()
# Routine()
# Spezial()
# Sammeln()
# schedule.every().day.at("08:30:00").do(Routine)
# schedule.every().day.at("10:00:00").do(Routine)
# schedule.every().day.at("11:30:00").do(Routine)
# schedule.every().day.at("12:30:00").do(Routine)
# schedule.every().day.at("14:30:00").do(Routine)
# schedule.every().day.at("16:00:00").do(Routine)
# schedule.every().day.at("17:30:00").do(Routine)
# #======1-8============================6:20 - 16:30
# Start()
# LogInBonus()
#Routine()
#Spezial()
#Sammeln()
#schedule.every().day.at("07:30:00").do(Routine)
#schedule.every().day.at("09:00:00").do(Routine)
#schedule.every().day.at("11:30:00").do(Routine)
#schedule.every().day.at("13:00:00").do(Routine)
#schedule.every().day.at("14:30:00").do(Routine)
#schedule.every().day.at("16:00:00").do(Routine)
# #======1-6============================6:20 - 14:30
# Start()
# LogInBonus()
# Routine()
# Spezial()
# Sammeln()
# schedule.every().day.at("07:30:00").do(Routine)
# schedule.every().day.at("09:00:00").do(Routine)
# schedule.every().day.at("11:30:00").do(Routine)
# schedule.every().day.at("13:00:00").do(Routine)
#==============================AbendRoutine======================
# schedule.every().day.at("22:00:00").do(Routine)
# schedule.every().day.at("22:02:00").do(Sammeln)
# schedule.every().day.at("22:25:00").do(Plündern)
# schedule.every().day.at("22:47:00").do(Sammeln)
# schedule.every().day.at("01:10:00").do(Routine)
# schedule.every().day.at("01:02:00").do(Plündern)
# schedule.every().day.at("01:25:00").do(Sammeln)
# schedule.every().day.at("01:45:00").do(Sammeln)
# schedule.every().day.at("03:10:00").do(Routine)
# schedule.every().day.at("03:02:00").do(Sammeln)
# schedule.every().day.at("03:25:00").do(Sammeln)
# schedule.every().day.at("03:40:00").do(Sammeln)
# schedule.every().day.at("05:10:00").do(Routine)
# schedule.every().day.at("05:02:00").do(Sammeln)
# schedule.every().day.at("05:25:00").do(Sammeln)
# schedule.every().day.at("05:40:00").do(Sammeln) 
# schedule.every().day.at("07:10:00").do(Routine)
# schedule.every().day.at("07:02:00").do(Sammeln)
# 
# while True:
#     schedule.run_pending()
  
   