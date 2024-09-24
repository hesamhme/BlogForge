from io import StringIO
from django.core.management.base import BaseCommand
from faker import Faker
from accounts.models import User, Profile
from blog.models import Post,Category
 



class Command(BaseCommand):
    help = "insert dummey data"
    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()
    
    def handle(self, *args, **options):
        user = User.objects.create_user(email=self.fake.email(), password="passgooD@1234567")
        profile = Profile.objects.get(user=user)
        profile.first_name = self.fake.first_name()
        profile.last_name = self.fake.last_name()
        profile.description = self.fake.paragraph(nb_sentences=5)
        profile.save()