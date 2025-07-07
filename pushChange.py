# pushChange.py (最终修正版)

import requests
import os
import json

def push(result, content="", summary=""):
    print("\n--- [pushChange.py] 开始执行推送 ---")

    if not result:
        print("[信息] 'result' 参数为 False，跳过推送。")
        return

    # 1. 从环境变量安全地获取 Secrets
    app_token = os.environ.get('APPTOKEN')
    topic_ids_str = os.environ.get('TOPICIDS', '') # 提供默认空值
    uids_str = os.environ.get('UIDS', '')

    if not app_token or (not topic_ids_str and not uids_str):
        print("[错误] APPTOKEN 或 UIDS/TOPICIDS 未在环境中设置。无法推送。")
        return

    # 2. --- 这是最关键的修正：强制将字符串转换为数字列表 ---
    topic_ids_list = []
    if topic_ids_str:
        try:
            # 将 "123,456" 这样的字符串，转换为 [123, 456] 这样的数字列表
            topic_ids_list = [int(tid.strip()) for tid in topic_ids_str.split(',') if tid]
        except ValueError:
            print(f"[错误] TOPICIDS 格式不正确 ('{topic_ids_str}')。应为以逗号分隔的数字。")
            return # 转换失败则直接退出，不再继续

    uids_list = [uid.strip() for uid in uids_str.split(',') if uid]

    # 3. 准备最终发送的 JSON 数据
    url = "https://wxpusher.zjiecode.com/api/send/message"
    json_data = {
        "appToken": app_token,
        "content": content,
        "summary": summary,
        "contentType": 1,
        "topicIds": topic_ids_list, # 确保这里是一个列表
        "uids": uids_list,
    }

    print("[信息] 准备发送给 wxpusher 的最终数据如下:")
    print(json.dumps(json_data, indent=4, ensure_ascii=False))

    # 4. 发送请求并获取响应
    try:
        response = requests.post(url, json=json_data, timeout=15)
        print(f"[信息] wxpusher 服务器响应状态码: {response.status_code}")
        print("[信息] wxpusher 服务器返回内容:")
        # 直接打印服务器返回的 JSON，无论成功或失败
        print(json.dumps(response.json(), indent=4, ensure_ascii=False))
    except requests.exceptions.RequestException as e:
        print(f"[错误] 网络请求失败: {e}")
