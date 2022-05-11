def findPlayerName(line: str) -> str:
    nome = line.split('n\\')[1].split('\\t')
    return nome[0]

def updateKills(line: str) -> tuple:
    killData = line.split(':')
    firstPlayer = killData[3].split('killed')[0].strip()
    secondPlayer = killData[3].split('killed')[1].split('by')[0].strip()
    if firstPlayer.__eq__('<world>'):
        return secondPlayer, -1
    elif firstPlayer.__eq__(secondPlayer):
        return secondPlayer, -1
    else:
        return firstPlayer, 1