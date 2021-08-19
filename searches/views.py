from django.shortcuts import render

from qna.models import Answer

from .models import SearchQuery

# Create your views here.
def search_view(request):
	query=request.GET.get('q', None)
	user= None
	if request.user.is_authenticated:
		user= request.user
	context= {"query": query}
	if query is not None:	
		SearchQuery.objects.create(user=user, query=query)
		answer_list= Answer.objects.search(query=query)	
		context['answer_list'] = answer_list
	return render(request,'searches/search.html', context)