from rest_framework import routers 
from .views import TutorViewset, CadastroViewset

# Criação das Routes para que as vizualizações sejam possíveis para ambas as entidades

router = routers.DefaultRouter()
router.register(r'tutor', TutorViewset)
router.register(r'cadastro', CadastroViewset)

urlpatterns = router.urls