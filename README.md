# facebook-app
# Setup and Running server
1. Clone directory
2. Run command `pip install -r requirements.txt`
4. Run command `python manage.py migrate`
5. Open file `facebookapp/settings/dev.py`. Add `SOCIAL_AUTH_FACEBOOK_KEY` and `SOCIAL_AUTH_FACEBOOK_SECRET`
6. Run command `python manage.py runserver`. You should be able to access the app on `http://localhost:8000`
