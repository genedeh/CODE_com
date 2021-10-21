import uuid

from django.db import models
from users.models import User


# Create your models here.

class Code(models.Model):
    code_file = models.FileField(upload_to='static/')
    commit = models.TextField(max_length=750, unique=True)
    commit_code = models.UUIDField(blank=True, default=uuid.uuid4())

    def __str__(self):
        return f'{self.code_file}'


class CodeBase(models.Model):
    name = models.CharField(max_length=120)
    code = models.ManyToManyField(Code)

    def __str__(self):
        return f'{self.name}'


class Projects(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=140, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    codebase = models.ManyToManyField(CodeBase)
    slug = models.SlugField(default='')

    def __str__(self):
        return f'{self.name}'
