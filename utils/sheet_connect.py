from . import wks


async def get_stat(name):

    stat = wks.get_all_records()

    for i in stat:
        if i["ФИО"] == name:
            stat = i
            break

    strings = []
    for key, item in stat.items():
        strings.append("{}: {}".format(key.capitalize(), item))
    phrase = "\n".join(strings)

    return phrase
