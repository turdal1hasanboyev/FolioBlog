from django.urls import path

from folio.views import index, grid, single


urlpatterns = [
    path('', index, name='index'),
    path('grid/', grid, name='grid'),
    path('single/<slug:slug>/', single, name='single'),
]
