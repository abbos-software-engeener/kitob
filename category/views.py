from api import serializer
from .serializer import *
from user.responses import ResponseFail, ResponseSuccess
from rest_framework.response import Response
from .models import *
from rest_framework.views import APIView
from .filter import *
from rest_framework.generics import CreateAPIView


def get_object_or_None(model, pk: int):
    try:
        return model.objects.get(id=pk)
    except:
        return None


class CategoryView(APIView):
    def __init__(self, **kwargs) -> None:
        self.MODEL = Category
        self.SERIALIZER = CategorySerializer
        self.GETSERIALIZER = CategoryGetSerializer 
        self.FILTER = CategoryFilter
        super().__init__(**kwargs)


    def list(self, request):
        queryset = self.MODEL.objects.all()
        filter = self.FILTER(request.GET, queryset=queryset)
        queryset = filter.qs
        serializer = self.GETSERIALIZER(queryset, many=True)
        return ResponseSuccess(serializer.data)


    def get(self, request, pk=None):
        if pk:
            queryset = get_object_or_None(self.MODEL, pk)
            if queryset:
                serializer = self.SERIALIZER(queryset, many=False)
                return ResponseSuccess(serializer.data)

            else:
                return ResponseFail('object not found')

        queryset = self.MODEL.objects.all()
        serializer = self.GETSERIALIZER(queryset, many=True)
        return Response(serializer.data)

    
class SubCategoryView(APIView):
    def __init__(self, **kwargs) -> None:
        self.MODEL = SubCategory
        self.SERIALIZER = SubCategorySerializer
        self.FILTER = CategoryFilter
        super().__init__(**kwargs)


    def list(self, request):
        queryset = self.MODEL.objects.all()
        filter = self.FILTER(request.GET, queryset=queryset)
        queryset = filter.qs
        serializer = self.SERIALIZER(queryset, many=True)
        return ResponseSuccess(serializer.data)


    def get(self, request, pk=None):
        if pk:
            queryset = get_object_or_None(self.MODEL, pk)
            if queryset:
                serializer = self.SERIALIZER(queryset, many=False)
                return ResponseSuccess(serializer.data)

            else:
                return ResponseFail('object not found')

        queryset = self.MODEL.objects.all()
        serializer = self.SERIALIZER(queryset, many=True)
        return Response(serializer.data)


class ContactView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
