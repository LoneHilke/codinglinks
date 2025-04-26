from django.urls import path
from django.conf import settings
from .views import Index, PythonView, DjangoView, Deploy, Terminals, Info, SmallView, Microsoft
from django.views import View
from django.conf.urls.static import static

urlpatterns = [
  path('', Index.as_view(), name='index'),
  path('python/', PythonView.as_view(), name='python'),
  path('django/', DjangoView.as_view(), name='django'),
  path('deploy/', Deploy.as_view(), name='deploy'),
  path('terminals/', Terminals.as_view(), name='terminals'),
  path('info/', Info.as_view(), name='info'),
  path('small/', SmallView.as_view(), name='small'),
  path('m365/', Microsoft.as_view(), name='m365'),
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)