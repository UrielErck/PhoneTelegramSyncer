import pystray
from PIL import Image
import os
from frameworks.telegram import sendcommand as send
from frameworks.ConfigReaderFile import readconfig as rc
from frameworks.loading import resource_path as path

class func:
	def __init__(self):
		super().__init__()
	def exitm(self):
		icon.stop()

	def OCF(self):
		os.system('../config.PTSC')

	def settings(self):
		import frameworks.SettingsUI as ui

	def reload(self):
		icon.stop()


commands = rc().get('COMMANDS')
menu = [pystray.MenuItem("Settings",
						 pystray.Menu(
							 pystray.MenuItem('Exit', func.exitm),
							 pystray.MenuItem('Open Config File', func.OCF),
							 pystray.MenuItem('Settings', func.settings),
							 pystray.MenuItem('Reload', func.reload),
						 ))]
for i in commands:
	if i == rc().get('VARIABLE').get('LCA'):
		LCA = True
	else:
		LCA = False
	menu.append(pystray.MenuItem(i, send, default=LCA, visible=commands.get(i)))

image = Image.open(path("frameworks\\ico.png"))

icon = pystray.Icon("GFG", image, "Phone", menu=pystray.Menu(*tuple(menu)))

icon.run()