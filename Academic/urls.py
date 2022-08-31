from django.urls import path
from . import views


urlpatterns = [
    path('',views.home),
    path('registrar_Curso/', views.registrar_Curso),
    path('eliminar_curso/<codigo>',views.eliminar_curso),
    path('edicion_curso/<codigo>',views.edicion_curso),
    path('editar_Curso/', views.editar_Curso),
]
