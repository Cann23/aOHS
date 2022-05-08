from . import myoffer

from django.http import HttpResponse
from django.template import loader

def index(request):
	template = loader.get_template('stream/index.html')
	context = {}
	return HttpResponse(template.render(context, request))

async def offer(request):
	response = await myoffer.offer(request)
	return response

