from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination

from .models import Employee
from .serializers import EmployeeSerializer


# Custom pagination class for Employee APIs
# Controls how many records are returned per page
class EmployeePagination(PageNumberPagination):
    page_size = 10                     # Default number of records per page
    page_size_query_param = 'page_size'  # Allows client to change page size via query param
    max_page_size = 100                # Maximum limit for page size


# ViewSet for handling all CRUD operations related to Employee
class EmployeeViewSet(viewsets.ModelViewSet):
    # Fetch all employee records
    queryset = Employee.objects.all()

    # Serializer used to convert Employee objects to JSON and vice versa
    serializer_class = EmployeeSerializer

    # Only authenticated users can access this API
    permission_classes = [IsAuthenticated]

    # Apply custom pagination
    pagination_class = EmployeePagination

    # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Fields allowed for filtering
    filterset_fields = ['department', 'role']

    # Fields used for search functionality
    search_fields = ['name', 'email']

    # Fields allowed for sorting the results
    ordering_fields = ['date_joined', 'name']


    # Override create method to customize employee creation
    def create(self, request, *args, **kwargs):
        # Validate incoming request data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Save employee record to database
        self.perform_create(serializer)

        # Prepare response headers
        headers = self.get_success_headers(serializer.data)

        # Return created employee data with HTTP 201 status
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )


    # Override destroy method to customize delete behavior
    def destroy(self, request, *args, **kwargs):
        # Fetch the employee object to be deleted
        instance = self.get_object()

        # Delete employee from database
        self.perform_destroy(instance)

        # Return HTTP 204 No Content on successful deletion
        return Response(status=status.HTTP_204_NO_CONTENT)