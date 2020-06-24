from django.urls import path
from ui import views

app_name = 'rpred'
urlpatterns = [
    path('', views.predict_rating, name='predict'),
]
