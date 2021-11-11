from django.urls import path

from .views import LoginView, ManualLoginView, LoginCustomView, CheckToken

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('manual/', ManualLoginView.as_view()),
    path('custom/', LoginCustomView.as_view()),
    path('check-token/', CheckToken.as_view()),
]
