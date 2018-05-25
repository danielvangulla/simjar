from django.conf.urls import url, include
from django.urls import path
from .views import HomePageView, lapangan_datasets, incidences_datasets, umum_datasets, trterminal_datasets, patchsulut_datasets, trlampu_datasets, trjembatan_datasets, trtrayek_datasets, telekomunikasi_datasets, smpjalan_datasets, \
    smpsungai_datasets, sanitasi_datasets, cctv_datasets, swalayan_datasets, bnbakl_datasets, bnbaistq_datasets, bnbamhkt_datasets, bnbatelb_datasets, \
    bnbatklak_datasets, bnbawngsel_datasets, bnbapin_datasets, bnbawngut_datasets, bnbalwng_datasets, bnbatwut_datasets, \
    bnbatwsel_datasets, bnbacal_datasets, bnbabmib_datasets, bnbamhkb_datasets, bnbasarut_datasets, bnbaranotana_datasets, bnbasakobar_datasets, bnbasario_datasets, \
    bnbasartum_datasets, bnbakrgwr_datasets, bnbapaal2_datasets, bnbaperkamil_datasets, bnbadenlu_datasets, bnbamalendeng_datasets, bnbaranomuut_datasets

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('lapangan_data/', lapangan_datasets, name='lapangan'),
    path('incidence_data/', incidences_datasets, name='incidences'),
    path('umum_data/', umum_datasets, name='umum'),
    path('patchsulut_data/', patchsulut_datasets, name='patchsulut'),
    path('trterminal_data/', trterminal_datasets, name='trterminal'),
    path('trlampu_data/', trlampu_datasets, name='trlampu'),
    path('trjembatan_data/', trjembatan_datasets, name='trjembatan'),
    path('trtrayek_data/', trtrayek_datasets, name='trtrayek'),
    path('telekomunikasi_data/', telekomunikasi_datasets, name='telekomunikasi'),
    path('smpjalan_data/', smpjalan_datasets, name='smpjalan'),
    path('smpsungai_data/', smpsungai_datasets, name='smpsungai'),
    path('sanitasi_data/', sanitasi_datasets, name='sanitasi'),
    path('cctv_data/', cctv_datasets, name='cctv'),
    path('swalayan_data/', swalayan_datasets, name='swalayan'),
    path('bnbakl_data/', bnbakl_datasets, name='bnbakl'),
    path('bnbaistq_data/', bnbaistq_datasets, name='bnbaistq'),
    path('bnbamhkt_data/', bnbamhkt_datasets, name='bnbamhkt'),
    path('bnbasarut_data/', bnbasarut_datasets, name='bnbasarut'),
    path('bnbaranotana_data/', bnbaranotana_datasets, name='bnbaranotana'),
    path('bnbasakobar_data/', bnbasakobar_datasets, name='bnbasakobar'),
    path('bnbasario_data/', bnbasario_datasets, name='bnbasario'),
    path('bnbasartum_data/', bnbasartum_datasets, name='bnbasartum'),
    path('bnbapin_data/', bnbapin_datasets, name='bnbapin'),
    path('bnbatelb_data/', bnbatelb_datasets, name='bnbatelb'),
    path('bnbatklak_data/', bnbatklak_datasets, name='bnbatklak'),
    path('bnbawngsel_data/', bnbawngsel_datasets, name='bnbawngsel'),
    path('bnbawngut_data/', bnbawngut_datasets, name='bnbawngut'),
    path('bnbalwng_data/', bnbalwng_datasets, name='bnbalwng'),
    path('bnbacal_data/', bnbacal_datasets, name='bnbacal'),
    path('bnbatwut_data/', bnbatwut_datasets, name='bnbatwut'),
    path('bnbatwsel_data/', bnbatwsel_datasets, name='bnbatwsel'),
    path('bnbabmib_data/', bnbabmib_datasets, name='bnbabmib'),
    path('bnbamhkb_data/', bnbamhkb_datasets, name='bnbamhkb'),
    path('bnbapaal2_data/', bnbapaal2_datasets, name='bnbapaal2'),
    path('bnbakrgwr_data/', bnbakrgwr_datasets, name='bnbakrgwr'),
    path('bnbaperkamil_data/', bnbaperkamil_datasets, name='bnbaperkamil'),
    path('bnbadenlu_data/', bnbadenlu_datasets, name='bnbadenlu'),
    path('bnbamalendeng_data/', bnbamalendeng_datasets, name='bnbamalendeng'),
    path('bnbaranomuut_data/', bnbaranomuut_datasets, name='bnbaranomuut'),
]