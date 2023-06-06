#!/bin/python
import pyautogui
import time
time.sleep(5)
count=0
while count <=100:
    pyautogui.typewrite("You have been hacked!....")
    pyautogui.press("enter")
    count = count+1
