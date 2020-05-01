from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
# from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import Studenterializer, StudenterializerModel
from .models import Student
from rest_framework import status
# import json
from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import  mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework import viewsets
##########################
## Start wokirng with function based rest api implementation
#########################
@csrf_exempt
def studet_list(request):
    if request.method == 'GET':
        students = Student.objects.all()
        # serializer = Studenterializer(students, many=True)
        serializer = StudenterializerModel(students, many=True)
        return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = StudenterializerModel(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def student_detail(request, pk=None):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return JsonResponse({"msg":"Requested "
                                              "resource is not "
                                              "available"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudenterializerModel(student)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        print("put is calling")
        data = JSONParser().parse(request)
        print("data", data)
        serializer = StudenterializerModel(student, data=data)
        if serializer.is_valid():
            print()
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PATCH":
        data = JSONParser().parse(request)
        serializer = StudenterializerModel(student, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        student.delete()
        return JsonResponse({"msg":"resource deleted successfully"},
                            status=status.HTTP_204_NO_CONTENT)

##########################
## End wokirng with functional base api
#########################
######################################################################################################################
##########################
## Start wokirng with functional base api View using api_view decorator
#########################
@api_view(['GET', 'POST'])
def studet_list_v2(request):
    if request.method == 'GET':
        students = Student.objects.all()
        # serializer = Studenterializer(students, many=True)
        serializer = StudenterializerModel(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = StudenterializerModel(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','PATCH','DELETE'])
def student_detail_v2(request, pk=None):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({"msg":"Requested resource is not available"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudenterializerModel(student)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = StudenterializerModel(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PATCH":
        serializer = StudenterializerModel(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        student.delete()
        return Response({"msg":"resource deleted successfully"},
                            status=status.HTTP_204_NO_CONTENT)


##########################
## end wokirng with functional based api View using api_view decorator
#########################

##########################
## Start wokirng with classe based rest api view using APIView class in restframework
#########################
class StudetListAPIView(APIView):

    def get(self, request, *args, **kwargs):
        students = Student.objects.all()
        # serializer = Studenterializer(students, many=True)
        serializer = StudenterializerModel(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = StudenterializerModel(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            student = Student.objects.get(pk=pk)
            return student
        except Student.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        student = self.get_object(pk)
        serializer = StudenterializerModel(student)
        if student:
            return Response(serializer.data)
        else:
            return Response({"msg": "Requested resource is not available"},
                     status=status.HTTP_404_NOT_FOUND)


    def put(self, request, pk, *args, **kwargs):
        student = self.get_object(pk)
        serializer = StudenterializerModel(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, *args, **kwargs):
        student = self.get_object(pk)
        serializer = StudenterializerModel(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        student = self.get_object(pk)
        if student:
            student.delete()
            return Response({"msg":"resource deleted successfully"},
                            status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"msg": "Requested resource is not available"},
                            status=status.HTTP_404_NOT_FOUND)

##########################
## end wokirng with classe based rest api view using APIView class in restframework
#########################
###########################################################################################

##########################
## Start wokirng with classe based rest api view using Genericview and mixins restframework classes
#########################
class StudentListGenericAPIView(generics.GenericAPIView,mixins.ListModelMixin,
                                mixins.CreateModelMixin):
    serializer_class = StudenterializerModel
    queryset = Student.objects.all()
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class StudentDetailGenericAPIView(generics.GenericAPIView, mixins.RetrieveModelMixin,
                                   mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = StudenterializerModel
    queryset = Student.objects.all()
    lookup_field = 'id'
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        return self.retrieve(request,id)

    def put(self, request, id=None):
        return self.update(request,id)

    # def patch(self, request, id=None):
    #     return self.partial_update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)


##########################
## End wokirng with classe based rest api view using Genericview and mixins restframework classes
#########################
#####################################################################################################


#######################################
## Start working with class based rest api view using Viewsets & Routers restframework classes
########################################
class StudentViewSet(viewsets.ViewSet):

    def list(self, request):
        students = Student.objects.all()
        serializer = Studenterializer(students, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = Studenterializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        student = get_object_or_404(Student, pk=pk)
        serializer = Studenterializer(student)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudenterializerModel(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudenterializerModel(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        student = get_object_or_404(Student, pk=pk)
        if student:
            student.delete()
            return Response({"msg": "resource deleted successfully"},
                            status=status.HTTP_204_NO_CONTENT)

#######################################
## End working with class based rest api view using Viewsets & Routers restframework classes
########################################
##################################################################################################
#######################################
## Start working with class based rest api view using Viewsets & Routers restframework classes
########################################
class StudentGenericViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,
                            mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class = Studenterializer
    queryset = Student.objects.all()
    # lookup_field = 'roll_no'

#######################################
## End working with class based rest api view using Viewsets & Routers restframework classes
########################################
####################################################################################################
#######################################
## Start working with class based rest api view using Viewsets & Routers restframework classes
########################################
class StudentModelViewSet(viewsets.ModelViewSet):
    serializer_class = Studenterializer
    queryset = Student.objects.all()
    # lookup_field = 'pk'

    # def update(self, request, pk=None):
    #     student = get_object_or_404(Student, pk=pk)
    #     serializer = StudenterializerModel(student, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#######################################
## End working with class based rest api view using Viewsets & Routers restframework classes
########################################