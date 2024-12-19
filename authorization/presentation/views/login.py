from rest_framework.views import APIView
from rest_framework.response import Response

from authorization.application.commands.login import LoginCommand
from authorization.application.container import get_container
from authorization.application.mediator import Mediator
from authorization.presentation.serializers.login import LoginSerializer

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        command = LoginCommand(request=request, username=serializer.validated_data['username'], password=serializer.validated_data['password'])
        container = get_container()
        mediator: Mediator = container.resolve(Mediator)
        session = mediator.handle_command(command)

        return Response({'session': session})