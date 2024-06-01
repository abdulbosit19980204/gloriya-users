from django.urls import path
from .views import tracker_view, load_data_view, add_chanel_view

urlpatterns = [
    path('channels/', tracker_view, name='tracker'),
    path('load-data/', load_data_view),
    path('add-channel/', add_chanel_view, name='add_channel'),

]
