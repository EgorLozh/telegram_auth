from rest_framework.views import APIView
from rest_framework.response import Response

from authorization.application.commands.logout import LogoutCommand
from authorization.application.container import get_container
from authorization.application.mediator import Mediator
from rest_framework.permissions import IsAuthenticated


class LogoutView(APIView):
    def post(self, request):
        permission_classes = [IsAuthenticated]
        container = get_container()
        mediator: Mediator = container.resolve(Mediator)
        mediator.handle_command(LogoutCommand())

        return Response()