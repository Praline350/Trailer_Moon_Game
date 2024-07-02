from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from characters.models import *
from trailers.models import *
from locations.models import *



class HomePageView(View):
    template_name = "core/home.html"

    def get(self, request):
        user_connected = request.user
        return render(request, self.template_name, {'user_connected': user_connected})
    

@method_decorator(login_required, name='dispatch')
class GameBoardView(View):
    template_name = "core/game_board.html"

    def get(self, request):
        trailers = Trailer.objects.filter(user=request.user)
        context = {
            'trailers': trailers,
        }
        return render(request, self.template_name, context=context)
    

class GameMainView(View):
    template_name = "core/game_main.html"

    def get(self, request):
        trailers = Trailer.objects.filter(user=request.user)
        map = request.user.current_map
        locations = Location.objects.filter(map=map)
        context = {
            'trailers' : trailers,
            'locations': locations,
            'map': map,
        }
        return render(request, self.template_name, context=context)