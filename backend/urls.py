from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('user/create-startup/', CreateStartupView.as_view()),
    path('user/get-startups/', GetStartupsView.as_view()),
    path('user/get-dashboard-data/', GetStartupView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)