from av.models import Brand
from django.http import HttpResponse
import requests


def parse_brand(request):
    url = "https://api.av.by/offer-types/cars/catalog/brand-items"
    #url = "http://localhost:8000/api/brand/"
    #url = "https://api.av.by/offer-types/cars/catalog/brand-items/1/models"

    payload = {}
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
            "Accept": "*/*"}

    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.status_code)
    # print(response.text)
    msg = "Парсинг завершен: новых марок авто не найдено!"

    brand_items = Brand.objects.all()
    brands_length = len(brand_items)

    for item in response.json():
        for brand in brand_items:
            if brand.name == item['name']:
                break
        else:
            brand_item = Brand()
            if brands_length == 0:
                brand_item.id = item["id"]   # could be used for the first parse without id check
            # else:
            #     for brand2 in brand_items:
            #         if item["id"] == brand2.id:
            #             break
            #     else:
            #         brand_item.id = item["id"]
            brand_item.name = item["name"]
            brand_item.slug = item["slug"]
            brand_item.save()
            msg = "Добавлены новые марки авто!!!"

    return HttpResponse(msg)