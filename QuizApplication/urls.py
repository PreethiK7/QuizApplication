from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('submitAnswer', views.submitAnswer, name="submitAnswer"),
    path('addQuiz', views.addQuiz, name="addQuiz"),
    path('getAddQuiz', views.getAddQuiz, name="getAddQuiz"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)