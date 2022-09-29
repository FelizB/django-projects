from django.shortcuts import render

# Create your views here.
def first_view(request):
    return render(request,'my_app/first.html')



def variable_view(request):
    number = [25,50]
    overaly=sum(number)
    my_var= { 'first_name': 'Willy',
               'second_name':'Felix',
               'list':[12,10,15,14,25],'dictionary':{'number':overaly}}

    

    return render(request,'my_app/variable.html', context=my_var)