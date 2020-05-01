from datetime import date


def calculate_age(date_of_birth):
    """年齢を返す"""
    today = date.today()  # 今日
    if today.month < 4:
        fiscalyear = today.year - 1
    else:
        fiscalyear = today.year

    age = today.year - date_of_birth.year

    # 今年の誕生日を迎えていなければ、ageを1つ減らす
    # 今日を表すタプル(7, 29) < 誕生日を表すタプル(7, 30)
    if (today.month, today.day) < (date_of_birth.month, date_of_birth.day):
        age -= 1
    return age
