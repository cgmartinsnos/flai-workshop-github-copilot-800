from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import (
    UserSerializer,
    TeamSerializer,
    ActivitySerializer,
    LeaderboardSerializer,
    WorkoutSerializer
)


@api_view(['GET'])
def api_root(request, format=None):
    """
    API root endpoint that provides links to all available endpoints.
    """
    return Response({
        'users': request.build_absolute_uri('/api/users/'),
        'teams': request.build_absolute_uri('/api/teams/'),
        'activities': request.build_absolute_uri('/api/activities/'),
        'leaderboard': request.build_absolute_uri('/api/leaderboard/'),
        'workouts': request.build_absolute_uri('/api/workouts/'),
    })


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for users.
    
    Supports:
    - GET /api/users/ - List all users
    - POST /api/users/ - Create a new user
    - GET /api/users/{id}/ - Retrieve a specific user
    - PUT /api/users/{id}/ - Update a specific user
    - DELETE /api/users/{id}/ - Delete a specific user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint for teams.
    
    Supports:
    - GET /api/teams/ - List all teams
    - POST /api/teams/ - Create a new team
    - GET /api/teams/{id}/ - Retrieve a specific team
    - PUT /api/teams/{id}/ - Update a specific team
    - DELETE /api/teams/{id}/ - Delete a specific team
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    """
    API endpoint for activities.
    
    Supports:
    - GET /api/activities/ - List all activities
    - POST /api/activities/ - Create a new activity
    - GET /api/activities/{id}/ - Retrieve a specific activity
    - PUT /api/activities/{id}/ - Update a specific activity
    - DELETE /api/activities/{id}/ - Delete a specific activity
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class LeaderboardViewSet(viewsets.ModelViewSet):
    """
    API endpoint for leaderboard.
    
    Supports:
    - GET /api/leaderboard/ - List all leaderboard entries
    - POST /api/leaderboard/ - Create a new leaderboard entry
    - GET /api/leaderboard/{id}/ - Retrieve a specific leaderboard entry
    - PUT /api/leaderboard/{id}/ - Update a specific leaderboard entry
    - DELETE /api/leaderboard/{id}/ - Delete a specific leaderboard entry
    """
    queryset = Leaderboard.objects.all().order_by('rank')
    serializer_class = LeaderboardSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    """
    API endpoint for workouts.
    
    Supports:
    - GET /api/workouts/ - List all workouts
    - POST /api/workouts/ - Create a new workout
    - GET /api/workouts/{id}/ - Retrieve a specific workout
    - PUT /api/workouts/{id}/ - Update a specific workout
    - DELETE /api/workouts/{id}/ - Delete a specific workout
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
