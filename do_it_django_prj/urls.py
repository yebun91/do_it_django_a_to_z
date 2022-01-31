
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # include 앱의 이름을 적고.urls
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
    # 접속했을 때 기본적으로 single_pages로 가게됨
    path('', include('single_pages.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)