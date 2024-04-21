from django.conf.urls.static import static
from django.urls import path

from business_api import views
from django.conf import settings as conf_settings

urlpatterns = [
    path('', views.home, name='home'),
    path('generate_token', views.generate_token, name='generate_token'),
    path('regenerate_token', views.regenerate_token, name='regenerate_token'),
    path('get_user_token', views.get_user_token, name='get_user_token'),

    path('api/initiate_mtn', views.initiate_mtn_transaction, name='initiate_mtn_transaction'),
    path('api/initiate_ishare', views.initiate_ishare_transaction, name='ishare_transaction'),
    path('api/initiate_big_time', views.initiate_big_time, name='big_time'),
    path('api/initiate_wallet_topup', views.wallet_topup, name='wallet_topup'),

    path('paystack_webhook', views.paystack_webhook, name='paystack_webhook'),


    path('elevated/api/initiate_mtn', views.admin_initiate_mtn_transaction, name='initiate_mtn_transaction'),
    path('elevated/api/initiate_ishare', views.admin_initiate_ishare_transaction, name='ishare_transaction'),
    path('elevated/api/initiate_big_time', views.admin_initiate_big_time, name='big_time'),

] + static(conf_settings.STATIC_URL, document_root=conf_settings.STATIC_ROOT)

