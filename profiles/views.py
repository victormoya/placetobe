from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View

from profiles.forms import RegistrationForm, LoginForm, EditForm
from profiles.models import MyUser


class RegistrationView(View):

    template_name = 'profiles/register.html'
    form_class = RegistrationForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'register_form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created, now you can login')
            return redirect(reverse('profiles:login'))
        messages.error(request, 'Ops! Some errors detected')
        return render(request, self.template_name, {'register_form': form})


class LoginView(View):

    template_name = 'profiles/login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'login_form': form})

    def post(self, request):
        if not request.POST.get('remember_me', None):
            request.session.set_expiry(0)
        user = request.POST['user']
        password = request.POST['password']

        if '@' not in user:
            try:
                user_object = MyUser.objects.get(username=user)
                user = user_object.get_full_name()
            except MyUser.DoesNotExist:
                messages.error(request, 'User does not exist, try email login')
                return redirect(reverse('profiles:login'))

        access = authenticate(username=user, password=password)
        if access is not None:
            if access.is_active:
                login(request, access)
                return redirect(reverse('events:suggested'))
            else:
                messages.error(request, 'Disabled account')
        else:
            messages.error(request, 'Incorrect email or password')
        return render(request, self.template_name, {'login_form': self.form_class()})


class LogoutView(View):

    @staticmethod
    def get(request):
        logout(request)
        messages.info(request, 'Logged out')
        return redirect(reverse('events:list'))


class EditView(View):

    form_class = EditForm
    template_name = 'profiles/edit.html'

    def get(self, request, pk):
        # user = MyUser.objects.get(slug=slug)
        user = get_object_or_404(MyUser, pk=pk)
        form = self.form_class(instance=user)
        data = {
            'profile_form': form,
        }
        return render(request, self.template_name, data)

    def post(self, request, pk):
        user = get_object_or_404(MyUser, pk=pk)
        form = self.form_class(request.POST, request.FILES, instance=user)
        data = {
            'profile_form': form,
        }
        if form.is_valid():
            form.save()
            messages.success(request, 'Changes are saved in your profile')
            return redirect(reverse('events:list'))
        messages.error(request, 'Some problems while editing your profile')
        return render(request, self.template_name, data)


class DetailView(View):

    template_name = 'profiles/detail.html'

    def get(self, request, publisher):

        user = get_object_or_404(MyUser, username=publisher)
        events = user.events.all()

        data = {
            'profile': user,
            'events': events
        }
        return render(request, self.template_name, data)









