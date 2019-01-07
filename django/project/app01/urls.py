from django.conf.urls import url,include
from app01 import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'shengfen',views.ShengFenViewSet)
router.register(r'xqdz',views.XqDzViewSet)
router.register(r'dianpu',views.DianPuViewSet)
router.register(r'dpmoney',views.DpMoneyViewSet)
router.register(r'dpproject',views.DpPorjectViewSet)

from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='店铺管理系统')

#TODO coreapi
from rest_framework.schemas import get_schema_view as getsv
from rest_framework.documentation import include_docs_urls
# coreapi = getsv(title='店铺管理系统')

urlpatterns = [
    url(r'^schema_view/',schema_view),
    url(r'^decs/',include_docs_urls(title='图示管理系统')),
    url('^',include(router.urls)),
    url('^api-auth/',include('rest_framework.urls',namespace='rest-framework')),
]