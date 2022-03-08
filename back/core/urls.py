from rest_framework.routers import SimpleRouter

from core.api import BusinessDomainsViewSet

app_name = "api"

router = SimpleRouter()

router.register("", BusinessDomainsViewSet, basename="domains")

urlpatterns = []

urlpatterns += router.urls

