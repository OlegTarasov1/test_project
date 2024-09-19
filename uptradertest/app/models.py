from django.db import models
from django.urls import reverse_lazy


class Menu(models.Model):
    parent_id = models.IntegerField(null = True, blank = True)
    title = models.CharField(max_length = 100)
    url = models.CharField(max_length = 500)

    def get_absolute_url(self):
        # if self.url.split('/')[0] not in ['http:', 'https:', 'ws:', 'wss:']:
        if '/' in self.url:
            return self.url
        else:
            return reverse_lazy(self.url)

    def save(self, *args, **kwargs):
        if self.parent_id:
            try:
                Menu.objects.get(pk = self.parent_id)
                super().save(*args, **kwargs)
            except:
                pass        
        else:
            super().save(*args, **kwargs)   

    def __str__(self):
        return f'obj_{self.pk}'