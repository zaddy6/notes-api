from django.urls import path
from rest_framework.routers import SimpleRouter
from notes.views import NoteView

router = SimpleRouter()

router.register('notes', NoteView, base_name="notes")

urlpatterns = router.urls

