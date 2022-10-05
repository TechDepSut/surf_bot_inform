from tkinter.font import names
from . import sh
from .person import Person


async def object_create(name):

    current_lvl = 0
    current_score = 0
    max_score_on_level = 0

    wks = sh.worksheet_by_title("Лист6")
    names_col = wks.get_col(1)

    for i in range(len(names_col)):
        if name == names_col[i]:
            person_statistic = wks.get_row(i + 1, include_tailing_empty=False)

    lvl_sh = sh.worksheet_by_title("lvl")
    levels = lvl_sh.get_col(1, include_tailing_empty=False)

    found = int(person_statistic[2])
    for i in range(len(levels)):
        if found < int(levels[i]):
            current_lvl = i + 1
            current_score = (found % int(levels[i - 1])) * 7
            max_score_on_level = (int(levels[i]) - int(levels[i - 1])) * 7
            break

    person_statistic.append(str(current_lvl))
    person_statistic.append(str(current_score))
    person_statistic.append(str(max_score_on_level))

    return person_statistic


async def get_statistic(name, type):

    wks = sh.worksheet_by_title("Лист6")
    stat = wks.get_all_records()

    for i in stat:
        if i["Имя"] == name:
            person_statistic = i
            break

    if type == "stat":
        strings = ["Твоя статистика", "━━━━━━━━━━━━━━"]
        for key, item in person_statistic.items():
            strings.append("{}: {}".format(key.capitalize(), item))
        strings.append("━━━━━━━━━━━━━━")
        phrase = "\n".join(strings)

        return phrase

    else:

        return person_statistic


async def get_level(name):

    person_statistic = await get_statistic(name=name, type="lvl")

    current_lvl = 0
    current_score = 0
    max_score_on_level = 0
    progressBar = ""

    lvl_sh = sh.worksheet_by_title("lvl")
    levels = lvl_sh.get_col(1, include_tailing_empty=False)

    found = int(person_statistic["Нашел"])
    for i in range(len(levels)):
        if found < int(levels[i]):
            current_lvl = i + 1
            current_score = (found % int(levels[i - 1])) * 7
            max_score_on_level = (int(levels[i]) - int(levels[i - 1])) * 7
            break

    procent = current_score / max_score_on_level
    part = round(15 * round(procent, 2))

    for i in range(15):
        if i < part:
            progressBar += "█"
        else:
            progressBar += "⎯"

    lvl_info = (
        "Твой уровень\n━━━━━━━━━━━━━━\nУровень: "
        + str(current_lvl)
        + "\nКоличество опыта: "
        + str(current_score)
        + "\nДо следующего уровня: "
        + str(max_score_on_level - current_score)
        + "\n\n"
        + progressBar
        + "\n"
        + str(round(procent, 4) * 100)
        + "%\n"
        + "\n━━━━━━━━━━━━━━"
    )
    return lvl_info
