from .views import crear_curso
from django.urls import path

from .views import saludo, saludo_con_template, crear_familiar, inicio, crear_curso

urlpatterns = [
    path('', inicio, name='inicio'),
    path('hola-mundo/', saludo),
    path('hola-mundo-template/', saludo_con_template),
    path('crear-familiar/<str:nombre>/', crear_familiar),
    path('crear-curso/', crear_curso, name='crear-curso'),

]

# ---------------------------------------------------------

urlpatterns = [
    path('crear-curso/', crear_curso, name='crear_curso'),
]
