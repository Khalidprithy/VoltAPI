from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('startup/create-strategy/', CreateStrategyView.as_view()),
    path('startup/get-strategies/', GetStrategiesView.as_view()),
    path('startup/get-strategy/', GetStrategyView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)