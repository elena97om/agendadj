from django.shortcuts import render

from django.views.generic import (
    ListView,
    TemplateView,
)
#
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView, #equivalente a createview
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView, # actualizar recuperando los datos
)
#
from .models import Person, Reunion
#
from .serializers import (
    PersonSerializer,
    PersonaSerializer,
    PersonaSerializer2,
    ReunionSerializer,
    PersonaSerializer3,
    ReunionSerializer2,
    ReunionSerializerLink,
    PersonPagination,
    CountReunionSerializer,
)


class ListaPersonas(ListView):
    template_name = "persona/persona.html"
    context_object_name = 'personas'

    def get_queryset(self):
        return Person.objects.all()

class PersonListApiView(ListAPIView):

    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()

class PersonListView(TemplateView):
    template_name = 'persona/lista.html'

class PersonSearchApiView(ListAPIView):

    serializer_class = PersonSerializer

    def get_queryset(self):
        # filtramos datos
        kword = self.kwargs['kword']
        return Person.objects.filter(
            full_name__icontains=kword
        )


class PersonCreateView(CreateAPIView):
    # se ejecuta un método post
    serializer_class = PersonSerializer

class PersonDetailView(RetrieveAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PersonDeleteView(DestroyAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PersonUpdateView(UpdateAPIView):
    # se ejecuta un método put
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PersonRetriveUpdateView(RetrieveUpdateAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PersonApiLista(ListAPIView):
    # Vista para interactuar con serializadores

    # serializer_class = PersonaSerializer
    serializer_class = PersonaSerializer3

    def get_queryset(self):
        return Person.objects.all()

class ReunionApiLista(ListAPIView):

    serializer_class = ReunionSerializer

    def get_queryset(self):
        return Reunion.objects.all()

class ReunionApiListaLink(ListAPIView):
    serializer_class = ReunionSerializerLink

    def get_queryset(self):
        return Reunion.objects.all()


class PersonPaginationList(ListAPIView):
    # Lista personas con paginacion

    serializer_class = PersonaSerializer
    pagination_class = PersonPagination

    def get_queryset(self):
        return Person.objects.all()


class ReunionByPersonJob(ListAPIView):

    serializer_class = CountReunionSerializer

    def get_queryset(self):
        return Reunion.objects.cantidad_reuniones_job()