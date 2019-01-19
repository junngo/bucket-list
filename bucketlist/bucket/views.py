from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, Http404
from django.template import loader
from .models import Bucket
from . import models

# Create your views here.
def index(request):

    if request.method == 'POST':
        """ POST """
        input_bucket = request.POST['input_bucket']
        user = request.user

        new_bucket = models.Bucket.objects.create(
            my_wish = input_bucket,
            creator = user,
            completed = False,
        )
        new_bucket.save

        return HttpResponseRedirect('/bucket/')

    else:
        """ GET """

        latest_bucket_list = Bucket.objects.order_by('-created_at')[:5]
        #template = loader.get_template('bucket/index.html')

        context = {
            'bucket_list': latest_bucket_list,
        }

        #return HttpResponse(template.render(context, request))
        return render(request, 'bucket/index.html', context)


def detail(request, bucket_id):

    if request.method == 'POST':
        """ POST """
        input_bucket_completed = request.POST.get('input_completed', None)
        print(input_bucket_completed)

        if input_bucket_completed != None:
            try:
                bucket = models.Bucket.objects.get(pk=input_bucket_completed)

            except models.Bucket.DoesNotExist:
                raise Http404("Question does not exist")

            bucket.completed = True
            bucket.save()

        return HttpResponseRedirect('/bucket/')

    else:
        """ GET """

        bucket = get_object_or_404(Bucket, pk=bucket_id)

        return render(request, 'bucket/detail.html', {'bucket': bucket})
