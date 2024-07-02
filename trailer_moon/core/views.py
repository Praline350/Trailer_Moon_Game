from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from characters.models import Character
from trailer.models import Trailer

class HomePageView(View):
    template_name = "core/home.html"

    def get(self, request):
        user_connected = request.user
        return render(request, self.template_name, {'user_connected': user_connected})

@method_decorator(login_required, name='dispatch')
class GameBoardView(View):
    template_name = "core/game_board.html"

    def get(self, request):
        trailers = Trailer.objects.filter(user=request.user).prefetch_related('characters')
        context = {
            'trailers': trailers
        }
        return render(request, self.template_name, context=context)