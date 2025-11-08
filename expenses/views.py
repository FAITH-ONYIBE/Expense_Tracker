from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Expense
from .forms import ExpenseForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    expenses = Expense.objects.filter(user=request.user)
    total = sum(exp.amount for exp in expenses)
    return render(request, 'expenses/home.html', {'expenses': expenses, 'total': total})

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('home')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})

@login_required
def delete_expense(request, pk):
    expense = Expense.objects.get(id=pk, user=request.user)
    expense.delete()
    return redirect('home')

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
