from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    team_id = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'users'
    
    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'teams'
    
    def __str__(self):
        return self.name


class Activity(models.Model):
    user_id = models.IntegerField()
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField(help_text="Duration in minutes")
    distance = models.FloatField(null=True, blank=True, help_text="Distance in km")
    calories = models.IntegerField()
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'activities'
        verbose_name_plural = 'Activities'
    
    def __str__(self):
        return f"{self.activity_type} - {self.duration} mins"


class Leaderboard(models.Model):
    user_id = models.IntegerField()
    team_id = models.IntegerField()
    total_calories = models.IntegerField(default=0)
    total_duration = models.IntegerField(default=0, help_text="Total duration in minutes")
    total_distance = models.FloatField(default=0.0, help_text="Total distance in km")
    rank = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'leaderboard'
    
    def __str__(self):
        return f"User {self.user_id} - Rank {self.rank}"


class Workout(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    activity_type = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    duration = models.IntegerField(help_text="Recommended duration in minutes")
    calories_per_session = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'workouts'
    
    def __str__(self):
        return self.name
