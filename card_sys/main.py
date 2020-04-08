import tools
while True:
    tools.show_menu()
    action_str = input("请输入您需要的操作：")
    if action_str == "1":
        print("添加名片")
        pass               # TODO 添加名片的具体
    elif action_str == "2":
        print("所有名片")
        pass               # TODO 显示所有名片
    elif action_str == "3":
        print("修改名片")   # TODO 修改名片
        pass
    else:
        print("输入有误，请重新选择！")