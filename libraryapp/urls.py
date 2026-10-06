
from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('accounts/login/',views.loginview,name="login"),
    path('logout',views.logout_view),
    path('accounts/sign_up/',views.sign_up,name="signup"),
    path('reset',views.Resethome,name='reset'),
    path('passwordreset',views.resetPassword,name="passwordreset"),
    path('sample',views.sample,name="home1"),
    path('history',views.history,name="history"),
    path('biography',views.biography,name="biography"),
    path('poetry',views.poetry,name="poetry"),
    path('fantasy',views.fantasy,name="fantasy"),
    path('classics',views.classics,name="classics"),
    path('about',views.about,name="about"),
    path('historybooks',views.display1),
    path('biographybooks',views.display2),
    path('classicsbooks',views.display3),
    path('fantasybooks',views.display4),
    path('poetrybooks',views.display5),
    path('shortstorybooks',views.display6),
    path('booking',views.booking,name="booking"),
    path('viewallbooks',views.viewallbooks),
]
