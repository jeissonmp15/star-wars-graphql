import graphene

from .mutations import Mutation as SchemeMutation
from .types import Query as SchemeQuery


class Query(SchemeQuery, graphene.ObjectType):
    pass


class Mutation(SchemeMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
