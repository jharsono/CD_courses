from __future__ import unicode_literals

from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors["name"] = "Course name should be more than 5 characters"
        if len(postData['desc']) < 15:
            errors["desc"] = "Course desc should be more than 15 characters"
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # *************************
    # Connect an instance of BlogManager to our Blog model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    objects = CourseManager()
    # **********************

    def __unicode__(self):
        return "Name: " + self.name + ", Desc: " + self.desc + ", Date Added: "\
        + str(self.created_at)
