from django.urls import path

from photo.views import IndexView, AddPhotoView, PhotoDetail, PhotoUpdateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add_post/', AddPhotoView.as_view(), name='add_photo'),
    path('photo/<int:pk>', PhotoDetail.as_view(), name='details'),
    path('photo/<int:pk>/update', PhotoUpdateView.as_view(), name='photo_update'),
]
