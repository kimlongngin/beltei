from django.shortcuts import render, redirect, get_object_or_404, Http404, render_to_response
from django.http import HttpResponse
from django.template import loader 
from django.views import generic
from django.urls import reverse_lazy

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.views.generic import View, TemplateView 
from .models import Student
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.template import loader 
from django.views.generic.list import ListView
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator

from django.utils import translation
from django.utils.translation import gettext as _
from django.utils.translation import activate, get_language_info


class IndexView(SuccessMessageMixin, generic.ListView):
	template_name =  'student/index.html'
	context_object_name = 'all_student'
	paginate_by = 5

	def get_queryset(self):
		# user_language = 'km'
		# translation.activate(user_language)
		# self.request.session[translation.LANGUAGE_SESSION_KEY] = user_language
		if translation.LANGUAGE_SESSION_KEY in self.request.session: 
			del self.request.session[translation.LANGUAGE_SESSION_KEY]
		return Student.objects.filter(is_status=True).order_by('-created_at')


class SearchStudentView(ListView):

	model = Student
	template_name = 'student/result_search.html'
	paginate_by = 5

	context = {
		'hello' : _('hello')
	}

	def get(self, request): 
		q = request.GET['q']
		data = Student.objects.filter(student_id=q.strip(), is_status=True) | Student.objects.filter(first_name_en__contains = q.strip(), is_status=True) | Student.objects.filter(last_name_kh__contains = q.strip(), is_status=True)| Student.objects.filter(last_name_en__contains = q.strip(), is_status=True)| Student.objects.filter(nationality_en__contains=q.strip(), is_status=True)| Student.objects.filter(nationality_kh__contains=q.strip(), is_status=True) | Student.objects.filter(first_name_kh__contains = q.strip(), is_status=True)
		return render(request, self.template_name, {'all_student':data, 'title':q, 'hello': _('Hello')})