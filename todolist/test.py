import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Taken environment variables from .env file
path = os.path.join(BASE_DIR, '.env')

print(BASE_DIR, path)