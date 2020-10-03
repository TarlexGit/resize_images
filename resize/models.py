from django.db import models 
from django.urls import reverse
# Create your models here.


class Image_model(models.Model):
    # title = models.CharField(max_length=50, blank=True, null=True)
    image_file = models.FileField(blank=True, null=True, upload_to='static/img/',max_length=255)
    
    # def __str__(self):
    #     return self.title
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of the model.
        """
        return reverse('model-detail-view', args=[str(self.id)])