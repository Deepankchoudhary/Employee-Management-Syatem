from django.urls import path,include

from .import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'testapp'
urlpatterns = [
     path('list/',views.Employeelist,name="list"),
     path('add/',views.add,name="add"),
     path('edit/',views.edit,name="edit"),
     path('delete/',views.delete,name="delete"),
     path('employee/<int:pk>/', views.UpdateView.as_view(), name='update-employee'),
     path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete-employee'),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)