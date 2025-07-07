# getscore.py (黑匣子调试版)

import json
import requests
import os

def get_score():
    print("--- [get_score.py] '黑匣子'开始记录 ---")
    
    # 1. 验证从环境中获取到的 Cookie
    cookie_from_env = os.environ.get('COOKIE')
    if not cookie_from_env:
        print("[黑匣子记录] 致命错误：没有从环境变量中获取到 COOKIE。")
        return None # 直接返回空值
    
    print(f"[黑匣子记录] 已获取到 COOKIE，长度为: {len(cookie_from_env)}。")
    
    # 2. 准备请求
    url = "https://njwxt.swupl.edu.cn/jwglxt/cjcx/cjcx_cxDgXscj.html?doType=query&gnmkdm=N305005"
    headers = {
        "Accept": 'application/json, text/javascript, */*; q=0.01',
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Cookie": cookie_from_env, # 使用从环境中获取的 Cookie
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
        "X-Requested-With": "XMLHttpRequest",
    }
    payload = {
        "xnm": os.environ.get('XNM'),
        "xqm": os.environ.get('XQM'),
        "queryModel.showCount": "100",
    }
    
    print(f"[黑匣子记录] 准备向URL发送POST请求: {url}")

    # 3. 发送请求并记录一切
    try:
        response = requests.post(url, headers=headers, data=payload, timeout=15)
        
        # 记录服务器返回的 HTTP 状态码
        print(f"[黑匣子记录] 服务器响应状态码: {response.status_code}")
        
        # 记录服务器返回的原始文本内容（无论是什么）
        print("--- [黑匣子记录] 服务器返回的原始响应内容如下: ---")
        print(response.text)
        print("--- [黑匣子记录] 原始响应内容结束 ---")

        # 尝试将返回内容解析为 JSON
        # 如果服务器返回的是登录页的HTML，这里会报错，但我们能从上面的打印中看到HTML内容
        return response.json()

    except json.JSONDecodeError:
        print("[黑匣子记录] 致命错误：服务器返回的内容不是有效的JSON格式。很可能是一个HTML登录页面，表示Cookie已失效。")
        return None # 返回空值，让主程序知道出错了
    except requests.exceptions.RequestException as e:
        # 记录所有网络相关的错误
        print(f"[黑匣子记录] 致命网络错误: {e}")
        return None
