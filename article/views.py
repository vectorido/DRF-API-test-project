from rest_framework import viewsets

from .models import Article
from .serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


# class ArticleView(viewsets.ViewSet):
#     """
#     A simple ViewSet that for listing or retrieving users.
#     """
#
#     def list(self, request):
#         queryset = Article.objects.all()
#         serializer = ArticleSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = Article.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = ArticleSerializer(user)
#         return Response(serializer.data)

# class ArticleView(ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#     def perform_create(self, serializer):
#         author = get_object_or_404(Author, id=self.request.data.get('author_id'))
#         return serializer.save(author=author)
#
#
# class SingleArticleView(RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class OldArticleView(APIView):
#
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response({"articles": serializer.data})
#
#     def post(self, request):
#         article = request.data.get('articles')
#
#         serializer = ArticleSerializer(data=article)
#         if serializer.is_valid(raise_exception=True):
#             article_saved = serializer.save()
#         return Response({'success': "Article '{}' created succesfully".format(article_saved.title)})
#
#     def put(self, request, pk):
#         saved_article = get_object_or_404(Article.objects.all(), pk=pk)
#         data = request.data.get('articles')
#         serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)
#
#         if serializer.is_valid(raise_exception=True):
#             article_saved = serializer.save()
#
#         return Response({
#             "success": "Article '{}' updated successfully".format(article_saved.title)
#         })
#
#     def delete(self, request, pk):
#         # get object with this pk
#         article = get_object_or_404(Article.objects.all(), pk=pk)
#         article.delete()
#         return Response({
#             "message": "Article with id '{}' has been deleted.".format(pk)
#         })
