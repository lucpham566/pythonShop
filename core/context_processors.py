from core.models import Service


def get_service_info(request):
    info_web =  Service.objects.get(pk=1)
    return {
        'info_web': info_web,
    }

