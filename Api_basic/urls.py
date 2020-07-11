from django.urls import path,include
from Api_basic import views as v1
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('article',v1.ArticleViewSet,basename='article')

urlpatterns = [
    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>',include(router.urls)),
    #path('article/',v1.article_list),
    path('article/',v1.ArticleView.as_view()),
    #path('detail/<int:pk>/',v1.article_detail),
    path('detail/<int:id>/',v1.ArticleDetail.as_view()),
    path('generic/article/<int:id>/',v1.GenericAPIView.as_view()),
]
