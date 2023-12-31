from django.urls import path
from .views import index, top_sellers, advertis, advertisement_post, login, profile, register

urlpatterns = {
    path('', index, name = 'main-page'),
    path('top-sellers/', top_sellers, name = 'top-sellers'),
    path('advertis/', advertis, name = 'advertis'),
    path('advertisement-post/', advertisement_post, name = 'advertisement-post'),
    path('login/', login, name = 'login'),
    path('profile/', profile, name = 'profile'),
    path('register/', register, name = 'register'),

}