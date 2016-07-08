# coding: utf-8

from marcus.models import UserProfile

def save_profile(backend, user, response, *args, **kwargs):
    try:
        profile = user.profile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=user)
        profile.save()

    if backend.name == 'facebook':
        profile.link = response.get('link')
        profile.save()
