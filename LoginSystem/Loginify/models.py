from django.db import models

# Create your models here.
class UserDetails(models.Model):
    username = models.CharField(max_length=50,primary_key=True)
    password = models.CharField(max_length=12,blank=True)
    email = models.EmailField(unique=True,max_length=50)
    
    class Meta: # It is used to define the metadata of the model
        ordering = ('username',) # It will order the categories by name
        verbose_name_plural = 'UserDetails' # It will change the name of the model in the admin page
    
    def __str__(self): # It will return the name of the category
        return self.username + ' ' + self.email+   ' ' + self.password