from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique module instances

class Content_Type(models.Model):
    """Model representing a module type."""
    name = models.CharField(max_length=200, help_text='Enter a module type (e.g. Saftey or Benefit)')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Module(models.Model):
    """Model representing a training module."""
    title = models.CharField(max_length=200)

    # Foreign Key used because the training module can only have one instructor, but instructor can have multiple training module
    instructor = models.ForeignKey('Instructor', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the training module')
    code = models.CharField('CODE', max_length=10, unique=True, 
                            help_text='')
    # ManyToManyField used because type can contain many module. Module can cover many types.
    content_type = models.ManyToManyField(Content_Type, help_text='Select a type for this module')
    
    class Meta:
        ordering = ['title']

    def display_content_type(self):
        """Create a string for the content_type. This is required to display type in Admin."""
        return ', '.join(content_type.name for content_type in self.content_type.all()[:3])
    
    display_content_type.short_description = 'Type'
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this module."""
        return reverse('module-detail', kwargs={'pk': self.pk })

    def __str__(self):
        """String for representing the Model object."""
        return self.title

class ModuleInstance(models.Model):
    """Model representing a specific module status."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular module in the training')
    module = models.ForeignKey('Module', on_delete=models.SET_NULL, null=True) 
    imprint = models.CharField(max_length=200)
    start_date = models.DateField(null=True, blank=True)

    MODULE_STATUS = (
        ('N', 'Not started'),
        ('P', 'On progress'),
        ('D', 'Done'),
        
    )

    status = models.CharField(
        max_length=1,
        choices=MODULE_STATUS,
        blank=True,
        default='N',
        help_text='Not Started',
    )

    class Meta:
        ordering = ['start_date']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.module.title})'

class Instructor(models.Model):
    """Model representing an instructor."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    class Meta:
        ordering = ['last_name']
    

    def get_absolute_url(self):
        """Returns the url to access a particular instructor instance."""
        return reverse('instructor-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

    