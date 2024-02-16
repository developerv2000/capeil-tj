import subprocess
import os
from faker import Faker
from authors.models import Author
from quotes.models import Quote
from categories.models import Category

fake = Faker()


def run():
    """
    Flush database & seed.
    Can be executed via django`s built-in shell commands:

    python manage.py shell
    import mainapp.seeder as seeder
    seeder.run()
    """

    flush_database()
    seed_database()
    print("", "Database seeding finished successfully!", "", sep="\n")


def seed_database():
    # Categories
    for _ in range(10):
        Category.objects.create(name=fake.name())

    # Authors
    for _ in range(10):
        author = Author.objects.create(name=fake.name())
        quote = author.quote_set.create(body=fake.text())
        categories = Category.objects.order_by("?").all()[:2]
        quote.categories.add(*categories)


def flush_database():
    """Run 'manage.py flush' shell command"""
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Move to the parent directory (where manage.py is located)
    parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
    os.chdir(parent_dir)

    subprocess.run(["python", "manage.py", "flush"])
