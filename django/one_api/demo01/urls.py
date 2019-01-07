from django.conf.urls import url, include
from demo01 import views


#配置视图集的路由
# book_list = views.BookViewSet.as_view(
#     {
#         'get':'list',
#         'post':'create'
#     }
# )
#
# book_detail = views.BookViewSet.as_view(
#     {
#         'get': 'retrieve',
#         'put': 'update',
#         'patch': 'partial_update',
#         'delete': 'destory'
#     }
# )
#
#
# publisher_list = views.PublisherViewSet.as_view(
#     {
#         'get':'list',
#         'post':'create'
#     }
# )
#
#
# publisher_detail = views.PublisherViewSet.as_view(
#     {
#         'get': 'retrieve',
#         'put': 'update',
#         'patch': 'partial_update',
#         'delete': 'destory'
#     }
# )

#TODO 改进代码（路由器）
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books',views.BookViewSet)
router.register(r'publishers',views.PublisherViewSet)

# TODO coreapi
"""
from rest_framework.schemas import get_schema_view
schema_view = get_schema_view(title='图书管理系统')


from rest_framework.documentation import include_docs_urls
schema_view = include_docs_urls(title='图书管理系统')
"""

#TODO 常用的架构
from rest_framework_swagger.views import get_swagger_view

docs = get_swagger_view(title='图书管理系统')



urlpatterns = [
    #不能加结束符号
    url(r'^docs/',docs),
    url(r'^',include(router.urls)),
    # url(r'^$',views.api_root),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]