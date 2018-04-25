from django.http import HttpResponse
from TestModel.models import Test

def testmysql(request):
    test1 = Test(name='testdemo')
    test1.save()
    return HttpResponse("Add success")