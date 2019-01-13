from django.conf.urls import url,include
from data_01 import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'zonglei',views.zongleiViewSet)
router.register(r'liebiao',views.liebiaoViewSet)
router.register(r'zhangjie',views.zhangjieViewSet)
router.register(r'content',views.contentViewSet)
router.register(r'UserInfo',views.UserInfoViewSet)

from rest_framework_swagger.views import get_swagger_view
schema_view =get_swagger_view(title='小说数据管理系统')

from rest_framework.documentation import include_docs_urls

urlpatterns = [
    url('^',include(router.urls)),
    url(r'^schema_view/',schema_view),
    url(r'^docs/',include_docs_urls(title='小说数据管理系统')),
    url('^api-auth/',include('rest_framework.urls',namespace='rest-framework')),
]