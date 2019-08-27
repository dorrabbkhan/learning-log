from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    """
    Register the user
    """

    if request.method != "POST":
        form = UserCreationForm()
        # make blank form if method is not POST

    else:
        form = UserCreationForm(data=request.POST)
        # create the form with user-filled data

        if form.is_valid():
            new_user = form.save()
            # if form is valid, save it and create new user

            login(request, new_user)
            return redirect('learning_logs:index')
            # log the user in and redirect to home
    
    context = {'form': form}
    return render(request, 'registration/register.html', context)
