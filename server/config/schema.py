import graphene
from graphene_django import DjangoObjectType
from products.models import Product


class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'quantity')


class Query(graphene.ObjectType):
    all_products = graphene.List(ProductType)

    def resolve_all_products(root, info):
        print(root, info)
        return Product.objects.all()


schema = graphene.Schema(query=Query)