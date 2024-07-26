from django.urls import path, re_path,include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from .views import statistical, users, specs, images,skus,orders,permissions,group,admin,options,spus,login

urlpatterns = [
    # 登录
    path('token/', login.MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # --------------  数据统计 -----------------
    # 用户总量
    path(r'statistical/total_count/', statistical.UserCountView.as_view()),
    # 日增用户
    path(r'statistical/day_increment/', statistical.UserDayCountView.as_view()),
    # 日活用户
    path(r'statistical/day_active/', statistical.UserDayActiveCountView.as_view()),
    # 下单用户
    path(r'statistical/day_orders/', statistical.UserDayOrdersCountView.as_view()),
    # 月增用户
    path(r'statistical/month_increment/', statistical.UserMonthCountView.as_view()),

    path(r'statistical/goods_day_views/', statistical.UserGoodsCountView.as_view()),

    # ------------- 用户管理路由--------------
    path(r'users/', users.UserView.as_view()),

    # ------------规格路由表-----------
    path(r'goods/simple/', specs.SpecsView.as_view({'get': 'simple'})),

    path(r'goods/specs/simple/', options.OptionSimple.as_view()),
    # ------------图片路由————————————
    path(r'skus/simple/', images.ImagesView.as_view({'get': 'simple'})),

    # ------------sku路由————————————
    re_path(r'goods/(?P<pk>\d+)/specs/', skus.SKUVIew.as_view({'get': 'specs'})),
    path(r'goods/brands/simple/', spus.SPUGoodsView.as_view({'get': 'brand'})),
    path(r'goods/channel/categories/', spus.SPUGoodsView.as_view({'get': 'channel'})),
    re_path(r'goods/channel/categories/(?P<pk>\d+)/', spus.SPUGoodsView.as_view({'get': 'channels'})),
    # --------权限路由--------
    path(r'permission/content_types/', permissions.PermissionsView.as_view({'get': 'content_type'})),

    path(r'permission/simple/', group.GroupView.as_view({'get': 'simple'})),

    path(r'permission/groups/simple/', admin.AdminView.as_view({'get': 'simple'})),


]

# ----------规格表路由------
router = DefaultRouter()
router.register('goods/specs', specs.SpecsView, basename='specs')
urlpatterns += router.urls

# -------图片表路由------
router = DefaultRouter()
router.register('skus/images', images.ImagesView, basename='images')
urlpatterns += router.urls

# --------sku路由--------
router = DefaultRouter()
router.register('skus', skus.SKUVIew, basename='skus')
urlpatterns += router.urls


# --------订单路由--------
router = DefaultRouter()
router.register('orders', orders.OrderView, basename='orders')

urlpatterns += router.urls


# --------权限路由--------
router = DefaultRouter()
router.register('permission/perms', permissions.PermissionsView, basename='perms')

urlpatterns += router.urls


# --------分组路由--------
router = DefaultRouter()
router.register('permission/groups', group.GroupView, basename='groups')
print(router.urls)
urlpatterns += router.urls


# --------管理员路由--------
router = DefaultRouter()
router.register('permission/admins',admin.AdminView, basename='admin')
print(router.urls)
urlpatterns += router.urls


router = DefaultRouter()
router.register('specs/options', options.OptionsView, basename='options')
print(router.urls)
urlpatterns += router.urls

router = DefaultRouter()
router.register('goods', spus.SPUGoodsView, basename='spus')
print(router.urls)
urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)