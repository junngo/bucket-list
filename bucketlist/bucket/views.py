from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
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
    bucket = get_object_or_404(Bucket, pk=bucket_id)

    # return HttpResponse("You're looking at bucket %s." % bucket_id)
    return render(request, 'bucket/detail.html', {'bucket': bucket})
