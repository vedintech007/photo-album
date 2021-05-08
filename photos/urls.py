from django.urls import path
from .views import gallery, viewPhoto, addPhotos,delete_photo, delete_category,editCategory, UpdateInfo

urlpatterns = [
	path('', gallery, name='gallery'),
	path('photo/<str:pk>/', viewPhoto, name='photo'),
	path('add/', addPhotos, name='add'),
	path('delete/<str:pk>', delete_photo, name='delete'),
	path('cat/<str:pk>/', delete_category, name='cat'),
	path('edit-cat/<str:pk>/', editCategory, name='edit-cat'),
	path('update-info/<str:pk>/', UpdateInfo, name='update-info')
]