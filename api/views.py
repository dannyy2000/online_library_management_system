from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .Pagination import DefaultPageNumberPagination
from .serializers import BookSerializer, BookCreateSerializer, AuthorSerializer
from book.models import Book, Author
from rest_framework import generics


# Create your views here.
# @api_view(['GET', 'POST'])
# def book_list(request):
#     if request.method == "GET":
#         queryset = Book.objects.all()
#         serializers = BookSerializer(queryset, many=True)
#         return Response(serializers.data)
#     elif request.method == "POST":
#         book = BookCreateSerializer(data=request.data)
#         book.is_valid(raise_exception=True)
#         book.save()
#         return Response("book created successfully")
#
#     # elif request.method == 'DELETE':
#     #     if id is not None:
#     #         try:
#     #             book = Book.objects.get(id=id)
#     #             book.delete()
#     #             return Response("book deleted successfully")
#     #         except Book.DoesNotExist:
#     #             return Response("Book not found", status=status.HTTP_404_NOT_FOUND)
#
#
# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def book_details(request, id):
#     if request.method == 'GET':
#         book = get_object_or_404(Book, pk=id)
#         serializer = BookSerializer(book)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#         # try:
#         #     book = Book.objects.get(id=id)
#         #     book.delete()
#         #     return Response("book deleted successfully")
#         # except Book.DoesNotExist:
#         #     return Response("Book not found", status=status.HTTP_404_NOT_FOUND)
#
#

#
# @api_view(['GET'])
# def author_list(request):
#     if request.method == "GET":
#         queryset = Author.objects.all()
#         serializers = AuthorSerializer(queryset, many=True)
#         return Response(serializers.data)
#
#
# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def author_details(request, id):
#     if request.method == 'GET':
#         author = get_object_or_404(Author, pk=id)
#         serializer = AuthorSerializer(author)
#         return Response(serializer.data, status=status.HTTP_200_OK)

# TODO to get a book object and also fetch the author objects
# class BookCreateApiView(generics.ListAPIView):
#     queryset = Book.objects.select_related('author').all()
#     serializer_class = BookSerializer


# class CreateBookApiView(generics.CreateAPIView):
#     serializer_class = BookSerializer
#
#     def perform_create(self, serializer):
#         author_id = self.request.data.get('author_id')
#         author = Author.objects.get(pk=author_id)
#         serializer.save(author=author)


# class BookDetailView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     lookup_field = 'id'


@api_view()
def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    serializer = AuthorSerializer(author)
    return Response(serializer.data)
#
#
# class CreateAuthorApiView(generics.CreateAPIView):
#     serializer_class = AuthorSerializer


# class AuthorDetailView(generics.RetrieveAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#     lookup_field = 'id'
#

class AuthorViewSet(ModelViewSet):
    pagination_class = DefaultPageNumberPagination
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# class AuthorListView(generics.ListAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
# # class BookListView(generics.ListAPIView):
# #     queryset = Book.objects.all()
# #     serializer_class = BookSerializer
#
class BookViewSet(ModelViewSet):
    pagination_class = DefaultPageNumberPagination
    queryset = Book.objects.all()
    serializer_class = BookSerializer
