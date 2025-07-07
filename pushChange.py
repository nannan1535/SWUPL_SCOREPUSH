import requests
import os

def push(result, content="", summary=""):
    if not result:
        return

    url = "https://wxpusher.zjiecode.com/api/send/message"
    app_token = os.environ.get('APPTOKEN')
    topic_ids_str = os.environ.get('TOPICIDS') # e.g., "123,456"
    uids_str = os.environ.get('UIDS') # e.g., "UID_xxx,UID_yyy"

    # 将从环境变量读取的字符串转换为列表
    # 如果字符串存在，则按逗号分割
    # topicIds 需要是整数列表
    topic_ids_list = [int(tid) for tid in topic_ids_str.split(',')] if topic_ids_str else []
    
    # uids 需要是字符串列表
    uids_list = uids_str.split(',') if uids_str else []

    json_data = {
        "appToken": app_token,
        "content": content,
        "summary": summary, 
        "contentType": 1,
        # 使用转换后的列表
        "topicIds": topic_ids_list,
        "uids": uids_list,
        "verifyPay": "false", 
        "verifyPayType": 0 
    }
    
    requests.post(url, json=json_data)
