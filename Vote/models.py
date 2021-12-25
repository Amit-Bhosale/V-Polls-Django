from django.db import models

# Create your models here.
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="")
    phone=models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, default="")
    password=models.CharField(max_length=50, default="")

    def __str__(self):
        return self.name


class Votes(models.Model):
    vote_id = models.AutoField(primary_key=True)
    quetion=models.TextField()
    creator_name =models.CharField(max_length=50,default='')
    option_one=models.CharField(max_length=50)
    option_two=models.CharField(max_length=50)
    option_three=models.CharField(max_length=50)
    option_four=models.CharField(max_length=50)
    option_one_count=models.IntegerField(default=0)
    option_two_count =models.IntegerField(default=0)
    option_three_count =models.IntegerField(default=0)
    option_four_count =models.IntegerField(default=0)
    date = models.DateField(blank=True,null=True)
    img = models.FileField(upload_to='media',default='media')

    def __str__(self):
        return self.quetion

    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count +self.option_four_count


class Notice(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    head0 = models.CharField(max_length=500, default="")
    chead0 = models.CharField(max_length=5000, default="")
    head1 = models.CharField(max_length=500, default="")
    chead1 = models.CharField(max_length=5000, default="")
    head2 = models.CharField(max_length=500, default="")
    chead2 = models.CharField(max_length=5000, default="")
    pub_date = models.DateField()
    thumbnail = models.ImageField(upload_to='media', default="")

    def __str__(self):
        return self.title