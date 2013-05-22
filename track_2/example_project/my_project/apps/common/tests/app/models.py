from django.db import models

from common import models as common_models

class TestModel(models.Model):
    """
        A simple test model to be used by tests
    """
    name = models.CharField(max_length=200)

class TestHierarchyModel(models.Model):
    """
    A so-damn easy model that is in a hierarchy.
    """
    name = models.CharField(max_length=200)
    parent = models.ForeignKey("TestHierarchyModel", null=True, blank=True)

    def __unicode__(self):
        return unicode(self.name)

class TestHierarchyClosureModel(common_models.BaseClosureModel):
    """
    A very efficient and concise model that is a closure model for
    TestHierarchyModel.
    """
    closure_for = TestHierarchyModel

