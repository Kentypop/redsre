from django.shortcuts import render
from .models import Question, Answer

def qna(request):
	context= {
		'questions': Question.objects.all(),
		'answers': Answer.objects.all(),
	}
	return render(request, 'qna/qna.html', context)	