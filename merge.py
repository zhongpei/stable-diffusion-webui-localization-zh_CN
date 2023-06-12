import json


def json2dict(json_file):
    with open(json_file, 'r') as f:
        return json.load(f)


def dict2json(dict_data, json_file):
    with open(json_file, 'w+') as f:
        json.dump(dict_data, f, indent=4, ensure_ascii=False)


def merge_dict(dict1, dict2):
    return dict1.update(dict2)


def merge_json(json_file1, json_file2):
    dict1 = json2dict(json_file1)

    dict2 = json2dict(json_file2)
    print(f"{json_file1} len: {len(dict1)}")
    print(f"{json_file2} len: {len(dict2)}")
    merge_dict(dict1, dict2)
    print(f"merge len: {len(dict1)}")
    return dict1


if __name__ == '__main__':
    json_file1 = './localizations/zh_CN.json'
    json_file2 = './stable-diffusion-webui-localization-zh_Hans/localizations/zh-Hans (Stable).json'
    data = merge_json(json_file1, json_file2)
    dict2json(data, "./localizations/zh_CN_merge.json")
