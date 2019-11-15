from django.urls import include, path
from django.contrib import admin
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import routers
from apps.plans.views import PlanViewSet, TodoViewSet
from apps.users.views import UserViewset


API_TITLE = 'PlanManager'
API_DESCRIPTION = '计划管理 API'
schema_view = get_schema_view(title=API_TITLE)


router = routers.DefaultRouter()
router.register('plans', PlanViewSet, base_name="plans")
router.register('todos', TodoViewSet, base_name="todos")
router.register('users', UserViewset, base_name="users")


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/login/', obtain_jwt_token),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/schema/', schema_view),
    path('api/docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
]
