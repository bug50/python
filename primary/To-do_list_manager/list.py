# 初始化待办事项列表
# 每个事项是一个字典，包含内容和完成状态
todo_list = []

def show_menu():
    """显示功能菜单"""
    print("\n" + "=" * 40)
    print("📋 待办事项管理器")
    print("=" * 40)
    print("1. 添加待办事项")
    print("2. 查看所有待办")
    print("3. 标记事项完成")
    print("4. 删除待办事项")
    print("5. 退出程序")
    print("=" * 40)

def add_todo():
    """添加待办事项"""
    content = input("请输入待办事项内容：")
    if content.strip() == "":
        print("❌ 事项内容不能为空！")
        return
    
    # 创建待办事项字典
    todo = {
        "content": content,
        "completed": False
    }
    todo_list.append(todo)
    print(f"✅ 已添加待办：{content}")

def show_todos():
    """显示所有待办事项"""
    if len(todo_list) == 0:
        print("📭 暂无待办事项")
        return
    
    print("\n📝 待办事项列表：")
    print("-" * 40)
    # 遍历列表，同时获取索引和内容
    for index, todo in enumerate(todo_list, 1):
        # 根据完成状态显示不同图标
        status = "✅" if todo["completed"] else "⬜"
        print(f"{index}. [{status}] {todo['content']}")
    print("-" * 40)
    # 统计完成情况
    completed = sum(1 for todo in todo_list if todo["completed"])
    print(f"进度：{completed}/{len(todo_list)} 已完成")

def mark_completed():
    """标记事项完成"""
    show_todos()
    if len(todo_list) == 0:
        return
    
    try:
        num = int(input("请输入要标记完成的事项编号："))
        if 1 <= num <= len(todo_list):
            todo_list[num - 1]["completed"] = True
            print(f"✅ 已标记事项 {num} 为完成状态")
        else:
            print("❌ 无效的编号！")
    except ValueError:
        print("❌ 请输入有效的数字！")

def delete_todo():
    """删除待办事项"""
    show_todos()
    if len(todo_list) == 0:
        return
    
    try:
        num = int(input("请输入要删除的事项编号："))
        if 1 <= num <= len(todo_list):
            deleted = todo_list.pop(num - 1)
            print(f"🗑️  已删除：{deleted['content']}")
        else:
            print("❌ 无效的编号！")
    except ValueError:
        print("❌ 请输入有效的数字！")

# 主程序入口
def main():
    while True:
        show_menu()
        choice = input("请选择操作（1-5）：")
        
        if choice == "1":
            add_todo()
        elif choice == "2":
            show_todos()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_todo()
        elif choice == "5":
            print("👋 感谢使用，再见！")
            break
        else:
            print("❌ 无效的选择，请输入1-5之间的数字")

# 运行程序
if __name__ == "__main__":
    main()