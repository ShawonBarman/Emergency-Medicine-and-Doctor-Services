from django.shortcuts import render, redirect
from .form import UserRegistrationForm,UserContactsForm,ProfileUpdateForm,UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user, authenticate, login
from django.contrib import messages
from .models import ProfileDetails
from doctor.models import Doctor
from medicine.models import Medicine,Category
from django.contrib.auth.models import User
from order.models import Order
from .models import Appointment


# Create your views here.
def homepage(request):
    if request.method == 'POST':
        form = UserContactsForm(request.POST)
        if form.is_valid():
            form.save()
            dict = request.POST
            if dict['name'] == '':
                error_name = 'Name is required. Please Enter your name'
                return render(request, 'home.html', {'form':form, 'error_name':error_name})
            return redirect('contactusSuccess')
    form = UserContactsForm(request.POST)
    context={
        'form': form
    }
    return render(request,'home.html',context)

def registration(request):
    if (request.method == 'POST'):
        form = UserRegistrationForm(request.POST)
        if(form.is_valid()):
            form.save()



            #auto login
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            new_user = authenticate(username=username,password=password)
            login(request,new_user)

            profile = ProfileDetails(user=request.user)
            profile.save()

            #message
            message = 'Hello! '+username+', Welcome to our website.'
            messages.success(request,message = message)


        return redirect('home')
    else:
        form = UserRegistrationForm()

    context={
        'form': form
    }
    return render(request, 'user_registration.html',context)

@login_required
def profile(request):
    user = get_user(request)

    context={
        'name': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
    }
    return render(request, 'user_profile.html',context)
@login_required
def profile_update(request):
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profiledetails)
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            return redirect('profile')
    user_update_form = UserUpdateForm(instance=request.user)
    profile_update_form = ProfileUpdateForm()
    context = {
        'user_update_form': user_update_form,
        'profile_update_form': profile_update_form
    }
    return render(request, 'user_profile_update.html', context)

# def contact(request):
#     sub = forms.ContactusForm()
#     if request.method == 'POST':
#         sub = forms.ContactusForm(request.POST)
#         if sub.is_valid():
#             email = sub.cleaned_data['Email']
#             name = sub.cleaned_data['Name']
#             message = sub.cleaned_data['Message']
#             send_mail(str(name) + ' || ' + str(email), message, settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER,
#                       fail_silently=False)
#             return render(request, 'contactussuccess.html')


def aboutpage(request):
    return render(request,'aboutus.html')
def contactus(request):
    if request.method == 'POST':
        form = UserContactsForm(request.POST)
        if form.is_valid():
            form.save()
            dict = request.POST
            if dict['name'] != '':
                print(dict['name'])
            else:
                error_name = 'Name is required. Please Enter your name'
                return render(request, 'contactus.html', {'form':form, 'error_name':error_name})
            return redirect('contactusSuccess')
    form = UserContactsForm(request.POST)
    context={
        'form': form
    }
    return render(request, 'contactus.html',context)
def contactusSuccess(request):
    return render(request,'contactussuccess.html')
def doctorServices(request):
    cart_add = request.session.get('cart_add')
    if not cart_add:
        request.session['cart_add'] = {}
    doctors = Doctor.objects.all()
    return render(request,'doctor_services.html',{'doctors':doctors})
# def medicineServices(request):
#     medicines = Medicine.objects.all()
#     return render(request,'medicine_services.html',{'medicines':medicines})

def medicinestore(request):
    cart_add = request.session.get('cart_add')
    if not cart_add:
        request.session['cart_add'] = {}

    postdata = request.GET
    medicine = Medicine.objects.all()
    category = Category.category()
    categoryId = postdata.get('category')
    cart = request.POST.get('addCart')
    remove = request.POST.get('remove')

    print(cart_add)
    if cart:
        if cart_add:
            quantity = cart_add.get(cart)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart_add.pop(cart)
                    else:
                        cart_add[cart] = quantity - 1
                else:
                    cart_add[cart] = quantity + 1
            else:
                cart_add[cart] = 1
                print(cart_add[cart])
        else:
            cart_add = {}
            cart_add[cart] = 1
        request.session['cart_add'] = cart_add
        print(request.session['cart_add'], cart)

    if categoryId:
        medicine = Medicine.get_product_by_id(categoryId)
    else:
        medicine = Medicine.objects.all()
    context = {
        'medicines': medicine,
        'category': category
    }
    return render(request, 'medicine_services.html', context)

@login_required
def cart(request):
    ids = list(request.session.get('cart_add').keys())
    # print(ids)
    medicines = Medicine.get_medicines_by_id(ids)
    return render(request,'cart.html',{'medicines':medicines})

@login_required
def check_out(request):
    user = get_user(request)
    print(user.id)
    address=request.POST.get('address')
    phone=request.POST.get('Phone')
    cart=request.session.get("cart_add")
    medicines=Medicine.get_medicines_by_id(list(cart.keys()))
    print("User_name is",user,address,phone,cart,medicines)
    for medicine in medicines:
        order=Order(user=User(id = user.id),
                    medicine=medicine,
                    price=medicine.price_BDT,
                    phone=phone,
                    address=address,
                    quantity=cart.get(str(medicine.medicine_id))
                    )
        order.placeOrder()
    request.session['cart_add']={}
    return redirect('cart')
@login_required
def orderPage(request):
    user = get_user(request)
    orders=Order.getUserByID(user.id)
    print(user,orders)
    return render(request,'order.html',{'orders':orders})

def appointmentCheckout(request):
    user = get_user(request)
    print(user.id)
    name = request.POST.get('name')
    address = request.POST.get('address')
    phone = request.POST.get('Phone')
    description = request.POST.get('description')
    doctorId = request.POST.get('doctor_id')
    print(doctorId)
    appointment = Appointment(user=User(id=user.id),
                  doctor=doctorId,
                  patientName = name,
                  phone=phone,
                  address=address,
                  description=description
                      )
    appointment.placeAppointment()
    return redirect('doctorservices')

def appointmentPage(request):
    user = get_user(request)
    appointment = Appointment.getUserByID(user.id)
    print(user, appointment)
    return render(request, 'appointment.html', {'appointment': appointment})