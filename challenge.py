from functions import *
import jsonpickle

with open('files/Quake.txt', 'r') as QuakeTxt:

    lines = []
    archive_json = []
    game = 0
    total_kills = 0
    players = []

    for row in QuakeTxt.readlines():
        lines.append(row)

    for line in lines:

        if line.split()[1].__eq__('InitGame:'):
            dict = {"game": game,
                    "status": {
                        "total_kills": total_kills,
                        "players": players
                    }}
            game += 1

        elif line.split()[1].__eq__('ClientUserinfoChanged:'):
            changeName = False
            for item in players:
                if item["id"] == line.split()[2]:
                    changeName = True
                    if item["nome"] == findPlayerName(line):
                        pass
                    else:
                        item["old_names"].append(item["nome"])
                        item["nome"] = findPlayerName(line)
            if not changeName:
                player = {"id": line.split()[2], "nome": findPlayerName(line), "kills": 0, "old_names": []}
                players.append(player)

        elif line.split()[1].__eq__('Kill:'):
            total_kills += 1
            playerDeath = updateKills(line)
            for item in players:
                if item["nome"].__eq__(playerDeath[0]):
                    item["kills"] += playerDeath[1]
                    if item["kills"] < 0:
                        item["kills"] = 0

        elif line.split()[1].__eq__('ShutdownGame:'):
            dict["game"] = game
            dict["status"]["total_kills"] = total_kills
            dict["status"]["players"] = players
            archive_json.append(dict)
            players = []
            total_kills = 0

QuakeTxt.close()

with open('files/Quake.json', 'w') as QuakeJson:
    json = jsonpickle.encode(archive_json, indent=4)
    QuakeJson.write(json)
QuakeJson.close()

