from django.core.management.base import BaseCommand, CommandError
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission

class Command(BaseCommand):
    help = 'Usage: manage.py createpermission app.Model name "description"'
    def handle(self, *info, **options):
        if len(info) != 3:
            raise CommandError('You must specify the app, model, name, and '
                'description')

        app_model = info[0]
        name = info[1]
        description = info[2]

        (app, model) = app_model.split('.')
        model = model.lower()

        ct = ContentType.objects.get_or_create(app_label=app, model=model)[0]
        ct.save()

        permission = Permission.objects.get_or_create(name=description,
            content_type=ct, codename=name)[0]
        permission.save()

        print 'Permission "{0}" has been created succesfully'.\
            format(permission)
