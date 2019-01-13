from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .models import Bucket

# Create your views here.
def index(request):

    latest_bucket_list = Bucket.objects.order_by('-created_at')[:5]
    #template = loader.get_template('bucket/index.html')

    context = {
        'bucket_list': latest_bucket_list,
    }

    #return HttpResponse(template.render(context, request))
    return render(request, 'bucket/index.html', context)


def detail(request, bucket_id):
    return HttpResponse("You're looking at bucket %s." % bucket_id)
