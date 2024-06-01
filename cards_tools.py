card_list = []
def show_menu():
    print("*"*50)
    print("欢迎使用 【名片管理系统】 V1.0")
    print("")
    print("1. 新建名片")
    print("2. 显示全部")
    print("3. 查询名片")
    print("")
    print("0. 退出系统")
    print("*"*50)

def new_card():
    """新建名片"""
    print("新建名片")
    print("-"*50)

    # 1.提示用户输入名片的详细信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入QQ：")
    email_str = input("请输入邮箱：")

    # 2.使用用户输入的名片信息建立一个字典
    card_dict = {"name":name_str,
                 "phone":phone_str,
                 "qq":qq_str,
                  "email":email_str}

    # 3.将名片添加都列表中
    card_list.append(card_dict)

    # 4.提示用户添加成功
    print("添加 %s 的名片成功！" % name_str)

def show_all():
    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")

    if len(card_list) == 0:
        print("当前没有任何的名片记录，请使用新增功能添加名片！")
        return
    for name in ["姓名","电话","QQ","邮箱"]:
        print(name,end="\t\t")
    print("")
    print("="*50)
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["email"]))
    print("="*50)

def search_card():
    """搜索名片"""
    print("-" * 50)
    print("搜索名片")
    find_name = input("请输入要搜索的姓名：")

    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("="*50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))
            # TODO 针对找到的名片记录执行修改和删除的操作
            deal_card(card_dict)
            break

        else:
            print("抱歉,没有找到%r"%find_name)


def deal_card(find_dict):
    """处理查找到的名片

    :param find_dict: 查找到的名片    
    :return:
    """
    print(find_dict)
    action_str=input("请选择要执行的操作"
                     "（1.修改 2.删除 0.返回上一级）：")
    if action_str == "1":
        print("修改名片")

        find_dict["name"] = input_card_info(find_dict["name"],"姓名：")
        find_dict["phone"] = input_card_info(find_dict["phone"],"电话：")
        find_dict["qq"] = input_card_info(find_dict["qq"],"QQ：")
        find_dict["email"] = input_card_info(find_dict["email"] ,"邮箱：")

        print("修改成功")
    elif action_str == "2":
        print("删除名片")
        card_list.remove(find_dict)
        print("删除名片成功！")
    elif action_str == "0":
        print("返回上一级")

def input_card_info(dict_value,tip_message):
    """

    :param dict_value: 字典中原有的值
    :param tip_message: 输入的提示文字
    :return: 如果输入了内容，就返回内容，否则返回字典中原有的值
    """
    result_str = input(tip_message)
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value