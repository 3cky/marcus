# coding: utf-8

from marcus.models import UserProfile

def save_profile(backend, user, response, *args, **kwargs):
    try:
        profile = user.profile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=user)
        profile.save()

#     from pprint import pprint
#     pprint(response)

    link = None
    if backend.name == 'facebook':
        link = response.get('link')
    elif backend.name == 'twitter':
        link = 'https://twitter.com/' + user.username
    elif backend.name == 'google-oauth2':
        link = response.get('url')
    elif backend.name == 'github':
        link = response.get('html_url')
    elif backend.name == 'vk-oauth2':
        link = 'https://vk.com/' + response.get('screen_name')

    if link:
        profile.link = link
        profile.save()
