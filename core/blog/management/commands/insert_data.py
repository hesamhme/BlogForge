import random
from django.core.management.base import BaseCommand
from faker import Faker
from datetime import datetime
from accounts.models import User, Profile
from blog.models import Post,Category
 
category_list = [
    'test1','test2','test3','test4','test5','test6','test7']


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

        for name in category_list:
            Category.objects.create(name=name)
        for _ in range(10):
            Post.objects.create(
                author = profile,
                title = self.fake.paragraph(nb_sentences=1) ,
                content = self.fake.paragraph(nb_sentences=10),
                status = True,
                category = Category.objects.get(name=random.choice(category_list)),
                publish_date = datetime.now()

            )