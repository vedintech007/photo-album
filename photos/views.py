from django.shortcuts import render, redirect
from .models import Category, Photo
from .forms import CategoryForm, PhotoForm


def gallery(request):
	category = request.GET.get('category')
	if category == None:
		photos = Photo.objects.all()
	else:
		photos = Photo.objects.filter(category__name=category)

	categories = Category.objects.all()

	context = {
		'categories': categories,
		'photos': photos
	}
	return render(request, 'photos/gallery.html', context)


def viewPhoto(request, pk):
	photos = Photo.objects.get(id=pk)

	context = {
		'photo': photos
	}

	return render(request, 'photos/photo.html', context)


def addPhotos(request):
	categories = Category.objects.all()

	if request.method == "POST":
		data = request.POST
		image = request.FILES.get('image')

		if data['category'] != 'none':
			category = Category.objects.get(id=data['category'])
		elif data['category_new'] != '':
			category, created = Category.objects.get_or_create(name=data['category_new'])

		else:
			category = None

		photo = Photo.objects.create(
			category=category,
			description=data['description'],
			image=image,
		)

		return redirect('gallery')

	context = {
		'categories': categories,
	}
	return render(request, 'photos/add.html', context)


def UpdateInfo(request, pk):
	photo = Photo.objects.get(id=pk)
	form = PhotoForm(instance=photo)


	if request.method == "POST":
		form = PhotoForm(request.POST,  request.FILES, instance=photo)

		if form.is_valid():
			form.save()
		return redirect('gallery')

	context = {
		'form': form
	}

	return render(request, 'photos/update_info.html', context)


def delete_photo(request, pk):
	photo = Photo.objects.get(id=pk)

	if request.method == "POST":
		photo.delete()
		return redirect('gallery')

	context = {
		'photo': photo
	}

	return render(request, 'photos/delete.html', context)


def editCategory(request, pk):
	category = Category.objects.get(id=pk)
	form = CategoryForm(instance=category)


	if request.method == "POST":

		form = CategoryForm(request.POST, instance=category)
		if form.is_valid():
			form.save()
		return redirect('gallery')

	context = {
		'form': form
	}

	return render(request, 'photos/edit_category.html', context)


def delete_category(request, pk):
	category = Category.objects.get(id=pk)

	if request.method == "POST":
		category.delete()
		return redirect('gallery')

	context = {
		'category': category
	}

	return render(request, 'photos/delete_cat.html', context)
