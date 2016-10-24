from __future__ import absolute_import

import re
import logging

from rest_framework import serializers

from ..models import User

logger = logging.getLogger(__name__)


def is_valid_mobile_number(value):
    pattern = re.compile('^[0-9]*$')
    if pattern.match(value):
        return True
    else:
        raise serializers.ValidationError('Not a valid mobile number.')


class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)