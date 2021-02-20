# Cointiply_Bot
This bot will log into Cointiply.com, join the rain pool for additional coins and activate the faucet.   During the faucet cooldown, the bot will periodically check to see if the rain pool has ended, and will rejoin. The browser will need to stay open due to the manner in which the captchas are solved, but can be minimized

Cointiply_Bot

This bot will log into Cointiply.com, join the rain pool for additional coins and activate the faucet.  
During the faucet cooldown, the bot will periodically check to see if the rain pool has ended, and will rejoin.
The browser will need to stay open due to the manner in which the captchas are solved, but can be minimized


In order to run the bot do the following:

Register at: http://cointiply.com/r/EPMAA

Open 'creds.txt'<br>
	- The formatting is very important in this document<br>
	- You don't need to change the site name<br>
	- Replace the word e-mail with the e-mail you want to use for the site<br>
	- Replace the word password with the password you want to use for the site<br>
	- Save and exit<br>

Install tesseract-ocr-setup-3.02.02.exe<br>
	- Set the install dir to: C:\Program Files\Tesseract-OCR\tesseract<br>

Run 'Cointiply_Bot.exe'
	- Make sure you have clicked the verification link in your e-mail<br>
	- Run the bot<br>
	- You can minimize the bot while it runs<br>

Troubleshooting:
	- Issues have occurred if the browser is maximized/minimized while the bot is trying to solve a captcha.<br>
	- If the bot begins failing captchas, it's because the captcha type has changed from the loading bar at the bottom<br>
	  to colorized text.  Close the bot for 15-60min and restart it if this happens and the built in captcha checks do not fix it automatically.<br>
