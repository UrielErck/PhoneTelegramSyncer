!!! Don`t forget to change path !!!
For your use edit file frameworks/config to your setting.
Than run the following command in powershell (install all need pakages):
pyinstaller --noconfirm --onefile --windowed --icon "D:/Files/TelegramBot/frameworks/ico.ico" --name "PhoneTelegramSyncer" --version-file "D:/Files/TelegramBot/versionfile" --add-data "D:/Files/TelegramBot/frameworks;frameworks/"  "D:/Files/TelegramBot/main.py"
Or you can import file config.json to auto-py-to-exe then run in powershell: 'auto-py-to-exe'
Pakages: pystray, auto-py-to-exe, PIL (if not installed), pytgbot
Enjoy :)