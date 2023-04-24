from django.urls import path
from mynexthome.users.views import MyObtainTokenPairView, ProfileCreate, RegisterView, LogoutView, UserList, UserDelete, ProfileList, ProfileDelete, ProfileUpdate, ProfileDetails
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('login', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('register', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', UserList.as_view(), name='list'),
    path('delete/<int:id>', UserDelete.as_view(), name='user_delete'),


    path('profile/create', ProfileCreate.as_view(), name='profile_create'),
    path('profile/list', ProfileList.as_view(), name='profile_list'),
    path('profile/update/<int:user_id>', ProfileUpdate.as_view(), name='profile_update'),
    path('profile/delete/<int:id>', ProfileDelete.as_view(), name='profile_delete'),
    path('profile/details/<int:user_id>', ProfileDetails.as_view(), name='profile_details'),
]