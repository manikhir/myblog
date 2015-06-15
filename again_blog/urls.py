from django.conf.urls import patterns, include, url
from django.contrib import admin
from blogs import views
from django.conf.urls.static import static
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns(
    '',
    (r'^comments/', include('django.contrib.comments.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', 'blogs.views.login'),
    url(r'^home/', views.home_page,name='home_page'),
    url(r'^logout/$', 'blogs.views.logout'),
    url(r'accounts/profile/', views.profile, name='userprofile'),
    url(r'^blog/addcategory/',views.addcategory,name='new_category'),
    url(r'^blog/newblog/',views.newblog,name='new_blog'),
    url(r'^blog/allblog/',views.allblog,name='all_blog'),
    url(r'^sales-image/(?P<sales_id>[a-zA-Z0-9-]+)/$',
    views.show_salesimage,
    name="show_sales_image"),

    url(r'^blog/post_detail/(?P<category_id>\d+)/$', views.detail, name='post_detail'),
    url(r'^blog/edit/(?P<post_id>\d+)/$',views.edit_blog,name='edit_blog'),
    url(r'^blog/delete/(?P<post_id>\d+)/$',views.delete_blog,name='delete_blog'),
    url(r'^blog/single/(?P<post_id>\d+)', views.single, name='single'),
    url(r'^comment/delete/(\d+)/$',views.delete_own_comment,name='comment-delete'),
    url('^blog/(?P<slug>\d+)/comment/edit/(?P<message_id>\d+)/$',  views.edit_own_comment,name='comment-edit'),
    url(r'^ajax_get_tags/$', 'blogs.ajax.ajax_get_tags', name='ajax_get_tags'),
    url(r'^delete-image/(?P<id>\d+)/$',views.delete_image,name="delete_image"),
    
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)