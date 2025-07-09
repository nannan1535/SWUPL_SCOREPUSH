from getscore import get_score
import json
import pushChange
import writefile
date = get_score()
course_list = []
newTotalResult = date['totalResult']
scoreChange = False  # 用于判断成绩是否有变化
noneOldScore = False
content = ""  # 用于存储成绩信息

if newTotalResult == 0:  # 如果没有成绩
    pushChange.push(1, "老师还没有上传成绩，请耐心等待", "没有成绩")
    exit()
else:
    for item in date['items']:
        course_info = {
            'courseName': item['kcmc'],
            'score': item['cj'],
            'teacherName': item['cjbdczr'],
            'newScoreSubmissionTime': item['cjbdsj']
        }
        course_list.append(course_info)
# 将成绩列表进行排序
sorted_grades_new = sorted(course_list, key=lambda item: item['newScoreSubmissionTime'], reverse=True)
jsonContent = {"newScoreSubmissionTime": sorted_grades_new[0]["newScoreSubmissionTime"],
               "TotalResult": newTotalResult}

# 对旧的JSON文件进行读取 
try:
    with open('grades_json_old.json', 'r', encoding='utf-8') as f:
        grades_data_old = json.load(f)
except:  # 如果旧成绩文件不存在或无法读取，则认为没有旧成绩
    with open('grades_json_old.json', 'w', encoding='utf-8') as f:
        noneOldScore = True
        grades_data_old = {
            "newScoreSubmissionTime": "",
            "TotalResult": 0
        }

changeNumber = jsonContent["TotalResult"] - grades_data_old["TotalResult"]

# 对比新旧成绩的数目
if noneOldScore:
    scoreChange = True
    for gradeInfo in sorted_grades_new[:jsonContent["TotalResult"]]:
        content += gradeInfo["courseName"] + "成绩：" + gradeInfo["score"] + "，任课老师：" + gradeInfo["teacherName"] + "，成绩提交时间：" + gradeInfo["newScoreSubmissionTime"] +"\n"
elif changeNumber > 0:  # 如果新成绩数目大于旧成绩数目
    scoreChange = True
    for gradeInfo in sorted_grades_new[:changeNumber]:
        content += gradeInfo["courseName"] + "成绩：" + gradeInfo["score"] + "，任课老师：" + gradeInfo["teacherName"] + "，成绩提交时间：" + gradeInfo["newScoreSubmissionTime"] +"\n"
elif changeNumber < 0:
    pushChange.push(1, "请删除grades_json_old.json后重试！！", "出错了")
else:
    scoreChange = False
# 将新成绩更新时间，总数目写入旧成绩文件
if scoreChange:
    writefile.writeFile('grades_json_old.json', jsonContent)
    pushChange.push(1, content, "有"+ str(changeNumber) +"门新成绩了！")
print(scoreChange,changeNumber)

