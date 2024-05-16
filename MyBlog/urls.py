from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
import members.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),
    path('DigLog/', include('blog.urls')),
    path('<int:id>/password/', members.views.PasswordsChangeView.as_view(), name='password-change-view-url'),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
