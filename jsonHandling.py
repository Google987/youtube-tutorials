# video link - https://youtu.be/qsI0Ka_tD0Q

import json

json_dic = {
    "name": "a-little-coding", 
    "url": "https://www.youtube.com/c/alittlecoding/videos"
}
# print(json_dic)
# jsonString = json.dumps(json_dic) # string
# print(jsonString)
# print(type(jsonString))


# json_dic = json.loads(jsonString) # python obj
# print(json_dic)

for k in json_dic.keys():
    print(k, json_dic.get(k))
    print(k, json_dic[k])



json_with_single_quote = """{
    'name': "a-little-coding", 
    'url': "https://www.youtube.com/c/alittlecoding/videos"
}"""
print(json_with_single_quote)
# jsonString = json.dumps(json_with_single_quote)
# print(jsonString)

# json_dic = json.loads(json_with_single_quote)
# print(json_dic)


import demjson
json_dic = demjson.decode(json_with_single_quote)
print(json_dic)
print(type(json_dic))


# https://stackoverflow.com/questions/4162642/single-vs-double-quotes-in-json