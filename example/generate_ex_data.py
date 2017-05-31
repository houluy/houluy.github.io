import json
import random
import hashlib
from pprint import pprint

prof_title_list = ['助教', '讲师', '副教授', '教授']

family_name_list = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王']
first_name_list = ['明', '建国', '重阳', '芳', '刚', '玉']

age_list = list(range(24, 44))

NUM = 10

teacher_list = []
md5 = hashlib.md5()

for i in range(NUM):
    t_name = random.choice(family_name_list) + random.choice(first_name_list)
    t_title = random.choice(prof_title_list)
    t_age = random.choice(age_list)
    t_intro = "这位是{}教师，职称：{}，年龄：{}".format(t_name, t_title, t_age)
    md5.update(''.join([t_name, t_title, str(t_age)]).encode())
    t_id = md5.hexdigest()
    teacher = {
        't_id': t_id,
        'title': t_title,
        'name': t_name,
        'age': t_age,
        'introduction': t_intro,
    }
    teacher_list.append(teacher)

with open('teacher.json', 'w', encoding='utf8') as f:
    json.dump(teacher_list, f, ensure_ascii=False, indent=2)
