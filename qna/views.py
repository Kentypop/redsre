from django.shortcuts import render, redirect
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def qna(request):
	context= {
		'questions': Question.objects.all(),
		'answers': Answer.objects.all(),
	}
	return render(request, 'qna/qna.html', context)	

@login_required
def question(request):
	if request.method== 'POST':
		q_form= QuestionForm(request.POST)
		if q_form.is_valid():
			#https://forum.djangoproject.com/t/automatically-get-user-id-to-assignate-to-form-when-submitting/5333/7
			#https://stackoverflow.com/questions/12848605/django-modelform-what-is-savecommit-false-used-for
			#saving with commit=False get me a model object, then I can add extra data and save it.
			# Return an object without saving to the DB
			obj = q_form.save(commit=False)
			# Add an author field which will contain current user's id
			obj.author = User.objects.get(pk=request.user.id)
			print("YAH GURRRLLL")
			print(User.objects.get(pk=request.user.id))
			# Save the final "real form" to the DB
			obj.save()
			title= q_form.cleaned_data.get('title')
			messages.success(request, f'Your question has been submitted! {title}')
			return redirect('question')
	else:
		q_form= QuestionForm()		
	return render(request, 'qna/question.html', {'q_form': q_form})	


def answer(request):
	a_form= AnswerForm(request.POST)
	if not request.user.is_superuser or not request.user.is_staff:
		return redirect('info-home')
	if a_form.is_valid():
		# Return an object without saving to the DB
		obj= a_form.save(commit=False)
		# Add an author field which will contain current user's id
		obj.author = User.objects.get(pk=request.user.id)
		a_form.save()
		body= a_form.cleaned_data.get('body')
		messages.success(request, f'Answer created for {body}!')
		return redirect('qna')


	return render(request, 'qna/answer.html', {'a_form': a_form})		