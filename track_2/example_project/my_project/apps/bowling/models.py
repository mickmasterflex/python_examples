from __future__ import unicode_literals

from django.db import models

from accounts import models as accounts_models

class Score(models.Model):
    """
    The class stores info about the user's score.
    """
    
    # Corresponds to the user that owns this profile.
    user = models.ForeignKey(accounts_models.User, unique=True)
    score = models.IntegerField(length=3, null=True)

    def __unicode__(self):
        if self.user.first_name:
            if self.user.last_name:
                return '{0} {1}\'s Score'.format(self.user.first_name,
                                                   self.user.last_name)
            else:
                return '{0}\'s Score'.format(self.user.first_name)
        else:
            return '{0}\'s Score'.format(self.user.username)
