from django.db import models


class Project(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    technologies = models.CharField(
        max_length=300,
        blank=True
    )

    image = models.CharField(
        max_length=300,
        blank=True
    )

    github_link = models.URLField(
        blank=True
    )

    live_link = models.URLField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.title


class ContactMessage(models.Model):

    name = models.CharField(
        max_length=100
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return f"{self.name} - {self.email}"