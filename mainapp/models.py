import random
from django.db import models
from django.utils.text import slugify


class TimestampedModel(models.Model):
    """
    Abstract base model class for timestamped models.

    This class provides fields to automatically track the creation and
    last update timestamps for models inheriting from it.

    Attributes:
        created_at (DateTimeField): A field that stores the datetime when the
            model instance was created. Automatically set to the current datetime
            when a new instance is saved to the database.
        updated_at (DateTimeField): A field that stores the datetime when the
            model instance was last updated. Automatically updated to the current
            datetime whenever the instance is saved to the database.

    Meta:
        abstract (bool): Indicates that this model should not have its own database table.
            Instead, it serves as a base class for other models to inherit from.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class RandomizeableModel(models.Model):
    """
    Abstract base model class for models with a method to retrieve a random item.

    This class provides a class method `get_random_item()` to retrieve a random
    instance of the model. It selects a random item from the queryset using the
    specified manager.

    Attributes:
        None

    Meta:
        abstract (bool): Indicates that this model should not have its own database table.
            Instead, it serves as a base class for other models to inherit from.
    """
    class Meta:
        abstract = True  # Avoid creating table for this model

    @classmethod
    def get_random_item(cls, manager="objects"):
        """
        Retrieve a random item from the model.

        Args:
            manager (str, optional): The name of the manager to use for querying the model.
                Defaults to 'objects'.

        Returns:
            RandomizeableModel: A random instance of the model.

        Raises:
            ValueError: If the specified manager does not exist for the model.
            DoesNotExist: If no items are found in the database.
        """
        manager_instance = getattr(cls, manager)
        all_ids = manager_instance.values_list("id", flat=True)
        random_id = random.choice(all_ids)
        random_item = manager_instance.get(pk=random_id)

        return random_item

class SluggableByNameModel(models.Model):
    """
    A Django base model class for creating slug fields based on the 'name' field.
    This class automatically generates a slug from the 'name' field and ensures its uniqueness.
    """

    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None) -> None:
        self.slug = slugify(self.name)

        # If 'name' field is updated, include 'slug' in update_fields to ensure it's updated
        if update_fields is not None and "name" in update_fields:
            update_fields = {"slug"}.union(update_fields)

        return super().save(force_insert, force_update, using, update_fields)
