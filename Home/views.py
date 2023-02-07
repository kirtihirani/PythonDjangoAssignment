from django.shortcuts import render,HttpResponse,redirect

from Home.models import Department, Employee

# Create your views here.
def index(request):
    
    # return HttpResponse("hello world")
    myemp = Employee.objects.all().values()
    mydept = Department.objects.all().values()
    deps = []
    depts={}
   
    for dept in mydept:
        
        if dept['manager_id']== None:
            
            dept.update(managername = 'Not Assigned' )
           
        else:
           empid = dept['manager_id']
           dept.update(managername = Employee.objects.get(pk=empid) )
        
        deps.append(dept)
   
    context={
        'myemps':myemp,
        'deps':deps,
        
    }

    return render(request,'index.html',context)

def addemp(request):
    if request.method == "POST":
        empname = request.POST.get('empname')
        email= request.POST.get('email')
        contact= request.POST.get('contact')
        employee=Employee(empname=empname,email=email,contact=contact)
        employee.save()
        return redirect('Home')

    return render(request,'addemp.html')

def updateemp(request,id):
    

    emp1 = Employee.objects.get(pk=id)
    context={
        'emp1':emp1
    }
    
    if request.method=="POST":
        empname = request.POST.get('empname')
        email= request.POST.get('email')
        contact= request.POST.get('contact')

        empp = Employee.objects.get(pk=id)
        empp.empname = empname
        empp.email = email
        empp.contact = contact
        empp.save()
        return redirect('Home')

    return render(request,'updateemp.html',context)



def deleteemp(request,id):
    emp = Employee.objects.get(pk=id)
    emp.delete()
    return redirect('Home')

def adddept(request):
    emp1 = Employee.objects.all().values()
    notManager= Employee.objects.filter(manager='no')
    print(notManager)
    context={
        'emp1':emp1,
        'notManager':notManager
    }
    if request.method == "POST":
        deptname = request.POST.get('deptname')
        empid= request.POST.get('manager')
        print(empid)
        employee = Employee.objects.get(pk=empid)
        employee.manager='yes'
        employee.save()
        dept=Department(deptname=deptname,manager=employee)
        dept.save()
        return redirect('Home')

    return render(request,'adddept.html',context)

def updatedept(request,id):
    department = Department.objects.get(pk=id)
    oldmanagerid = department.manager_id
    oldempp = Employee.objects.get(pk=oldmanagerid)
    notManager= Employee.objects.filter(manager='no')

    context={
        'notManager' : notManager,
        'department' :department
    }

    if request.method=="POST":
        deptname = request.POST.get('deptname')
        newmanagerid = request.POST.get('manager') 
        
        if(oldmanagerid != newmanagerid):
            
            oldempp.manager='no'
            oldempp.save()

            newempp = Employee.objects.get(pk=newmanagerid)
            newempp.manager='yes'
            newempp.save()

            dept = Department.objects.get(pk=id)
            dept.deptname = deptname
            dept.manager = newempp
            dept.save()
        else:
            dept = Department.objects.get(pk=id)
            dept.deptname = deptname
            dept.manager = oldempp
            dept.save()
        
        return redirect('Home')


    return render(request,'updatedept.html',context)


def deletedept(request,id):

    dept = Department.objects.get(pk=id)
    if dept.manager_id != None:
        empid = dept.manager_id
        emp = Employee.objects.get(pk=empid)
        emp.manager='no'
        emp.save()
        print(empid)
    dept.delete()
    return redirect('Home')