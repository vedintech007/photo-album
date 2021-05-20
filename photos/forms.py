from .models import Category, Photo
from django.forms import ModelForm
from django import forms
# from django.forms.widgets import TextInput, Textarea

class CategoryForm(ModelForm):
	name = forms.CharField(
		widget=forms.TextInput(
			attrs={
				'placeholder' : 'Update Category Name..'
			}
		)
	)

	class Meta:
		model = Category
		fields = '__all__'


class PhotoForm(ModelForm):

	description = forms.CharField(
		required=False,
		widget=forms.TextInput(
			attrs={
				'class': 'form-control',
			}
		)
	)

	class Meta:
		model = Photo
		fields = '__all__'