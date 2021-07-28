from django.shortcuts import render, redirect
from .models import Question, Answer
from .forms import QuestionForm
from django.contrib import messages

def qna(request):
	context= {
		'questions': Question.objects.all(),
		'answers': Answer.objects.all(),
	}
	return render(request, 'qna/qna.html', context)	

def question(request):
	if request.method== 'POST':
		q_form= QuestionForm(request.POST)
		if q_form.is_valid():
			q_form.save()
			username= q_form.cleaned_data.get('title')
			messages.success(request, f'Your question has been submitted!')
			return redirect('question')
	else:
		q_form= QuestionForm()		
	return render(request, 'qna/question.html', {'q_form': q_form})	