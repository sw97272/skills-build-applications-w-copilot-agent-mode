from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.db import transaction

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        with transaction.atomic():
            # Clear existing data
            for obj in Activity.objects.all():
                if obj.pk:
                    obj.delete()
            for obj in Workout.objects.all():
                if obj.pk:
                    obj.delete()
            for obj in Leaderboard.objects.all():
                if obj.pk:
                    obj.delete()
            for obj in User.objects.all():
                if obj.pk:
                    obj.delete()
            for obj in Team.objects.all():
                if obj.pk:
                    obj.delete()

            # Create teams
            marvel = Team.objects.create(name='Marvel')
            dc = Team.objects.create(name='DC')

            # Create users
            users = [
                User(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
                User(name='Iron Man', email='ironman@marvel.com', team=marvel),
                User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
                User(name='Batman', email='batman@dc.com', team=dc),
            ]
            for user in users:
                user.save()

            # Create activities
            Activity.objects.create(user=users[0], type='Running', duration=30, date='2025-10-30')
            Activity.objects.create(user=users[1], type='Cycling', duration=45, date='2025-10-29')
            Activity.objects.create(user=users[2], type='Swimming', duration=60, date='2025-10-28')
            Activity.objects.create(user=users[3], type='Yoga', duration=50, date='2025-10-27')

            # Create workouts
            workout1 = Workout.objects.create(name='Cardio Blast', description='High intensity cardio workout')
            workout2 = Workout.objects.create(name='Strength Training', description='Build muscle strength')
            workout1.suggested_for.set([users[0], users[2]])
            workout2.suggested_for.set([users[1], users[3]])

            # Create leaderboard
            Leaderboard.objects.create(team=marvel, points=150)
            Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
