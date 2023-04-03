from django.urls import path

from mynexthome.properties.views import PropertyList, PropertyCreate, PropertyDetails, PropertyUpdate, PropertyDelete


urlpatterns = (
    path('', PropertyList.as_view(), name='list'),
    path('create', PropertyCreate.as_view(), name='create'),
    path('update/<int:id>', PropertyUpdate.as_view(), name='update'),
    path('delete/<int:id>', PropertyDelete.as_view(), name='delete'),
    path('details/<int:id>', PropertyDetails.as_view(), name='details'),
)