from django.urls import path
from .views import *

urlpatterns = [
    path('', MainHome.as_view(), name='home'),
    path('news/', NewsViews.as_view(), name='news'),
    path('news/new/<int:post_id>/', show_post_news, name='news_post'),
    path('news/new/<slug:post_slug>/', ShowPostNews.as_view(), name='news_post'),
    path('about_us/', AboutUsView.as_view(), name='about_us'),
    path('contact_us/', ContactUsView.as_view(), name='contact_us'),
    path('school_rules/', SchoolRulesView.as_view(), name='school_rules'),
    path('addpage', AddPageView.as_view(), name='addpage'),
    path('employees/', EmployeesView.as_view(), name='employees'),
    path('employees/post/<int:post_id>/', show_post_employees, name='employees_post'),
    path('employees/post/<slug:post_slug>/', show_post_employees, name='employees_post'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('categorys/', CategorysView.as_view(), name='categorys'),
    path('category/<int:cat_id>/', category, name='category'),
    path('category/<slug:cat_slug>/', category, name='category'),
    path('raspisanie/', rasView, name='raspisanie'),
    path('raspisanie/<slug:class_slug>/', rasViewClasses, name='class_ras'),
    path('accounts/profile/', profile_user, name='profile')
]
