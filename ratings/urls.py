from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns=[
    url('^$',views.home,name='home'),
    # url(r'^search/',views.search_category,name='search_category'),
    # url(r'^photo/(\d+)',views.single_photo,name='photo'),
    # url(r'^new/image$', views.new_image, name='new-image'),
    # url(r'^new/profile$', views.new_profile, name='new-profile'),
    # url(r'^updateprofile$',views.updateprofile,name='updateprofile'),
    # url(r'^comment$',views.makecomment,name='makecomment'),
    # url(r'^like$',views.like_a_post,name='like_a_post'),
    # url(r'^follow$',views.follow,name='follow'),
    # url(r'^delete/(?P<post_id>\d+)$',views.delete_post,name='delete'),
    # url(r'displayprofile/(?P<user_id>\d+)$',views.display_profile,name='displayprofile')
    
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


