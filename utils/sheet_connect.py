from . import sh


async def get_stat(name):

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


async def get_enemy(person):

    wks = sh.worksheet_by_title("Лист6")
    founded = wks.get_col(3, include_tailing_empty=False)

    founded.pop(0)
    founded = list(map(int, founded))

    min_f = -1
    max_f = -1

    founded_sort = sorted(founded)
    for i in range(len(founded_sort)):
        if founded_sort[i] == int(person.founded):

            if i != 0:
                min_f = founded_sort[i - 1]

            if i != len(founded_sort) - 1:
                max_f = founded_sort[i + 1]

    min_person = ["", "", "", ""]
    max_person = ["", "", "", ""]

    if min_f != -1:
        for i in range(len(founded)):
            if min_f == founded[i]:
                min_person = wks.get_row(i + 2, include_tailing_empty=False)

    if max_f != -1:
        for i in range(len(founded)):
            if max_f == founded[i]:
                max_person = wks.get_row(i + 2, include_tailing_empty=False)

    return [min_person, max_person]
