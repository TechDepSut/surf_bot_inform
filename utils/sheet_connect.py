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


async def print_stat(person):

    stat = (
        "📈Твоя статистика:\n━━━━━━━━━━━━━━\n"
        + "Имя: "
        + person.name
        + "\nКол-во: "
        + person.amount
        + "\nНайдено: "
        + person.founded
        + "\nОсталось: "
        + person.left
        + "\n━━━━━━━━━━━━━━"
    )

    return stat


async def print_lvl(person):

    bar = await get_progressBar(person.current_score, person.max_score_on_level)

    lvl = (
        "🏆Твой уровень:\n━━━━━━━━━━━━━━\n"
        + "Уровень: "
        + person.current_level
        + "\nКоличество опыта: "
        + person.current_score
        + "\nДо следующего уровня: "
        + str(int(person.max_score_on_level) - int(person.current_score))
        + "\n\n"
        + bar[0]
        + "\n"
        + bar[1]
        + "%"
        + "\n\n━━━━━━━━━━━━━━"
    )

    return lvl


async def get_progressBar(current_score, max_score_on_level):

    progressBar = ""

    procent = float(current_score) / float(max_score_on_level)
    part = round(15 * round(procent, 2))

    for i in range(15):
        if i < part:
            progressBar += "█"
        else:
            progressBar += "⎯"

    return [progressBar, str(round(procent * 100, 2))]
