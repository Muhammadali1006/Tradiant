from django.urls import path
from app.views import home
from app.views import about
from app.views import why

urlpatterns = [
    path('', home),
    path('LoginIN/', about, name="about"),
    path('why/', why, name="why"),
]
