from django.conf.urls import patterns, include, url

from rest_framework_nested import routers

from thinkster_django_angular_boilerplate.views import IndexView
from authentication.views import AccountViewSet, LoginView, LogoutView

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

urlpatterns = patterns(
    '',
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),
    url(r'^api/v1/', include(router.urls, app_name='API endpoint for JS Client')),

    url('^.*$', IndexView.as_view(), name='index'),
)
