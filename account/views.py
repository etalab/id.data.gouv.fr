from django.views.generic import View
from django.http import JsonResponse
from oauth2_provider.models import AccessToken


class UserView(View):
    def get(self, request, *args, **kwargs):
        token_value = request.GET.get('access_token', '')
        token_object = AccessToken.objects.get(token=token_value)
        user = token_object.user

        return JsonResponse({
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'is_active': user.is_active,
        })
