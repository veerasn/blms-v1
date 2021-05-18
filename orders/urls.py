from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers

from . import views
from .views import PersonItemViewSet

router = routers.DefaultRouter()
router.register('person-item', PersonItemViewSet, basename='person-item')

urlpatterns = [
    url(r'^review/$', views.personApi),
    url(r'^review/[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-b]{3}-[0-9a-f]{12}$', views.personApi),
    path('', include(router.urls)),
    path('', views.index, name='index'),
    path('<uuid:person_id>/', views.detail, name='detail'),
    path('<uuid:person_id>/patient/', views.patient, name='patient'),
    path('<uuid:patient_id>/order/', views.order, name='order'),
]
