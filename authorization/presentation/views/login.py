from rest_framework.views import APIView
from rest_framework.response import Response

from authorization.application.commands.login import LoginCommand
from authorization.application.container import get_container
from authorization.application.mediator import Mediator

class LoginView(APIView):
    def get(self, request):

        telegram_token = request.COOKIES.get('telegram_token')
        if not telegram_token:
            return Response({'success': False})
        command = LoginCommand(request=request, telegram_token=telegram_token)
        container = get_container()
        mediator: Mediator = container.resolve(Mediator)
        try:
            mediator.handle_command(command)
        except Exception as e:
            return Response({'success': False})

        return Response({'success': True})
