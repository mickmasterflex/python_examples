from django.core.management.base import BaseCommand, CommandError
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
    cd_admin = (
        'accounts.UserProfile', 'cd_admin',
        'Content Domain Administrator Permissions',
        )
    pi_admin = (
        'accounts.UserProfile', 'pi_admin',
        'Platform Instance Administrator Permissions',
    )
    ses_staff = (
        'accounts.UserProfile', 'ses_staff',
        'Speak Easy Spot Staff Permissions',
    )
    ses_admin = (
        'accounts.UserProfile', 'ses_admin',
        'Speak Easy Spot Administrator Permissions',
    )

    perms = {}

    groups = (
            ('Speak Easy Spot Administrators', (ses_admin, ses_staff,
                                                pi_admin, cd_admin, user)),
            ('Speak Easy Spot Staff', (ses_staff, pi_admin, cd_admin,
                                                user)),
            ('Platform Instance Administrators', (pi_admin, cd_admin, user)),
            ('Content Domain Administrators', (cd_admin, user)),
            ('Registered Users', (user),
    )

    for item in (ses_admin, ses_staff, pi_admin, cd_admin, user):
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
            'ses_admin': perms[ses_admin],
            'ses_staff': perms[ses_staff],
            'pi_admin': perms[pi_admin],
            'cd_admin': perms[cd_admin],
            'user': perms[user],
    }
