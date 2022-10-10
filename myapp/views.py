from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import *


# Create your views here.
def home(request):
    return HttpResponse("home")


class Myview(View):
    def get(self, request):
        return HttpResponse("get")

    def post(self, request):
        return HttpResponse("post")


from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


class ProtectedView(TemplateView):
    template_name = 'secrets.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView


class PublisherListView(ListView):
    model = Publisher
    context_object_name = 'name_for_variable_in_template'

    # queryset = Publisher.objects.all().order_by("-id")  # use this if you wants to override filter data, no need to write default

    def get_queryset(self):
        """use this if you wants to override filter with dynamic content"""
        query = self.request.GET.get('query', None)  # get query parameter
        print(query)
        return Publisher.objects.filter(book__authors__id=self.request.user.id).order_by('-id')[:5]


class PublisherDetailView(DetailView):
    model = Publisher
    context_object_name = "publishers"  # default is object
    template_name = 'myapp/publisher_detail.html'
    queryset = Publisher.objects.all()
    pk_url_kwarg = "id"  # default is pk

    # def get_object(self):
    #         """if wants to modifies data on detail """
    #     obj = super().get_object()
    #
    #     # Record the last accessed date
    #     obj.last_accessed = timezone.now()
    #     obj.save()
    #     return obj

    # def get_context_data(self, **kwargs):
    #     """ override everything here"""
    #
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #
    #     # Add in a QuerySet of all the books
    #     context['book_list'] = Book.objects.all()
    #     return context


class PublisherDeleteView(DeleteView):
    model = Publisher
    queryset = Publisher.objects.all()
    success_url = "/"


class PublisherCreateView(CreateView):
    model = Publisher
    queryset = Publisher.objects.all()
    fields = "__all__"
    success_url = "/"


class PublisherUpdateView(UpdateView):
    model = Publisher
    fields = "__all__"
    success_url = "/"
