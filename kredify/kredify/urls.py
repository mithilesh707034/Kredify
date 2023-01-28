from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('about',views.aboutPage),
    path('loan-services',views.loanServicePage),
    path('apply-now',views.applyPage),
    path('contact-us',views.contactPage)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
