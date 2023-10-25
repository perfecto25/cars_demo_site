from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CarsForm
from .models import Cars
from loguru import logger

def index(request):
    """ display Cars data """

    if request.method == "POST":
        form = CarsForm(request.POST)
        if form.is_valid():
            form.save(commit=True)

    form = CarsForm()

    cars_qs = Cars.objects.all().order_by("id")

    grouplist = list(request.user.groups.values_list('name', flat=True))

    context = {"form": form, "cars_qs": cars_qs, "grouplist": grouplist}
    return render(request, "index.html", context)

@login_required
def delete(request, car_id):
    """ deletes a row """
    try:
        row = Cars.objects.get(id=car_id)
        row.delete()
    except Cars.DoesNotExist:
        pass

    return HttpResponse(f"<div class='warning'>Deleted Car ID: {car_id}</div>")

@login_required
def edit_form(request, car_id):
    """ edit a row via Form submit """
    row = Cars.objects.get(id=car_id)

    if request.method == "GET":
        form = CarsForm(instance=row)
        context = {"form": form, "car_id": car_id}
        return render(request, "edit.html", context)

    if request.method == "POST":
        if row:
            form = CarsForm(request.POST, instance=row)
            if form.is_valid():
                form.save()
                context = {"form": form}
                return redirect("index")

@login_required
def edit_htmx(request, car_id):
    """ edits a row via HTMX Post request """
    logger.warning("editing with HTMX")

    if request.method == "GET":
        try:
            row = Cars.objects.get(id=car_id)
        except Cars.DoesNotExist:
            raise ValueError("lookup does not exist")

        return HttpResponse(f"<hr><div style='background-color:#CCFF99'> \
            <h2>Edit car recrod with HTMX</h2><br> \
            <b>This HTML div is coming from edit_htmx function in views.py</b><br><br> \
            Make <input type='text' name='make' id='make' value='{row.make}'/> \
            Model <input type='text' name='model' id='model' value='{row.model}'/> \
            Year <input type='text' name='year' id='year' value='{row.year}'/> \
            <input type='button' hx-post='/edit_htmx/{car_id}' hx-target='#row_{car_id}' \
            hx-include='#make, #model, #year' value='Save' \
            </div><hr>")

    if request.method == "POST":
        row = Cars.objects.get(id=car_id)
        row.model = request.POST.get('model')
        row.make = request.POST.get('make')
        row.year = request.POST.get('year')
        row.save()
        messages.success(request, "successfully saved car record with HTMX")
        return redirect("index")

