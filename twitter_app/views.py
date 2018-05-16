from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from twitter_app.forms import AddTwittForm, LoginForm, RegisterForm
from twitter_app.models import Twitt, Messages


class IndexView(View):
    def get(self, request):
        form = AddTwittForm()
        twitts = Twitt.objects.all().order_by('-creation_date')
        return render(request, 'index.html', {'twitts': twitts, 'form': form})

    def post(self, request):
        form = AddTwittForm(request.POST)
        if form.is_valid():
            user = request.user
            content = form.cleaned_data['content']
            Twitt.objects.create(content=content, user=user)
            return redirect('/', {'form': form})


class AddTwittView(LoginRequiredMixin, View):
    def get(self, request):
        form = AddTwittForm()
        return render(request, 'add_twitt.html', {'form': form})
    def post(self, request):

        form = AddTwittForm(request.POST)
        if form.is_valid():
            user = request.user
            content = form.cleaned_data['content']
            Twitt.objects.create(content=content, user=user)
            return redirect('/', {'form': form})

class UserView(LoginRequiredMixin, View):
    def get(self, request, username):
        user = User.objects.get(username=username)
        twitts = Twitt.objects.filter(user_id=user.pk)
        return render(request, 'user.html', {'twitts': twitts, 'user': user})



class ContentDetailsView(View):
    def get(self, request):
        form = AddTwittForm()
        twitts = Twitt.objects.all()
        return render(request, 'content.html', {'twitts': twitts, 'form': form})

    def post(self, request):
        form = AddTwittForm(request.POST)
        if form.is_valid():
            user = request.user
            content = form.cleaned_data['content']
            Twitt.objects.create(content=content, user=user)
            return redirect('/', {'form': form})


class MessagesView(View):
    def get(self,request):
        messages = Messages.objects.all()
        return render(request, 'user_messages.html', {'messages': messages})


class LoginView(View):
    def get(self,request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/user/{}'.format(request.user.username))

            else:
                return render(request, 'login.html', {'form': form, 'message': 'Wrong login or password'})


class RegisterView(View):
    def get(self,request):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})
    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']

            if password != password2:
                return render(request, 'register.html', {'form': form, 'message': 'The password does not match'})
            elif User.objects.filter(email=email):
                return render(request, 'register.html', {'form': form, 'message': 'email already used by another user'})
            else:
                try:
                    User.objects.create_user(username=username, email=email, password=password, first_name=first_name,
                                             last_name=last_name)
                    return render(request, 'register.html', {'form': form, 'success': 'User created'})
                except:
                    return render(request, 'register.html', {'form': form, 'message': 'Username already exist'})
        else:
            form = RegisterForm()
            return render(request, 'register.html', {'form': form, 'message': 'Invalid data'})

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')