from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden, HttpResponse
from django.template.loader import render_to_string
from django.views.generic import DeleteView, ListView
from .models import ShortURL
from django.shortcuts import get_object_or_404, redirect, render
from accounts.mixins import PageTitleMixins

class ProfileView(PageTitleMixins, LoginRequiredMixin, ListView):
    page_title = "Profile"
    model = ShortURL
    template_name = "shortener/profile.html"
    context_object_name = "links"

    def get_queryset(self):
        return ShortURL.objects.filter(user=self.request.user).order_by("-created_at")

class URLDeleteView(LoginRequiredMixin, DeleteView):
    model = ShortURL
    slug_field = "shortened"
    slug_url_kwarg = "shortened"

    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() == "delete":
            return self.delete(request, *args, **kwargs)
        return super().dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user != request.user:
            return HttpResponseForbidden("Not allowed")
        self.object.delete()
        return HttpResponse("", status=200)

@login_required
def delete_confirm(request, shortened):
    """Return confirmation modal HTML for HTMX"""
    obj = get_object_or_404(ShortURL, shortened=shortened, user=request.user)
    html = render_to_string(
        "shortener/delete_confirm.html",
        {"shortened": shortened},
        request=request,
    )
    return HttpResponse(html)

def hit_count(request, shortened):
    """Only update hit counter on profile page"""
    obj = get_object_or_404(ShortURL, shortened=shortened)
    return HttpResponse(str(obj.hits))

def redirector(request, shortened):
    """Redirect short link -> original and increase hits"""
    obj = get_object_or_404(ShortURL, shortened=shortened)
    obj.hits += 1
    obj.save(update_fields=["hits"])
    return redirect(obj.link)
