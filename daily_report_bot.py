import pyautogui
import time
from datetime import datetime

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1

print("Step 1: Open the chrome browser...")
time.sleep(2)

pyautogui.hotkey('win', 'r')  # Open the Run dialog
time.sleep(1)
pyautogui.typewrite('chrome\n')  # Type 'chrome' and press Enter
time.sleep(2)  # Wait for Chrome to open
print("Step 1: Chrome browser opened successfully.")

print("Step 2: Navigating to the website...")
time.sleep(1)
pyautogui.typewrite('https://www.angelone.in/stocks?gclsrc=aw.ds&&utm_source=google&utm_medium=cpc&utm_campaign=B2C_Search_AI_Max_May%2726&network=g&keyword=best%20platform%20to%20buy%20stocks&matchtype=e&creative=821006615743&device=c&devicemodel=&gad_source=1&gad_campaignid=23885427081&gbraid=0AAAAAD3HJ829RoKcOPgQ9z2XndQ0E3Mof&gclid=Cj0KCQiA77DXBhCHARIsAHf2MNr18VGG0yPUhWzMyxee6H0ntRbKMZZUeTbZHhr6-1qilTpUuugCaDcaApffEALw_wcB\n')  # Type the URL and press Enter
time.sleep(5)  # Wait for the website to load
print("Step 2: Website loaded successfully.")

print("Step 3: Copy the full data from the website...")
pyautogui.hotkey('ctrl', 'a')  # Select all text
time.sleep(1)
pyautogui.hotkey('ctrl', 'c')  # Copy the selected text
time.sleep(1)
print("Step 3: Full data copied successfully.")

print("Step 4: Open Excel...")
time.sleep(1)
pyautogui.hotkey('win', 'r')  # Open the Run dialog
time.sleep(1)
pyautogui.typewrite('excel\n')  # Type 'excel' and press Enter
time.sleep(2)  # Wait for excel to open
pyautogui.hotkey('ctrl', 'n')   
time.sleep(2)  # Wait for new excel to open
pyautogui.click(150,150)  # Click on the first cell of the excel sheet
time.sleep(1)
print("Step 4: excel opened successfully.")
time.sleep(4)  # Wait for Excel to open
pyautogui.hotkey('ctrl', 'v')  # Paste the copied data into Excel
time.sleep(3)
print("Step 4: Data pasted into Excel successfully.") 
time.sleep(3) 
pyautogui.hotkey('ctrl', 's')  # Save the Excel file
time.sleep(1)
pyautogui.typewrite('Daily_Report_2026_11_05.xlsx\n')  # Type the file name and press Enter
time.sleep(5)  # Wait for the file to save




