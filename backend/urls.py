from django.urls import path, include
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm
from .views import RegisterUser, LoginUser, UserDetails, ContactView, \
    ProviderUpdate, ProviderState, ProductView, BasketView, OrderView, ProviderOrders, CategoryViewSet, ShopView, \
    ConfirmAccount
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'categories',
                CategoryViewSet, basename="category")

app_name = 'backend'

urlpatterns = [
    path('', include(router.urls)),
    path('user/register', RegisterUser.as_view(), name='user-register'),
    path('user/register/confirm', ConfirmAccount.as_view(), name='user-register-confirm'),
    path('user/login', LoginUser.as_view(), name='user-login'),
    path('user/contact', ContactView.as_view(), name='user-contact'),
    path('user/details', UserDetails.as_view(), name='user-details'),
    path('user/password_reset', reset_password_request_token, name='password-reset'),
    path('user/password_reset/confirm', reset_password_confirm, name='password-reset-confirm'),
    path('shops', ShopView.as_view(), name='shops'),
    path('products', ProductView.as_view(), name='products'),
    path('partner/update', ProviderUpdate.as_view(), name='partner-update'),
    path('partner/state', ProviderState.as_view(), name='partner-state'),
    path('partner/ord', ProviderOrders.as_view(), name='partner-shopAPI'),
    path('basket', BasketView.as_view(), name='basket'),
    path('order', OrderView.as_view(), name='order'),
]