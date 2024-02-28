from django.shortcuts import redirect
from django.utils import timezone
from django.views.decorators.http import require_POST

from .forms import PromocodeApplyForm
from .models import Promocode


@require_POST
def apply(request):
    now = timezone.now()
    form = PromocodeApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            promocode = Promocode.objects.get(code__iexact=code,
                                              valid_from__lte=now,
                                              valid_to__gte=now,
                                              active=True)
            request.session['promocode_id'] = promocode.id
        except Promocode.DoesNotExists:
            request.session['promocode_id'] = None
    return redirect('cart_detail')
