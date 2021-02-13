from django.urls import path

from . import views
from game.views import show, playerchoose, delete_QB, delete_RB, delete_WR, delete_TE, delete_K

urlpatterns = [
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('delete_QB/<int:id>', views.delete_QB, name="delete_QB"),
    path('delete_RB/<int:id>', views.delete_RB, name="delete_RB"),
    path('delete_WR/<int:id>', views.delete_WR, name="delete_WR"),
    path('delete_TE/<int:id>', views.delete_TE, name="delete_TE"),
    path('delete_K/<int:id>', views.delete_K, name="delete_K"),
    path('show',views.show, name="show"),
    path('scoreboard', views.scoreboard, name="scoreboard"),
    path('teamscores/<int:id>', views.teamscores, name="teamscores"), 
    path('playerchoose', views.playerchoose, name="playerchoose"),
    path('editname', views.editname, name="editname"),
    path('createteamname', views.createteamname, name="createteamname")
    
]