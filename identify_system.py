from pick import pick
import re

result = ""
selected = []
all_feature = []

def loadDB(filename):
    dictionary = {}
    all = []
    global all_feature
    with open(filename, 'r') as f:
        for line in f.readlines():
            if line[0] == "#":
                continue
            # 产生式应该长这样：<编号>：IF <条件1> [& <条件2>...] -> <结论>
            num = line.split("IF")[0].strip()
            tmp = re.findall(r'IF(.*?)->', line.replace(" ", ""))[0]
            conditions = tmp.split("&")
            all.extend(conditions)
            conclusion = line.split("->")[1].strip()
            dictionary[conclusion] = conditions
            # print(num, conditions, conclusion)
    all_feature = list(set(all))
    # print(all_feature)
    return dictionary



def IS(text, current_dict):
    ans = {}
    for key, value in current_dict.items():
        if text in value:
            ans[key] = value
    return ans


def main():
    dictionary = loadDB("db.txt")

    title = "请选择全部条件。"
    temp = pick(all_feature, title, multiselect=True, min_selection_count=1)
    selected.extend(i[0] for i in temp)

    for i in selected:
        dictionary = IS(i, dictionary)
    # print(dictionary)

    if len(dictionary) == 0:
        print("没有通过条件找到您的结论")
    elif len(dictionary) == 1:
        print(f"您输入的条件找到的结论是：{list(dictionary.keys())[0]}！")
    elif len(dictionary) > 1:
        print(f"您提供的条件对应数条结论，第一条是：{list(dictionary.keys())[0]}！")


if __name__ == "__main__":
    main()
