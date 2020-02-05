from django.shortcuts import render,redirect
from foodapp.models import FoodModel
from foodapp.forms import FoodForm
from django.http import HttpResponse

def filterFoodRest(request):
	fname=request.GET['food']
	#fname='i'
	food=FoodModel.objects.filter(name__contains=fname)
	return HttpResponse(food,content_type="text/plain")

# Create your views here.
def showAllFoodsView(request):
	foods=FoodModel.objects.all()
	return render(request,'foodapp/foods.html',{'allfoods':foods})

def deleteFoodByIdView(request,id):
	print('deleteFoodByIdView')
	foundFood=FoodModel.objects.get(id=id)
	foundFood.delete()
	return redirect('/foodapp/foods')

def createFoodView(request):
	form=FoodForm()
	if request.method == 'POST':
		form=FoodForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/foodapp/foods')
	return render(request,'foodapp/addfood.html',{'form':form})

def updateFoodByIdView(request,id):
	print('IN UPDATE')
	foundFood=FoodModel.objects.get(id=id)
	form=FoodForm(instance=foundFood)
	if request.method == 'POST':
		form=FoodForm(request.POST,instance=foundFood)
		if form.is_valid():
			form.save()
			return redirect('/foodapp/foods')
	return render(request,'foodapp/updatefood.html',{'form':form})

	
