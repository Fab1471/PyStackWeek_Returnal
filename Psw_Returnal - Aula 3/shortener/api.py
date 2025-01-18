from ninja import Router
from .schemas import LinkSchema
from .models import Links

shortener_router = Router()

@shortener_router.post('create/', response={200: LinkSchema, 409: dict})
def create(request, link_schema: LinkSchema):
    data = (link_schema.to_model_data())

    token = data['token']
    redirect_link = data['redirect_link']
    expiration_time = data['expiration_time']
    max_uniques_cliques = data['max_uniques_cliques']

    if token and Links.objects.filter(token=token).exists():
        return 409, {'error': 'Token já existe, use outro.'}
    
    
    link = Links(**data)
    link.save()
    

    '''link = Links(
        redirect_link=redirect_link,
        expiration_time=expiration_time,
        max_uniques_cliques=max_uniques_cliques,
        token=token
    )
    '''
    link.save()

    return 200, LinkSchema.from_model(link)
