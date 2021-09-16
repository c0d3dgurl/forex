from django.http import HttpResponse
from django.urls import path
from django.urls.conf import include
from .views import SignalGetterView,CheckUser, schema_view
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.documentation import include_docs_urls
from django.conf.urls import url


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
) 


# router = DefaultRouter()

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/',CheckUser.as_view(),name='check_user'),
    url(r'^$', schema_view),
    path('signal',SignalGetterView.as_view()),
    # path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),


] 

# urlpatterns += router.urls