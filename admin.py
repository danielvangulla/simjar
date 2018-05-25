from django.contrib.gis import admin
from .models import Incindences, Bloklapangan, Umum, TrTerminal, TrLampu, TrJembatan, TrTrayek, Telekomunikasi, SmpJalan, \
    SmpSungai, Sanitasi, Cctv, Swalayan, BnbaKl, BnbaIstq, BnbaMhkt, BnbaTelb, BnbaTklak, BnbaWngsel, \
    BnbaPin, BnbaWngut, BnbaLwng, BnbaTwut, BnbaTwsel, BnbaCal, BnbaBmib, BnbaMhkb, BnbaSarUt, BnbaRanotana, \
    BnbaSaKobar, BnbaSario, BnbaSarTum, BnbaPaal2, BnbaKrgwr, BnbaPerkamil, BnbaDenlu, BnbaMalendeng, BnbaRanomuut
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
class IncidencesAdmin(LeafletGeoAdmin):
    list_display = ('name','location')

class BnbaKlAdmin(LeafletGeoAdmin):
    list_display = ('no_rumah','nop')
    list_per_page = 10
    search_fields = ('no_rumah', 'nop')

class BnbaIstqAdmin(LeafletGeoAdmin):
    list_display = ('no_rumah','nop')
    list_per_page = 10
    search_fields = ('no_rumah', 'nop')

class BnbaMhktAdmin(LeafletGeoAdmin):
    list_display = ('no_rumah','nop')
    list_per_page = 10
    search_fields = ('no_rumah', 'nop')

class BnbaPinAdmin(LeafletGeoAdmin):
    list_display = ('no_rumah','nop')
    list_per_page = 10
    search_fields = ('no_rumah', 'nop')

class BnbaTelbAdmin(LeafletGeoAdmin):
    list_display = ('no_rumah','nop')
    list_per_page = 10
    search_fields = ('no_rumah', 'nop')

class BnbaTklakAdmin(LeafletGeoAdmin):
    list_display = ('no_rumah','nop')
    list_per_page = 10
    search_fields = ('no_rumah', 'nop')

class BnbaWngselAdmin(LeafletGeoAdmin):
    list_display = ('no_rumah','nop')
    list_per_page = 10
    search_fields = ('no_rumah', 'nop')

class BnbaWngutAdmin(LeafletGeoAdmin):
    list_display = ('no_rumah','nop')
    list_per_page = 10
    search_fields = ('no_rumah', 'nop')

class BnbaLwngAdmin(LeafletGeoAdmin):
    list_display = ('no_rumah','nop')
    list_per_page = 10
    search_fields = ('no_rumah', 'nop')

class BnbaCalAdmin(LeafletGeoAdmin):
    list_display = ('no_rumah','nop')
    list_per_page = 10
    search_fields = ('no_rumah', 'nop')

class BnbaTwutAdmin(LeafletGeoAdmin):
    list_display = ('no_rumah','nop')
    list_per_page = 10
    search_fields = ('no_rumah', 'nop')

class BnbaTwselAdmin(LeafletGeoAdmin):
    list_display = ('no_rumah','nop')
    list_per_page = 10
    search_fields = ('no_rumah', 'nop')

class BnbaBmibAdmin(LeafletGeoAdmin):
    list_display = ('no_rumah','nop')
    list_per_page = 10
    search_fields = ('no_rumah', 'nop')

class BnbaMhkbAdmin(LeafletGeoAdmin):
    list_display = ('no_rumah','nop')
    list_per_page = 10
    search_fields = ('no_rumah', 'nop')

class BnbaSarutAdmin(LeafletGeoAdmin):
    list_display = ('no_rumah','nop')
    list_per_page = 10
    search_fields = ('no_rumah', 'nop')

class BnbaRanotanaAdmin(LeafletGeoAdmin):
    list_display = ('no_rumah','nop')
    list_per_page = 10
    search_fields = ('no_rumah', 'nop')

class BnbaSakobarAdmin(LeafletGeoAdmin):
    list_display = ('no_rumah','nop')
    list_per_page = 10
    search_fields = ('no_rumah', 'nop')

class BnbaSarioAdmin(LeafletGeoAdmin):
    list_display = ('no_rumah','nop')
    list_per_page = 10
    search_fields = ('no_rumah', 'nop')

class BnbaSartumAdmin(LeafletGeoAdmin):
    list_display = ('no_rumah','nop')
    list_per_page = 10
    search_fields = ('no_rumah', 'nop')

class BnbaPaal2Admin(LeafletGeoAdmin):
    list_display = ('no_rumah','nop')
    list_per_page = 10
    search_fields = ('no_rumah', 'nop')

class BnbaKrgwrAdmin(LeafletGeoAdmin):
    list_display = ('no_rumah','nop')
    list_per_page = 10
    search_fields = ('no_rumah', 'nop')

class BnbaPerkamilAdmin(LeafletGeoAdmin):
    list_display = ('no_rumah','nop')
    list_per_page = 10
    search_fields = ('no_rumah', 'nop')

class BnbaMalendengAdmin(LeafletGeoAdmin):
    list_display = ('no_rumah','nop')
    list_per_page = 10
    search_fields = ('no_rumah', 'nop')

class BnbaDenluAdmin(LeafletGeoAdmin):
    list_display = ('no_rumah','nop')
    list_per_page = 10
    search_fields = ('no_rumah', 'nop')

class BnbaRanomuutAdmin(LeafletGeoAdmin):
    list_display = ('no_rumah','nop')
    list_per_page = 10
    search_fields = ('no_rumah', 'nop')

######################################## BATAS BNBA ##################################################################

class BloklapanganAdmin(LeafletGeoAdmin):
    list_display = ('nop', 'blok', 'luasbumi', 'luasbangun', 'legalitasb')
    list_per_page = 10
    search_fields = ('nop', 'legalitasb')

class UmumAdmin(LeafletGeoAdmin):
    list_display = ('lingkungan', 'kecamatan', 'kelurahan')
    list_per_page = 10
    search_fields = ('kecamatan','kelurahan')

class TrTerminalAdmin(LeafletGeoAdmin):
    list_display = ('nama_obyek', 'kode')
    list_per_page = 10
    search_fields = ('nama_obyek','kode')

class SwalayanAdmin(LeafletGeoAdmin):
    list_display = ('nama', 'keterangan', 'minimarket')
    list_per_page = 10
    search_fields = ('nama','keterangan', 'minimarket')

class TrLampuAdmin(LeafletGeoAdmin):
    list_per_page = 10

class TrJembatanAdmin(LeafletGeoAdmin):
    list_per_page = 10

class TrTrayekAdmin(LeafletGeoAdmin):
    list_per_page = 10

class TelekomunikasiAdmin(LeafletGeoAdmin):
    list_per_page = 10

class SmpJalanAdmin(LeafletGeoAdmin):
    list_per_page = 10

class SmpSungaiAdmin(LeafletGeoAdmin):
    list_per_page = 10

class SanitasiAdmin(LeafletGeoAdmin):
    list_per_page = 10

class CctvAdmin(LeafletGeoAdmin):
    list_per_page = 10


# admin.site.register(Incindences, IncidencesAdmin)
admin.site.register(BnbaKl, BnbaKlAdmin)
admin.site.register(BnbaIstq, BnbaIstqAdmin)
admin.site.register(BnbaMhkt, BnbaMhktAdmin)
admin.site.register(BnbaPin, BnbaPinAdmin)
admin.site.register(BnbaTelb, BnbaTelbAdmin)
admin.site.register(BnbaTklak, BnbaTklakAdmin)
admin.site.register(BnbaWngsel, BnbaWngselAdmin)
admin.site.register(BnbaWngut, BnbaWngutAdmin)
admin.site.register(BnbaLwng, BnbaLwngAdmin)
admin.site.register(BnbaCal, BnbaCalAdmin)
admin.site.register(BnbaTwut, BnbaTwutAdmin)
admin.site.register(BnbaTwsel, BnbaTwselAdmin)
admin.site.register(BnbaBmib, BnbaBmibAdmin)
admin.site.register(BnbaMhkb, BnbaMhkbAdmin)
admin.site.register(BnbaSarUt, BnbaSarutAdmin)
admin.site.register(BnbaRanotana, BnbaRanotanaAdmin)
admin.site.register(BnbaSaKobar, BnbaSakobarAdmin)
admin.site.register(BnbaSario, BnbaSarioAdmin)
admin.site.register(BnbaSarTum, BnbaSartumAdmin)
admin.site.register(BnbaPaal2, BnbaPaal2Admin)
admin.site.register(BnbaKrgwr, BnbaKrgwrAdmin)
admin.site.register(BnbaPerkamil, BnbaPerkamilAdmin)
admin.site.register(BnbaDenlu, BnbaDenluAdmin)
admin.site.register(BnbaMalendeng, BnbaMalendengAdmin)
admin.site.register(BnbaRanomuut, BnbaRanomuutAdmin)


########################### BATAS BNBA ##############################################
admin.site.register(Bloklapangan, BloklapanganAdmin)
admin.site.register(Umum, UmumAdmin)
admin.site.register(TrTerminal, TrTerminalAdmin)
admin.site.register(TrLampu, TrLampuAdmin)
admin.site.register(TrJembatan, TrJembatanAdmin)
admin.site.register(TrTrayek, TrTrayekAdmin)
admin.site.register(Telekomunikasi, TelekomunikasiAdmin)
admin.site.register(SmpJalan, SmpJalanAdmin)
admin.site.register(SmpSungai, SmpSungaiAdmin)
admin.site.register(Sanitasi, SanitasiAdmin)
admin.site.register(Cctv, CctvAdmin)
admin.site.register(Swalayan, SwalayanAdmin)
admin.site.site_header = 'Big Data Studio Kota Manado'
admin.site.site_title = 'Big Data Studio Kota Manado'