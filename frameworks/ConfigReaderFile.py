def bintobool(num: int) -> bool:
    if not type(num) == int:
        num = int(num)
    if num == 1:
        return True
    elif num == 0:
        return False
    else:
        raise ValueError
def gettext(paramname: str, text: str) -> str:
    lenght = len(paramname)
    fintext = text[text.find(f'### {paramname} ###')+lenght+8:text.find(f'&& {paramname} &&')]
    return fintext


def readconfig() -> dict:
    from frameworks.loading import resource_path as path
    findata = {}
    temp = {}
    file = open(f'config.PTSC', 'r')
    text = file.read()
    Nvariabletext = gettext('MAIN VARIABLE', text)
    commandstext = gettext('COMMANDS', text)
    variablestext = gettext('VARIABLES', text)
    file.close()
    for i in Nvariabletext.split('\n'):
        if '=' in i:
            name = i[0:i.find('=')-1]
            value = i[i.find('=')+2:]
            temp.update({name: value})
    findata.update({'MVARIABLE': temp})
    temp = {}
    for i in commandstext.split('\n'):
        if not i and not '=' in i:
            pass
        else:
            name = i[0:i.find('=') - 1]
            isvisible = bintobool(i[i.find('=') + 2:])
            temp.update({name: isvisible})
    findata.update({'COMMANDS': temp})
    temp = {}
    for i in variablestext.split('\n'):
        if '=' in i:
            name = i[0:i.find('=') - 1]
            value = i[i.find('=') + 2:]
            if value.isdigit():
                value = bintobool(value)
            temp.update({name: value})
    findata.update({'VARIABLE': temp})
    temp = 0
    return findata

def editconfig(configname, data):
    # if configname == 'MAIN VARIABLE':
    #     pass
    # elif configname == 'COMMANDS':
    conftext = ''
    for i in data.keys():
        if conftext != None:
            conftext += '\n'
        conftext += f'{i} = {data.get(i)}'
    file = open(f'config.PTSC', 'r')
    filetext = file.read()
    file.close()
    file = open(f'config.PTSC', 'w')
    conftext = f"{filetext[0:filetext.find(f'### {configname} ###') + len(configname)+8]}{conftext}\n{filetext[filetext.find(f'&& {configname} &&'):]}"
    file.write(conftext)
    file.close()
    return conftext
    # elif configname == 'VARIABLES':
    #     pass
