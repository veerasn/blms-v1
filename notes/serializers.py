from rest_framework import serializers
from notes.models import Note


class NoteSerializer(serializers.ModelSerializer):
    note = serializers.CharField(max_length=180, allow_blank=False)

    class Meta:
        model = Note
        fields = ['note']
