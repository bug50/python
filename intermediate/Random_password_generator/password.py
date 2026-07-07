# 导入随机模块和字符串模块
import random
import string

def generate_password(length=12, use_digits=True, use_uppercase=True, 
                      use_lowercase=True, use_special=True):
    """
    生成随机密码
    参数：
        length: 密码长度，默认12位
        use_digits: 是否包含数字
        use_uppercase: 是否包含大写字母
        use_lowercase: 是否包含小写字母
        use_special: 是否包含特殊字符
    返回：
        生成的密码字符串
    """
    # 构建字符池
    char_pool = ""
    
    # 根据参数添加不同类型的字符
    if use_digits:
        char_pool += string.digits  # '0123456789'
    if use_uppercase:
        char_pool += string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if use_lowercase:
        char_pool += string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
    if use_special:
        char_pool += "!@#$%^&*()_+-=[]{}|;:,.<>?"  # 常用特殊字符
    
    # 检查字符池是否为空
    if len(char_pool) == 0:
        raise ValueError("至少需要选择一种字符类型！")
    
    # 确保密码至少包含每种选中类型的一个字符
    password_chars = []
    
    if use_digits:
        password_chars.append(random.choice(string.digits))
    if use_uppercase:
        password_chars.append(random.choice(string.ascii_uppercase))
    if use_lowercase:
        password_chars.append(random.choice(string.ascii_lowercase))
    if use_special:
        password_chars.append(random.choice("!@#$%^&*()_+-=[]{}|;:,.<>?"))
    
    # 计算还需要补充的字符数量
    remaining_length = length - len(password_chars)
    
    # 从字符池中随机选择剩余字符
    for _ in range(remaining_length):
        password_chars.append(random.choice(char_pool))
    
    # 打乱密码字符顺序（重要！否则前面的字符类型固定）
    random.shuffle(password_chars)
    
    # 将字符列表转换为字符串
    return ''.join(password_chars)

def get_user_settings():
    """获取用户的密码生成设置"""
    print("\n⚙️  密码生成设置")
    print("-" * 40)
    
    # 获取密码长度
    while True:
        try:
            length = int(input("请输入密码长度（推荐8-32）："))
            if 4 <= length <= 128:
                break
            else:
                print("❌ 密码长度请在4-128之间")
        except ValueError:
            print("❌ 请输入有效的数字")
    
    # 获取各选项设置
    def get_yes_no(prompt):
        """辅助函数：获取是/否选择"""
        while True:
            choice = input(prompt).strip().lower()
            if choice in ['y', 'yes', '']:
                return True
            elif choice in ['n', 'no']:
                return False
            else:
                print("❌ 请输入 y 或 n")
    
    use_digits = get_yes_no("包含数字？(Y/n，默认是)：")
    use_uppercase = get_yes_no("包含大写字母？(Y/n，默认是)：")
    use_lowercase = get_yes_no("包含小写字母？(Y/n，默认是)：")
    use_special = get_yes_no("包含特殊符号？(Y/n，默认是)：")
    
    # 获取生成数量
    while True:
        try:
            count = int(input("生成几个密码？（默认1）：") or 1)
            if 1 <= count <= 50:
                break
            else:
                print("❌ 数量请在1-50之间")
        except ValueError:
            print("❌ 请输入有效的数字")
    
    return length, use_digits, use_uppercase, use_lowercase, use_special, count

def calculate_strength(password):
    """计算密码强度"""
    score = 0
    length = len(password)
    
    # 长度评分
    if length >= 16:
        score += 30
    elif length >= 12:
        score += 20
    elif length >= 8:
        score += 10
    
    # 字符多样性评分
    has_digit = any(c.isdigit() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_special = any(not c.isalnum() for c in password)
    
    score += sum([has_digit, has_upper, has_lower, has_special]) * 17.5
    
    # 强度等级
    if score >= 80:
        return "🔒 非常强", score
    elif score >= 60:
        return "🔐 强", score
    elif score >= 40:
        return "⚠️  中等", score
    else:
        return "❌ 弱", score

def main():
    """主程序"""
    print("=" * 50)
    print("🔐 随机密码生成器")
    print("=" * 50)
    
    while True:
        # 获取用户设置
        settings = get_user_settings()
        length, use_digits, use_uppercase, use_lowercase, use_special, count = settings
        
        # 生成密码
        print("\n🎯 生成的密码：")
        print("-" * 50)
        
        for i in range(count):
            try:
                password = generate_password(
                    length=length,
                    use_digits=use_digits,
                    use_uppercase=use_uppercase,
                    use_lowercase=use_lowercase,
                    use_special=use_special
                )
                strength, score = calculate_strength(password)
                print(f"{i+1:2d}. {password:{length}s} | {strength} ({score:.0f}分)")
            except ValueError as e:
                print(f"❌ 错误：{e}")
                break
        
        print("-" * 50)
        
        # 询问是否继续
        again = input("\n是否继续生成？(Y/n)：").strip().lower()
        if again in ['n', 'no']:
            print("\n👋 再见！记得保管好你的密码~")
            break

if __name__ == "__main__":
    main()