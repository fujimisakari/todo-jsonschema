# -*- coding: utf-8 -*-

from django.db import models
from .schema import TodoListSchemaMixin, TodoItemSchemaMixin


class TodoList(TodoListSchemaMixin, models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class TodoItem(TodoItemSchemaMixin, models.Model):
    todo_list = models.ForeignKey(TodoList)
    done = models.BooleanField(default=False)
    text = models.CharField(max_length=100)
