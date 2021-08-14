from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="lista"),
    path("actualiza_tarea/<str:pk>/", views.actualiza_tarea, name="actualiza_tarea"),
    path("eliminar/<str:pk>/", views.eliminar_tarea, name="eliminar"),
]
