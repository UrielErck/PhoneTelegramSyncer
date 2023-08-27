import customtkinter as ctk
import frameworks.ConfigReaderFile as Config
root = ctk.CTk()
data = Config.readconfig()
MVARIABLES = data.get('MAIN VARIABLE')
COMMANDS = data.get('COMMANDS')
VARIABLES = data.get('VARIABLES')
class settings(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        class MFrame:
            self.API = ctk.CTkEntry(self)
            self.API.insert(MVARIABLES.get('API'))
            self.API.grid(x=1, y=1)
        self.grid(x=0, y=0)
root.mainloop()