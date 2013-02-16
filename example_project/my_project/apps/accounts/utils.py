from django.contrib.auth.models import User

def is_username_valid(username):
    user_count = User.objects.filter(username__iexact=username).count()
    return user_count == 0
