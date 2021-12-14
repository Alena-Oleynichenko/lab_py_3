import argparse
import json
from Shell.valid import *
from Shell.sort import *
from tqdm import tqdm


parser = argparse.ArgumentParser()
parser.add_argument('-input', type=str,  default="C:\\labs_py\\106.txt", dest='input')
parser.add_argument('-output', type=str, default="C:\\labs_py\\output.txt", dest='output')
parser.add_argument('-output_sort', type=str, default="C:\\labs_py\\result.txt", dest='output_sort')
args = parser.parse_args()

data = json.load(open(args.input, encoding='windows-1251'))

true_data = list()
telephone = 0
weight = 0
snils = 0
passport_num = 0
university = 0
work_experience = 0
worldview = 0
address = 0
political_views = 0

with tqdm(total=len(data)) as progressbar:
    for person in data:
        temp = True
        if not Validator.control_telephone(person['telephone']):
            telephone += 1
            temp = False
        if not Validator.control_weight(person['weight']):
            weight += 1
            temp = False
        if not Validator.control_snils(person['snils']):
            snils += 1
            temp = False
        if not Validator.control_work_experience(person['work_experience']):
            work_experience += 1
            temp = False
        if not Validator.control_worldview(person['worldview']):
            worldview += 1
            temp = False
        if not Validator.control_passport_num(person['passport_number']):
            passport_num += 1
            temp = False
        if not Validator.control_university(person['university']):
            university += 1
            temp = False
        if not Validator.control_address(person["address"]):
            address += 1
            temp = False
        if not Validator.control_political_views(person['political_views']):
            political_views += 1
            temp = False
        if temp:
            true_data.append(person)
        progressbar.update(1)

out = open(args.output, 'w', encoding='windows-1251')
new_data = json.dumps(true_data, ensure_ascii=False, indent=4)
out.write(new_data)
out.close()
print(f'Число валидных записей: {len(true_data)}')
print(f'Число невалидных записей: {len(data) - len(true_data)}')
print(f'Число невалидных телефонных номеров: {telephone}')
print(f'Число невалидных маcc: {weight}')
print(f'Число невалидных снилсов: {snils}')
print(f'Число невалидных паспортных номеров: {passport_num}')
print(f'Число невалидных университетов: {university}')
print(f'Число невалидных рабочих стажей: {work_experience}')
print(f'Число невалидных политических взглядов:{political_views}')
print(f'Число невалидных мировоззрений: {worldview}')
print(f'Число невалидных адрессов: {address}')

shell_sort(true_data)
serialization(true_data, args.output_sort)
print(deserialization(args.output_sort))
