from django.db import migrations

def create_groups_and_permissions(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    # Создаем группы
    user_group, _ = Group.objects.get_or_create(name='User')
    manager_group, _ = Group.objects.get_or_create(name='Manager')

    # Пример: добавим менеджерам право изменять модель Message (замени 'mail_messages' и 'message' на свои app и model)
    permission = Permission.objects.filter(codename='change_message').first()
    if permission:
        manager_group.permissions.add(permission)

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),  # замени на актуальную миграцию после которой хочешь делать эту
        ('auth', '0012_alter_user_first_name_max_length'),  # актуальная зависимость auth
    ]

    operations = [
        migrations.RunPython(create_groups_and_permissions),
    ]
