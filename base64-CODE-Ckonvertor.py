#            ____          _                                 
#           / ___|   _ ___| |_ ___  _ __ ___                 
#          | |  | | | / __| __/ _ \| '_ ` _ \                
#          | |__| |_| \__ \ || (_) | | | | | |               
#           \____\__,_|___/\__\___/|_| |_| |_|         __    
# _ __  _ __ ___   __ _ _ __ __ _ _ __ ___  _ __ ___   \ \   
#| '_ \| '__/ _ \ / _` | '__/ _` | '_ ` _ \| '_ ` _ \   \ \  
#| |_) | | | (_) | (_| | | | (_| | | | | | | | | | | |   \ \ 
#| .__/|_|  \___/ \__, |_|  \__,_|_| |_| |_|_| |_| |_|    \_\
#|_|__  _ __ ___  |___/___  ___ ___                          
#| '_ \| '__/ _ \ / __/ _ \/ __/ __|                         
#| |_) | | | (_) | (_|  __/\__ \__ \                         
#| .__/|_|  \___/ \___\___||___/___/                         
#|_|_              ________  ____                            
# / _| ___  _ __  |__  / _ \/ ___|                           
#| |_ / _ \| '__|   / / | | \___ \                           
#|  _| (_) | |     / /| |_| |___) |                          
#|_|  \___/|_|    /____\___/|____/                                                                                    

import base64
import pyperclip #pip install pyperclip
#=======Custom programm \ process=========#

#==========structure==============#
#moin Это main
#process это процесс

#Программу можно сделать так:
#moin и process(moin + process), 
#только process, 
#только moin

#Минус в том что в ZOS(ZQ) можно можно поставить только 1 кастом приложение\процесс 

#======================API===========#
#API я так называю import


#Вот доступные библеотеки(могут добавиться новые):
#getpass
#sys
#time
#threading
#itertools
#click
#random
#base64
#os
#wikipedia
#calendar
#simpleaudio
#socket
#keyboard
#pyperclip
#rich
#rich.console
#rich.syntax 
#wasabi
#term_image.image
#terminaltexteffects.effects
#art

#=======soon\скоро 
#  telebot(soon\скоро)
#  tkinter(soon\скоро)

#======================working zone===================================#



source_code = '''
def moin():
    

def process(): 
    
'''




#=========================Assemble====================================#
#НЕТ ТОРОГАТЬ\NO TOUCHING
encoded = base64.b64encode(source_code.encode('utf-8')).decode('utf-8')
print("Encoded code:")
print(encoded)

#=====================clipboard=======================================#
byverobmen = input("Записать в Буфер-Обмен. Y/N: ")

def pyperclip64():
    if byverobmen == "Y":
        pyperclip.copy(encoded)
        print("Готово")

pyperclip64()

