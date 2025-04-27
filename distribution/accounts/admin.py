from django.contrib.auth.models import Group

# Создание групп для пользователей
user_group, created = Group.objects.get_or_create(name='User')
manager_group, created = Group.objects.get_or_create(name='Manager')


