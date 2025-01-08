# import app
from app import app
# import model and db instance
from models import db, Sighting

from faker import Faker
import random

# Define seeding functions (optional: use Faker to help generate fake data)
shapes = ['round','square','strange','confusing']

fake = Faker()

def seed():
    sightings = []
    for _ in range(0,5):
        sights = Sighting(
            date=fake.date("%m-%d-%Y"),
            time=fake.time(),
            location=fake.address(),
            shape_of_craft=random.choice(shapes),
            approximate_size=random.randint(10,1000),
            approximate_speed=random.randint(5,500),
            description=fake.text(40),
            reporter=fake.name(),
            reporter_reliable_witness=fake.boolean()
        )
        sightings.append(sights)
   
    db.session.add_all(sightings)
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        seed()
