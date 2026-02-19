from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import datetime, timedelta
import random
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Clearing existing data...'))
        
        # Delete existing data using Django ORM
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        
        self.stdout.write(self.style.SUCCESS('Existing data cleared.'))
        self.stdout.write(self.style.WARNING('Inserting test data...'))
        
        # Create Teams
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Assemble! The mightiest heroes of the Marvel Universe',
            created_at=timezone.now()
        )
        
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League - Defending truth and justice',
            created_at=timezone.now()
        )
        
        self.stdout.write(self.style.SUCCESS(f'Created teams: {team_marvel.name}, {team_dc.name}'))
        
        # Create Marvel Users
        marvel_heroes = [
            {'name': 'Tony Stark', 'email': 'ironman@marvel.com'},
            {'name': 'Steve Rogers', 'email': 'captainamerica@marvel.com'},
            {'name': 'Thor Odinson', 'email': 'thor@marvel.com'},
            {'name': 'Natasha Romanoff', 'email': 'blackwidow@marvel.com'},
            {'name': 'Bruce Banner', 'email': 'hulk@marvel.com'},
            {'name': 'Peter Parker', 'email': 'spiderman@marvel.com'},
        ]
        
        # Create DC Users
        dc_heroes = [
            {'name': 'Clark Kent', 'email': 'superman@dc.com'},
            {'name': 'Bruce Wayne', 'email': 'batman@dc.com'},
            {'name': 'Diana Prince', 'email': 'wonderwoman@dc.com'},
            {'name': 'Barry Allen', 'email': 'flash@dc.com'},
            {'name': 'Arthur Curry', 'email': 'aquaman@dc.com'},
            {'name': 'Hal Jordan', 'email': 'greenlantern@dc.com'},
        ]
        
        marvel_users = []
        for hero in marvel_heroes:
            user = User.objects.create(
                name=hero['name'],
                email=hero['email'],
                password='password123',
                team_id=team_marvel.id,
                created_at=timezone.now()
            )
            marvel_users.append(user)
        
        dc_users = []
        for hero in dc_heroes:
            user = User.objects.create(
                name=hero['name'],
                email=hero['email'],
                password='password123',
                team_id=team_dc.id,
                created_at=timezone.now()
            )
            dc_users.append(user)
        
        all_users = marvel_users + dc_users
        self.stdout.write(self.style.SUCCESS(f'Created {len(all_users)} superhero users'))
        
        # Create Activities
        activity_types = ['Running', 'Cycling', 'Swimming', 'Weightlifting', 'Yoga', 'Boxing']
        activities_created = 0
        
        for user in all_users:
            # Create 5-10 random activities for each user
            num_activities = random.randint(5, 10)
            for _ in range(num_activities):
                activity_type = random.choice(activity_types)
                duration = random.randint(15, 120)
                distance = round(random.uniform(1.0, 20.0), 2) if activity_type in ['Running', 'Cycling', 'Swimming'] else None
                calories = duration * random.randint(5, 15)
                days_ago = random.randint(0, 30)
                
                Activity.objects.create(
                    user_id=user.id,
                    activity_type=activity_type,
                    duration=duration,
                    distance=distance,
                    calories=calories,
                    date=timezone.now() - timedelta(days=days_ago),
                    created_at=timezone.now()
                )
                activities_created += 1
        
        self.stdout.write(self.style.SUCCESS(f'Created {activities_created} activities'))
        
        # Create Leaderboard entries
        leaderboard_entries = 0
        for user in all_users:
            user_activities = Activity.objects.filter(user_id=user.id)
            total_calories = sum(a.calories for a in user_activities)
            total_duration = sum(a.duration for a in user_activities)
            total_distance = sum(a.distance for a in user_activities if a.distance)
            
            Leaderboard.objects.create(
                user_id=user.id,
                team_id=user.team_id,
                total_calories=total_calories,
                total_duration=total_duration,
                total_distance=round(total_distance, 2),
                rank=0,  # Will be calculated later
                updated_at=timezone.now()
            )
            leaderboard_entries += 1
        
        # Update ranks based on total_calories
        leaderboard = Leaderboard.objects.all().order_by('-total_calories')
        for rank, entry in enumerate(leaderboard, start=1):
            entry.rank = rank
            entry.save()
        
        self.stdout.write(self.style.SUCCESS(f'Created {leaderboard_entries} leaderboard entries'))
        
        # Create Workouts
        workouts_data = [
            {
                'name': 'Super Soldier Training',
                'description': 'High-intensity training inspired by Captain America',
                'activity_type': 'Weightlifting',
                'difficulty': 'Hard',
                'duration': 60,
                'calories_per_session': 600
            },
            {
                'name': 'Speedster Sprint',
                'description': 'Lightning-fast running workout inspired by The Flash',
                'activity_type': 'Running',
                'difficulty': 'Medium',
                'duration': 30,
                'calories_per_session': 400
            },
            {
                'name': 'Amazonian Warrior Workout',
                'description': 'Combat training inspired by Wonder Woman',
                'activity_type': 'Boxing',
                'difficulty': 'Hard',
                'duration': 45,
                'calories_per_session': 550
            },
            {
                'name': 'Asgardian Strength',
                'description': 'Mythical strength training inspired by Thor',
                'activity_type': 'Weightlifting',
                'difficulty': 'Hard',
                'duration': 90,
                'calories_per_session': 800
            },
            {
                'name': 'Web-Slinger Agility',
                'description': 'Flexibility and agility workout inspired by Spider-Man',
                'activity_type': 'Yoga',
                'difficulty': 'Easy',
                'duration': 45,
                'calories_per_session': 300
            },
            {
                'name': 'Atlantean Swimming',
                'description': 'Aquatic conditioning inspired by Aquaman',
                'activity_type': 'Swimming',
                'difficulty': 'Medium',
                'duration': 60,
                'calories_per_session': 500
            },
            {
                'name': 'Dark Knight Cycling',
                'description': 'Endurance cycling inspired by Batman',
                'activity_type': 'Cycling',
                'difficulty': 'Medium',
                'duration': 75,
                'calories_per_session': 650
            },
            {
                'name': 'Kryptonian Power',
                'description': 'Maximum strength training inspired by Superman',
                'activity_type': 'Weightlifting',
                'difficulty': 'Hard',
                'duration': 60,
                'calories_per_session': 700
            },
        ]
        
        for workout_data in workouts_data:
            Workout.objects.create(**workout_data, created_at=timezone.now())
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(workouts_data)} superhero workouts'))
        
        # Summary
        self.stdout.write(self.style.SUCCESS('✓ Database population complete!'))
        self.stdout.write(self.style.SUCCESS(f'  - Teams: {Team.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'  - Users: {User.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'  - Activities: {Activity.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'  - Leaderboard entries: {Leaderboard.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'  - Workouts: {Workout.objects.count()}'))
