from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User
from .serializers import UserSerializer

# Create your views here.


@api_view(['GET','POST'])
def hellorest(request):

    if request.method=='POST':
        return Response(data={"message":"Post Request"},status=status.HTTP_200_OK)
    else:
      return Response(data={"message":20},status=status.HTTP_200_OK)
# @api_view(['GET','POST'])
# def student(request):

    if request.method=='POST':
        return Response(data={"message":"Post Request"},status=status.HTTP_200_OK)
    else:
      students = Student.objects.all() #query set and i want return json response
      student_list = []
      for student in students:
         student_list.append({
            'name':student.name,
            'age':student.age,
            'gpa':str(student.gpa)
         })
      return Response(data={"students":student_list},status=status.HTTP_200_OK)


@api_view(['GET','POST'])
def student(request):

    if request.method=='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(data="Student Created Successfully",status=status.HTTP_201_CREATED)
        else:
           return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    else:
      students = Student.objects.all() #query set and i want return json response
      #serialize convert queryset to json and deserialize json to queryset
      serializer=StudentSerializer(students,many=True)

      return Response(data=serializer.data,status=status.HTTP_200_OK)



class StudentClassBasedView(APIView):
    # def get(self,request):
    #     students = Student.objects.all()
    #     serializer=StudentSerializer(students,many=True)
    #     return Response(data=serializer.data,status=status.HTTP_200_OK)



    # def post(self,request):
    #     serializer=StudentSerializer(data=request.data)
    #     if serializer.is_valid():
    #        serializer.save()
    #        return Response(data="Student Created Successfully",status=status.HTTP_201_CREATED)
    #     else:
    #        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    def getObject(self,request,pk):
        try:
            return Student.objects.get(pk=pk)
        except Exception as e:
            return Response(data=str(e),status=status.HTTP_404_NOT_FOUND)


    def get(self,request,pk):
      try:
         student=Student.objects.get(pk=pk)
         serializer=StudentSerializer(student)
         return Response(data=serializer.data,status=status.HTTP_200_OK)
      except Exception as e:
         return Response(data=str(e),status=status.HTTP_404_NOT_FOUND)




    def put(self,request,pk,partial_status=False):
        try:
            student=Student.objects.get(pk=pk) # i need convert this student object to json and also convert json to student object after update
            # data in serializer is request.data which is json while instance is student object from db
            serializer=StudentSerializer(instance=student,data=request.data,partial=partial_status) #to edit on this existing student object
            if serializer.is_valid():
                serializer.save()
                return Response(data="Student Updated Successfully",status=status.HTTP_200_OK)
            else:
                return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(data=str(e),status=status.HTTP_404_NOT_FOUND)

    def patch(self,request,pk):
        return self.put(request,pk,partial_status=True)
    def delete(self,request,pk):
        try:
            student=Student.objects.get(pk=pk)
            student.delete()
            return Response(data="Student Deleted Successfully",status=status.HTTP_200_OK)
        except Exception as e:
            return Response(data=str(e),status=status.HTTP_404_NOT_FOUND)





# Generic Views for Student get and post
class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Generic Views for Student retrieve , update , destroy
class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class UserListCreate(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer




