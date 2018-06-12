from django.shortcuts import render
from django.http import HttpResponse
#from django.views.generic import TemplateView
from .models import Board
# Create your views here.


#class HomePageView(TemplateView):
#	def get(self,request,**kwargs):
#		return render(request,'index.html',context=None)
def home(request):
    boards = Board.objects.all()

    """
    boards_names = list()
    for board in boards:
        boards_names.append(board.name)

    response_html = '<br>'.join(boards_names)

    return HttpResponse(response_html)
	"""
    return render(request, 'home.html', {'boards':boards})