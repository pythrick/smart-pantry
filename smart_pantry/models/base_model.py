from smart_pantry.models.mixins import TimestampMixin, UUIDMixin
from tortoise import Model


class AbstractBaseModel(UUIDMixin, TimestampMixin, Model):
    class Meta:
        abstract = True

    def __str__(self):
        return str(self.pk)

    def __repr__(self):
        return f"{self.__class__.__name__}<{self}>"
