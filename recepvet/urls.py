from rest_framework import routers 
from .views import TutorViewset, CadastroViewset, VetViewset

# Criação das Routes para que as vizualizações sejam possíveis para ambas as entidades

router = routers.DefaultRouter()
router.register(r'tutor', TutorViewset, basename="Tutor")
router.register(r'cadastro', CadastroViewset, basename="Cadastro")
router.register(r'vet', VetViewset, basename="Veterinário")

urlpatterns = router.urls