from django.forms import ModelForm
from sviaz.models import Platform

class PlatformForm(ModelForm):
    class Meta:
        model = Platform
        fields = ['platform', 'address', 'region', 'oil_base', 'latitude',
                  'longitude', 'state', 'ip', 'note']

#formForPlatform = PlatformForm()

#platform = Platform.objects.get(pk=1)
#formForPlatform = PlatformForm(instance=platform)