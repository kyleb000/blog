from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm as UserCreationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/user_registration.html', {'form': form, 'title': 'Registration'})


@login_required
def profile(request, edit='0'):

    if request.method == 'POST' and edit == '1':

        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(request, f'Profile updated')
            return redirect('user-profile', edit=0)
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    page_edit = ''
    if edit == '1' :
        page_edit = '1'

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'edit': page_edit,
        'editable':'True'
    }
    return render(request, 'users/profile.html', context)


def view_profile(request, view_user):

    try:
        profile_model = User.objects.all().filter(username=view_user).first()
        user_f = UserUpdateForm(instance=profile_model)
        profile_form = ProfileUpdateForm(instance=profile_model.profile)
        return render(request, 'users/profile.html', {'editable': '', 'p_form': profile_form, 'u_form': user_f})

    except:
        print("ERROR")
        messages.warning(request, f'No profile exists for user {view_user}!')
        return redirect('blog-home')




