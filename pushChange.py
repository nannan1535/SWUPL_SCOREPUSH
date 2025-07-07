# pushChange.py (终极调试版)

import requests
import os
import json

def push(result, content="", summary=""):
    print("\n--- [pushChange.py] '黑匣子'开始记录推送过程 ---")

    if not result:
        print("[黑匣子记录] 'result' 参数为 False，跳过推送。")
        return

    # 1. 验证从环境变量中获取到的 Secrets
    app_token = os.environ.get('APPTOKEN')
    topic_ids_str = os.environ.get('TOPICIDS', '') # 提供默认空值
    uids_str = os.environ.get('UIDS', '')

    print(f"[黑匣子记录] 获取到的 APPTOKEN 长度为: {len(app_token) if app_token else 0}")
    print(f"[黑匣子记录] 获取到的 TOPICIDS 字符串为: '{topic_ids_str}'")
    print(f"[黑匣子记录] 获取到的 UIDS 字符串为: '{uids_str}'")

    if not app_token or (not topic_ids_str and not uids_str):
        print("[黑匣子记录] 致命错误：APPTOKEN 或 UIDS/TOPICIDS 未在环境中设置。无法推送。")
        return


    url = "https://wxpusher.zjiecode.com/api/send/message"
    json_data = {
        "appToken": app_token,
        "content": content,
        "summary": summary,
        "contentType": 1,
        "topicIds": topic_ids_str,
        "uids": uids_str,
    }

    print("[黑匣子记录] 准备发送给 wxpusher 的最终 JSON 数据如下:")
    # 使用 json.dumps 打印格式化的 JSON，方便查看
    print(json.dumps(json_data, indent=4, ensure_ascii=False))

    # 3. 发送请求并记录服务器的详细响应
    try:
        print("[黑匣子记录] 正在发送 POST 请求...")
        response = requests.post(url, json=json_data, timeout=15)

        print(f"[黑匣子记录] wxpusher 服务器响应状态码: {response.status_code}")
        print("--- [黑匣子记录] wxpusher 服务器返回的原始响应内容如下: ---")
        # 尝试以 JSON 格式打印，如果失败则打印原始文本
        try:
            print(json.dumps(response.json(), indent=4, ensure_ascii=False))
        except json.JSONDecodeError:
            print(response.text)
        print("--- [黑匣子记录] 原始响应内容结束 ---")

    except requests.exceptions.RequestException as e:
        print(f"[黑匣子记录] 致命网络错误: {e}")

    print("--- [pushChange.py] '黑匣子'记录结束 ---\n")
