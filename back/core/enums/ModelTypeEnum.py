from enum import Enum

from core.models import BusinessDomains, Tables
from core.serializers import BusinessDomainsSerializer, TablesSerializer


class ModelTypeEnum(Enum):
    domain = (BusinessDomains, BusinessDomainsSerializer)
    table = (Tables, TablesSerializer)

    def __init__(self, model, serializer):
        self.model = model
        self.serializer = serializer
