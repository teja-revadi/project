from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from notes.models import Note
from notes.serializers import NoteSerializer

class NoteViewSetTestCase(TestCase):
    fixtures = ['Notes_fixture.json']
    #There are total 10 test cases in Notes_fixtures.json

    def test_create_note(self):
        #1st test case
        client = APIClient()
        data = {'title': 'Test Note', 'body': 'This is a test note.'}
        response = client.post('/api/notes/', data, format='json')
        #response ok if created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #response ok if title is same
        self.assertEqual(response.data['title'], 'Test Note')
        #response ok if the body is same
        self.assertEqual(response.data['body'], 'This is a test note.')

        #2nd test case without title
        client = APIClient()
        data = {'body': 'This is a test note.'}
        response = client.post('/api/notes/', data, format='json')
        #response ok if created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #response ok if title is same
        self.assertEqual(response.data['title'], 'Test Note')
        #response ok if the body is same
        self.assertEqual(response.data['body'], 'This is a test note.')

        #3rd test case without body
        client = APIClient()
        data = {'title': 'Test Note'}
        response = client.post('/api/notes/', data, format='json')
        #response ok if created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #response ok if title is same
        self.assertEqual(response.data['title'], 'Test Note')
        #response ok if the body is same
        self.assertEqual(response.data['body'], 'This is a test note.')

    def test_get_note_by_pk(self):
        #1st test case
        client = APIClient()
        #Creating Test Case
        data = {'title': 'Test Note', 'body': 'This is a test note.'}
        response = client.get(f'/api/notes/{note.id}/')
        #response ok if there note related to the id
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #response ok if title is same
        self.assertEqual(response.data['title'], note.title)
        #response ok if the body is same
        self.assertEqual(response.data['body'], note.body)

        #2nd test case, id out of range
        client = APIClient()
        response = client.get(f'/api/notes/{1000}/')
        ##response ok if there a note related to the id
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 3rd test case
        client = APIClient()
        response = client.get(f'/api/notes/{7}/')
        #response ok if there a note related to the id
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #response ok if title is same
        self.assertEqual(response.data['title'], "Book Summary - The Great Gatsby")
        #response ok if body is same
        self.assertEqual(response.data['body'], "Summary:\nThe Great Gatsby follows the lives of the narrator, Nick Carraway, and his mysterious neighbor Jay Gatsby. Set in the roaring twenties, the novel explores themes of love, wealth, and the American Dream. Gatsby's obsession with Daisy Buchanan leads to tragedy, highlighting the emptiness of materialism and the illusion of the American Dream.")


    def test_update_note(self):
        #1st test case
        client = APIClient()
        #Newly created test case
        note = Note.objects.create(title='Initial Title', body='Initial body')
        data = {'title': 'Updated Title', 'body': 'Updated body'}
        response = client.put(f'/api/notes/{note.id}/', data, format='json')
        #response ok if updated
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_note = Note.objects.get(pk=note.pk)
        #response ok if title is equal to 'Updated Title'
        self.assertEqual(updated_note.title, 'Updated Title')
        #response ok if body is equal to 'Updated Body'
        self.assertEqual(updated_note.body, 'Updated body')

        #2nd test case invalid id
        client = APIClient()
        data = {'title': 'Updated Title', 'body': 'Updated body'}
        response = client.put(f'/api/notes/{1000}/', data, format='json')
        #response ok if updated
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_note = Note.objects.get(pk=note.pk)
        #response ok if title is equal to 'Updated Title'
        self.assertEqual(updated_note.title, 'Updated Title')
        #response ok if body is equal to 'Updated Body'
        self.assertEqual(updated_note.body, 'Updated body')

    def test_filter_notes_by_title(self):
        client = APIClient()
        note = Note.objects.create(title='hello', body= 'This is a test note.')#Creating Test Case
        response = client.get('/api/notes/?title=he')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        filtered_notes = response.data
        self.assertEqual(len(filtered_notes),3)#True if number of filtered_notes are 3

    