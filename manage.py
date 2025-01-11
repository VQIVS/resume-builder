import os
import django
from django.core.management import execute_from_command_line

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

if __name__ == "__main__":
    execute_from_command_line()