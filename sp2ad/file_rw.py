import json


def writejson(a_dict):
    # json_str = json.dumps(a_dict)
    with open('data.json', 'w') as json_file:
        # print(type(a_dict))
        json.dump(a_dict, json_file)
        # print(a_dict)


def readjson(path):
    with open("data.json", 'r') as load_f:
        load_dict = json.load(load_f)
        return load_dict
        # print(load_dict)


if __name__ == '__main__':
    a_dict = {"time": 1534836232.4316688, "key": "https://media3.99kk44.com/remote_control.php?time=1534838843&cv=732a789eb839ea759f69977cfb1a138d&lr=0&cv2=e62e99547cfca3dc3c8f6d8eae295182&file=/videos/%s/%s/%s.mp4"}
    writejson(a_dict)
    print(readjson('data.json')["key"])
