from django.db import models

class Video(models.Model):
    video_file = models.FileField(upload_to='videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    prediction = models.CharField(max_length=100, blank=True)
    confidence = models.FloatField(default=0.0)

    def __str__(self):
        return self.video_file.name
