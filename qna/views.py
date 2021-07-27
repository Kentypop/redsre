from django.shortcuts import render


def qna(request):
	context= {
		'posts': Post.objects.all()
	}
	return render(request, 'info/home.html', context)	