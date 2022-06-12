


from django.db import models

class Credentials(models.Model):
    userid= models.CharField(max_length=100,primary_key=True,null=False)
    username=models.CharField(max_length=1000,null=False)
    password=models.CharField(max_length=150,null=False)
    role=models.IntegerField(null=False)
    email=models.CharField(max_length=1000)
    login_status=models.BooleanField(null=False)


class Teams(models.Model):
    teamid=models.CharField(max_length=100,primary_key=True,null=False)
    teamname=models.CharField(max_length=1000,null=False)
    coachid=models.OneToOneField(Credentials,on_delete=models.CASCADE)

class Player(models.Model):
    playerid=models.OneToOneField(Credentials,on_delete=models.CASCADE,primary_key=True,null=False)
    teamid=models.OneToOneField(Teams,on_delete=models.CASCADE)
    playername=models.CharField(max_length=100,null=False)


