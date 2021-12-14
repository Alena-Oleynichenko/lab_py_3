import re


class Validator:

    def __init__(self):
        pass

    def control_telephone(telephone)->bool:
        if re.match(r"(?:\+7|8)-\(\d{3}\)(-\d{3})(-\d{2}){2}", telephone) is not None:
            return True
        return False

    def control_weight(weight)->bool:
        pattern = '\d{2,3}'
        if re.match(pattern, str(weight)) is not None:
            if 150 > int(weight) > 40:
                return True
        return False

    def control_snils(snils: str) -> bool:
        if len(snils) == 11:
            return True
        return False

    def control_passport_num(passport_number: int) -> bool:
        if len(str(passport_number)) == 6:
            return True
        return False

    def control_address(address) -> bool:
        if type(address) != str:
            return False
        if re.match(r"^(ул\.)?(Аллея)?\s[\w\.\s-]+\d+$", address) is not None:
            return True
        return False

    def control_work_experience(work_number) -> bool:
        if type(work_number) == int:
            if(work_number<80 and work_number>0):
                return True
        return False

    def control_political_views(political_view: str) -> bool:
        valid_political_views = 'Индифферентные, Социалистические, Умеренные, Либеральные, Консервативные, Коммунистические, Анархистские, Либертарианские'
        if type(political_view) != str:
            return False
        if political_view not in valid_political_views:
            return False
        return True

    def control_worldview(worldview: str) -> bool:
        valid_worldview = 'Секулярный гуманизм, Иудаизм, Деизм, Конфуцианство, Католицизм, Пантеизм, Агностицизм, Атеизм, Буддизм'
        if type(worldview) != str:
            return False
        if worldview not in valid_worldview:
            return False
        return True

    def control_university(university) -> bool:
        invalid_university = 'Дурмстранг, Шамбартон, Хогвартс, Кирин-Тор, Аретуза, Бан Ард, Каражан, Гвейсон Хайль'
        if type(university) != str:
            return False
        if university not in invalid_university:
            return True
        return False
