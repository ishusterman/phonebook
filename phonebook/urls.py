from django.conf.urls import url, include
from book.admin import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^book/', include('book.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



