def writeFile(writeFileName, jsonContent,):
    import json
    with open(writeFileName, 'w', encoding='utf-8') as f:
                json.dump(jsonContent, f, ensure_ascii=False, indent=4)
