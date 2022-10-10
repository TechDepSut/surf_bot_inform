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
    part = round(20 * round(procent, 2))

    for i in range(20):
        if i < part:
            progressBar += "■"
        else:
            progressBar += "□"

    return [progressBar, str(round(procent * 100, 2))]


async def enemies_print(min_person, max_person):

    min_print = ""
    max_print = ""

    if min_person.name != "":
        min_print = (
            "Ближайший серфер с меньшим количеством людей:\n━━━━━━━━━━━━━━\n"
            + "Имя: "
            + min_person.name
            + "\nКол-во: "
            + min_person.amount
            + "\nНайдено: "
            + min_person.founded
            + "\nОсталось: "
            + min_person.left
            + "\n━━━━━━━━━━━━━━"
        )

    if max_person.name != "":
        max_print = (
            "Ближайший серфер с большим количеством людей:\n━━━━━━━━━━━━━━\n"
            + "Имя: "
            + max_person.name
            + "\nКол-во: "
            + max_person.amount
            + "\nНайдено: "
            + max_person.founded
            + "\nОсталось: "
            + max_person.left
            + "\n━━━━━━━━━━━━━━"
        )

    return [min_print, max_print]
