from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from crm.forms import EnrollmentForm, EnrollmentForm2, CustomerForm, CustomerForm2
from crm import models
from django.core.mail import send_mail


# Create your views here.


@login_required
def dashboard(request):
    return render(request, "crm/dashboard.html")


@login_required
def customers(request):
    return render(request, "crm/customers.html")


@login_required
def customer_enrollment(request, customer_id):
    msg = {}
    enrollment_form = EnrollmentForm(initial={'customer': customer_id})
    customer_name = enrollment_form.fields.get("customer")._get_queryset().get(id=customer_id)
    if request.method == "POST":
        enrollment_form = EnrollmentForm(request.POST)
        if enrollment_form.is_valid():
            enrollment_form.save()
        enrollment_obj = models.Enrollment.objects.filter(**enrollment_form.cleaned_data)
        if enrollment_obj:

            if not enrollment_obj[0].contract_agreed:
                msg = {'step': 1, 'data': '请把此链接发送给学员填写http://127.0.0.1:8000/crm/student/enrollment/%s/'
                                          % enrollment_obj[0].id}
            else:
                return redirect("/crm/customer_enrollment/audit/%s/" % enrollment_obj[0].id)
            return render(request, "crm/enrollment.html", {'form': enrollment_form, 'customer_name': customer_name, 'msg': msg})
        else:
            print(enrollment_form.errors)

    return render(request, "crm/enrollment.html", {'form': enrollment_form, 'customer_name': customer_name, 'msg': msg})


@login_required
def stu_enrollment(request, enrollment_id):
    enrollment_obj = models.Enrollment.objects.get(id=enrollment_id)

    if request.method == "POST":
        form = CustomerForm(instance=enrollment_obj.customer, data=request.POST)
        if form.is_valid():

            print(request.POST)
            contract_agreed = request.POST.get('contract_agreed')
            if contract_agreed:
                enrollment_obj.contract_agreed = True
                enrollment_obj.save()
                form.save()

    if enrollment_obj.contract_agreed:
        return HttpResponse("报名表单已提交")

    form = CustomerForm(instance=enrollment_obj.customer)

    return render(request, "crm/stu_enrollment.html", locals())


@login_required
def enrollment_audit(request, enrollment_id):
    enrollment_obj = models.Enrollment.objects.get(id=enrollment_id)
    if request.method == "POST":
        enrollment_form = EnrollmentForm2(instance=enrollment_obj, data=request.POST)
        if enrollment_form.is_valid():
            enrollment_form.save()
            print("发送账号信息")
            # send_mail(
            #     '报名成功',
            #     '欢迎加入世界上最好的语言python大神班',
            #     '448461456@qq.com',
            #     ['448461456@qq.com'],
            #     fail_silently=False,
            # )
        return redirect("/freeadmin/crm/customer/")

    form = CustomerForm2(instance=enrollment_obj.customer)
    enrollment_form = EnrollmentForm2(instance=enrollment_obj)
    return render(request, "crm/enrollment_audit.html", locals())

