import pystray
from PIL import Image
import os
from frameworks.telegram import sendcommand as send
from frameworks.ConfigReaderFile import readconfig as rc
from frameworks.loading import resource_path as path


def exitm(icon):
	icon.stop()

def OCF(icon):
	os.system('config.PTSC')


commands = rc().get('COMMANDS')
menu = [pystray.MenuItem("Settings",
						 pystray.Menu(
							 pystray.MenuItem('Exit', exitm),
							 pystray.MenuItem('Open Config File', OCF)
						 ))]
for i in commands:
	if i == rc().get('VARIABLE').get('LCA'):
		LCA = True
	else:
		LCA = False
	menu.append(pystray.MenuItem(i, send, default=LCA))

image = Image.open(path("frameworks\\ico.png"))

icon = pystray.Icon("GFG", image, "Phone", menu=pystray.Menu(*tuple(menu)))

icon.run()
