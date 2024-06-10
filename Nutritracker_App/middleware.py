from typing import Any


class CurrentUserMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request):
        request.current_username=None
        if request.current_username.is_authenticated:
            request.current_username = request.user.username

        response = self.get_response(request)
        return response
        