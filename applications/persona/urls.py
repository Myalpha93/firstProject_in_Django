from django.contrib import admin
from django.urls import path

from . import views

app_name = "persona_app"

urlpatterns = [
    path(
        '', 
        views.InicioView.as_view(), 
        name='inicio'
    ),
    path(
        'listar-todo-empleados/', 
        views.ListAllempleadosListView.as_view(),
        name='empleados_all'),
    path(
        'listar-by-area/<shorname>/', 
        views.ListbyAreaEmpleadosListView.as_view(),
        name='empleados_area',
        ),
    path(
        'lista-admin-empleados/', 
        views.ListbyAreaEmpleadosAdmin.as_view(),
        name='lista_empleados_admin',
        ),
    path('buscar-empleados/', views.ListEmpleadoByKwordListView.as_view()),
    path('lista-habilidades/', views.ListHabilidadesListView.as_view()),
    path(
        'ver-empleado/<pk>/', 
        views.EmpleadoDetailView.as_view(),
        name='empleado_detail'),
    path(
        'crear-empleado/', 
        views.EmpleadoCreateView.as_view(),
        name='crear_empleado'
        ),
    path(
        'success-empleado/', 
        views.SuccessView.as_view(), 
        name='correcto'
    ),
    path(
        'update-empleado/<pk>/', 
        views.EmpleadoUpdateView.as_view(), 
        name='modificar_empleado'
    ),
    path(
        'delete-empleado/<pk>/', 
        views.EmpleadoDeleteView.as_view(), 
        name='eliminar_empleado'
    ),
]