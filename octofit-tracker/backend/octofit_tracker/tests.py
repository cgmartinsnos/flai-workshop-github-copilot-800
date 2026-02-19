from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout


class UserModelTest(TestCase):
    """Test case for User model."""
    
    def setUp(self):
        self.user = User.objects.create(
            name='Test Hero',
            email='test@hero.com',
            password='testpass123',
            team_id=1
        )
    
    def test_user_creation(self):
        """Test that a user can be created."""
        self.assertEqual(self.user.name, 'Test Hero')
        self.assertEqual(self.user.email, 'test@hero.com')
        self.assertIsNotNone(self.user.created_at)
    
    def test_user_str(self):
        """Test the string representation of User."""
        self.assertEqual(str(self.user), 'Test Hero')


class TeamModelTest(TestCase):
    """Test case for Team model."""
    
    def setUp(self):
        self.team = Team.objects.create(
            name='Test Team',
            description='A test team'
        )
    
    def test_team_creation(self):
        """Test that a team can be created."""
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(self.team.description, 'A test team')
    
    def test_team_str(self):
        """Test the string representation of Team."""
        self.assertEqual(str(self.team), 'Test Team')


class ActivityModelTest(TestCase):
    """Test case for Activity model."""
    
    def setUp(self):
        self.activity = Activity.objects.create(
            user_id=1,
            activity_type='Running',
            duration=30,
            distance=5.0,
            calories=300,
            date=timezone.now()
        )
    
    def test_activity_creation(self):
        """Test that an activity can be created."""
        self.assertEqual(self.activity.activity_type, 'Running')
        self.assertEqual(self.activity.duration, 30)
        self.assertEqual(self.activity.calories, 300)


class UserAPITest(APITestCase):
    """Test case for User API endpoints."""
    
    def test_create_user(self):
        """Test creating a user via API."""
        url = '/api/users/'
        data = {
            'name': 'API Hero',
            'email': 'api@hero.com',
            'password': 'testpass123',
            'team_id': 1
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().name, 'API Hero')
    
    def test_get_users(self):
        """Test retrieving users list via API."""
        User.objects.create(
            name='Hero 1',
            email='hero1@test.com',
            password='pass123',
            team_id=1
        )
        url = '/api/users/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class TeamAPITest(APITestCase):
    """Test case for Team API endpoints."""
    
    def test_create_team(self):
        """Test creating a team via API."""
        url = '/api/teams/'
        data = {
            'name': 'API Team',
            'description': 'Test team via API'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 1)
    
    def test_get_teams(self):
        """Test retrieving teams list via API."""
        Team.objects.create(name='Team 1', description='First team')
        url = '/api/teams/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ActivityAPITest(APITestCase):
    """Test case for Activity API endpoints."""
    
    def test_create_activity(self):
        """Test creating an activity via API."""
        url = '/api/activities/'
        data = {
            'user_id': 1,
            'activity_type': 'Swimming',
            'duration': 45,
            'distance': 2.0,
            'calories': 400,
            'date': timezone.now().isoformat()
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Activity.objects.count(), 1)


class LeaderboardAPITest(APITestCase):
    """Test case for Leaderboard API endpoints."""
    
    def test_create_leaderboard_entry(self):
        """Test creating a leaderboard entry via API."""
        url = '/api/leaderboard/'
        data = {
            'user_id': 1,
            'team_id': 1,
            'total_calories': 1000,
            'total_duration': 100,
            'total_distance': 10.0,
            'rank': 1
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Leaderboard.objects.count(), 1)


class WorkoutAPITest(APITestCase):
    """Test case for Workout API endpoints."""
    
    def test_create_workout(self):
        """Test creating a workout via API."""
        url = '/api/workouts/'
        data = {
            'name': 'Test Workout',
            'description': 'A test workout routine',
            'activity_type': 'Weightlifting',
            'difficulty': 'Medium',
            'duration': 60,
            'calories_per_session': 500
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Workout.objects.count(), 1)
    
    def test_get_workouts(self):
        """Test retrieving workouts list via API."""
        Workout.objects.create(
            name='Workout 1',
            description='First workout',
            activity_type='Running',
            difficulty='Easy',
            duration=30,
            calories_per_session=300
        )
        url = '/api/workouts/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class APIRootTest(APITestCase):
    """Test case for API root endpoint."""
    
    def test_api_root(self):
        """Test that API root returns links to all endpoints."""
        url = '/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)
