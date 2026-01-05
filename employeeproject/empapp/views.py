from django.shortcuts import render

# Create your views here.
def home(request):
    dict={"name":'kiran kumar',"age":25,"contact":"9999999999"}
    return render(request,'empapp/home.html',dict)

def employees(reequest):
    employees = [
    {"emp_id": 101, "name": "Arun", "designation": "Developer", "salary": 60000},
    {"emp_id": 102, "name": "Kumar", "designation": "Tester", "salary": 45000},
    {"emp_id": 103, "name": "Sita", "designation": "Manager", "salary": 80000}
    ]
    dict={"emp_list":employees}
    return render(reequest,'empapp/employees.html',dict)

