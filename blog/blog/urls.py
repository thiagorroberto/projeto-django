from django.contrib import admin
from django.urls import path
from produtos.views import produto, index, frete, forma
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', index),
    path('produto/<int:id>/', produto, name="tela_produto"),
    path('frete/<int:id>/', frete, name="tela_frete"),
    path('forma/', forma)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
