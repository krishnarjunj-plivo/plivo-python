# -*- coding: utf-8 -*-
"""Call transcription resource."""

from plivo.base import PlivoResource, PlivoResourceInterface


class Transcript(PlivoResource):
    _name = 'Transcript'
    _identifier_string = 'transcript_uuid'

    def get(self):
        return self.client.transcripts.get(self.id)


class Transcripts(PlivoResourceInterface):
    _resource_type = Transcript

    def create(self, call_uuid, transcription_url=None, language='en-US'):
        """Request a transcript for a completed call recording.

        Args:
            call_uuid: UUID of the call to transcribe.
            transcription_url: Optional webhook URL to POST the transcript to.
            language: BCP-47 language code; defaults to 'en-US'.
        """
        return self.client.request(
            'POST',
            ('Call', call_uuid, 'Transcript'),
            {'transcription_url': transcription_url, 'language': language},
        )
