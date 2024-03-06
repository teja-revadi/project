from notes.models import Note
from rest_framework.response import Response
from notes.serializers import NoteSerializer
from rest_framework import status, viewsets
from django.shortcuts import render, redirect, get_object_or_404
from .forms import NoteForm


class NoteViewSet(viewsets.ModelViewSet):
    # Notes backend api's
    queryset = Note.objects.all().order_by("-created_at")
    serializer_class = NoteSerializer

    def create(self, request, *args, **kwargs):
        data = dict(request.data)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        queryset = super().get_queryset()
        title_substring = self.request.query_params.get('title', None)
        if title_substring:
            queryset = queryset.filter(title__icontains=title_substring)
        return queryset

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


def home_page(request):
    # frontend home page view
    objects = Note.objects.all().order_by("-created_at")

    query = request.GET.get('title')
    if query:
        # Filter objects based on the search query (you might need to adjust this based on your model fields)
        objects = objects.filter(title__icontains=query)

    # Render the template with the list of objects
    return render(request, 'notes/query_list.html', {'object_list': objects})


def edit_note(request, note_id):
    # view to edit a note with frontend
    note = get_object_or_404(Note, id=note_id)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            # Redirect to the list of notes or any other appropriate page
            return redirect('object_list')
    else:
        form = NoteForm(instance=note)

    # Render the template with the note and the form
    return render(request, 'notes/edit_note.html', {'note': note, 'form': form})


def create_note(request):
    # view to create notes from frontend
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('object_list')  # Redirect to the notes list page after creating a new note
    else:
        form = NoteForm()

    return render(request, 'notes/create_note.html', {'form': form})

