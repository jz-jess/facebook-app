from core.models import Profile


def save_profile(strategy, backend, uid, response, details, user,  *args, **kwargs):
    if backend.name == 'facebook':
        social = user.social_auth.get(provider='facebook')

        if hasattr(user, 'profile'):
            profile = user.profile
        else:
            profile = Profile(user=user)  # New user

        profile.picture = social.extra_data['picture']['data']['url']
        profile.token = social.extra_data['access_token']
        profile.save()


def exchange_token(strategy, backend, uid, response, details, user,  *args, **kwargs):
    if backend.name == 'facebook':
        social = user.social_auth.get(provider='facebook')
        social.refresh_token(strategy)
