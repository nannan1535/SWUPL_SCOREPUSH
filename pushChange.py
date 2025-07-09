
def push(result, content="",summary=""):
    import requests
    # import secret
    import os
    url = "https://wxpusher.zjiecode.com/api/send/message"

    app_token = os.environ.get('APPTOKEN')
    topic_ids_github = os.environ.get('TOPICIDS')
    uids_github = os.environ.get('UIDS')
    #转换
    topic_ids_str = [int(tid) for tid in topic_ids_github.split(',')] if topic_ids_github else []
    uids_str = uids_github.split(',') if uids_github else []


    # app_token = secret.appToken
    # topic_ids_str = secret.topicIds
    # uids_str = secret.uids

    json_data = {
        "appToken":app_token,
        "content": content,
        "summary": summary, 
        "contentType":1,
        "topicIds":topic_ids_str,
        "uids":uids_str,
        "verifyPay":"false", 
        "verifyPayType":0 
        }
    if result:
        response  = requests.post(url, json=json_data)
        response_data = response.json()
        print("Wxpusher是否请求成功",response_data.get('success'), "Wxpusher返回内容",response_data.get('msg'))
        print("请以是否受到通知为准")


