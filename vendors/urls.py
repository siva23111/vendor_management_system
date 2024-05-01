from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import VendorViewSet, home, vendor_list, vendor_create, vendor_update, vendor_delete, purchase_order_list, purchase_order_create, purchase_order_update, purchase_order_delete, historical_performance_list, historical_performance_create, historical_performance_update, historical_performance_delete

#for API endpoints
router = DefaultRouter()
router.register(r'vendors', VendorViewSet)


urlpatterns = [
    path('', home, name='home'),
    # path('', include(router.urls)),
    path('vendors/', vendor_list, name='vendor-list'),
    path('vendors/create/', vendor_create, name='vendor-create'),
    path('vendors/<int:pk>/update/', vendor_update, name='vendor-update'),
    path('vendors/<int:pk>/delete/', vendor_delete, name='vendor-delete'),
    path('purchase-orders/', purchase_order_list, name='purchaseorder-list'),
    path('purchase-orders/create/', purchase_order_create, name='purchaseorder-create'),
    path('purchase-orders/<int:pk>/update/', purchase_order_update, name='purchaseorder-update'),
    path('purchase-orders/<int:pk>/delete/', purchase_order_delete, name='purchaseorder-delete'),
    path('historicalperformances/', historical_performance_list, name='historicalperformance-list'),
    path('historicalperformances/create/', historical_performance_create, name='historicalperformance-create'),
    path('historicalperformances/<int:pk>/update/', historical_performance_update, name='historicalperformance-update'),
    path('historicalperformances/<int:pk>/delete/', historical_performance_delete, name='historicalperformance-delete'),
]
