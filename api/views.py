from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from oauth2_provider.views import TokenView

from core.decorators import class_decorator


@class_decorator(login_required)
class ProfileView(TokenView):

    def get(self, request, *args, **kwargs):
        user = request.user
        _, request = self.verify_request(request)
        response = {'id': user.pk}

        if request.access_token.scope == 'email':
            response['email'] = user.email

        return JsonResponse(response)
