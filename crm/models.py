from django.db import models

# Create your models here.


class Customer(models.Model):
    pass


class Enrollment(models.Model):
    """学员报名信息"""



class FollowUpRecord(models.Model):
    pass


class Course(models.Model):
    pass


class ClassList(models.Model):
    pass


class CourseRecord(models.Model):
    """每节课上课记录"""
    pass


class StudyRecord(models.Model):
    """每个学生上的每节课的成绩记录"""
    pass



