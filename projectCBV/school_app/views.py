from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from school_app import models
# from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return render(request, 'school_app/index.html')

# class CBView(View):
#     def get(self, request):
#         return HttpResponse("Class based views are cool")

class SchoolListView(ListView):# it actually works like it retrieves a list of rows
    context_object_name = 'schools'
    model = models.School
    # because of the previous line and the class extending List view, it returns a list with name lowercase(School)_list i.e. school_list
    # or uncomment the line before "model = models.School" to rename "school_list" to "schools" and use it in html files


class SchoolDetailView(DetailView):# it actually works like it retrieves the cells/data of a row
    context_object_name = 'school_detail' # if you don't write this line or comment this line then the details will be lower case of (school) i.e. school
    model = models.School

    template_name = 'school_app/school_details.html'

class IndexView(TemplateView):
    template_name = "school_app/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION'

        return context
