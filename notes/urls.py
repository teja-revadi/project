from django.urls import path, include
from rest_framework.routers import DefaultRouter
from notes.views import NoteViewSet,home_page,edit_note,create_note

router = DefaultRouter()
router.register(r'notes', NoteViewSet)

urlpatterns = [
    # backend urls
    path('', include(router.urls)),

    # frontend home page
    path('home/', home_page, name='object_list'),
    # frontend notes edit
    path('home/<int:note_id>/edit/', edit_note, name='edit_note'),
    # frontend notes create page
    path('home/create/', create_note, name='create_note'),
]











