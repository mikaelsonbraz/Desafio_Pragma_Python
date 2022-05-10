

def findPlayerName(list: str) -> str:
    nome = list.split('n\\')[1].split('\\t')
    return nome[0]