import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

import random
from users_app.models import users
from faker import Faker

fakegen = Faker()

emailOptions = ["@gmail.com", "@hotmail.com", "@yahoo.com", "@webmail.com"]

def populate(N=5):

    for entry in range(N):

        # create the fake data for that entry
        fake_firstName = fakegen.name()
        fake_lastName = fakegen.name()
        fake_emailName = fakegen.name()
        fake_email = fake_emailName+random.choice(emailOptions)

        # create the new webpage entry
        usersList = users.objects.get_or_create(firstName=fake_firstName, lastName=fake_lastName, email=fake_email)[0]



if __name__ == "__main__":
    print("Populating script")
    populate(20)
    print("Populating complete")
