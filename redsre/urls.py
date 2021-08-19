"""redsre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from qna import views as qna_views
from searches.views import search_view
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', user_views.MyLoginView.as_view() , name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name= 'users/logout.html'), name='logout'),
    path('password-reset/', 
        auth_views.PasswordResetView.as_view(template_name= 'users/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/', 
        auth_views.PasswordResetDoneView.as_view(template_name= 'users/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name= 'users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('qna/', qna_views.qna, name='qna'),
    path('question/', qna_views.question, name='question'),
    path('answer/', qna_views.answer, name='answer'),
    path('qnalist/', qna_views.QNAListView.as_view(), name='qnalist'),
    path('search/', search_view, name='searchview'),
    path('userlist/<str:username>', qna_views.UserListView.as_view(), name='userlist'),
    path('answerdetail/<int:pk>/', qna_views.AnswerDetailView.as_view(), name='answerdetail'),
    path('questiondetail/<int:pk>/', qna_views.QuestionDetailView.as_view(), name='questiondetail'),
    path('questionna/new/', qna_views.QuestionCreateView.as_view() , name='question-create'),
    path('qnanswer/<int:pk>/updateanswer', qna_views.AnswerUpdateView.as_view() , name='answer-update'),
    path('questionna/<int:pk>/updatequestion', qna_views.QuestionUpdateView.as_view() , name='question-update'),
    path('answer/<int:pk>/delete/', qna_views.AnswerDeleteView.as_view() , name='answerdelete'),
    path('question/<int:pk>/delete/', qna_views.QuestionDeleteView.as_view() , name='questiondelete'),
    path('', include('info.urls')),
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


