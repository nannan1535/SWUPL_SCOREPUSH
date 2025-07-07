def push(result, content="",summary=""):
    import requests
    import secret

    url = "https://wxpusher.zjiecode.com/api/send/message"
    json_data = {
        "appToken":secret.appToken,
        "content": content,
        "summary": summary, 
        "contentType":1,
        "topicIds":secret.topicIds,
        "uids":secret.uids,
        "verifyPay":"false", 
        "verifyPayType":0 }
    if result:
        requests.post(url, json=json_data)