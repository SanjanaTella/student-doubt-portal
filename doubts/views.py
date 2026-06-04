from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Doubt
from .models import Feedback


# 🏠 Home Page
def home(request):
    return render(request, 'home.html')


# 📝 Register
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        User.objects.create_user(username=username, password=password)
        messages.success(request, "User Registered Successfully")

        return redirect('login')

    return render(request, 'register.html')


# 🔐 Login
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')   # ✅ ALWAYS go to dashboard
        else:
            return render(request, 'login.html', {'error': 'Invalid login'})

    return render(request, 'login.html')


# 🚪 Logout
def user_logout(request):
    logout(request)
    return redirect('home')   


# 📊 Dashboard
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')  


# ➕ Add Doubt
@login_required
def add_doubt(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        custom_subject = request.POST.get('custom_subject')
        doubt_text = request.POST['doubt_text']

        # If "Other" selected
        if subject == "Other" and custom_subject:
            subject = custom_subject

        Doubt.objects.create(
            student=request.user,
            subject=subject,
            doubt_text=doubt_text
        )

        return redirect('view_doubts')

    return render(request, 'add_doubt.html')


# 📄 View Doubts (with search)
@login_required
def view_doubts(request):
    query = request.GET.get('q')

    if query:
        doubts = Doubt.objects.filter(
            student=request.user,
            subject__icontains=query
        )
    else:
        doubts = Doubt.objects.filter(student=request.user)

    return render(request, 'view_doubts.html', {'doubts': doubts})


# ✏️ Edit Doubt
@login_required
def edit_doubt(request, id):
    doubt = Doubt.objects.get(id=id)

    if request.method == 'POST':
        doubt.subject = request.POST['subject']
        doubt.doubt_text = request.POST['doubt_text']
        doubt.save()

        return redirect('view_doubts')

    return render(request, 'edit_doubt.html', {'doubt': doubt})


# ❌ Delete Doubt
@login_required
def delete_doubt(request, id):
    doubt = Doubt.objects.get(id=id)
    doubt.delete()

    return redirect('view_doubts')


@login_required
def feedback(request):
    if request.method == 'POST':
        message = request.POST['message']
        rating = request.POST['rating']

        Feedback.objects.create(
            user=request.user,
            message=message,
            rating=rating
        )

        return redirect('dashboard')

    return render(request, 'feedback.html')

