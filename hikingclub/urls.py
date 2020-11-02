from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile", views.profile, name="profile"),
    path("filterby", views.filterby, name="filterby"),
    path("singlehike/<int:id>", views.singlehike, name="singlehike"),
    path("booking", views.booking, name="booking"),
    path("comment/<int:id>", views.comment, name="comment"),
    path("favourite", views.favourite, name="favourite"),
    path("favswitcher/<int:id>", views.favswitcher, name="favswitcher"),
    
    #API ROUTE
    path("api", views.api, name="api")
    
]
