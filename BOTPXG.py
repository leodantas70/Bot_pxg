from importlib.resources import is_resource
from multiprocessing.connection import wait
from time import sleep
import winsound
import pyautogui
import teclado
import button
import keyboard
import os
import ctypes

def get_pause_state():
    hllDll = ctypes.WinDLL ("User32.dll")
    VK_PAUSE = 0x13
    return hllDll.GetKeyState(VK_PAUSE)

def mover_para_arvore_longe_e_sul_e (foto):
    return pyautogui.locateOnScreen(foto, confidence=0.6, region=(519, 322, 80, 80))

def mover_para_arvore_longe_e_norte_e (foto):
    return pyautogui.locateOnScreen(foto, confidence=0.6, region=(519, 219, 80, 80))

def mover_para_arvore_longe_e_norte_d (foto):
    return pyautogui.locateOnScreen(foto, confidence=0.6, region=(622, 219, 80, 80))

def mover_para_arvore_longe_e_sul_d (foto):
    return pyautogui.locateOnScreen(foto, confidence=0.6, region=(622, 322, 80, 80))    

def cortar_n (foto):
    return pyautogui.locateOnScreen(foto, confidence=0.6, region=(575, 219, 80, 80))    

def cortar_s (foto):
    return pyautogui.locateOnScreen(foto, confidence=0.6, region=(575, 322, 80, 80)) 

def cortar_e (foto):
    return pyautogui.locateOnScreen(foto, confidence=0.6, region=(520, 275, 60, 60)) 

def cortar_d (foto):
    return pyautogui.locateOnScreen(foto, confidence=0.5, region=(622, 275, 60, 60)) 

def andar_e_cortar (tecla1, tecla2, foto):
        print ("Posicionando")
        teclado.press(button.key[tecla1])
        sleep(0.5)
        teclado.press(button.key[tecla2])
        sleep(1)        
        click = pyautogui.locateOnScreen(foto, confidence=0.5, region=(510, 210, 175, 175))
        if click is not None:
            x_click, y_click = pyautogui.center(click)
            pyautogui.moveTo(x_click, y_click, 1)
            teclado.press(button.key['F1'])
            sleep(1)
            pyautogui.click()            
            print("Cortando")
            sleep(2)

def cortar (foto):
        click = pyautogui.locateOnScreen(foto, confidence=0.5, region=(510, 210, 175, 175))
        if click is not None:
            x_click, y_click = pyautogui.center(click)
            pyautogui.moveTo(x_click, y_click, 1)
            teclado.press(button.key['F1'])
            sleep(1)
            pyautogui.click()            
            print("Cortando")
            sleep(2)

def buscar_arvores():
    #BUSCANDO PRIMEIRA ARVORE
    i=0
    while i < 20:
        print ("Buscando Arvore 1")
        arvore_1 = pyautogui.locateOnScreen("andacerto.PNG", confidence=0.75)
        if arvore_1 is not None:
            x_arvore_1, y_arvore_1 = pyautogui.center(arvore_1)
            pyautogui.moveTo(x_arvore_1, y_arvore_1, 1)
            pyautogui.rightClick()
            print("pausando 6seg por que cliquei na arvore")
            sleep(6)
                                #CORTAR ARVORES DIAGONAL
            anda_s_e = mover_para_arvore_longe_e_sul_e("andacerto.PNG")   
            anda_n_e = mover_para_arvore_longe_e_norte_e("andacerto.PNG")
            anda_n_d = mover_para_arvore_longe_e_norte_d("andacerto.PNG")
            anda_s_d = mover_para_arvore_longe_e_sul_d("andacerto.PNG")
            cortar_norte = cortar_n("andacerto.PNG")
            cortar_sul = cortar_s("andacerto.PNG")
            cortar_esquerda = cortar_e("andacerto.PNG")
            cortar_direita = cortar_d("andacerto.PNG")
            if anda_s_e is not None:
                x_anda_s_e, y_anda_s_e = pyautogui.center(anda_s_e)
                print("achei a arvore vou andar para o sul esquerda", anda_s_e)
                sleep(0.5)
                andar_e_cortar("DOWN","LEFT","andacerto.PNG")
                sleep(2)
            if anda_n_e is not None:
                x_anda_n_e, y_anda_n_e = pyautogui.center(anda_n_e)
                print("achei a arvore vou andar para o norte esquerda", anda_n_e)
                sleep(0.5)
                andar_e_cortar("UP","LEFT","andacerto.PNG")
                sleep(2)
            if anda_n_d is not None:
                x_anda_n_d, y_anda_n_d = pyautogui.center(anda_n_d)
                print("achei a arvore vou andar para o norte direita", anda_n_d)
                sleep(0.5)
                andar_e_cortar("UP","RIGHT","andacerto.PNG")
                sleep(2)
            if anda_s_d is not None:
                x_anda_s_d, y_anda_s_d = pyautogui.center(anda_s_d)
                print("achei a arvore vou andar para o Sul direita", anda_s_d)
                sleep(0.5)
                andar_e_cortar("DOWN","RIGHT","andacerto.PNG")
                sleep(2)
                                #CORTAR ARVORES HORIZONTAL/VERTICAL
            if cortar_norte is not None:
                x_cortar_norte, y_cortar_norte = pyautogui.center(cortar_norte)
                print("achei a arvore no norte", cortar_norte)
                sleep(0.5)
                cortar("andacerto.PNG")
                sleep(2)
            if cortar_sul is not None:
                x_cortar_sul, y_cortar_sul = pyautogui.center(cortar_sul)
                print("achei a arvore no sul", cortar_sul)
                sleep(0.5)
                cortar("andacerto.PNG")
                sleep(2)
            if cortar_esquerda is not None:
                x_cortar_esquerda, y_cortar_esquerda = pyautogui.center(cortar_esquerda)
                print("achei a arvore na esquerda", cortar_esquerda)
                sleep(0.5)
                cortar("andacerto.PNG")
                sleep(2)
            if cortar_direita is not None:
                x_cortar_direita, y_cortar_direita = pyautogui.center(cortar_direita)
                print("achei a arvore na direita", cortar_direita)
                sleep(0.5)
                cortar("andacerto.PNG")
                sleep(2)
        #Checando Pause
        get_pause_state()     
        p=get_pause_state()
        if p != 0:
            break  
        print ("Buscando Arvore 2")
        #BUSCANDO SEGUNDA ARVORE
        arvore_2 = pyautogui.locateOnScreen("andacerto1.PNG", confidence=0.6)
        if arvore_2 is not None:
            x_arvore_2, y_arvore_2 = pyautogui.center(arvore_2)
            pyautogui.moveTo(x_arvore_2, y_arvore_2, 1)
            pyautogui.rightClick()
            print("pausando 6seg por que cliquei na arvore", arvore_2)
            sleep(6)
                                #CORTAR ARVORES DIAGONAL
            anda_s_e = mover_para_arvore_longe_e_sul_e("andacerto1.PNG")   
            anda_n_e = mover_para_arvore_longe_e_norte_e("andacerto1.PNG")
            anda_n_d = mover_para_arvore_longe_e_norte_d("andacerto1.PNG")
            anda_s_d = mover_para_arvore_longe_e_sul_d("andacerto1.PNG")
            cortar_norte = cortar_n("andacerto1.PNG")
            cortar_sul = cortar_s("andacerto1.PNG")
            cortar_esquerda = cortar_e("andacerto1.PNG")
            cortar_direita = cortar_d("andacerto1.PNG")
            if anda_s_e is not None:
                x_andas, y_andas = pyautogui.center(anda_s_e)
                print("achei a arvore vou andar para o sul esquerda", anda_s_e)
                sleep(0.5)
                andar_e_cortar("DOWN","LEFT","andacerto1.PNG")
                sleep(2)
            if anda_n_e is not None:
                x_andan, y_andan = pyautogui.center(anda_n_e)
                print("achei a arvore vou andar para o norte esquerda", anda_n_e)
                sleep(0.5)
                andar_e_cortar("UP","LEFT","andacerto1.PNG")
                sleep(2)
            if anda_n_d is not None:
                x_andand, y_andand = pyautogui.center(anda_n_d)
                print("achei a arvore vou andar para o norte direita", anda_n_d)
                sleep(0.5)
                andar_e_cortar("UP","RIGHT","andacerto1.PNG")
                sleep(2)
            if anda_s_d is not None:
                x_andasd, y_andasd = pyautogui.center(anda_s_d)
                print("achei a arvore vou andar para o Sul direita", anda_s_d)
                sleep(0.5)
                andar_e_cortar("DOWN","RIGHT","andacerto1.PNG")
                sleep(2)
                                #CORTAR ARVORES HORIZONTAL/VERTICAL
            if cortar_norte is not None:
                x_cortar_norte, y_cortar_norte = pyautogui.center(cortar_norte)
                print("achei a arvore no norte", cortar_norte)
                sleep(0.5)
                cortar("andacerto1.PNG")
                sleep(2)
            if cortar_sul is not None:
                x_cortar_sul, y_cortar_sul = pyautogui.center(cortar_sul)
                print("achei a arvore no sul", cortar_sul)
                sleep(0.5)
                cortar("andacerto1.PNG")
                sleep(2)
            if cortar_esquerda is not None:
                x_cortar_esquerda, y_cortar_esquerda = pyautogui.center(cortar_esquerda)
                print("achei a arvore na esquerda", cortar_esquerda)
                sleep(0.5)
                cortar("andacerto1.PNG")
                sleep(2)
            if cortar_direita is not None:
                x_cortar_direita, y_cortar_direita = pyautogui.center(cortar_direita)
                print("achei a arvore na direita", cortar_direita)
                sleep(0.5)
                cortar("andacerto1.PNG")
                sleep(2)
        print (arvore_1, "e", arvore_2)
        if arvore_1 is None and arvore_2 is None:
            print (arvore_1,arvore_2, "vou para proximo waypoint")
            break             
        #Checando Pause
        get_pause_state()          
        p=get_pause_state()
        if p != 0:
            break        
        i = i+1

def map(foto1):
    get_pause_state()          
    p=get_pause_state()
    if p == 0:
        waypoint = pyautogui.locateOnScreen(foto1, confidence=0.5, region= (1214, 186, 300, 300))
        if waypoint is not None:
            x_waypoint, y_waypoint = pyautogui.center(waypoint)
            pyautogui.moveTo(x_waypoint, y_waypoint, 1)
            pyautogui.click()
            sleep(25)  

while True:
    while True:
        #Checando Pause
        get_pause_state()          
        p=get_pause_state()
        if p != 0:            
            break
        for waypoint in ("waypoint1.PNG","waypoint2.PNG","waypoint3.PNG","waypoint4.PNG","waypoint5.PNG"):
            #Buscando Arvore
            buscar_arvores()
            #Checando Pause
            get_pause_state()          
            p=get_pause_state()            
            if p != 0:
                break
            map(waypoint)

    while True:
        #Checando Pause
        get_pause_state()          
        p=get_pause_state()
        sleep(2)
        print("Bot pausado")
        if p == 0:
            print ("Bot Retornado")
            break

