from django.urls import path, include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('base', views.BasicModelViewSet, basename='BasicModel')
router.register('basicModel', views.PublicBasicModelViewSet)
router.register('profile', views.ProfileViewSet, basename='Profile')
router.register('publicProfile', views.PublicProfileViewSet, basename='Profile')
router.register('strategy', views.StrategyModelViewSet, basename='StrategyModel')
router.register('research', views.ResearchModelViewSet, basename='ResearchModel')
router.register('researches', views.ResearchViewSet, basename='Research')

# basicModel_router = routers.NestedDefaultRouter(router, 'basicModel', lookup='basicModel')
# basicModel_router.register('strategy', views.StrategyModelViewSet, basename='basicModel-strategy')
# basicModel_router.register('research', views.ResearchModelViewSet, basename='basicModel-research')
# basicModel_router.register('profile', views.PublicProfileViewSet, basename='basicModel-profile')

urlpatterns = [
    path('', include(router.urls)),
    # path('', include(basicModel_router.urls)),
]

