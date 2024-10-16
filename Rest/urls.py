from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import AlunoViewSets

router = DefaultRouter()
router.register(r'alunos', AlunoViewSets)

urlpatterns = [
    path('', include(router.urls))
]