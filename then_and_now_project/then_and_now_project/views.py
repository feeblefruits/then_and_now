from django.shortcuts import render, redirect
from .forms import BeforePhotoForm, AfterPhotoForm, BeforePhoto, AfterPhoto

def home_view(request):
    before_photos = BeforePhoto.objects.all()
    return render(request, 'home.html', {'before_photos': before_photos})

def upload_before_photo(request):
    if request.method == 'POST':
        form = BeforePhotoForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            pseudonym = form.cleaned_data['pseudonym']
            
            before_photo = form.save(commit=False)
            before_photo.title = title
            before_photo.description = description
            before_photo.pseudonym = pseudonym
            before_photo.save()
            
            return redirect('upload_success')
    else:
        form = BeforePhotoForm()
        
    return render(request, 'upload_photo.html', {'form': form})

def upload_after_photo(request):
    if request.method == 'POST':
        # If the request method is POST, process the form data
        form = AfterPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            # If the form data is valid, save the form data and redirect to the success page
            form.save()
            return redirect('upload_success')
    else:
        # If the request method is not POST, render the form page
        form = AfterPhotoForm()
    # Render the form page with the form object
    return render(request, 'upload_photo.html', {'form': form})

def upload_success(request):
    return render(request, 'upload_success.html')
