from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    gender= models.CharField(max_length=30)
    address= models.CharField(max_length=30)


class predict_online_student_judgement(models.Model):

    Fid= models.CharField(max_length=300)
    age= models.CharField(max_length=300)
    gender= models.CharField(max_length=300)
    lunch= models.CharField(max_length=300)
    parental_level_of_education= models.CharField(max_length=300)
    degree_t= models.CharField(max_length=300)
    race_ethnicity= models.CharField(max_length=300)
    test_preparation_course= models.CharField(max_length=300)
    math_score= models.CharField(max_length=300)
    reading_score= models.CharField(max_length=300)
    writing_score= models.CharField(max_length=300)
    Internships= models.CharField(max_length=300)
    solving_tasks_by_time= models.CharField(max_length=300)
    taks_submitted_on_date= models.CharField(max_length=300)
    Prediction= models.CharField(max_length=300)

class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



