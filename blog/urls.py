
from django.urls import path

from .views import(
    # blog_post_detail_page,
    blog_post_list_view,
    blog_post_create_view,
    blog_post_update_view,
    blog_post_delete_view,
)

urlpatterns = [
    # re_path(r'^pages?/$', about_page),
    # re_path(r'^about/$', about_page),
    # path('contact/', contact_page),
    # path('example/', example_page),
    # path('admin/', admin.site.urls),
    # path('blog/<str:slug>/', blog_post_detail_page),
    path('', blog_post_list_view),
    # path('blog-new/', blog_post_create_view),
    path('<str:slug>/edit/', blog_post_update_view),
    path('<str:slug>/delete/', blog_post_delete_view),
]
