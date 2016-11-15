from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render_to_response
from sviaz.models import Kpd, Platform
#from conda.config import platform
from sviaz.forms import PlatformForm
from django.http.response import HttpResponseRedirect

# Create your views here.
def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(platform__icontains = query) |
            Q(contract_number_legal__icontains = query) |
            Q(contract_number_system__icontains = query) |
            Q(provider__icontains = query)
        )
        results = Kpd.objects.filter(qset).distinct()
        #results = []
        #for result in int_results:
        #    results.append(result.platform)
    else:
        results = []
    return render_to_response("sviaz/search.html", {
        #"results":sorted(results),
        "results":results,
        "query":query,
    })

def object_info(request, object_platform):
    request_kpd = Kpd.objects.get(platform = object_platform)
    request_platform = Platform.objects.get(platform = object_platform)
    return render_to_response("sviaz/object.html",{
        "object":request_kpd.platform,
        "address":request_platform.address,
        "provider":request_kpd.provider,
        "service":request_kpd.service,
        "throughput":request_kpd.throughput,
        "last_mile":request_kpd.last_mile,
        "contract_number_legal":request_kpd.contract_number_legal,
        "b_z":request_kpd.b_z,
        "tarif":float(request_kpd.tarif),
    })

def platform_info(request):
    if request.method == "POST":
        form = PlatformForm(request.POST)
        result = Platform.objects.get(request)
        return render_to_response('sviaz/platform_info.html', 
                                  {'form': result})
    else:
        form=PlatformForm()
    return render_to_response('sviaz/platform_info.html', {'form': form})

def thanks(request):
    return render_to_response('thanks.html')