from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def ProductPage(request):
    return render(request,'Product.html')


def ProductList(request):
    Data = {
    'Products': [
        {
            'Name': 'Deluxe Widget',
            'Price': '2450',
            'Image': 'https://example.com/images/product1.jpg',
            'Description': 'A high-quality product that offers excellent performance and durability.'
        },
        {
            'Name': 'Pro Gadget',
            'Price': '3300',
            'Image': 'https://example.com/images/product2.jpg',
            'Description': 'Designed for professionals who need reliable and efficient tools.'
        },
        {
            'Name': 'Smart Gizmo',
            'Price': '5600',
            'Image': 'https://example.com/images/product3.jpg',
            'Description': 'The perfect solution for smart technology enthusiasts.'
        },
        {
            'Name': 'Ultimate Device',
            'Price': '7200',
            'Image': 'https://example.com/images/product4.jpg',
            'Description': 'An ultimate device for all your needs, combining power and efficiency.'
        },
        {
            'Name': 'Eco Widget',
            'Price': '1500',
            'Image': 'https://example.com/images/product5.jpg',
            'Description': 'An eco-friendly product that minimizes environmental impact.'
        },
        {
            'Name': 'Advanced Gadget',
            'Price': '4800',
            'Image': 'https://example.com/images/product6.jpg',
            'Description': 'An advanced gadget with the latest technology features.'
        },
        {
            'Name': 'Premium Gizmo',
            'Price': '6700',
            'Image': 'https://example.com/images/product7.jpg',
            'Description': 'A premium product that guarantees top-notch quality.'
        },
        {
            'Name': 'Budget Device',
            'Price': '44',
            'Image': 'https://example.com/images/product8.jpg',
            'Description': 'A budget-friendly option that doesn’t compromise on performance.'
        }
        ]
        }  

    return JsonResponse({"Data":Data})