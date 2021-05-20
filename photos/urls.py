from django.urls import path

from .views import gallery, viewPhoto, addPhotos, delete_photo, delete_category, editCategory, UpdateInfo, addCategory

urlpatterns = [
	path('', gallery, name='gallery'),

	path('add/', addPhotos, name='add'),
	path('create_category/', addCategory, name='create_category'),

	path('photo/<str:pk>/', viewPhoto, name='photo'),
	path('delete/<str:pk>', delete_photo, name='delete'),
	path('cat/<str:pk>/', delete_category, name='cat'),
	path('edit-cat/<str:pk>/', editCategory, name='edit-cat'),
	path('update-info/<str:pk>/', UpdateInfo, name='update-info')
]
