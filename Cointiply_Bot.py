from selenium import webdriver
from PIL import Image
from io import BytesIO
import time
import pytesseract
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pyperclip
import keyboard
from random import randrange
import sys
import os
import cv2
import numpy as np
from skimage.metrics import structural_similarity
import argparse
import imutils


def MAX(ssim_total):
    return (max(ssim_total))


dir_path = os.path.dirname(os.path.realpath(__file__))
credentials = "creds.txt"

tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata"'

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

driver_path = "chromedriver.exe"
brave_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"

with open(credentials) as f:
    creds = f.readlines()
time.sleep(1)

ads_remaining = True
ads_viewed = 0
ad_viewtime = int(ads_viewed) * 20
ptc_reduced = False
first_check = 1
ptc_early = 0

option = webdriver.ChromeOptions()
option.binary_location = brave_path
#option.add_argument("--incognito")
#option.add_argument("--headless")

# Create new Instance of Chrome
browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
browser.maximize_window()
print("Browser launched")

username = creds[9]
password = creds[10]

browser.get("https://cointiply.com/login")
print("Navigate: Cointiply login page")

login_field = browser.find_element_by_css_selector("input[type='text']")
login_field.send_keys(username)
print("Entered Username")

pw_field = browser.find_element_by_css_selector("input[type='password']")
pw_field.send_keys(password)
print("Entered Password")

print("Waiting for Captcha...")
time.sleep(10)


captcha = browser.find_element_by_id("adcopy-outer").screenshot("captcha.png")
print("Solving Captcha...")
img = Image.open("captcha.png")
width, height = img.size
img_res = img.crop((0, 130, width, height))
img_res.save("captcha.png")

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

captcha_string = pytesseract.image_to_string("captcha.png", config=tessdata_dir_config)
s = captcha_string
sliced_captcha = s[14:]
print(sliced_captcha)

pyperclip.copy(sliced_captcha)

captcha_field = browser.find_element_by_css_selector("input[type='text'][name='adcopy_response'][class='md-input']")

captcha_field.click()
time.sleep(1)

captcha_field.send_keys(sliced_captcha)
#keyboard.send("ctrl+v")
print("Captcha Solved")

time.sleep(2)

#browser.find_element_by_css_selector("button[type='button'][class='md-button md-raised md-accent font-weight-600 md-theme-default']").click
pw_field.click()
keyboard.send("enter")

######################################################

time.sleep(5)

browser.get("https://cointiply.com/home?intent=faucet")
print("Navigating to Faucet")

time.sleep(3)

try:
    print("Joining Rain Pool...")
    chat_button = browser.find_element_by_xpath(
        "/html/body/div/div/div[4]/div/div/div[1]/div[4]/div[2]/div[1]/div[3]/label")
    chat_button.click()

    time.sleep(5)

    rain_button = browser.find_element_by_xpath(
        "/html/body/div/div/div[4]/div/div/div[1]/div[4]/div[2]/div/div[2]/div/label[2]")
    rain_button.click()
    time.sleep(2)
    tos_button = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/button[2]")
    tos_button.click()
    print("Rain Pool successfully joined")
except:
    print("Error joining Rain Pool - already joined")

time.sleep(1)

#roll_button = browser.find_element_by_class_name("md-ink-ripple").click()
try:
    roll_button = browser.find_element_by_xpath("/html/body/div/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/button")
    roll_button.click()
    print("Clicked Roll Button")

    print("Waiting for Captcha...")
    time.sleep(11)

    captcha2 = browser.find_element_by_id("adcopy-outer").screenshot("captcha2.png")
    print("Solving Captcha #2...")
    img2 = Image.open("captcha2.png")
    width, height = img2.size
    img_res2 = img2.crop((0, 130, width, height))
    img_res2.save("captcha2.png")

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

    captcha_string2 = pytesseract.image_to_string("captcha2.png", config=tessdata_dir_config)
    s = captcha_string2
    sliced_captcha2 = s[14:]
    print(sliced_captcha2)

    pyperclip.copy(sliced_captcha2)

    captcha_field2 = browser.find_element_by_xpath("/html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[3]/div[2]/div[2]/input")

    captcha_field2.click()
    time.sleep(2)

    captcha_field2.send_keys(sliced_captcha2)
    #keyboard.send("ctrl+v")
    print("Captcha Solved")

    time.sleep(2)

    final_roll = browser.find_element_by_xpath("/html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/button")
    final_roll.click()
    time.sleep(2)
    print("Clicked Roll Button")
except:
    print("Countdown timer active")

while True:
    if first_check == 0:
        print("Waiting for countdown...")
        very_human = randrange(180)
        roll_wait = 3600 -- ad_viewtime
        #total_wait = roll_wait + very_human
        rain_differential = roll_wait // 10
        rain_check = 0
        while rain_check <= 9:
            for remaining in range(rain_differential, 0, -1):
                sys.stdout.write("\r")
                sys.stdout.write("Checking Rain Pool in {:2d} seconds.".format(remaining))
                sys.stdout.flush()
                time.sleep(1)

            sys.stdout.write("\rChecking Rain Pool...            \n")

            try:
                print("Joining Rain Pool...")
                rain_button = browser.find_element_by_xpath("/html/body/div/div/div[4]/div/div/div[1]/div[4]/div[2]/div/div[2]/div/label[2]")
                rain_button.click()
                time.sleep(2)
                tos_button = browser.find_element_by_xpath("/html/body/div[3]/div[1]/div[3]/button[2]")
                tos_button.click()
                print("Rain Pool successfully joined")

            except:
                print("Error joining Rain Pool - already joined")

            rain_check += 1

        print("Roll Timer complete!")

        for remaining in range(very_human, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write("Randomizing wait time: {:2d} seconds remaining".format(remaining))
            sys.stdout.flush()
            time.sleep(1)

        sys.stdout.write("\rRandomized wait time complete!            \n")

        ads_remaining = True

        #countdown = roll_wait + very_human
        #time.sleep(roll_wait + very_human)

        #browser.refresh()
        browser.get("https://cointiply.com/home?intent=faucet")
        time.sleep(3)

        try:
            print("Joining Rain Pool...")
            chat_button = browser.find_element_by_xpath(
                "/html/body/div/div/div[4]/div/div/div[1]/div[4]/div[2]/div[1]/div[3]/label")
            chat_button.click()

            time.sleep(5)

            rain_button = browser.find_element_by_xpath(
                "/html/body/div/div/div[4]/div/div/div[1]/div[4]/div[2]/div/div[2]/div/label[2]")
            rain_button.click()
            time.sleep(2)
            tos_button = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/button[2]")
            tos_button.click()
            print("Rain Pool successfully joined")
        except Exception as e:
            print(e)
            print("Error joining Rain Pool - already joined")

        time.sleep(1)

        roll_button = browser.find_element_by_xpath("/html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/button")
        roll_button.click()
        print("Clicked Roll Button")

        print("Waiting for Captcha...")
        time.sleep(10)

        captcha2 = browser.find_element_by_id("adcopy-outer").screenshot("captcha2.png")
        print("Solving Captcha #2...")
        img2 = Image.open("captcha2.png")
        width, height = img2.size
        img_res2 = img2.crop((0, 130, width, height))
        img_res2.save("captcha2.png")

        #pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

        captcha_string2 = pytesseract.image_to_string("captcha2.png", config=tessdata_dir_config)
        s = captcha_string2
        sliced_captcha2 = s[14:]
        print(sliced_captcha2)

        pyperclip.copy(sliced_captcha2)

        captcha_field2 = browser.find_element_by_xpath("/html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[3]/div[2]/div[2]/input")
        captcha_field2.click()
        time.sleep(2)
        captcha_field2.send_keys(sliced_captcha2)
        #keyboard.send("ctrl+v")
        print("Captcha Solved")

        time.sleep(1)

        final_roll = browser.find_element_by_xpath("/html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/button")
        final_roll.click()
        print("Clicked Roll Button")

        time.sleep(5)

        try:
            print("Wrong Answer Check...")
            error = browser.find_element_by_xpath("//*[contains(text(), 'wrong answer')]").is_displayed()
            #error2 = browser.find_element_by_xpath("//*[contains(text(), 'puzzle expired')]").is_displayed()
            if error == True: #or error2 == True:
                print("Captcha Failed - Wrong Answer")
                print("Retrying in 15 min.")
                #time.sleep(900)
                for remaining in range(900, 0, -1):
                    sys.stdout.write("\r")
                    sys.stdout.write("{:2d} seconds remaining.".format(remaining))
                    sys.stdout.flush()
                    time.sleep(1)
                sys.stdout.write("\rComplete!            \n")
                #refresh = browser.find_element_by_xpath("/html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[3]/div[2]/div[2]/button")
                #refresh.click()
                #browser.refresh
                #time.sleep(12)
                browser.get("https://cointiply.com/home?intent=faucet")

                time.sleep(3)

                try:
                    print("Joining Rain Pool...")
                    chat_button = browser.find_element_by_xpath(
                        "/html/body/div/div/div[4]/div/div/div[1]/div[4]/div[2]/div[1]/div[3]/label")
                    chat_button.click()

                    time.sleep(5)

                    rain_button = browser.find_element_by_xpath(
                        "/html/body/div/div/div[4]/div/div/div[1]/div[4]/div[2]/div/div[2]/div/label[2]")
                    rain_button.click()
                    time.sleep(2)
                    tos_button = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/button[2]")
                    tos_button.click()
                    print("Rain Pool successfully joined")
                except:
                    print("Error joining Rain Pool - already joined")

                time.sleep(1)

                # roll_button = browser.find_element_by_class_name("md-ink-ripple").click()
                roll_button = browser.find_element_by_xpath(
                    "/html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/button")
                roll_button.click()
                print("Clicked Roll Button")

                print("Waiting for Captcha...")
                time.sleep(11)

                captcha2 = browser.find_element_by_id("adcopy-outer").screenshot("captcha2.png")
                print("Solving Captcha #2...")
                img2 = Image.open("captcha2.png")
                width, height = img2.size
                img_res2 = img2.crop((0, 130, width, height))
                img_res2.save("captcha2.png")

                pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

                captcha_string2 = pytesseract.image_to_string("captcha2.png", config=tessdata_dir_config)
                s = captcha_string2
                sliced_captcha2 = s[14:]
                print(sliced_captcha2)

                pyperclip.copy(sliced_captcha2)

                captcha_field2 = browser.find_element_by_xpath(
                    "/html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[3]/div[2]/div[2]/input")

                captcha_field2.click()
                time.sleep(2)

                captcha_field2.send_keys(sliced_captcha2)
                #keyboard.send("ctrl+v")
                print("Captcha Solved")

                time.sleep(2)

                final_roll = browser.find_element_by_xpath(
                    "/html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/button")
                final_roll.click()
                time.sleep(2)
                print("Clicked Roll Button")
        except NoSuchElementException:
            print("Wrong Answer check passed")


        try:
            print("Invalid Captcha Check...")
            #error = browser.find_element_by_xpath("//*[contains(text(), 'wrong answer')]").is_displayed()
            error2 = browser.find_element_by_xpath("//*[contains(text(), 'Invalid captcha response')]").is_displayed()
            if error2 == True: #or error2 == True:
                print("Captcha Failed - Invalid captcha response")
                print("Retrying in 15 min.")
                #time.sleep(900)
                for remaining in range(900, 0, -1):
                    sys.stdout.write("\r")
                    sys.stdout.write("{:2d} seconds remaining.".format(remaining))
                    sys.stdout.flush()
                    time.sleep(1)
                sys.stdout.write("\rComplete!            \n")
                #refresh = browser.find_element_by_xpath("/html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[3]/div[2]/div[2]/button")
                #refresh.click()
                #time.sleep(12)
                #browser.refresh()
                browser.get("https://cointiply.com/home?intent=faucet")

                time.sleep(3)

                try:
                    print("Joining Rain Pool...")
                    chat_button = browser.find_element_by_xpath(
                        "/html/body/div/div/div[4]/div/div/div[1]/div[4]/div[2]/div[1]/div[3]/label")
                    chat_button.click()

                    time.sleep(5)

                    rain_button = browser.find_element_by_xpath(
                        "/html/body/div/div/div[4]/div/div/div[1]/div[4]/div[2]/div/div[2]/div/label[2]")
                    rain_button.click()
                    time.sleep(2)
                    tos_button = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/button[2]")
                    tos_button.click()
                    print("Rain Pool successfully joined")
                except:
                    print("Error joining Rain Pool - already joined")

                time.sleep(1)

                # roll_button = browser.find_element_by_class_name("md-ink-ripple").click()
                roll_button = browser.find_element_by_xpath(
                    "/html/body/div/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/button")
                roll_button.click()
                print("Clicked Roll Button")

                print("Waiting for Captcha...")
                time.sleep(11)

                captcha2 = browser.find_element_by_id("adcopy-outer").screenshot("captcha2.png")
                print("Solving Captcha #2...")
                img2 = Image.open("captcha2.png")
                width, height = img2.size
                img_res2 = img2.crop((0, 130, width, height))
                img_res2.save("captcha2.png")

                pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

                captcha_string2 = pytesseract.image_to_string("captcha2.png", config=tessdata_dir_config)
                s = captcha_string2
                sliced_captcha2 = s[14:]
                print(sliced_captcha2)

                pyperclip.copy(sliced_captcha2)

                captcha_field2 = browser.find_element_by_xpath(
                    "/html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[3]/div[2]/div[2]/input")

                captcha_field2.click()
                time.sleep(2)

                captcha_field2.send_keys(sliced_captcha2)
                #keyboard.send("ctrl+v")
                print("Captcha Solved")

                time.sleep(2)

                final_roll = browser.find_element_by_xpath(
                    "/html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/button")
                final_roll.click()
                time.sleep(2)
                print("Clicked Roll Button")
        except NoSuchElementException:
            print("Invalid Captcha Check Passed")

        try:
            print("Puzzle Expired Check...")
            #error = browser.find_element_by_xpath("//*[contains(text(), 'wrong answer')]").is_displayed()
            error2 = browser.find_element_by_xpath("//*[contains(text(), 'puzzle expired')]").is_displayed()
            if error2 == True: #or error2 == True:
                print("Captcha Failed - Puzzle Expired")
                print("Retrying in 15 min.")
                #time.sleep(900)
                for remaining in range(900, 0, -1):
                    sys.stdout.write("\r")
                    sys.stdout.write("{:2d} seconds remaining.".format(remaining))
                    sys.stdout.flush()
                    time.sleep(1)
                sys.stdout.write("\rComplete!            \n")
                #refresh = browser.find_element_by_xpath("/html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[3]/div[2]/div[2]/button")
                #refresh.click()
                #time.sleep(12)
                #browser.refresh()
                browser.get("https://cointiply.com/home?intent=faucet")

                time.sleep(3)

                try:
                    print("Joining Rain Pool...")
                    chat_button = browser.find_element_by_xpath(
                        "/html/body/div/div/div[4]/div/div/div[1]/div[4]/div[2]/div[1]/div[3]/label")
                    chat_button.click()

                    time.sleep(5)

                    rain_button = browser.find_element_by_xpath(
                        "/html/body/div/div/div[4]/div/div/div[1]/div[4]/div[2]/div/div[2]/div/label[2]")
                    rain_button.click()
                    time.sleep(2)
                    tos_button = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/button[2]")
                    tos_button.click()
                    print("Rain Pool successfully joined")
                except:
                    print("Error joining Rain Pool - already joined")

                time.sleep(1)

                # roll_button = browser.find_element_by_class_name("md-ink-ripple").click()
                roll_button = browser.find_element_by_xpath(
                    "/html/body/div/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/button")
                roll_button.click()
                print("Clicked Roll Button")

                print("Waiting for Captcha...")
                time.sleep(11)

                captcha2 = browser.find_element_by_id("adcopy-outer").screenshot("captcha2.png")
                print("Solving Captcha #2...")
                img2 = Image.open("captcha2.png")
                width, height = img2.size
                img_res2 = img2.crop((0, 130, width, height))
                img_res2.save("captcha2.png")

                pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

                captcha_string2 = pytesseract.image_to_string("captcha2.png", config=tessdata_dir_config)
                s = captcha_string2
                sliced_captcha2 = s[14:]
                print(sliced_captcha2)

                pyperclip.copy(sliced_captcha2)

                captcha_field2 = browser.find_element_by_xpath(
                    "/html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[3]/div[2]/div[2]/input")

                captcha_field2.click()
                time.sleep(2)

                captcha_field2.send_keys(sliced_captcha2)
                #keyboard.send("ctrl+v")
                print("Captcha Solved")

                time.sleep(2)

                final_roll = browser.find_element_by_xpath(
                    "/html/body/div[1]/div/div[4]/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/button")
                final_roll.click()
                time.sleep(2)
                print("Clicked Roll Button")
        except NoSuchElementException:
            print("Puzzle Expired Check Passed")

        try:
            print("Joining Rain Pool...")
            chat_button = browser.find_element_by_xpath(
                "/html/body/div/div/div[4]/div/div/div[1]/div[4]/div[2]/div[1]/div[3]/label")
            chat_button.click()

            time.sleep(5)

            rain_button = browser.find_element_by_xpath(
                "/html/body/div/div/div[4]/div/div/div[1]/div[4]/div[2]/div/div[2]/div/label[2]")
            rain_button.click()
            time.sleep(2)
            tos_button = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/button[2]")
            tos_button.click()
            print("Rain Pool successfully joined")
        except:
            print("Error joining Rain Pool - already joined")

    time.sleep(5)

    first_check = 0
    browser.get("https://cointiply.com/ptc")
    print("Navigating to PTC Ads")
    time.sleep(2)
    total_timer = 0

    while ads_remaining == True and total_timer < 3600:
        captcha_attempt = 0

        ptc_very_human = randrange(300)
        print("Randomizing PTC wait time: " + str(ptc_very_human) + " seconds")
        for remaining in range(ptc_very_human, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write("{:2d} seconds remaining.".format(remaining))
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write("\rComplete!            \n")

        total_timer += ptc_very_human

        try:
            print("Joining Rain Pool...")
            chat_button = browser.find_element_by_xpath(
                "/html/body/div/div/div[4]/div/div/div[1]/div[4]/div[2]/div[1]/div[3]/label")
            chat_button.click()

            time.sleep(5)

            rain_button = browser.find_element_by_xpath(
                "/html/body/div/div/div[4]/div/div/div[1]/div[4]/div[2]/div/div[2]/div/label[2]")
            rain_button.click()
            time.sleep(2)
            tos_button = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/button[2]")
            tos_button.click()
            print("Rain Pool successfully joined")
        except:
            print("Error joining Rain Pool - already joined")

        try:
            PTC_Button = browser.find_element_by_xpath(
                "/html/body/div/div/div[4]/div/div/div[2]/div[1]/div/div[1]/div[3]/button")
            PTC_Button.click()
            print("Loading top paying ad")

            ad = browser.window_handles[1]
            browser.switch_to_window(ad)
            print("Focused on ad window")

            for remaining in range(20, 0, -1):
                sys.stdout.write("\r")
                sys.stdout.write("Viewing ad: {:2d} seconds remaining".format(remaining))
                sys.stdout.flush()
                time.sleep(1)

            sys.stdout.write("\rAd view timer complete!            \n")
            total_timer += 20
            # time.sleep(60)
            # browser.close()
            # print("Closing ad")
            ads_viewed += 1
            ad_complete = True
            ptc_main = browser.window_handles[0]

            while ad_complete == True:
                browser.switch_to_window(ptc_main)
                time.sleep(1)
                total_timer += 1
                print("Saving Captcha images")

                try:
                    ptc_captcha1 = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/img[1]")
                    ptc_captcha1.screenshot("ptc_captcha1.png")
                    ptc_captcha2 = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/img[2]")
                    ptc_captcha2.screenshot("ptc_captcha2.png")
                    ptc_captcha3 = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/img[3]")
                    ptc_captcha3.screenshot("ptc_captcha3.png")
                    ptc_captcha4 = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/img[4]")
                    ptc_captcha4.screenshot("ptc_captcha4.png")
                    ptc_captcha5 = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/img[5]")
                    ptc_captcha5.screenshot("ptc_captcha5.png")

                except:
                    try:
                        print("Reduced captcha count detected")
                        ptc_captcha1 = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/img[1]")
                        ptc_captcha1.screenshot("ptc_captcha1.png")
                        ptc_captcha2 = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/img[2]")
                        ptc_captcha2.screenshot("ptc_captcha2.png")
                        ptc_captcha3 = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/img[3]")
                        ptc_captcha3.screenshot("ptc_captcha3.png")
                        ptc_captcha4 = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/img[4]")
                        ptc_captcha4.screenshot("ptc_captcha4.png")
                        ptc_reduced = True
                    except:
                        try:
                            browser.switch_to_window(ad)
                            time.sleep(10)
                            browser.switch_to_window(ptc_main)
                            time.sleep(1)
                            ptc_early += 1

                            if ptc_early <= 2:
                                continue
                            if ptc_early == 3:
                                ptc_early = 0
                                ad_complete = False

                            ad_complete = False
                            skip_ad = browser.find_element_by_xpath(
                                "/html/body/div/div/div[4]/div/div/div[2]/div[1]/div/div[2]/div/div/div[3]/button")
                            skip_ad.click()
                            print("Ad timeout error")
                            print("Skipping ad")
                            browser.switch_to_window(ad)
                            browser.close()
                            browser.switch_to_window(ptc_main)
                            time.sleep(1)
                            browser.get("https://cointiply.com/ptc")
                            time.sleep(1)
                            ptc_early = 0
                            continue
                        except:
                            print("Unknown Error")
                            ad_complete = False
                            browser.switch_to_window(ad)
                            browser.close()
                            browser.switch_to_window(ptc_main)
                            browser.get("https://cointiply.com/ptc")
                            ptc_early = 0
                            continue

                ptc_captcha_string = browser.find_elements_by_xpath("//*[contains(text(), 'Select:')]")
                ptc_text = ptc_captcha_string[0].text
                ptc_text = ptc_text.replace("Select: ", "")
                print(ptc_text)

                ptc_captcha_db = cv2.imread("captcha/" + ptc_text + ".png")

                ptc_no = 1
                # current_ptc_captcha = "ptc_captcha"+ str(ptc_no) +".png"
                ptc_captcha1_png = cv2.imread("ptc_captcha1.png")
                ptc_captcha2_png = cv2.imread("ptc_captcha2.png")
                ptc_captcha3_png = cv2.imread("ptc_captcha3.png")
                ptc_captcha4_png = cv2.imread("ptc_captcha4.png")
                try:
                    ptc_captcha5_png = cv2.imread("ptc_captcha5.png")
                except:
                    pass

                try:
                    if ptc_no == 1:
                        imageA = cv2.imread("captcha/" + ptc_text + ".png")
                        imageB = cv2.imread("ptc_captcha1.png")
                        grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
                        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
                        (score, diff) = structural_similarity(grayA, grayB, full=True)
                        diff = (diff * 255).astype("uint8")
                        print("Captcha 1 SSIM: {}".format(score))
                        ptc_ssim1 = score
                        ptc_no += 1

                    if ptc_no == 2:
                        imageA = cv2.imread("captcha/" + ptc_text + ".png")
                        imageB = cv2.imread("ptc_captcha2.png")
                        grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
                        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
                        (score, diff) = structural_similarity(grayA, grayB, full=True)
                        diff = (diff * 255).astype("uint8")
                        print("Captcha 2 SSIM: {}".format(score))
                        ptc_ssim2 = score
                        ptc_no += 1

                    if ptc_no == 3:
                        imageA = cv2.imread("captcha/" + ptc_text + ".png")
                        imageB = cv2.imread("ptc_captcha3.png")
                        grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
                        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
                        (score, diff) = structural_similarity(grayA, grayB, full=True)
                        diff = (diff * 255).astype("uint8")
                        print("Captcha 3 SSIM: {}".format(score))
                        ptc_ssim3 = score
                        ptc_no += 1

                    if ptc_no == 4:
                        imageA = cv2.imread("captcha/" + ptc_text + ".png")
                        imageB = cv2.imread("ptc_captcha4.png")
                        grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
                        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
                        (score, diff) = structural_similarity(grayA, grayB, full=True)
                        diff = (diff * 255).astype("uint8")
                        print("Captcha 4 SSIM: {}".format(score))
                        ptc_ssim4 = score
                        if ptc_reduced == False:
                            ptc_no += 1

                    if ptc_no == 5:
                        imageA = cv2.imread("captcha/" + ptc_text + ".png")
                        imageB = cv2.imread("ptc_captcha5.png")
                        grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
                        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
                        (score, diff) = structural_similarity(grayA, grayB, full=True)
                        diff = (diff * 255).astype("uint8")
                        print("Captcha 5 SSIM: {}".format(score))
                        ptc_ssim5 = score
                        ptc_no += 1

                    ssim_total = set([ptc_ssim1, ptc_ssim2, ptc_ssim3, ptc_ssim4, ptc_ssim5])
                    ssim_match = MAX(ssim_total)

                    if ssim_match == ptc_ssim1:
                        ptc_captcha1.click()
                        print("Captcha 1 is the closest match")
                        time.sleep(1)
                        ptc_reduced = False
                        browser.switch_to_window(ad)
                        browser.close()
                        browser.switch_to_window(ptc_main)
                        print("Closing ad")
                        ad_complete = False
                        time.sleep(2)
                        total_timer += 3
                    elif ssim_match == ptc_ssim2:
                        ptc_captcha2.click()
                        print("Captcha 2 is the closest match")
                        time.sleep(1)
                        ptc_reduced = False
                        browser.switch_to_window(ad)
                        browser.close()
                        browser.switch_to_window(ptc_main)
                        print("Closing ad")
                        ad_complete = False
                        time.sleep(2)
                        total_timer += 3
                    elif ssim_match == ptc_ssim3:
                        ptc_captcha3.click()
                        print("Captcha 3 is the closest match")
                        time.sleep(1)
                        ptc_reduced = False
                        browser.switch_to_window(ad)
                        browser.close()
                        browser.switch_to_window(ptc_main)
                        print("Closing ad")
                        ad_complete = False
                        time.sleep(2)
                        total_timer += 3
                    elif ssim_match == ptc_ssim4:
                        ptc_captcha4.click()
                        print("Captcha 4 is the closest match")
                        time.sleep(1)
                        ptc_reduced = False
                        browser.switch_to_window(ad)
                        browser.close()
                        browser.switch_to_window(ptc_main)
                        print("Closing ad")
                        ad_complete = False
                        time.sleep(2)
                        total_timer += 3
                    elif ssim_match == ptc_ssim5:
                        ptc_captcha5.click()
                        print("Captcha 5 is the closest match")
                        time.sleep(1)
                        browser.switch_to_window(ad)
                        browser.close()
                        browser.switch_to_window(ptc_main)
                        print("Closing ad")
                        ad_complete = False
                        time.sleep(2)
                        total_timer += 3
                except:
                    print("PTC Captcha failed")
                    print(Exception)
                    browser.switch_to_window(ad)
                    browser.close()
                    browser.switch_to_window(ptc_main)
        except:
            print("No ads remaining")
            print(Exception)
            ads_remaining = False