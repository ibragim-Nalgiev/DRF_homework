import re

from rest_framework.serializers import ValidationError


class LinkValidator:
    ALLOWED_HOST = 'youtube.com'

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        match = re.search(LinkValidator.ALLOWED_HOST, tmp_val)
        if not match:
            raise ValidationError("Недопустимая ссылка для видео")
