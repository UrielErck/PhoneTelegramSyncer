def main():
    import customtkinter as ctk
    import frameworks.ConfigReaderFile as CRF
    import os
    import sys
    standartcolor = ('#FFFFFF', '#333333')
    app = ctk.CTk(fg_color=standartcolor)

    class Variables:
        visible = False
        root = ctk.CTkFrame(master=app, fg_color=standartcolor)
        items = CRF.readconfig().get('VARIABLE')
        dataEnt = []
        Entframe = 0

        def save(self, data):
            self.ischanged = 1
            if not self.visible:
                return 1
            print(f'Old data: {self.items}')
            self.items.clear()
            for i in data:
                value = i.get('Value').get()
                name = str(i.get('Label').cget('text'))[:-2]
                self.items.update({name: value})
            self.Entframe.destroy()
            self.__init__()
            print(f'New data: {self.items}')
            print(CRF.editconfig('VARIABLES', self.items))

        def __init__(self):
            super().__init__()
            self.dataEnt = []
            self.root.grid(row=0, column=1)
            self.Entframe = ctk.CTkFrame(master=self.root, fg_color='transparent')
            self.Entframe.grid(row=0, column=0)
            row = 0
            savebtn = 0
            app.bind('<Return>', lambda event: self.save(self.dataEnt))
            for i in self.items.keys():
                row += 1
                tmpFrame = ctk.CTkFrame(master=self.Entframe, fg_color='transparent')
                print(str(self.items.get(i)))
                if type(self.items.get(i)) == bool or self.items.get(i) in ['True', 'False']:
                    Value = ctk.CTkSwitch(master=tmpFrame, onvalue=True, offvalue=False, text='')
                    if str(self.items.get(i)) == 'True':
                         Value.select()
                    else:
                        Value.deselect()
                else:
                     Value = ctk.CTkEntry(master=tmpFrame, placeholder_text='Put value here...', width=350)
                self.dataEnt.append({"id": i,
                                     'Label': ctk.CTkLabel(master=tmpFrame, text=f"{i}: ", width=50),
                                     'Value': Value,
                                     'Frame': tmpFrame,
                                     })
                tmpFrame.grid(row=row - 1, column=0, sticky='WN', ipadx=3, ipady=3, padx=5, pady=5)
                self.dataEnt[row - 1].get('Label').grid(row=0, column=0, ipadx=5)
                try:
                    self.dataEnt[row - 1].get('Value').insert(0, self.items.get(i))
                except AttributeError:
                    pass
                self.dataEnt[row - 1].get('Value').grid(row=0, column=1)
            savebtn = ctk.CTkButton(master=self.root, text='Save', fg_color='green', hover_color='dark green',
                                    command=lambda: self.save(self.dataEnt))
            savebtn.grid(column=0, sticky='S', row=3)

    class MVariables:
        visible = False
        root = ctk.CTkFrame(master=app, fg_color=standartcolor)
        items = CRF.readconfig().get('MVARIABLE')
        dataEnt = []
        Entframe = 0

        def save(self, data):
            self.ischanged = 1
            if not self.visible:
                return 1
            print(f'Old data: {self.items}')
            self.items.clear()
            for i in data:
                value = i.get('Entry').get()
                name = str(i.get('Label').cget('text'))[:-2]
                self.items.update({name: value})
            self.Entframe.destroy()
            self.__init__()
            print(f'New data: {self.items}')
            print(CRF.editconfig('MAIN VARIABLE', self.items))

        def __init__(self):
            super().__init__()
            self.dataEnt = []
            self.root.grid(row=0, column=1)
            self.Entframe = ctk.CTkFrame(master=self.root, fg_color='transparent')
            self.Entframe.grid(row=0, column=0)
            row = 0
            savebtn = 0
            app.bind('<Return>', lambda event: self.save(self.dataEnt))
            for i in self.items.keys():
                row += 1
                tmpFrame = ctk.CTkFrame(master=self.Entframe, fg_color='transparent')
                self.dataEnt.append({"id": i,
                                     'Label': ctk.CTkLabel(master=tmpFrame, text=f"{i}: ", width=50),
                                     'Entry': ctk.CTkEntry(master=tmpFrame, placeholder_text='Put value here...', width=350),
                                     'Frame': tmpFrame,
                                     })
                tmpFrame.grid(row=row-1, column=0, sticky='WN', ipadx=3, ipady=3, padx=5, pady=5)
                self.dataEnt[row-1].get('Label').grid(row=0, column=0, ipadx=5)
                self.dataEnt[row-1].get('Entry').insert(0, self.items.get(i))
                self.dataEnt[row-1].get('Entry').grid(row=0, column=1)
            savebtn = ctk.CTkButton(master=self.root, text='Save', fg_color='green', hover_color='dark green',
                                    command=lambda: self.save(self.dataEnt))
            savebtn.grid(column=0, sticky='S', row=3)

    class Command:

        def delete(self, index, datalist):
            datalist[index].get('Frame').destroy()
            datalist.pop(index)

        def save(self, datalist):
            self.ischanged = 1
            if not self.visible:
                return 0
            print(f'Old data: {self.items}')
            self.items.clear()
            for i in datalist:
                newValure = i.get('Lever').get()
                newName = i.get('Entry').get()
                print(f'dictel: {newName}: {newValure}')
                self.items.update({newName: newValure})
            self.commandsframe.destroy()
            self.__init__()
            print(f'New data: {self.items}')
            CRF.editconfig('COMMANDS', self.items)

        def add(self):
            self.items.update({'NEW': True})
            self.commandsframe.destroy()
            self.__init__()

        ischanged = 1
        visible = False
        root = ctk.CTkFrame(master=app, fg_color=standartcolor)
        items = CRF.readconfig().get('COMMANDS')
        UICommands = []
        print(items)

        def __init__(self):
            self.ischanged = 1
            app.bind('<Return>', lambda event: Command.save(self=self, datalist=self.UICommands))
            super().__init__()
            self.UICommands = []
            self.root.grid(row=0, column=1)
            self.commandsframe = ctk.CTkScrollableFrame(master=self.root, fg_color=standartcolor, width=310)
            self.commandsframe.grid(row=0, column=0)
            index = 0
            for i in self.items.keys():
                index += 1
                tempframe = ctk.CTkFrame(master=self.commandsframe, fg_color=standartcolor)
                self.UICommands.append({'id': index - 1,
                                        'Frame': tempframe,
                                        'Lever': ctk.CTkSwitch(master=tempframe, offvalue=0, onvalue=1, text='visible'),
                                        'Entry': ctk.CTkEntry(master=tempframe, width=300),
                                        'Button': ctk.CTkButton(master=tempframe, text='×', command=lambda index=index:self.delete(index-1, self.UICommands),
                                        width=30, font=('Calibre', 20), height=25, hover_color='dark red', fg_color='red')
                                        })
                tempframe.grid(row=index-1, column=0, ipadx=5, ipady=5)
                self.UICommands[index-1].get('Entry').insert(0, i)
                self.UICommands[index-1].get('Entry').grid(row=0, columnspan=2, column=0)
                if self.items.get(i):
                    self.UICommands[index-1].get('Lever').select()
                else:
                    self.UICommands[index-1].get('Lever').deselect()
                self.UICommands[index-1].get('Lever').grid(row=1, column=0, sticky='WN')
                self.UICommands[index-1].get('Button').grid(row=1, column=1, sticky='EN')

                # tempEnt.configure(textvariable=self.UICommands[index-1].update())
            savebtn = ctk.CTkButton(master=self.root, text='Save', fg_color='green',
                                    hover_color='dark green', command=lambda: self.save(self.UICommands), width=75)
            savebtn.grid(column=0, row=2, sticky='WS')
            addbtn = ctk.CTkButton(master=self.root, text='+', fg_color='green',
                                    hover_color='dark green', command=self.add, width=70)
            addbtn.grid(column=0, row=2, sticky='SE')

    class HelloPage:
        visible = False
        root = ctk.CTkFrame(master=app, fg_color=standartcolor)
        def __init__(self):
            super().__init__()
            self.root.grid(row=0, column=1)
            self.title = ctk.CTkLabel(master=self.root, text='Hello Page')
            self.title.grid(row=0, columnspan=2, sticky='WE')
            class text:
                frame = ctk.CTkScrollableFrame(master=self.root, fg_color=standartcolor, width=300)
                text = ctk.CTkLabel(master=frame, text=open('frameworks/HelloPageText.text').read())
                text.grid(column=0, row=0, ipadx=5, ipady=5)
            self.text = text
            self.text.frame.grid(row=1, columnspan=2, column=0)

    class Menu:
        btncolor = ''
        frame = None
        buttonslist = []
        mainframe = None
        items = {'Hello page': HelloPage, 'Commands': Command, 'Main variable': MVariables, 'Variables': Variables}
        ismenuvisible = False
        btnitemsframe = None

        def __init__(self):
            super().__init__()
            self.frame = ctk.CTkFrame(master=self.mainframe)
            self.frame.grid(row=0, column=0, sticky='NS')
            menubtn = ctk.CTkButton(master=self.frame, text='≡', font=('Arial', 27), command=self.openmenu,
                                    width=30)
            menubtn.configure(bg_color=menubtn.cget('fg_color'))
            self.btncolor = menubtn.cget('bg_color')
            self.frame.configure(fg_color=self.btncolor)
            menubtn.grid(row=0, column=0, sticky='N')
            self.addmenuitems()


        def addmenuitems(self):
            self.btnitemsframe = ctk.CTkFrame(master=self.frame, fg_color=self.btncolor)
            row = 0
            i = 0
            for i in self.items.keys():
                row += 1
                def tempcommand():
                    self.openel(self.items.get(str(i)))
                self.buttonslist.append(
                    [ctk.CTkButton(master=self.btnitemsframe, text=i), i,
                     lambda i=i: setvisible(self.items.get(i))])
                self.buttonslist[row - 1][0].configure(command=self.buttonslist[row - 1][2],
                                                       bg_color=self.buttonslist[row - 1][0].cget('fg_color'),)
                self.buttonslist[row-1][0].grid(row=row, column=0)
            return self.btnitemsframe

        def openmenu(self):
            if self.ismenuvisible:
                self.ismenuvisible = False
                self.btnitemsframe.grid_forget()
            else:
                self.ismenuvisible = True
                self.btnitemsframe.grid(row=1, column=0)

    class ExitMenu:
        root = None
        exitcode = False
        def end(self, code):
            self.root.destroy()
            if not type(code) == bool:
                return code
            self.exitcode = code
        def __init__(self):
            super().__init__()
            self.root.grid()
            Inotext = ctk.CTkLabel(master=self.root, text='Some settings was changed.\n do you wish restart program to apply changes?')
            Inotext.grid(row=0, sticky='NSWE', columnspan=2, padx=10, pady=10, ipadx=5, ipady=5)
            yesbtn = ctk.CTkButton(master=self.root, text='Yes', command=lambda : self.end(True), fg_color='green', hover_color='dark green')
            yesbtn.grid(row=1, column=0, padx=10, pady=10, ipadx=5, ipady=5)
            nobtn = ctk.CTkButton(master=self.root, text='No', fg_color='green', hover_color='dark green',
                                    command=lambda : self.end(False))
            nobtn.grid(row=1, column=1, padx=10, pady=10, ipadx=5, ipady=5)


    def setvisible(frame):
        for i in Menu.items.values():
            print(i)
            try:
                if i.visible:
                    i.visible = False
                    i.root.grid_forget()
            except AttributeError:
                pass
        if not frame:
            return 1
        if not frame.visible:
            frame.visible = True
            frame()
        else:
            frame.visible = False
            frame.root.grid_forget()

    # def callback(frame):
    #     temp = 0
    #     for i in [Command, MVariables, Variables]:
    #         try:
    #             if i.ischanged == 1:
    #                 temp = 1
    #         except AttributeError:
    #             pass
    #     print(temp)
    #     if temp == 1:
    #         ExitMenu.root = ctk.CTkToplevel(master=app, fg_color=standartcolor)
    #         with ExitMenu() as temp:
    #             if temp:
    #                 os.execv(sys.argv[0], sys.argv)
    #             else:
    #                 frame.destroy()
    #     else:
    #         frame.destroy()

    # app.protocol("WM_DELETE_WINDOW", lambda frame=app: callback(frame))
    Menu.mainframe = app
    Menu()
    setvisible(HelloPage)
    app.mainloop()
