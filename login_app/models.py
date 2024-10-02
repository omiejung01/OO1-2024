from django.db import models

# Create your models here.
VOID_CHOICES = (
    ("0", "0"),
    ("1", "1")
)

class AppUser (models.Model):
    # For development only not for production

    UID = models.UUIDField

    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200)

    created_by = models.CharField(max_length=30, default='Auto')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=30, default='Auto')
    void = models.CharField(max_length=1,
                            choices=VOID_CHOICES,
                            default="0")

    def __str__(self):
        return self.email