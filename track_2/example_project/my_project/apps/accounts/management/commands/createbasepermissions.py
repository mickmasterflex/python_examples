from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission, Group

class Command(BaseCommand):
    help = "Usage: manage.py createbasepermissions"
    def handle(self, *info, **options):
        _create_base_perms()

def _create_base_perms():
    user = (
        'accounts.UserProfile', 'user', 'Registered User Permissions',
    )
    admin = (
        'accounts.UserProfile', 'admin',
        'Administrator Permissions',
        )
    staff = (
        'accounts.UserProfile', 'staff',
        'Staff Permissions',
    )

    perms = {}

    groups = (
            ('Administrators', (admin, staff, user)),
            ('Staff', (staff, user)),
            ('Registered Users', (user),
    )

    for item in (admin, staff, user):
        (app_model, name, description) = item
        (app, model) = app_model.split('.')
        model = model.lower()

        ct = ContentType.objects.get_or_create(app_label=app, model=model)[0]
        ct.save()

        permission = Permission.objects.get_or_create(
            name=description, content_type=ct, codename=name)[0]
        permission.save()

        perms[item] = permission

    for item in groups:
        (name, groupperms) = item

        group = Group.objects.get_or_create(name=name)[0]
        group.save()
        [group.permissions.add(perms[p]) for p in groupperms]

    return {
            'admin': perms[admin],
            'staff': perms[staff],
            'user': perms[user],
    }
