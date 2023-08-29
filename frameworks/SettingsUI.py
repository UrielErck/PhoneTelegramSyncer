import customtkinter as ctk
import frameworks.ConfigReaderFile as CRF
standartcolor = ('#c4c4c4','#333333')
root = ctk.CTk(fg_color=standartcolor)
class Command:
    def delete(self, index, datalist):
        datalist[index].get('Frame').destroy()
        datalist.pop(index)

    def save(self, datalist):
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
    visible = False
    root = ctk.CTkFrame(master=root, fg_color=standartcolor)
    items = CRF.readconfig().get('COMMANDS')
    UICommands = []
    print(items)
    def __init__(self):
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
    root = ctk.CTkFrame(master=root, fg_color=standartcolor)
    def __init__(self):
        super().__init__()
        self.root.grid(row=0, column=1)
        self.title = ctk.CTkLabel(master=self.root, text='Hello Page')
        self.title.grid(row=0, column=0, columnspan=2)
        class text:
            frame = ctk.CTkFrame(master=self.root, fg_color=standartcolor)
            text = ctk.CTkLabel(master=frame, text=open('frameworks/HelloPageText.text').read())
            text.grid(column=0, row=0, ipadx=5, ipady=5)
        self.text = text
        self.text.frame.grid(row=1, columnspan=2, column=0)
class menu:
    frame = None
    buttonslist = []
    mainframe = None
    items = {'Hello page': HelloPage, 'Commands': Command, 'Main variable': None, 'Variables': None}
    ismenuvisible = False
    btnitemsframe = None

    def __init__(self):
        super().__init__()
        self.frame = ctk.CTkFrame(master=self.mainframe, fg_color=standartcolor)
        self.frame.grid(row=0, column=0, sticky='NS')
        menubtn = ctk.CTkButton(master=self.frame, text='≡', font=('Arial', 35), command=self.openmenu,
                                width=35, fg_color='transparent')
        menubtn.configure(bg_color=menubtn.cget('fg_color'))
        menubtn.grid(row=0, column=0, sticky='N')
        self.addmenuitems()


    def addmenuitems(self):
        self.btnitemsframe = ctk.CTkFrame(master=self.frame, fg_color=standartcolor)
        row = 0
        i = 0
        for i in self.items.keys():
            row += 1
            def tempcommand():
                self.openel(self.items.get(str(i)))
            self.buttonslist.append(
                [ctk.CTkButton(master=self.btnitemsframe, text=i, fg_color='transparent'), i,
                 lambda i=i: setvisible(self.items.get(i))])
            self.buttonslist[row - 1][0].configure(command=self.buttonslist[row - 1][2])
            self.buttonslist[row-1][0].grid(row=row, column=0)
        return self.btnitemsframe

    def openmenu(self):
        if self.ismenuvisible:
            self.ismenuvisible = False
            self.btnitemsframe.grid_forget()
        else:
            self.ismenuvisible = True
            self.btnitemsframe.grid(row=1, column=0)


def setvisible(frame):
    for i in menu.items.values():
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
menu.mainframe = root
menu()
setvisible(HelloPage)
root.mainloop()