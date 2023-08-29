import customtkinter as ctk
import frameworks.ConfigReaderFile as Config
root = ctk.CTk()
root.geometry("850x500")
data = Config.readconfig()
MVARIABLES = data.get('MVARIABLE')
COMMANDS = data.get('COMMANDS')
VARIABLES = data.get('VARIABLES')
class settings:
    def addcomand(self):
        frame = ctk.CTkFrame(master=self.command.commandroot)
        frame.grid(column=0)
        Ent = ctk.CTkEntry(master=frame, width=350)
        Ent.grid(row=0, column=0, padx=10, pady=15)

        # temp = deleteENT(Ent=Ent, bnt=commandrembtn, self=self)
        commandrembtn = ctk.CTkButton(master=frame, text='-', fg_color='red', width=35,
                                      hover_color='dark red')
        commandrembtn.configure(command=frame.destroy)
        commandrembtn.grid(row=0, column=1, padx=10, pady=5)
        self.command.commandaddbtn.destroy()
        self.command.commandaddbtn = ctk.CTkButton(master=self.command.commandroot, text='+', fg_color='green', width=35,
                                      hover_color='dark green', command=self.addcomand)
        self.command.commandaddbtn.grid(column=0, sticky='S', padx=10)
    def __init__(self):
        super().__init__()
        self.root = ctk.CTkFrame(master=root, width=600, height=500)
        self.root.grid(column=0, row=0)
        class MSettings:
            MSettingsFrame = ctk.CTkScrollableFrame(master=self.root, width=450, height=100)
            MSettingsFrame.grid(column=0, row=self.root.grid_info().get('row'), sticky='W')

            MSettingsTXT = ctk.CTkLabel(master=MSettingsFrame, text='main variable'.title())
            MSettingsTXT.grid(column=0, row=0, padx=10, pady=5, columnspan=10)
            gridindrow = 1
            for i in MVARIABLES.keys():

                Name = ctk.CTkLabel(master=MSettingsFrame, text=f'{i}: ')
                Name.grid(row=gridindrow, column=0, padx=10, pady=5)

                Ent = ctk.CTkEntry(master=MSettingsFrame, width=350)
                Ent.insert(string=MVARIABLES.get(f'{i}'), index=0)
                Ent.grid(column=1, row=gridindrow, padx=10, pady=5)
                gridindrow += 1
        class Command:
            commandroot = ctk.CTkScrollableFrame(master=self.root, width=450, height=100)
            commandroot.grid(column=0, row=self.root.grid_info().get('row')+1, sticky='W')

            commandTXT = ctk.CTkLabel(master=commandroot, text='commands'.title())
            commandTXT.grid(column=0, row=0, padx=10, pady=5, columnspan=1, sticky='N')

            framesdatalist = []
            for i in COMMANDS:
                frame = ctk.CTkFrame(master=commandroot)
                frame.grid(column=0, sticky='N')
                Ent = ctk.CTkEntry(master=frame, width=350)
                Ent.insert(string=i, index=0)
                Ent.grid(column=0, padx=10, pady=15)

                # temp = deleteENT(Ent=Ent, bnt=commandrembtn, self=self)
                commandrembtn = ctk.CTkButton(master=frame, text='-', fg_color='red', width=35,
                                                   hover_color='dark red')
                commandrembtn.configure(command=frame.destroy)
                commandrembtn.grid(row=0, column=1, padx=10, pady=5)
                framesdatalist.append(frame)
            commandaddbtn = ctk.CTkButton(master=commandroot, text='+', fg_color='green', width=35,
                                               hover_color='dark green', command=self.addcomand)
            commandaddbtn.grid(column=0, sticky='S', padx=10, pady=5)
        self.command = Command

settings()
root.mainloop()