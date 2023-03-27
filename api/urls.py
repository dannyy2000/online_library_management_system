from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('authors', views.AuthorViewSet)
router.register('books', views.BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('books/', views.BookCreateApiView.as_view()),
    # path('books/create/', views.CreateBookApiView.as_view()),
    # path('books/<int:id>', views.BookDetailView.as_view(), name="book_detail"),
    # path('author/create/', views.CreateAuthorApiView.as_view(), name='create_author'),
    path('author/<int:pk>', views.author_detail, name='author_detail'),
    # path('author/', views.AuthorListView.as_view(), name='author-list'),
    # path('authors/<int:pk>/', views.author_detail, name='author-detail')
    # path('books/', views.book_list, name='book_list'),
    # path('books/<int:id>', views.book_details, name='book_details'),
    # path('books/<int:id>/', views.book_details, name='delete_book_list'),
    # path('author/', views.author_list, name='author_list'),
    # path('author/<int:id>/', views.author_details, name='author_details')

]
