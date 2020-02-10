from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import date
from django.conf import settings
import os
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

GENDER = (
    ('Male', 'M'),
    ('Female', 'F'),
)


def upload_location(instance, filename):
    filebase, extension = filename.split(".")
    return "%s/%s.%s" %(instance.id, instance.id, extension)

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.png', '.jpg', '.jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')



def user_directory_path(request, filename):
	# return "files/users/%s/%s" % (request.user.id, filename)
    return '/'.join(['content', request.student_id, filename])



def increment_student_id():
    last_student = Student.objects.all().order_by('id').last()
    if not last_student:
        return 'BLT00001'
    width = 5
    student_number = last_student.student_id
    student_int = int(student_number.split('BLT')[-1])
    new_student_int = student_int + 1
    formatted = (width - len(str(new_student_int))) * "0" + str(new_student_int)
    new_student_int = 'BLT' + str(formatted)
    return str(new_student_int)


# def increment_student_id():
# 	last_student = Student.objects.all().order_by('id').last()
# 	if not last_product:
# 		return 'BLT00001'
# 	width = 5
# 	product_number = last_student.product_number
# 	product_int = int(product_number.split('BLT')[-1])
# 	new_product_int = product_int + 1
# 	formatted = (width - len(str(new_product_int))) * "0" + str(new_product_int)
# 	new_product_int = 'BLT' + str 


class Student(models.Model): 
    student_id = models.CharField(max_length=500, null=True, blank=True, 
        validators=[RegexValidator(regex='^[a-zA-Z0-9]*$',
        message='Produce number must be Alphanumeric',code='Number is invalide'),], 
        default=increment_student_id)
    first_name_en = models.CharField(max_length=255)
    first_name_kh = models.CharField(max_length=255)
    last_name_en = models.CharField(max_length=255)
    last_name_kh = models.CharField(max_length=255)
    gender = models.CharField(max_length=20, choices=GENDER)
    nationality_en = models.CharField(max_length=30)
    nationality_kh = models.CharField(max_length=30)
    image = models.FileField(blank=True, upload_to=user_directory_path,  validators=[validate_file_extension])
    certificate = models.FileField(blank=True, upload_to=user_directory_path,  validators=[validate_file_extension])
    description_en = models.TextField() 
    description_kh = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_status = models.BooleanField(default=True)
    def __str__ (self):
    	# return self.name + ' ' + str(self.created_at)
    	return str(self.first_name_en) +' ' + str(self.last_name_en)
    class  Meta:
    	ordering = ['-created_at']





