from django.http import JsonResponse


def start(request):
    return JsonResponse({'message':'Your api is online'})