from django.db import models


class AnimalImage(models.Model):
    url = models.URLField()
    species = models.CharField(
        default='cat',
        max_length=5,
        choices=[('cat', 'Cat'), ('dog', 'Dog')],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(
        default='png',
        max_length=5,
        choices=[('png', 'png'), ('gif', 'gif'), ('jpg', 'jpg'), ('jpeg', 'jpeg')],
    )
