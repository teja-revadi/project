from django.urls import path, include
from rest_framework.routers import DefaultRouter
from notes.views import NoteViewSet,object_list_view,edit_note,create_note

router = DefaultRouter()
router.register(r'notes', NoteViewSet)

urlpatterns = [
    path('home/',object_list_view, name='object_list'),
    path('home/<int:note_id>/edit/', edit_note, name='edit_note'),
    path('home/create/', create_note, name='create_note'),
    path('', include(router.urls)),
]











