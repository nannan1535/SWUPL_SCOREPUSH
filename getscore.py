import os
import requests
def get_score():
    url = "https://njwxt.swupl.edu.cn/jwglxt/cjcx/cjcx_cxDgXscj.html?doType=query&gnmkdm=N305005"
    headers = {
        "Accept": 'application/json, text/javascript, */*; q=0.01',
        "Accept-Encoding": 'gzip, deflate, br, zstd',
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Content-Length": "149",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Cookie": os.environ.get('COOKIE'),
        "Host": "njwxt.swupl.edu.cn",
        "Origin": "https://njwxt.swupl.edu.cn",
        "Referer": "https://njwxt.swupl.edu.cn/jwglxt/cjcx/cjcx_cxDgXsxmcj.html?gnmkdm=N305007&layout=default",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Windows"
    }

    response = requests.post(url, headers=headers, data={
        "xnm": os.environ.get('XNM'),
        "xqm": os.environ.get('XQM'),
        "queryModel.showCount": "100",}
    )
    data = response.json()
    if not data print("不正常")
    return data
