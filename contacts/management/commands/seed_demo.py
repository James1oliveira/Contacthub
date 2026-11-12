"""
Fills the demo account with sample contacts so the app never looks empty.
Runs automatically from build.sh on every deploy. Safe to run more than once.
"""
import os

from django.core.management.base import BaseCommand

from contacts.models import Contact, User

SAMPLE_CONTACTS = [
    ("Thandi Mokoena", "thandi.mokoena@example.com"),
    ("Liam van der Merwe", "liam.vdm@example.com"),
    ("Ayesha Patel", "ayesha.patel@example.com"),
    ("Sipho Ndlovu", "sipho.ndlovu@example.com"),
    ("Emma Botha", "emma.botha@example.com"),
    ("Daniel Okafor", "daniel.okafor@example.com"),
    ("Naledi Khumalo", "naledi.khumalo@example.com"),
    ("Ryan Pillay", "ryan.pillay@example.com"),
    ("Chloe Smith", "chloe.smith@example.com"),
    ("Kabelo Dlamini", "kabelo.dlamini@example.com"),
    ("Sarah Jacobs", "sarah.jacobs@example.com"),
    ("Michael Naidoo", "michael.naidoo@example.com"),
]


class Command(BaseCommand):
    help = "Add sample contacts to the demo account"

    def handle(self, *args, **options):
        username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "demo")
        user = User.objects.filter(username=username).first()
        if user is None:
            self.stdout.write(f"No user called '{username}' yet, skipping sample contacts.")
            return

        added = 0
        for name, email in SAMPLE_CONTACTS:
            _, created = Contact.objects.get_or_create(
                user=user, email=email, defaults={"name": name}
            )
            added += created
        self.stdout.write(self.style.SUCCESS(f"Sample contacts ready ({added} added)."))
