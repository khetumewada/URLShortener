from glob import escape
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, RedirectView
from django.views.generic.edit import CreateView, FormView
from shortener.forms import ShortenForm
from shortener.models import ShortURL
from . import forms
from .mixins import PageTitleMixins


class HomeView(PageTitleMixins, TemplateView):
    page_title = "Home"
    template_name = "accounts/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ShortenForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ShortenForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data["link"]
            custom_url = form.cleaned_data["custom_url"]

            if custom_url:
                if not request.user.is_authenticated:
                    login_url = reverse_lazy("accounts:login")

                    if request.headers.get("HX-Request"):
                        response = HttpResponse(status=302)
                        response["HX-Redirect"] = login_url
                        return response
                    else:
                        return redirect(login_url)
                if ShortURL.objects.filter(shortened=custom_url).exists():
                    return HttpResponse(
                        f'''
                            <div class="p-4 bg-red-50 text-red-700 rounded-lg">
                                ❌ Custom name <b>{escape(custom_url)}</b> already exists. Please choose another.
                            </div>
                        '''
                    )
                shortened = custom_url
                user = request.user
            else:
                shortened = ShortURL.generate_random_code()
                user = request.user if request.user.is_authenticated else None

            short = ShortURL.objects.create(link=link, shortened=shortened, user=user)

            return HttpResponse(
                f'''
                <div class="p-4 bg-green-50 rounded-lg space-y-3">
                    <p>Shortened URL: 
                        <a href="{reverse_lazy("shortener:redirector", args=[short.shortened])}" 
                           class="text-blue-600 font-medium" target="_blank">
                           {request.build_absolute_uri(reverse_lazy("shortener:redirector", args=[short.shortened]))}
                        </a>
                    </p>
                    <button 
                        type="button"
                        onclick="document.querySelector('#shorten-form').reset(); document.getElementById('short-result').innerHTML='';"
                        class="px-4 py-2 bg-gray-800 text-white rounded-lg shadow hover:bg-gray-900 transition">
                        Shorten Another URL
                    </button>
                </div>
                '''
            )

        return self.render_to_response({"form": form})


class AboutView(PageTitleMixins, TemplateView):
    template_name = "accounts/about.html"
    page_title = "About"


class ContactView(PageTitleMixins, CreateView):
    page_title = "Contact"
    form_class = forms.ContactForm
    template_name = "accounts/contact.html"
    success_url = "/"


class RegistrationView(PageTitleMixins, CreateView):
    form_class = forms.RegistrationForm
    template_name = "accounts/registration.html"
    page_title = "Registration"
    success_url = reverse_lazy("accounts:login")  # redirect after successful registration

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("shortener:profile")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # auto-login user after registration
        return super().form_valid(form)


class LoginView(PageTitleMixins, FormView, TemplateView):
    form_class = forms.LoginForm
    success_url = "/profile"
    template_name = "accounts/login.html"
    page_title = "Login"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return redirect(self.success_url)
        else:
            return self.form_invalid(form)


class LogoutView(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)