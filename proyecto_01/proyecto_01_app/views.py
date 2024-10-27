from django.shortcuts import render

# Create your views here.
def my_view(request):
    car_list = [
        {"title": "Audi A4"},
        {"title": "BMW 320i"},
        {"title": "Mercedes C220"}
    ]
    context = {
        "car_list": car_list
    }
    return render(request, "proyecto_01_app/car_list.html", context)
