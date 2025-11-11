from django.urls import path

from . import views

urlpatterns = [
    # path('student/', views.student),
    # path('student/<int:pk>', views.StudentClassBasedView.as_view()),
    path('student/', views.StudentListCreate.as_view()),
    path('student/<int:pk>', views.StudentRetrieveUpdateDestroy.as_view()),
    path('users/', views.UserListCreate.as_view()),

]
