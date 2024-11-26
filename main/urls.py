from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from main_page import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about_me/', views.about_me, name='about_me'),
    path('about_my_pets/', views.about_my_pets, name='about_my_pets'),
    path('image_link/', views.picture_view, name='picture_view'),
    path('system_time/', views.system_time, name='system_time'),
    path('book_list', views.book_list, name='book_list'),
    path('', include('main_page.urls')),
    path('', include('hashtags.urls')),
    path('', include('todo.urls')),
    path('', include('cbv.urls')),
    path('<int:pk>/', views.book_detail, name='book_detail'),
    path('admin/', admin.site.urls),
    path('', include('parsing_openlibrary.urls')),
    path('', include('users.urls')),
]
urlpatterns += static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
                     document_root=settings.STATIC_ROOT)