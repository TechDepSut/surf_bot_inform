from . import sh


async def get_stat(name):

    wks = sh.worksheet_by_title("Лист6")
    stat = wks.get_all_records()

    for i in stat:
        if i["Имя"] == name:
            person_statistic = i
            break

    strings = ["Твои параметры", "━━━━━━━━━━━━━━"]
    for key, item in person_statistic.items():
        strings.append("{}: {}".format(key.capitalize(), item))
    phrase = "\n".join(strings)
    phrase += "\n━━━━━━━━━━━━━━"

    level_info = get_level(person_statistic)    

    return [phrase, level_info]


def get_level(person_statistic):
    
    current_lvl = 0
    current_score = 0
    max_score_on_level = 0
    next_level = 0

    lvl_sh = sh.worksheet_by_title("lvl")
    levels = lvl_sh.get_col(1, include_tailing_empty=False)

    found = int(person_statistic['Нашел'])
    for i in range(len(levels)):
        if found < int(levels[i]):
            current_lvl = i + 1
            current_score = found % int(levels[i - 1])
            max_score_on_level = int(levels[i]) - int(levels[i - 1])
            break
    
    lvl_info = "Твой уровень\n━━━━━━━━━━━━━━\nУровень: " + str(current_lvl) + "\nКоличество опыта: " + str(current_score) + "\nДо следующего уровня: " + str(max_score_on_level - current_score) + "\n━━━━━━━━━━━━━━"
    return lvl_info
