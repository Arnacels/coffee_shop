from django.conf.urls import url
from .views import UserCreate, AccountList, CreateCard
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^createuser/$', UserCreate.as_view(), name='account-create'),
    url(r'^viewusers/$', AccountList.as_view(), name='account-view'),
    url(r'^createnewcard/$', CreateCard.as_view(), name='card-create')
]

urlpatterns = format_suffix_patterns(urlpatterns)
