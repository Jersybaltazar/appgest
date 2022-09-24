
from django.urls import path, re_path

from .views import barcode_view, product_rpc_view, purchase_order_sheet_view, k_sales_view

urlpatterns = [
    path('barcode', barcode_view, name='barcode'),
    path('purchase-order-sheet', purchase_order_sheet_view, name='purchase_order_sheet'),
    path('k-sales', k_sales_view, name='k_sales'),
    re_path(r"^product-rpc/(|product-product|purchase-order|reports|refunds)", product_rpc_view, name='product_rpc'),
]
