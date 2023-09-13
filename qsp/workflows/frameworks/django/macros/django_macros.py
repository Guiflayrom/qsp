import os
import shutil


def organize_poetry_folder(*args, **context):
    shutil.rmtree(f'{context["output"]}/restapi/')
    os.makedirs(f'{context["output"]}/src')


def default_django_settings(*args, **context):
    return {"secret": "keysuhdjdsnfksmsdf", "apps": [], "django_version": "1"}
