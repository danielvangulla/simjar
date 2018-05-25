from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Bloklapangan, Incindences, Umum, PatchSulut, TrTerminal, TrLampu, TrJembatan, TrTrayek, Telekomunikasi, SmpJalan, \
    SmpSungai, Sanitasi, Cctv, Swalayan, BnbaKl, BnbaIstq, BnbaMhkt, BnbaTelb, BnbaTklak, BnbaWngsel, BnbaPin, BnbaWngut, BnbaLwng, \
    BnbaTwut, BnbaTwsel, BnbaCal, BnbaBmib, BnbaMhkb, BnbaSarUt, BnbaRanotana, BnbaSaKobar, BnbaSario, BnbaSarTum, BnbaKrgwr, BnbaPerkamil, \
    BnbaPaal2, BnbaDenlu, BnbaMalendeng, BnbaRanomuut

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

def bnbakl_datasets(request):
    bnbakl = serialize('geojson', BnbaKl.objects.all())
    return HttpResponse(bnbakl, content_type='json')

def bnbaistq_datasets(request):
    bnbaistq = serialize('geojson', BnbaIstq.objects.all())
    return HttpResponse(bnbaistq, content_type='json')

def bnbamhkt_datasets(request):
    bnbamhkt = serialize('geojson', BnbaMhkt.objects.all())
    return HttpResponse(bnbamhkt, content_type='json')

def bnbapin_datasets(request):
    bnbapin = serialize('geojson', BnbaPin.objects.all())
    return HttpResponse(bnbapin, content_type='json')

def bnbatelb_datasets(request):
    bnbatelb = serialize('geojson', BnbaTelb.objects.all())
    return HttpResponse(bnbatelb, content_type='json')

def bnbatklak_datasets(request):
    bnbatklak = serialize('geojson', BnbaTklak.objects.all())
    return HttpResponse(bnbatklak, content_type='json')

def bnbawngsel_datasets(request):
    bnbawngsel = serialize('geojson', BnbaWngsel.objects.all())
    return HttpResponse(bnbawngsel, content_type='json')

def bnbawngut_datasets(request):
    bnbawngut = serialize('geojson', BnbaWngut.objects.all())
    return HttpResponse(bnbawngut, content_type='json')

def bnbalwng_datasets(request):
    bnbalwng = serialize('geojson', BnbaLwng.objects.all())
    return HttpResponse(bnbalwng, content_type='json')

def bnbacal_datasets(request):
    bnbacal = serialize('geojson', BnbaCal.objects.all())
    return HttpResponse(bnbacal, content_type='json')

def bnbatwut_datasets(request):
    bnbatwut = serialize('geojson', BnbaTwut.objects.all())
    return HttpResponse(bnbatwut, content_type='json')

def bnbatwsel_datasets(request):
    bnbatwsel = serialize('geojson', BnbaTwsel.objects.all())
    return HttpResponse(bnbatwsel, content_type='json')

def bnbabmib_datasets(request):
    bnbabmib = serialize('geojson', BnbaBmib.objects.all())
    return HttpResponse(bnbabmib, content_type='json')

def bnbamhkb_datasets(request):
    bnbamhkb = serialize('geojson', BnbaMhkb.objects.all())
    return HttpResponse(bnbamhkb, content_type='json')

def bnbasarut_datasets(request):
    bnbasarut = serialize('geojson', BnbaSarUt.objects.all())
    return HttpResponse(bnbasarut, content_type='json')

def bnbaranotana_datasets(request):
    bnbaranotana = serialize('geojson', BnbaRanotana.objects.all())
    return HttpResponse(bnbaranotana, content_type='json')

def bnbasakobar_datasets(request):
    bnbasakobar = serialize('geojson', BnbaSaKobar.objects.all())
    return HttpResponse(bnbasakobar, content_type='json')

def bnbasario_datasets(request):
    bnbasario = serialize('geojson', BnbaSario.objects.all())
    return HttpResponse(bnbasario, content_type='json')

def bnbasartum_datasets(request):
    bnbasartum = serialize('geojson', BnbaSarTum.objects.all())
    return HttpResponse(bnbasartum, content_type='json')

def bnbapaal2_datasets(request):
    bnbapaal2 = serialize('geojson', BnbaPaal2.objects.all())
    return HttpResponse(bnbapaal2, content_type='json')

def bnbakrgwr_datasets(request):
    bnbakrgwr = serialize('geojson', BnbaKrgwr.objects.all())
    return HttpResponse(bnbakrgwr, content_type='json')

def bnbaperkamil_datasets(request):
    bnbaperkamil = serialize('geojson', BnbaPerkamil.objects.all())
    return HttpResponse(bnbaperkamil, content_type='json')

def bnbadenlu_datasets(request):
    bnbadenlu = serialize('geojson', BnbaDenlu.objects.all())
    return HttpResponse(bnbadenlu, content_type='json')

def bnbamalendeng_datasets(request):
    bnbamalendeng = serialize('geojson', BnbaMalendeng.objects.all())
    return HttpResponse(bnbamalendeng, content_type='json')

def bnbaranomuut_datasets(request):
    bnbaranomuut = serialize('geojson', BnbaRanomuut.objects.all())
    return HttpResponse(bnbaranomuut, content_type='json')

#################Batas BNBA###########################################################################################

def lapangan_datasets(request):
    lapangan = serialize('geojson', Bloklapangan.objects.all())
    return HttpResponse(lapangan, content_type='json')

def incidences_datasets(request):
    incidences = serialize('geojson', Incindences.objects.all())
    return HttpResponse(incidences, content_type='json')

def umum_datasets(request):
    umum = serialize('geojson', Umum.objects.all())
    return HttpResponse(umum, content_type='json')

def patchsulut_datasets(request):
    patchsulut = serialize('geojson', PatchSulut.objects.all())
    return HttpResponse(patchsulut, content_type='json')

def trterminal_datasets(request):
    trterminal = serialize('geojson', TrTerminal.objects.all())
    return HttpResponse(trterminal, content_type='json')

def trlampu_datasets(request):
    trlampu = serialize('geojson', TrLampu.objects.all())
    return HttpResponse(trlampu, content_type='json')

def trjembatan_datasets(request):
    trjembatan = serialize('geojson', TrJembatan.objects.all())
    return HttpResponse(trjembatan, content_type='json')

def trtrayek_datasets(request):
    trtrayek = serialize('geojson', TrTrayek.objects.all())
    return HttpResponse(trtrayek, content_type='json')

def telekomunikasi_datasets(request):
    telekomunikasi = serialize('geojson', Telekomunikasi.objects.all())
    return HttpResponse(telekomunikasi, content_type='json')

def smpjalan_datasets(request):
    smpjalan = serialize('geojson', SmpJalan.objects.all())
    return HttpResponse(smpjalan, content_type='json')

def smpsungai_datasets(request):
    smpsungai = serialize('geojson', SmpSungai.objects.all())
    return HttpResponse(smpsungai, content_type='json')

def sanitasi_datasets(request):
    sanitasi = serialize('geojson', Sanitasi.objects.all())
    return HttpResponse(sanitasi, content_type='json')

def cctv_datasets(request):
    cctv = serialize('geojson', Cctv.objects.all())
    return HttpResponse(cctv, content_type='json')

def swalayan_datasets(request):
    swalayan = serialize('geojson', Swalayan.objects.all())
    return HttpResponse(swalayan, content_type='json')

def indomaret_datasets(request):
    swalayan = serialize('geojson', Swalayan.objects.values())
    return HttpResponse(swalayan, content_type='json')

