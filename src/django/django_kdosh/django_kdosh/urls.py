

from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic.base import TemplateView


urlpatterns = [
    path("", include("barcode.urls")),
    path("", include("product_rpc.urls")),
    path("", include("pos_close_control.urls")),
    path("", include("miscellaneous.urls")),
    path("", include("react.urls")),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


admin.site.site_header = "Kdosh Administration"
admin.site.index_title = "Kdosh Administration"
