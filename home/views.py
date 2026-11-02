from django.http import Http404
from django.shortcuts import render

PRODUCTS = [
    {"id": 0, "brand": "Bioderma", "name": "Atoderm Cream Ultra Nemlendirici Krem 500 ml", "image": "images/product1.jpg", "price": "47,13", "old_price": "70,35", "discount": 33, "rating": 4.6, "reviews": 16382},
    {"id": 1, "brand": "The Purest Solutions", "name": "Yağlı ve Karma Ciltler için Siyah Nokta Bakım Seti", "image": "images/product2.jpg", "price": "10,19", "old_price": "20,38", "discount": 50, "rating": 4.5, "reviews": 35441},
    {"id": 2, "brand": "CALLIËL", "name": "Leke Karşıtı Etkili, Aydınlatıcı Cilt Tonu Eşitleyici Serum", "image": "images/product3.jpg", "price": "13,86", "old_price": "27,73", "discount": 50, "rating": 4.3, "reviews": 1956},
    {"id": 3, "brand": "The Ceel", "name": "Mor Karbon Diş Beyazlatma Seti", "image": "images/product4.jpg", "price": "21,78", "old_price": "36,30", "discount": 39, "rating": 4.1, "reviews": 24007},
    {"id": 4, "brand": "CALLIËL", "name": "Gözenek Karşıtı Tonik Seti", "image": "images/product5.jpg", "price": "31,50", "old_price": "42,00", "discount": 25, "rating": 4.3, "reviews": 11356},
    {"id": 5, "brand": "Kiperin", "name": "Çift Hidrolize Multi Kolajen Kapsül | ATP", "image": "images/product6.jpg", "price": "24,89", "old_price": "48,37", "discount": 48, "rating": 4.5, "reviews": 1934},
    {"id": 6, "brand": "The Purest Solutions", "name": "Yağlı ve Karma Ciltler için Siyah Nokta Bakım Seti", "image": "images/flash1.jpg", "price": "10,19", "old_price": "20,38", "discount": 50, "rating": 4.5, "reviews": 35441},
    {"id": 7, "brand": "Ocean", "name": "Vitamin D3K2 Damla - 2'li Avantajlı Paket", "image": "images/flash2.jpg", "price": "18,63", "old_price": "37,26", "discount": 50, "rating": 4.7, "reviews": 3652},
    {"id": 8, "brand": "The Ceel", "name": "Mor Karbon Diş Beyazlatma Seti", "image": "images/flash3.jpg", "price": "21,78", "old_price": "36,30", "discount": 39, "rating": 4.1, "reviews": 24007},
    {"id": 9, "brand": "Collagen Forte Platinum", "name": "Omega-3 Balık Yağı 90 Kapsül", "image": "images/flash4.jpg", "price": "16,84", "old_price": "35,78", "discount": 52, "rating": 4.5, "reviews": 20215},
    {"id": 10, "brand": "Nutraxin", "name": "Magnezyum Complex 60 Tablet 125 Mg - Bisiglinat", "image": "images/flash5.jpg", "price": "14,30", "old_price": "23,83", "discount": 39, "rating": 4.6, "reviews": 37944},
    {"id": 11, "brand": "Kale Termos", "name": "1706 MEYVE PRESİ (INDUSTRIAL TYPE FRUIT PRESS)", "image": "images/flash6.jpg", "price": "88,24", "old_price": "126,06", "discount": 30, "rating": 4.3, "reviews": 30},
]


def index(request):
    return render(request, 'index.html')


def product_detail(request, pk):
    product = None
    for p in PRODUCTS:
        if p["id"] == pk:
            product = p
    if product is None:
        raise Http404("Məhsul tapılmadı")
    others = [p for p in PRODUCTS if p["id"] != pk][:5]
    return render(request, 'product.html', {"product": product, "others": others})