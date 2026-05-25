# 导入随机数模块
import random

# 生成1-100之间的随机整数作为答案
secret_number = random.randint(1, 100)

# 初始化猜测次数计数器
guess_count = 0

# 打印游戏欢迎信息
print("=" * 40)
print("欢迎来到猜数字游戏！")
print("我已经想好了一个1-100之间的数字，你来猜猜看吧！")
print("=" * 40)

# 游戏主循环
while True:
    # 获取用户输入并转换为整数
    user_input = input("\n请输入你猜的数字：")
    
    # 增加猜测次数
    guess_count += 1
    
    # 将用户输入转换为整数
    try:
        guess = int(user_input)
    except ValueError:
        print("❌ 请输入有效的数字！")
        continue
    
    # 判断猜测结果
    if guess < secret_number:
        print("📉 太小了，再大一点！")
    elif guess > secret_number:
        print("📈 太大了，再小一点！")
    else:
        # 猜对了，结束游戏
        print(f"\n🎉 恭喜你猜对了！答案就是 {secret_number}")
        print(f"🏆 你一共猜了 {guess_count} 次")
        
        # 根据猜测次数给出评价
        if guess_count <= 5:
            print("🌟 太厉害了！你是天才吗？")
        elif guess_count <= 10:
            print("👍 不错哦，表现很好！")
        else:
            print("💪 继续加油，多练习会更好！")
        break