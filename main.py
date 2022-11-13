import pyfiglet
import pyautogui
import os
from PIL import Image
#Dumbass cringy text credit
m1 = (pyfiglet.figlet_format('Valorant', font = 'banner3-D', width = 200))
m2 = (pyfiglet.figlet_format('Instalock', font = 'banner3-D', width = 200))
m3 = (pyfiglet.figlet_format('By Taechapat', font = 'banner3-D', width = 200))
print(m1)
print(m2)
print(m3)

AgentList = ["Astra", "Breach", "Brimstone",
"Cypher", "Reyna", "Killjoy", "Sova", "Omen",
"Viper", "Sage", "Fade", "KayO", "Neon", "Chamber",
"Skye", "Yoru", "Phoniex", "Raze", "Jett", "Harbor"]

print(*AgentList, sep = "\n")

Agent = input("What agent do you want to autolock?:")

if(Agent in AgentList):
    print("Autolocking " + Agent + " ....")
else:
    print("You dumbass cannot even type the right agent name bozo")


folderpath = 'Agent1366x768'
imgpath = os.path.join(folderpath, Agent + '.png')
Agentpix = Image.open(imgpath)


while True:
    locate = pyautogui.locateCenterOnScreen(Agentpix, confidence = 0.9, minSearchTime=999999)
    pyautogui.moveTo(locate, duration = 0)
    pyautogui.leftClick()
    pyautogui.moveTo(679, 579, duration = 0)
    pyautogui.leftClick()
    break