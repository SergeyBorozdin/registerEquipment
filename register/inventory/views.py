from django.shortcuts import render, get_object_or_404, redirect
from .models import Equipment
from .forms import EquipmentForm

def equipment_list(request):
    equipments = Equipment.objects.all()
    return render(request, 'inventory/equipment_list.html', {'equipments': equipments})

def equipment_detail(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    return render(request, 'inventory/equipment_detail.html', {'equipment': equipment})

def equipment_new(request):
    if request.method == "POST":
        form = EquipmentForm(request.POST, request.FILES)
        if form.is_valid():
            equipment = form.save(commit=False)
            equipment.save()
            return redirect('equipment_detail', pk=equipment.pk)
    else:
        form = EquipmentForm()
    return render(request, 'inventory/equipment_edit.html', {'form': form})

def equipment_edit(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == "POST":
        form = EquipmentForm(request.POST, request.FILES, instance=equipment)
        if form.is_valid():
            equipment = form.save(commit=False)
            equipment.save()
            return redirect('equipment_detail', pk=equipment.pk)
    else:
        form = EquipmentForm(instance=equipment)
    return render(request, 'inventory/equipment_edit.html', {'form': form})
