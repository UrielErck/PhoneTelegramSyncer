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
    temp = []
    for i in commandstext.split('\n'):
        if i:
            temp.append(i)
    findata.update({'COMMANDS': temp})
    temp = {}
    for i in variablestext.split('\n'):
        if '=' in i:
            name = i[0:i.find('=') - 1]
            value = i[i.find('=') + 2:]
            if value.isdigit():
                value = int(value)
            temp.update({name: value})
    findata.update({'VARIABLE': temp})
    temp = 0
    return findata
