import json

from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Ad, Category


def index(request):
    return HttpResponse("200 {'status': 'ok'}")


@method_decorator(csrf_exempt, name='dispatch')
class AdView(View):
    def get(self, request):
        ads = Ad.objects.all()

        response = []
        for ad in ads:
            response.append({
                'id': ad.id,
                'name': ad.name,
                'author': ad.author,
                'price': ad.price,
            })
        return JsonResponse(response, safe=False)

    def post(self, request):
        data = json.loads(request.body)

        ad = Ad.objects.create(
            name=data['name'],
            author=data['author'],
            price=data['price'],
            description=data['description'],
            address=data['address'],
            is_published=data['is_published']
        )
        return JsonResponse({
            'id': ad.id,
            'name': ad.name,
            'author': ad.author,
            'price': ad.price,
            'description': ad.description,
            'address': ad.address,
            'is_published': ad.is_published,
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()

        response = []
        for cat in categories:
            response.append({
                'id': cat.id,
                'name': cat.name,
            })
        return JsonResponse(response, safe=False)

    def post(self, request):
        data = json.loads(request.body)

        cat = Category.objects.create(
            name=data['name'],
        )
        return JsonResponse({
                'id': cat.id,
                'name': cat.name,
        })


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()

        return JsonResponse({
            'id': ad.id,
            'name': ad.name,
            'author': ad.author,
            'price': ad.price,
            'description': ad.description,
            'address': ad.address,
            'is_published': ad.is_published,
        })


class CatDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        cat = self.get_object()

        return JsonResponse({
            'id': cat.id,
            'name': cat.name,
        })
