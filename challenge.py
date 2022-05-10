
from functions import *


with open('arquivos/gameInfoTest.txt', 'r') as gameInfoTest:

    linhas = []
    archive_json = []
    game = 0
    total_kills = 0
    players = []

    dict = {"game": game,
            "status": {
                "total_kills": total_kills,
                "players": []
            }}

    for row in gameInfoTest.readlines():
        linhas.append(row)

    for linha in linhas:

        print(linha.split())

        if linha.split()[1].__eq__('InitGame:'):
            game += 1

        elif linha.split()[1].__eq__('ShutdownGame:'):
            dict["game"] = game
            dict["status"]["players"] = players
            archive_json.append(dict)
            total_kills = 0
            players = []

        elif linha.split()[1].__eq__('ClientUserinfoChanged:'):
            passa = True

            for item in players:
                if item["id"] == linha.split()[2]:
                    passa = False
                    if item["nome"] == findPlayerName(linha):
                        pass
                    else:
                        item["old_names"].append(item["nome"])
                        item["nome"] = findPlayerName(linha)

            if passa:
                player = {"id": linha.split()[2], "nome": findPlayerName(linha), "kills": 0, "old_names": []}
                players.append(player)

print(archive_json)
