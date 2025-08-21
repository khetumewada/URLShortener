from django.urls import path

from . import views

app_name = "shortener"
urlpatterns = [
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("delete/<slug:shortened>/", views.URLDeleteView.as_view(), name="url_delete"),
    path("count/<slug:shortened>/", views.hit_count, name="hit_count"),
    path("<slug:shortened>/", views.redirector, name="redirector"),
    path("delete-confirm/<slug:shortened>/", views.delete_confirm, name="delete_confirm"),

]
