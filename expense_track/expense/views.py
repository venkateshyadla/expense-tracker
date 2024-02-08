import os
from django.shortcuts import render,redirect
from .forms import CredentialsForm,UserDetailsForm,ExpenseForm
from .models import UserCredentials, UserDetails, Expense
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.urls import reverse

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')
def register(request):
    if request.method == 'POST':
        credentials_form = CredentialsForm(request.POST)
        details_form = UserDetailsForm(request.POST, request.FILES)
        if credentials_form.is_valid() and details_form.is_valid():
            email = credentials_form.cleaned_data['email']
            mobile_number = credentials_form.cleaned_data['mob']
            password = credentials_form.cleaned_data['pwd']

            if UserCredentials.objects.filter(Q(email=email) | Q(mob=mobile_number)).exists():
                error_message = "User with this email or mobile number already exists. Please use a different email or mobile number."
                return render(request, 'register.html', {'credentials_form': credentials_form, 'error_message': error_message})

            user_credentials = UserCredentials.objects.create(
                email=email,
                mob=mobile_number,
                pwd=password
            )

            name = details_form.cleaned_data['name']
            date_of_birth = details_form.cleaned_data['dob']
            gender = details_form.cleaned_data['gender']
            occupation = details_form.cleaned_data['occupation']
            marital_status = details_form.cleaned_data['m_s']
            income = details_form.cleaned_data['income']

            # Check if profile image is provided
            if 'profile_image' in request.FILES:
                profile_image = request.FILES['profile_image']
                image_filename = f"STD_{user_credentials.id}_{profile_image.name}"
                profile_image_path = os.path.join(settings.MEDIA_ROOT, image_filename)

                with open(profile_image_path, 'wb') as f:
                    for chunk in profile_image.chunks():
                        f.write(chunk)

                UserDetails.objects.create(
                    user_credentials=user_credentials,
                    name=name,
                    dob=date_of_birth,
                    gender=gender,
                    profile_image_path=image_filename,
                    occupation = occupation,
                    m_s = marital_status,
                    income = income
                    
                )
            else:
                UserDetails.objects.create(
                    user_credentials=user_credentials,
                    name=name,
                    dob=date_of_birth,
                    gender=gender,
                    occupation = occupation,
                    m_s = marital_status,
                    income = income
                )
            return redirect('login')

    else:
        credentials_form = CredentialsForm()
        details_form = UserDetailsForm()

    return render(request, 'register.html', {'credentials_form': credentials_form, 'details_form': details_form})

def make_opera(user_details):
    income = user_details.income
    expenses = Expense.objects.filter(user_id=user_details.id)
    exp = [expense.amount for expense in expenses]
    expenditure = sum(exp)
    savings = int(income) - expenditure
    user_details.savings = savings
    user_details.save()
    expenses_data = [{'category': expense.pre_category, 'amount': float(expense.amount)} for expense in expenses]
    if expenditure > 0:
        return user_details,expenses_data,True
    return user_details,expenses_data,False

def login(request):
    if request.method == 'POST':
        email_or_mobile = request.POST.get('email_mob')
        password = request.POST.get('pwwd')
        user = UserCredentials.objects.filter(
            Q(email=email_or_mobile) | Q(mob=email_or_mobile)
        ).first()
        if user and user.pwd == password:
            user_det = UserDetails.objects.get(user_credentials=user)
            user_details,expenses_data,chart_data = make_opera(user_det)
            user_id = user_details.id
            request.session['user_id'] = user_id
            request.session.save()

            return render(request,'dashboard.html',{'user_info':user_details,'expenses_data':expenses_data,'chart_data':chart_data})
        else:
            error_message = "Invalid email/mobile number or password. Please try again."
            return render(request, 'login.html', {'error_message': error_message})
    return render(request,'login.html')

def dashboard(request):
    user_id = request.session.get('user_id')
    user_det = UserDetails.objects.get(id=user_id)
    user_details,expenses_data,chart_data = make_opera(user_det)
    return render(request,'dashboard.html',{'user_info':user_details,'expenses_data':expenses_data,'chart_data':chart_data})

def add_expense(request):
    user_id = request.session.get('user_id')
    user_info = UserDetails.objects.get(id=user_id)
    if request.method == 'POST':
        msg = "Select or Write expenses....!"
        form = ExpenseForm()
        btn_type = request.POST.get('btn_type')
        expense_form = ExpenseForm(request.POST)
        if btn_type == 'add_exp':
            msg = "Today expenses is updated...!"
            if expense_form.is_valid():
                amount = expense_form.cleaned_data['amount']
                category = expense_form.cleaned_data['category']
                write = expense_form.cleaned_data['write_category']
                if write:
                    Expense.objects.create(
                        user_id = user_id,
                        pre_category = write,
                        amount = amount
                    )
                elif category:
                    Expense.objects.create(
                        user_id = user_id,
                        pre_category = category,
                        amount = amount
                    )
    else:
        form = ExpenseForm()
    return render(request,'expense_add.html',{'user_info':user_info,'form':form,'msg':msg})
def logout(request):
    return redirect('welcome')