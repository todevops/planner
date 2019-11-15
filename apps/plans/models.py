from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

PRIORITY = (
    (1, '十万火急'),
    (2, '非常重要'),
    (3, '一般重要'),
    (4, '日常任务'),
    (5, '可以暂缓')
)


class Plan(models.Model):
    plan_title = models.CharField(max_length=150, default='Untitled', verbose_name='计划名')
    created_time = models.DateTimeField(auto_now=True, verbose_name='计划创建时间')
    plan_start_time = models.DateTimeField(null=False, verbose_name='计划开始的时间')
    plan_finish_time = models.DateTimeField(null=False, verbose_name='计划完成的时间')
    owner = models.ForeignKey(User, related_name='user_plan', on_delete=models.CASCADE, verbose_name="所有者")
    priority = models.IntegerField(choices=PRIORITY, default=4, verbose_name='优先级')
    is_finish = models.BooleanField(default=False, verbose_name='是否完成')

    def __str__(self):
        return self.plan_title

    class Meta:
        verbose_name = "今日计划"
        verbose_name_plural = verbose_name


class Todo(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='plan_todo', verbose_name='计划名')
    todo_title = models.CharField(max_length=300, null=False, verbose_name='任务清单')
    created_time = models.DateTimeField(auto_now=True, verbose_name='计划创建时间')
    is_done = models.BooleanField(default=False, verbose_name='是否完成')
    owner = models.ForeignKey(User, related_name='user_todo', on_delete=models.CASCADE, verbose_name="所有者")

    def __str__(self):
        return self.todo_title

    class Meta:
        verbose_name = "任务清单"
        verbose_name_plural = verbose_name
