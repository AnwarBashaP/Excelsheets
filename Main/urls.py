from django.urls import path
#

from .views import HomeView, LoginView, TableView

#
urlpatterns = [
    path('', HomeView, name='home'),
    path('login', LoginView.as_view(), name='UploadView'),
    path('main', TableView, name='TableView'),
    # path('loggedin', LoginApiview.as_view(), name='Logged In'),
]
