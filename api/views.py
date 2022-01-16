from .serializer import *
from user.responses import ResponseFail, ResponseSuccess
from rest_framework.response import Response
from .models import *
from rest_framework.views import APIView
from .filter import *


def get_object_or_None(model, pk: int):
    try:
        return model.objects.get(id=pk)
    except:
        return None


class BookView(APIView):
    def __init__(self, **kwargs) -> None:
        self.MODEL = Book
        self.GETSERIALIZER = BookGetSerializer
        self.SERIALIZER = BookSerializer
        self.Filter = BookFilter
        self.FILTER_FIELDS = [
            'title','author','min_price','max_price'
        ]
        super().__init__(**kwargs)


    def list(self, request):
        queryset = self.MODEL.objects.all()
        filter = self.FILTER(request.GET, queryset=queryset)
        queryset = filter.qs
        serializer = self.GETSERIALIZER(queryset, many=True)
        return ResponseSuccess(serializer.data, filter_fields=self.FILTER_FIELDS)


    def get(self, request, pk=None):
        if pk:
            queryset = get_object_or_None(self.MODEL, pk)
            if queryset:
                serializer = self.GETSERIALIZER(queryset, many=False)
                return ResponseSuccess(serializer.data)

            else:
                return ResponseFail('object not found')

        queryset = self.MODEL.objects.all()
        serializer = self.SERIALIZER(queryset, many=True)
        return Response(serializer.data)

  


class BookingView(APIView):
    def __init__(self, **kwargs) -> None:
        self.MODEL = Booking
        self.SERIALIZER = BookingSerializer
        self.GETSERIALIZER = BookingGetSerializer 
        self.FILTER = BookingFilter
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

    def post(self, request):
        serializer = self.SERIALIZER(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseSuccess(serializer.data)
        else:
            return ResponseFail(serializer.errors)

    def delete(self, request, pk=None):
        if pk:
            queryset = get_object_or_None(self.MODEL, pk)
            if queryset:
                queryset.delete()
                return ResponseSuccess('item deleted')

            else:
                return ResponseFail('object not found')

        else:
            return ResponseFail('id required')

    def put(self, request, pk=None):
        if pk:
            queryset = get_object_or_None(self.MODEL, pk)
            if queryset:
                serializer = self.SERIALIZER(data=request.data, instance=queryset)

                if serializer.is_valid():
                    serializer.save()
                    return ResponseSuccess(serializer.data)

                else:
                    return ResponseFail(serializer.errors)

            else:
                return ResponseFail('object not found')

        else:
            return ResponseFail('id required')

    def patch(self, request, pk=None):
        if pk:
            queryset = get_object_or_None(self.MODEL, pk)
            if queryset:
                serializer = self.SERIALIZER(data=request.data, instance=queryset, partial=True)

                if serializer.is_valid():
                    serializer.save()
                    return ResponseSuccess(serializer.data)

                else:
                    return ResponseFail(serializer.errors)

            else:
                return ResponseFail('object not found')

        else:
            return ResponseFail('id required')



class AchievementView(APIView):
    def __init__(self, **kwargs) -> None:
        self.MODEL = Achievement
        self.SERIALIZER = AchievementSerializer
        self.Filter = AchievementFilter
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
                serializer = self.GETSERIALIZER(queryset, many=False)
                return ResponseSuccess(serializer.data)

            else:
                return ResponseFail('object not found')

        queryset = self.MODEL.objects.all()
        serializer = self.SERIALIZER(queryset, many=True)
        return Response(serializer.data)


class AboutUsView(APIView):
    def __init__(self, **kwargs) -> None:
        self.MODEL = AboutUs
        self.GETSERIALIZER = AboutUsGetSerializer
        self.SERIALIZER = AboutUsSerializer
        self.Filter = AboutUsFilter

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
                serializer = self.GETSERIALIZER(queryset, many=False)
                return ResponseSuccess(serializer.data)

            else:
                return ResponseFail('object not found')

        queryset = self.MODEL.objects.all()
        serializer = self.SERIALIZER(queryset, many=True)
        return Response(serializer.data)



  


class CardView(APIView):
    def __init__(self, **kwargs) -> None:
        self.MODEL = Card
        self.SERIALIZER = CardSerializer
        self.GETSERIALIZER = CardGetSerializer
        super().__init__(**kwargs)


    def list(self, request):
        queryset = self.MODEL.objects.all()
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

    def post(self, request):
        serializer = self.SERIALIZER(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return ResponseSuccess(serializer.data)
        else:
            return ResponseFail(serializer.errors)

    def delete(self, request, pk=None):
        if pk:
            queryset = get_object_or_None(self.MODEL, pk)
            if queryset:
                queryset.delete()
                return ResponseSuccess('item deleted')

            else:
                return ResponseFail('object not found')

        else:
            return ResponseFail('id required')

    def put(self, request, pk=None):
        if pk:
            queryset = get_object_or_None(self.MODEL, pk)
            if queryset:
                serializer = self.SERIALIZER(data=request.data, instance=queryset)

                if serializer.is_valid():
                    serializer.save()
                    return ResponseSuccess(serializer.data)

                else:
                    return ResponseFail(serializer.errors)

            else:
                return ResponseFail('object not found')

        else:
            return ResponseFail('id required')

    def patch(self, request, pk=None):
        if pk:
            queryset = get_object_or_None(self.MODEL, pk)
            if queryset:
                serializer = self.SERIALIZER(data=request.data, instance=queryset, partial=True)

                if serializer.is_valid():
                    serializer.save()
                    return ResponseSuccess(serializer.data)

                else:
                    return ResponseFail(serializer.errors)

            else:
                return ResponseFail('object not found')

        else:
            return ResponseFail('id required')
