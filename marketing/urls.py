from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('startup/create-marketing/', CreateMarketingView.as_view()),
    path('startup/get-marketing-strategies/', GetMarketingStrategiesView.as_view()),
    path('startup/get-marketing/', GetMarketingStrategyView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)