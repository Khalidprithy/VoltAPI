from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *

class CreateProductView(APIView):
    def post(self, request, format=None):
        data = request.data
        startup_key = request.GET.get('startup_key')
        startup = Startup.objects.get(key=startup_key)
        productModule = ProductModule.objects.get(startup=startup)
        strategy = Strategy.objects.get(strategyTitle=data.get("strategyTitle"))
        product = Product.objects.create(
            productModule=productModule,
            name = data.get("name"),
            productLeader = data.get("productLeader"),
            platform = data.get("platform"),
            phase = data.get("phase"),
            description = data.get("description"),
            keyword = data.get("keyword"),
            completed = data.get("completed"),
            version = data.get("version"),
            deployed_link = data.get("deployed_link"),
        )
        return Response({"message": "done"})

class GetProductsView(APIView):
    def get(self, request, format=None):
        startup = request.GET.get('startup')
        productModule = ProductModule.objects.get(startup=startup)
        your_product = Product.objects.filter(productModule=productModule)
        your_product_data = PublicProductSerializer(your_product, many=True).data
        payload = {
            'products': your_product_data
        }
        return Response(payload, status=status.HTTP_200_OK)

class GetProductView(APIView):
    def get(self, request, format=None):
        product_key = request.GET.get('product_key')
        product = Product.objects.get(key=product_key)
        features = Feature.objects.filter(product=product)
        timeline = Timeline.objects.filter(product=product)
        _features = []
        for feature in features:
            _feature = {}
            _feature["img"] = Image.objects.filter(feature=feature, is_ss=False).first().img
            _feature["details"] = FeatureSerializer(feature).data
            _features.append(_feature)
        payload = {
            'features': _features,
            'product': ProductSerializer(product).data,
            'timeline': TimelineSerializer(timeline).data
        }
        return Response(payload, status=status.HTTP_200_OK)
    
class GetFeatureView(models.Model):
    def get(self, request, format=None):
        feature_key = request.GET.get("key")
        feature = Feature.objects.get(key=feature_key)
        imgs = Image.objects.filter(feature=feature)
        payload = {
            'feature': FeatureSerializer(feature).data,
            'imgs': ImageSerializer(imgs, many=True).data,
        }
        return Response(payload, status=status.HTTP_200_OK)

class CreateFeatureView(APIView):
    def post(self, request, format=None):
        data = request.data
        product_key = data.get("product_key")
        product = Product.objects.get(key=product_key)
        assigned_to = User.objects.get(username=data.get("username"))
        feature = Feature.objects.create(
            product=product,
            title = data.get("title"),
            assigned_to = assigned_to,
            desc = data.get("desc"),
            deadline = data.get("deadline"),
        )
        return Response({"message": "done"})