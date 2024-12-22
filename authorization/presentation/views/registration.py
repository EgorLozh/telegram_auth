from django.shortcuts import render
from django.views import View

from authorization.application.commands.registration import RegistrationCommand
from authorization.application.container import get_container
from authorization.application.mediator import Mediator


class RegistrationView(View):
    def post(self, request):
        container = get_container()
        mediator: Mediator = container.resolve(Mediator)
        return mediator.handle_command(RegistrationCommand(request=request))
    
    def get(self, request):
        return render(request, 'base.html', {'user': request.user})
