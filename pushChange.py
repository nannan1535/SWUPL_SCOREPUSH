def push(result, content="",summary=""):
    import requests
    import os
    url = "https://wxpusher.zjiecode.com/api/send/message"
    app_token = os.environ.get('APPTOKEN')
    topic_ids_str = os.environ.get('TOPICIDS')
    uids_str = os.environ.get('UIDS')
    json_data = {
        "appToken":app_token,
        "content": content,
        "summary": summary, 
        "contentType":1,
        "topicIds":topic_ids_str,
        "uids":uids_str,
        "verifyPay":"false", 
        "verifyPayType":0 }
    if result:
        requests.post(url, json=json_data)
