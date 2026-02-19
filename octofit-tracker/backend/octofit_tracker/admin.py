from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'team_id', 'created_at']
    list_filter = ['team_id', 'created_at']
    search_fields = ['name', 'email']
    ordering = ['-created_at']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    search_fields = ['name']
    ordering = ['-created_at']


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'activity_type', 'duration', 'distance', 'calories', 'date']
    list_filter = ['activity_type', 'date']
    search_fields = ['activity_type']
    ordering = ['-date']


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id', 'team_id', 'total_calories', 'total_duration', 'total_distance', 'rank']
    list_filter = ['team_id']
    ordering = ['rank']


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'activity_type', 'difficulty', 'duration', 'calories_per_session']
    list_filter = ['activity_type', 'difficulty']
    search_fields = ['name', 'description']
    ordering = ['name']
