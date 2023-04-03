from django.urls import path

from mynexthome.comments.views import CommentList, CommentCreate, CommentDetails, CommentUpdate, CommentDelete


urlpatterns = (
    path('', CommentList.as_view(), name='list'),
    path('create', CommentCreate.as_view(), name='create'),
    path('update/<int:id>', CommentUpdate.as_view(), name='update'),
    path('delete/<int:id>', CommentDelete.as_view(), name='delete'),
    path('details/<int:id>', CommentDetails.as_view(), name='details'),
)