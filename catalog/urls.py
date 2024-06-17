from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView
from catalog.views import ContactListView
from catalog.views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactListView.as_view(), name='contacts'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('product/create', ProductCreateView.as_view(), name='create_product'),
    path('product/update/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='delete_product'),

    path('blog/', ArticleListView.as_view(), name='blog'),
    path('blog/<int:pk>', ArticleDetailView.as_view(), name='view_article'),
    path('blog/create', ArticleCreateView.as_view(), name='create_article'),
    path('blog/update/<int:pk>', ArticleUpdateView.as_view(), name='update_article'),
    path('blog/delete/<int:pk>', ArticleDeleteView.as_view(), name='delete_article'),
]
