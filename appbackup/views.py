from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import BackupTbl, PartTbl, RegionTbl
import json

def index(request):
    # 'flat=True'는 리스트의 리스트 대신 단일 리스트를 반환하도록 합니다.
    parts = PartTbl.objects.all()
    part_id = None
    ids_list = PartTbl.objects.values_list('id', flat=True)

    # 리스트가 비어있지 않다면 첫 번째 'id' 값을 가져옵니다.
    if ids_list:
        part_id = ids_list[0]
    # part_id가 제공되었다면 해당 part_id에 해당하는 BackupTbl 인스턴스만 필터링합니다.
    if part_id is not None:
        backups = BackupTbl.objects.filter(part_id=part_id)
        
    pharmacies_list = BackupTbl.objects.all()
    paginator = Paginator(pharmacies_list, 10)  # 페이지 당 10개의 약국을 보여줍니다.

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    #parts = PartTbl.objects.all()
    regions = RegionTbl.objects.all()
    # 'id'와 'name' 필드만 선택하여 딕셔너리의 리스트로 변환합니다.
    regions_values = list(regions.values('id', 'name'))

    # JSON 문자열로 변환합니다. ensure_ascii=False를 설정하여 유니코드 문자가 이스케이프되지 않도록 합니다.
    regions_json = json.dumps(regions_values, ensure_ascii=False)

    # 페이지네이션 정보를 딕셔너리로 생성
    pagination_info = {
        'current_page': page_obj.number,
        'num_pages': page_obj.paginator.num_pages,
    }
    # JSON 문자열로 변환
    pagination_json = json.dumps(pagination_info, ensure_ascii=False)

    return render(request, 'html/index.html', {
        'page_obj': page_obj,
        'parts': parts,
        'regions_json': regions_json,  # JSON 문자열을 템플릿에 전달
        'pagination_json': pagination_json  # 페이지네이션 정보 추가
    })

def dialog_add(request):
    return render(request, 'html/dialog/dialog_add.html')

def save_pharmacy(request):
    if request.method == "POST":
        # 폼 데이터 처리
        part = int(request.POST.get('parts'))
        name = request.POST.get('name')
        business_number = request.POST.get('business_number')
        representative = request.POST.get('representative')
        contact = request.POST.get('contact')
        region = int(request.POST.get('region'))
        detail_region = request.POST.get('detail_region')
        contract_date = request.POST.get('contract_date')
        expiry_date = request.POST.get('expiry_date')
        category = request.POST.get('category')
        list_price = int(request.POST.get('list_price').replace(',', ''))
        discount = int(request.POST.get('discount').replace(',', ''))
        sales = int(request.POST.get('sales').replace(',', ''))
        cost = int(request.POST.get('cost').replace(',', ''))
        profit = int(request.POST.get('profit').replace(',', ''))
        # 데이터베이스에 저장
        BackupTbl.objects.create(part_id=part, pharmacy=name, businessnum=business_number, owner=representative, phonenum=contact, 
                                 region_id=region, detailregion=detail_region, contractdate=contract_date, expirydate=expiry_date,
                                 category=category, listprice=list_price, discount=discount, salesamount=sales, cost=cost, profit=profit)
        
        return redirect('index')  # 처리 후 리다이렉트, 'index'는 예시 URL 이름