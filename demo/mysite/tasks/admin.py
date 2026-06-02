from django.contrib import admin

# Register your models here.


from .models import Task  # 导入你定义的模型

# 将模型注册到后台
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')  # 可选：指定列表页显示哪些字段