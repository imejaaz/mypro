from django.urls import path
from django.urls import include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import seen

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', seen.index, name='project'),
    path('about/', seen.about),
    path('receipe/', include('receipe.urls')),
    path('authentication/', include('authentication.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)