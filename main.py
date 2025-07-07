from getscore import get_score
import json
import os
from pushChange import push
import pushChange
date = get_score()
course_list = []

for item in date['items']:
    course_info = {
        '课程名称': item['kcmc'],
        '成绩': item['cj'],
        '任课老师': item['cjbdczr'],
        '成绩提交时间': item['cjbdsj']
    }
    course_list.append(course_info)

with open('grades_json_new.txt', 'w', encoding='utf-8') as f:
    json.dump(course_list, f, ensure_ascii=False, indent=4)


###
old_filename = 'grades_json_old.txt'
input_filename_new = 'grades_json_new.txt'
output_filename = 'grades_json_old.txt'

# 读取新的JSON文件内容 进行排序 但不保存
try:
    with open(input_filename_new, 'r', encoding='utf-8') as f:
        grades_data = json.load(f)
        if not grades_data:
            pushChange.push(0)
            os.remove(input_filename_new)  # 删除空文件
            exit()
    sorted_grades_new = sorted(grades_data, key=lambda item: item['成绩提交时间'], reverse=True)
    content = sorted_grades_new[0]["课程名称"] + " 成绩：" + sorted_grades_new[0]["成绩"] + "，任课老师：" + sorted_grades_new[0]["任课老师"] + "，成绩提交时间：" + sorted_grades_new[0]["成绩提交时间"]
except:
    pushChange.push(0)
    os.remove(input_filename_new)
    exit()

# 对旧的JSON文件进行读取 
try:
    with open(old_filename, 'r', encoding='utf-8') as f:
        grades_data_old = json.load(f)
        if not grades_data_old: #旧文件为空
            pushChange.push(1,content,"有新成绩了！")
            with open(output_filename, 'w', encoding='utf-8') as f:
                json.dump(sorted_grades_new, f, ensure_ascii=False, indent=4)
                os.remove(input_filename_new)  # 删除新文件
                exit()

except: #如果旧成绩文件不存在或无法读取，则认为没有旧成绩
    with open(output_filename, 'w', encoding='utf-8') as f:
        pushChange.push(1,content,"有新成绩了！")
        json.dump(sorted_grades_new, f, ensure_ascii=False, indent=4)
        os.remove(input_filename_new)
        exit()
        
    
if sorted_grades_new[0]["成绩提交时间"] <= grades_data_old[0]["成绩提交时间"]:
        os.remove(input_filename_new)  # 删除新文件
        pushChange.push(1,"成绩没有更新哦！","成绩没有更新哦！")
        exit()
else:
    pushChange.push(1,content,"有新成绩了！")
    os.remove(input_filename_new)
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(sorted_grades_new, f, ensure_ascii=False, indent=4)
