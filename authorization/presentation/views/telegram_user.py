from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from authorization.application.commands.telegram_user import CreateTelegramUserCommand
from authorization.domain.entities.user import User
from authorization.presentation.serializers.telegram_user import TelegramUserSerializer
from authorization.application.container import get_container
from authorization.application.mediator import Mediator


class TelegramUserView(APIView):
    def post(self, request):
        permission_classes = [IsAdminUser]

        serializer = TelegramUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        command = CreateTelegramUserCommand(telegram_id=serializer.validated_data['telegram_id'], 
                                            username=serializer.validated_data['username'], 
                                            first_name=serializer.validated_data['first_name'], 
                                            token=serializer.validated_data['token'])
        container = get_container()
        mediator: Mediator = container.resolve(Mediator)
        user: User = mediator.handle_command(command)
        
        if not user:
            return Response({'error': 'Invalid token'}, status=400)

        data = {'user': {'id': user.id, 'telegram_id': user.telegram_id, 'username': user.username, 'first_name': user.first_name}}
        return Response(data)