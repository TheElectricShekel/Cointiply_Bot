# Cointiply_Bot
This bot will log into Cointiply.com, join the rain pool for additional coins, activate the faucet, and complete all of the PTC ad offers.   During the faucet cooldown, the bot will complete all of the PTC ad offers and will check to rejoin the rain pool. The browser will need to stay open due to the manner in which the captchas are solved, but can be minimized (RBTray or another hide to tray program is great for keeping it out of the way).

***Due to the 25MB upload limit on github, the Windows standalone must be unzipped from the following parts:***<br>
	Cointiply_Bot_v1.06.zip.001<br>
	Cointiply_Bot_v1.06.zip.002<br>
	Cointiply_Bot_v1.06.zip.003<br>
	Cointiply_Bot_v1.06.zip.004<br>
	Cointiply_Bot_v1.06.zip.005<br>

**In order to run the bot do the following:**

Register at: http://cointiply.com/r/EPMAA

Ensure Chrome is installed (C:/Program Files/Google/Chrome/Application/chrome.exe)

Open 'creds.txt'<br>
	- The formatting is very important in this document<br>
	- You don't need to change the site name<br>
	- Replace the word e-mail with the e-mail you want to use for the site<br>
	- Replace the word password with the password you want to use for the site<br>
	- Save and exit<br>

Install tesseract-ocr-w64-setup-v5.0.0-alpha.20201127<br>
	- Unzip included zip files for installer or download here: https://github.com/UB-Mannheim/tesseract/wiki<br>
	- Set the install dir to: C:\Program Files\Tesseract-OCR<br>

Run 'Cointiply_Bot.exe'<br>
	- Make sure you have clicked the verification link in your e-mail<br>
	- Run the bot<br>
	- You can minimize the bot while it runs<br>
	- Make sure the captcha folder is in the same folder as the Cointiply_Bot.exe

Troubleshooting:<br>
	- Issues have occurred if the browser is maximized/minimized while the bot is trying to solve a captcha.<br>
	- If the bot begins failing SolveMedia captchas, it's because the captcha type has changed from the loading bar at the bottom<br>
	  to colorized text.  Close the bot for 15-60min and restart it if this happens and the built in captcha checks do not fix it automatically.<br>
