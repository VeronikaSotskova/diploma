from rest_framework.routers import SimpleRouter

from core.api import BusinessDomainsViewSet, DbtViewSet, TagViewSet

app_name = "api"

router = SimpleRouter()

router.register("", BusinessDomainsViewSet, basename="domains")
router.register("dbt", DbtViewSet, basename="dbt")
router.register("tags", TagViewSet, basename="tags")

urlpatterns = []

urlpatterns += router.urls

