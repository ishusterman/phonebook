from django.http import HttpResponse
from django.shortcuts import render

from book.models import Otdel, Building, Person

from django.db.models import Q


def index(request):
    return HttpResponse("Hello, world. You're at the polls index!!.")

def book(request):

    Otdel_list = Otdel.objects.order_by('Name')
    Building_List = Building.objects.order_by('Name')

    if 'id_otdel' in request.GET:
        id_otdel = request.GET['id_otdel']
    else:
        id_otdel = "0"


    Data = Person.objects

    if id_otdel!="" and id_otdel!="0":
        Data = Data.filter(Otdel = id_otdel)



    """ if request.method == "POST":
        Otdel_id = request.POST['Otdel']
        Building_id = request.POST['Building']
        Txt = request.POST['Txt']
        Show = request.POST['Show']


    else:
        Otdel_id = 1
        Building_id = 1
        Txt = ""
        Show = "Показать все"

    

    if Show == "Показать все":
        Otdel_id = "0"
        Building_id = "0"
        Txt = ""


    if Otdel_id!="" and Otdel_id!="0":
        Data = Data.filter(Otdel = Otdel_id)

    if Building_id != "" and Building_id != "0":
            Data = Data.filter(Building_id=Building_id)

    if Txt != "":
            Data = Data.filter(Q(SurName__icontains=Txt) | Q(FirstName__icontains=Txt)| Q(Patronymic__icontains=Txt)) 


    context = {'Building': Building_List, 'Otdel': Otdel_list, 'Building_id': int(Building_id), 'Otdel_id': int(Otdel_id), 'Txt': Txt, 'Data': Data, 'Show': Show, "id_otdel": id_otdel}
    """

    context = {'Building': Building_List, 'Otdel': Otdel_list, 'Data': Data, 'id_otdel': id_otdel}
    return render(request,'rep3.html', context)



