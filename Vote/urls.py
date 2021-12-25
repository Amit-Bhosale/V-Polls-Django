from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name="Voteer"),
    path('signin/',views.signin,name="signin"),
    path('register/', views.register, name="register"),
    path('contact/',views.contact,name="contact"),
    path('notice/', views.notice, name="notice"),
    path("blogpost/<int:id>", views.blogpost, name="blogHome"),
    path('vote/<vote_id>/',views.vote,name="voting"),
    path('create/',views.create,name="create"),
    path('result/<vote_id>',views.result,name="result"),
    path('voteresult/',views.voteresult,name="voteresult"),
path('ongoingvote/',views.ongoingvote,name="ongoingvote")

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)