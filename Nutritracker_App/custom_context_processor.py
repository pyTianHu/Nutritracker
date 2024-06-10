from django.shortcuts import render

def get_username(request):
    if request.user.is_authenticated:
        return {'username':request.user.username, 'message': "Welcome"}
    else:
        return {'username': None, 'message': 'You are currently not signed in!'}