from django.db import models
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager

# Create your models here.
class Incindences(models.Model):
    name = models.CharField(max_length=20)
    location = models.PointField(srid=4326)
    objects = GeoManager()


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Incidences"

class BnbaKl(models.Model):
    no_rumah = models.CharField(max_length=50, null=True)
    nop = models.CharField(max_length=50, null=True)
    lingkungan = models.CharField(max_length=50, null=True)
    kode_foto = models.CharField(max_length=50, null=True)
    stat = models.CharField(max_length=50, null=True)
    path_foto = models.CharField(max_length=100, null=True)
    trans_id = models.CharField(max_length=50, null=True)
    kode_kec = models.CharField(max_length=50, null=True)
    kode_kel = models.CharField(max_length=50, null=True)
    upk = models.CharField(max_length=50, null=True)
    geom = models.MultiPolygonField(srid=32651)

    def __str__(self):
        return self.no_rumah

    class Meta:
        verbose_name_plural = "Komo Luar"

    class Meta:
        verbose_name = "Komo Luar"

class BnbaIstq(models.Model):
    nop = models.CharField(max_length=50, null=True)
    no_rumah = models.CharField(max_length=50, null=True)
    lingkungan = models.CharField(max_length=50, null=True)
    kode_foto = models.CharField(max_length=50, null=True)
    stat = models.CharField(max_length=50, null=True)
    path_foto = models.CharField(max_length=100, null=True)
    trans_id = models.CharField(max_length=50, null=True)
    kode_kec = models.CharField(max_length=50, null=True)
    kode_kel = models.CharField(max_length=50, null=True)
    upk = models.CharField(max_length=50, null=True)
    geom = models.MultiPolygonField(srid=32651)

    def __str__(self):
        return self.no_rumah

    class Meta:
        verbose_name_plural = "Istiqlal"

    class Meta:
        verbose_name = "Istiqlal"

class BnbaMhkt(models.Model):
    nop = models.CharField(max_length=50, null=True)
    no_rumah = models.CharField(max_length=50, null=True)
    lingkungan = models.CharField(max_length=50, null=True)
    kode_foto = models.CharField(max_length=50, null=True)
    stat = models.CharField(max_length=50, null=True)
    path_foto = models.CharField(max_length=100, null=True)
    trans_id = models.CharField(max_length=50, null=True)
    kode_kec = models.CharField(max_length=50, null=True)
    kode_kel = models.CharField(max_length=50, null=True)
    upk = models.CharField(max_length=50, null=True)
    geom = models.MultiPolygonField(srid=32651)

    def __str__(self):
        return self.no_rumah

    class Meta:
        verbose_name_plural = "Mahakeret Timur"

    class Meta:
        verbose_name = "Mahakeret Timur"

class BnbaPin(models.Model):
    nop = models.CharField(max_length=50, null=True)
    no_rumah = models.CharField(max_length=50, null=True)
    lingkungan = models.CharField(max_length=50, null=True)
    kode_foto = models.CharField(max_length=50, null=True)
    stat = models.CharField(max_length=50, null=True)
    path_foto = models.CharField(max_length=100, null=True)
    trans_id = models.CharField(max_length=50, null=True)
    kode_kec = models.CharField(max_length=50, null=True)
    kode_kel = models.CharField(max_length=50, null=True)
    upk = models.CharField(max_length=50, null=True)
    geom = models.MultiPolygonField(srid=32651)

    def __str__(self):
        return self.no_rumah

    class Meta:
        verbose_name_plural = "Pinaesaan"

    class Meta:
        verbose_name = "Pinaesaan"

class BnbaTelb(models.Model):
    nop = models.CharField(max_length=50, null=True)
    no_rumah = models.CharField(max_length=50, null=True)
    lingkungan = models.CharField(max_length=50, null=True)
    kode_foto = models.CharField(max_length=50, null=True)
    stat = models.CharField(max_length=50, null=True)
    path_foto = models.CharField(max_length=100, null=True)
    trans_id = models.CharField(max_length=50, null=True)
    kode_kec = models.CharField(max_length=50, null=True)
    kode_kel = models.CharField(max_length=50, null=True)
    upk = models.CharField(max_length=50, null=True)
    geom = models.MultiPolygonField(srid=32651)

    def __str__(self):
        return self.no_rumah

    class Meta:
        verbose_name_plural = "Teling Bawah"

    class Meta:
        verbose_name = "Teling Bawah"

class BnbaTklak(models.Model):
    nop = models.CharField(max_length=50, null=True)
    no_rumah = models.CharField(max_length=50, null=True)
    lingkungan = models.CharField(max_length=50, null=True)
    kode_foto = models.CharField(max_length=50, null=True)
    stat = models.CharField(max_length=50, null=True)
    path_foto = models.CharField(max_length=100, null=True)
    trans_id = models.CharField(max_length=50, null=True)
    kode_kec = models.CharField(max_length=50, null=True)
    kode_kel = models.CharField(max_length=50, null=True)
    upk = models.CharField(max_length=50, null=True)
    geom = models.MultiPolygonField(srid=32651)

    def __str__(self):
        return self.no_rumah

    class Meta:
        verbose_name_plural = "Tikala Kumaraka"

    class Meta:
        verbose_name = "Tikala Kumaraka"

class BnbaWngsel(models.Model):
    nop = models.CharField(max_length=50, null=True)
    no_rumah = models.CharField(max_length=50, null=True)
    lingkungan = models.CharField(max_length=50, null=True)
    kode_foto = models.CharField(max_length=50, null=True)
    stat = models.CharField(max_length=50, null=True)
    path_foto = models.CharField(max_length=100, null=True)
    trans_id = models.CharField(max_length=50, null=True)
    kode_kec = models.CharField(max_length=50, null=True)
    kode_kel = models.CharField(max_length=50, null=True)
    upk = models.CharField(max_length=50, null=True)
    geom = models.MultiPolygonField(srid=32651)

    def __str__(self):
        return self.no_rumah

    class Meta:
        verbose_name_plural = "Wenang Selatan"

    class Meta:
        verbose_name = "Wenang Selatan"

class BnbaWngut(models.Model):
    nop = models.CharField(max_length=50, null=True)
    no_rumah = models.CharField(max_length=50, null=True)
    lingkungan = models.CharField(max_length=50, null=True)
    kode_foto = models.CharField(max_length=50, null=True)
    stat = models.CharField(max_length=50, null=True)
    path_foto = models.CharField(max_length=100, null=True)
    trans_id = models.CharField(max_length=50, null=True)
    kode_kec = models.CharField(max_length=50, null=True)
    kode_kel = models.CharField(max_length=50, null=True)
    upk = models.CharField(max_length=50, null=True)
    geom = models.MultiPolygonField(srid=32651)

    def __str__(self):
        return self.no_rumah

    class Meta:
        verbose_name_plural = "Wenang Utara"

    class Meta:
        verbose_name = "Wenang Utara"


class BnbaLwng(models.Model):
    nop = models.CharField(max_length=50, null=True)
    no_rumah = models.CharField(max_length=50, null=True)
    lingkungan = models.CharField(max_length=50, null=True)
    kode_foto = models.CharField(max_length=50, null=True)
    stat = models.CharField(max_length=50, null=True)
    path_foto = models.CharField(max_length=100, null=True)
    trans_id = models.CharField(max_length=50, null=True)
    kode_kec = models.CharField(max_length=50, null=True)
    kode_kel = models.CharField(max_length=50, null=True)
    upk = models.CharField(max_length=50, null=True)
    geom = models.MultiPolygonField(srid=32651)

    def __str__(self):
        return self.no_rumah

    class Meta:
        verbose_name_plural = "Lawangirung"

    class Meta:
        verbose_name = "Lawangirung"

class BnbaCal(models.Model):
    no_rumah = models.CharField(max_length=50, null=True)
    nop = models.CharField(max_length=50, null=True)
    lingkungan = models.CharField(max_length=50, null=True)
    kode_foto = models.CharField(max_length=50, null=True)
    stat = models.CharField(max_length=50, null=True)
    path_foto = models.CharField(max_length=100, null=True)
    trans_id = models.CharField(max_length=50, null=True)
    kode_kec = models.CharField(max_length=50, null=True)
    kode_kel = models.CharField(max_length=50, null=True)
    upk = models.CharField(max_length=50, null=True)
    geom = models.MultiPolygonField(srid=32651)

    def __str__(self):
        return self.no_rumah

    class Meta:
        verbose_name_plural = "Calaca"

    class Meta:
        verbose_name = "Calaca"

class BnbaTwut(models.Model):
    nop = models.CharField(max_length=50, null=True)
    no_rumah = models.CharField(max_length=50, null=True)
    lingkungan = models.CharField(max_length=50, null=True)
    kode_foto = models.CharField(max_length=50, null=True)
    stat = models.CharField(max_length=50, null=True)
    path_foto = models.CharField(max_length=100, null=True)
    trans_id = models.CharField(max_length=50, null=True)
    kode_kec = models.CharField(max_length=50, null=True)
    kode_kel = models.CharField(max_length=50, null=True)
    upk = models.CharField(max_length=50, null=True)
    geom = models.MultiPolygonField(srid=32651)

    def __str__(self):
        return self.no_rumah

    class Meta:
        verbose_name_plural = "Titiwungen Utara"

    class Meta:
        verbose_name = "Titiwungen Utara"

class BnbaTwsel(models.Model):
    nop = models.CharField(max_length=50, null=True)
    no_rumah = models.CharField(max_length=50, null=True)
    lingkungan = models.CharField(max_length=50, null=True)
    kode_foto = models.CharField(max_length=50, null=True)
    stat = models.CharField(max_length=50, null=True)
    path_foto = models.CharField(max_length=100, null=True)
    trans_id = models.CharField(max_length=50, null=True)
    kode_kec = models.CharField(max_length=50, null=True)
    kode_kel = models.CharField(max_length=50, null=True)
    upk = models.CharField(max_length=50, null=True)
    geom = models.MultiPolygonField(srid=32651)

    def __str__(self):
        return self.no_rumah

    class Meta:
        verbose_name_plural = "Titiwungen Selatan"

    class Meta:
        verbose_name = "Titiwungen Selatan"

class BnbaBmib(models.Model):
    nop = models.CharField(max_length=50, null=True)
    no_rumah = models.CharField(max_length=50, null=True)
    lingkungan = models.CharField(max_length=50, null=True)
    kode_foto = models.CharField(max_length=50, null=True)
    stat = models.CharField(max_length=50, null=True)
    path_foto = models.CharField(max_length=100, null=True)
    trans_id = models.CharField(max_length=50, null=True)
    kode_kec = models.CharField(max_length=50, null=True)
    kode_kel = models.CharField(max_length=50, null=True)
    upk = models.CharField(max_length=50, null=True)
    geom = models.MultiPolygonField(srid=32651)

    def __str__(self):
        return self.no_rumah

    class Meta:
        verbose_name_plural = "Bumi Beringin"

    class Meta:
        verbose_name = "Bumi Beringin"

class BnbaMhkb(models.Model):
    nop = models.CharField(max_length=50, null=True)
    no_rumah = models.CharField(max_length=50, null=True)
    lingkungan = models.CharField(max_length=50, null=True)
    kode_foto = models.CharField(max_length=50, null=True)
    stat = models.CharField(max_length=50, null=True)
    path_foto = models.CharField(max_length=100, null=True)
    trans_id = models.CharField(max_length=50, null=True)
    kode_kec = models.CharField(max_length=50, null=True)
    kode_kel = models.CharField(max_length=50, null=True)
    upk = models.CharField(max_length=50, null=True)
    geom = models.MultiPolygonField(srid=32651)

    def __str__(self):
        return self.no_rumah

    class Meta:
        verbose_name_plural = "Mahakeret Barat"

    class Meta:
        verbose_name = "Mahakeret Barat"

class BnbaSarUt(models.Model):
    nop = models.CharField(max_length=50, null=True)
    no_rumah = models.CharField(max_length=50, null=True)
    lingkungan = models.CharField(max_length=50, null=True)
    kode_foto = models.CharField(max_length=50, null=True)
    stat = models.CharField(max_length=50, null=True)
    path_foto = models.CharField(max_length=100, null=True)
    trans_id = models.CharField(max_length=50, null=True)
    kode_kec = models.CharField(max_length=50, null=True)
    kode_kel = models.CharField(max_length=50, null=True)
    upk = models.CharField(max_length=50, null=True)
    geom = models.MultiPolygonField(srid=32651, null=True)

    def __str__(self):
        return self.no_rumah

    class Meta:
        verbose_name_plural = "Sario Utara"

    class Meta:
        verbose_name = "Sario Utara"

class BnbaSario(models.Model):
    nop = models.CharField(max_length=50, null=True)
    no_rumah = models.CharField(max_length=50, null=True)
    lingkungan = models.CharField(max_length=50, null=True)
    kode_foto = models.CharField(max_length=50, null=True)
    stat = models.CharField(max_length=50, null=True)
    path_foto = models.CharField(max_length=100, null=True)
    trans_id = models.CharField(max_length=50, null=True)
    kode_kec = models.CharField(max_length=50, null=True)
    kode_kel = models.CharField(max_length=50, null=True)
    upk = models.CharField(max_length=50, null=True)
    geom = models.MultiPolygonField(srid=32651)

    def __str__(self):
        return self.no_rumah

    class Meta:
        verbose_name_plural = "Sario"

    class Meta:
        verbose_name = "Sario"

class BnbaSaKobar(models.Model):
    nop = models.CharField(max_length=50, null=True)
    no_rumah = models.CharField(max_length=50, null=True)
    lingkungan = models.CharField(max_length=50, null=True)
    kode_foto = models.CharField(max_length=50, null=True)
    stat = models.CharField(max_length=50, null=True)
    path_foto = models.CharField(max_length=100, null=True)
    trans_id = models.CharField(max_length=50, null=True)
    kode_kec = models.CharField(max_length=50, null=True)
    kode_kel = models.CharField(max_length=50, null=True)
    upk = models.CharField(max_length=50, null=True)
    geom = models.MultiPolygonField(srid=32651)

    def __str__(self):
        return self.no_rumah

    class Meta:
        verbose_name_plural = "Sario Kotabaru"

    class Meta:
        verbose_name = "Sario Kotabaru"

class BnbaSarTum(models.Model):
    nop = models.CharField(max_length=50, null=True)
    no_rumah = models.CharField(max_length=50, null=True)
    lingkungan = models.CharField(max_length=50, null=True)
    kode_foto = models.CharField(max_length=50, null=True)
    stat = models.CharField(max_length=50, null=True)
    path_foto = models.CharField(max_length=100, null=True)
    trans_id = models.CharField(max_length=50, null=True)
    kode_kec = models.CharField(max_length=50, null=True)
    kode_kel = models.CharField(max_length=50, null=True)
    upk = models.CharField(max_length=50, null=True)
    geom = models.MultiPolygonField(srid=32651)

    def __str__(self):
        return self.no_rumah

    class Meta:
        verbose_name_plural = "Sario Tumpaan"

    class Meta:
        verbose_name = "Sario Tumpaan"

class BnbaRanotana(models.Model):
    nop = models.CharField(max_length=50, null=True)
    no_rumah = models.CharField(max_length=50, null=True)
    lingkungan = models.CharField(max_length=50, null=True)
    kode_foto = models.CharField(max_length=50, null=True)
    stat = models.CharField(max_length=50, null=True)
    path_foto = models.CharField(max_length=100, null=True)
    trans_id = models.CharField(max_length=50, null=True)
    kode_kec = models.CharField(max_length=50, null=True)
    kode_kel = models.CharField(max_length=50, null=True)
    upk = models.CharField(max_length=50, null=True)
    geom = models.MultiPolygonField(srid=32651)

    def __str__(self):
        return self.no_rumah

    class Meta:
        verbose_name_plural = "Ranotana"

    class Meta:
        verbose_name = "Ranotana"

class BnbaPaal2(models.Model):
    nop = models.CharField(max_length=50, null=True)
    no_rumah = models.CharField(max_length=50, null=True)
    lingkungan = models.CharField(max_length=50, null=True)
    kode_foto = models.CharField(max_length=50, null=True)
    stat = models.CharField(max_length=50, null=True)
    path_foto = models.CharField(max_length=100, null=True)
    trans_id = models.CharField(max_length=50, null=True)
    kode_kec = models.CharField(max_length=50, null=True)
    kode_kel = models.CharField(max_length=50, null=True)
    upk = models.CharField(max_length=50, null=True)
    geom = models.MultiPolygonField(srid=32651)

    def __str__(self):
        return self.no_rumah

    class Meta:
        verbose_name_plural = "Paal 2"

    class Meta:
        verbose_name = "Paal 2"

class BnbaKrgwr(models.Model):
    nop = models.CharField(max_length=50, null=True)
    no_rumah = models.CharField(max_length=50, null=True)
    lingkungan = models.CharField(max_length=50, null=True)
    kode_foto = models.CharField(max_length=50, null=True)
    stat = models.CharField(max_length=50, null=True)
    path_foto = models.CharField(max_length=100, null=True)
    trans_id = models.CharField(max_length=50, null=True)
    kode_kec = models.CharField(max_length=50, null=True)
    kode_kel = models.CharField(max_length=50, null=True)
    upk = models.CharField(max_length=50, null=True)
    geom = models.MultiPolygonField(srid=32651)

    def __str__(self):
        return self.no_rumah

    class Meta:
        verbose_name_plural = "Kairagi Weru"

    class Meta:
        verbose_name = "Kairagi Weru"

class BnbaPerkamil(models.Model):
    nop = models.CharField(max_length=50, null=True)
    no_rumah = models.CharField(max_length=50, null=True)
    lingkungan = models.CharField(max_length=50, null=True)
    kode_foto = models.CharField(max_length=50, null=True)
    stat = models.CharField(max_length=50, null=True)
    path_foto = models.CharField(max_length=100, null=True)
    trans_id = models.CharField(max_length=50, null=True)
    kode_kec = models.CharField(max_length=50, null=True)
    kode_kel = models.CharField(max_length=50, null=True)
    upk = models.CharField(max_length=50, null=True)
    geom = models.MultiPolygonField(srid=32651)

    def __str__(self):
        return self.no_rumah

    class Meta:
        verbose_name_plural = "Perkamil"

    class Meta:
        verbose_name = "Perkamil"

class BnbaMalendeng(models.Model):
    nop = models.CharField(max_length=50, null=True)
    no_rumah = models.CharField(max_length=50, null=True)
    lingkungan = models.CharField(max_length=50, null=True)
    kode_foto = models.CharField(max_length=50, null=True)
    stat = models.CharField(max_length=50, null=True)
    path_foto = models.CharField(max_length=100, null=True)
    trans_id = models.CharField(max_length=50, null=True)
    kode_kec = models.CharField(max_length=50, null=True)
    kode_kel = models.CharField(max_length=50, null=True)
    upk = models.CharField(max_length=50, null=True)
    geom = models.MultiPolygonField(srid=32651)

    def __str__(self):
        return self.no_rumah

    class Meta:
        verbose_name_plural = "Malendeng"

    class Meta:
        verbose_name = "Malendeng"

class BnbaDenlu(models.Model):
    nop = models.CharField(max_length=50, null=True)
    no_rumah = models.CharField(max_length=50, null=True)
    lingkungan = models.CharField(max_length=50, null=True)
    kode_foto = models.CharField(max_length=50, null=True)
    stat = models.CharField(max_length=50, null=True)
    path_foto = models.CharField(max_length=100, null=True)
    trans_id = models.CharField(max_length=50, null=True)
    kode_kec = models.CharField(max_length=50, null=True)
    kode_kel = models.CharField(max_length=50, null=True)
    upk = models.CharField(max_length=50, null=True)
    geom = models.MultiPolygonField(srid=32651)

    def __str__(self):
        return self.no_rumah

    class Meta:
        verbose_name_plural = "Dendengan luar"

    class Meta:
        verbose_name = "Dendengan Luar"

class BnbaRanomuut(models.Model):
    nop = models.CharField(max_length=50, null=True)
    no_rumah = models.CharField(max_length=50, null=True)
    lingkungan = models.CharField(max_length=50, null=True)
    kode_foto = models.CharField(max_length=50, null=True)
    stat = models.CharField(max_length=50, null=True)
    path_foto = models.CharField(max_length=100, null=True)
    trans_id = models.CharField(max_length=50, null=True)
    kode_kec = models.CharField(max_length=50, null=True)
    kode_kel = models.CharField(max_length=50, null=True)
    upk = models.CharField(max_length=50, null=True)
    geom = models.MultiPolygonField(srid=32651)

    def __str__(self):
        return self.no_rumah

    class Meta:
        verbose_name_plural = "Ranomuut"

    class Meta:
        verbose_name = "Ranomuut"
#############################BATAS BNBA##############################################################################
class Swalayan(models.Model):
    nama = models.CharField(max_length=50, null=True)
    keterangan = models.CharField(max_length=50, null=True)
    minimarket = models.CharField(max_length=50, null=True)
    geom = models.MultiPointField(srid=32651)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = "Swalayan"

    class Meta:
        verbose_name = "Swalayan"


class Bloklapangan(models.Model):
    nop_field = models.CharField(max_length=50)
    d_nop = models.CharField(max_length=50)
    blok = models.CharField(max_length=50)
    num = models.FloatField()
    nop = models.CharField(max_length=254)
    wajibpajak = models.CharField("Wajib Pajak ",max_length=254)
    nik = models.CharField("NIK ",max_length=254)
    alamat = models.CharField(max_length=254)
    luasbumi = models.CharField(max_length=254)
    luasbangun = models.CharField(max_length=254)
    jumlahlant = models.CharField(max_length=254)
    kondisiata = models.CharField(max_length=254)
    kondisidin = models.CharField(max_length=254)
    jenislanta = models.CharField(max_length=254)
    keterangan = models.CharField(max_length=254)
    penghuni = models.CharField(max_length=254)
    pria = models.CharField(max_length=254)
    wanita = models.CharField(max_length=254)
    difabel = models.CharField(max_length=254)
    sumberair = models.CharField(max_length=254)
    jamban = models.CharField(max_length=254)
    sampah = models.CharField(max_length=254)
    pekerjaan = models.CharField(max_length=254)
    kesehatan = models.CharField(max_length=254)
    pendidikan = models.CharField(max_length=254)
    penguasaan = models.CharField(max_length=254)
    legalitasb = models.CharField(max_length=254)
    lahanbng = models.CharField(max_length=254)
    geom = models.MultiPolygonField(srid=32651)

    def __str__(self):
        return self.nop_field

    class Meta:
        verbose_name = "Baseline"

class Umum(models.Model):
    num = models.CharField(max_length=50)
    kecamatan = models.CharField(max_length=254)
    kelurahan = models.CharField(max_length=254)
    lingkungan = models.CharField(max_length=254)
    jumlah = models.FloatField()
    penduduk_laki_laki = models.FloatField()
    penduduk_perempuan = models.FloatField()
    disabilitas = models.FloatField()
    satuan1 = models.CharField(max_length=254)
    pertanian = models.FloatField()
    perikanan = models.FloatField()
    tambang = models.FloatField()
    industri = models.FloatField()
    konstruksi = models.FloatField()
    perdagangan = models.FloatField()
    pemerintah = models.FloatField()
    dalam_kel = models.FloatField()
    luar_kel = models.FloatField()
    kota_luar = models.FloatField()
    tidak_sekolah = models.FloatField()
    tidak_ada_angg = models.FloatField()
    satuan2 = models.CharField(max_length=254)
    luas = models.IntegerField()
    kepadatan_penduduk = models.FloatField()
    geom = models.MultiPolygonField(srid=32651)

    def __str__(self):
        return self.lingkungan

    class Meta:
        verbose_name_plural = "Umum"

class PatchSulut(models.Model):
    objectid = models.IntegerField()
    area = models.IntegerField()
    toponym = models.CharField(max_length=25)
    geom = models.MultiPolygonField(srid=32651)


    def __str__(self):
        return self.toponym

    class Meta:
        verbose_name_plural = "Patch Sulut"

    class Meta:
        verbose_name = "Patch Sulut"


class TrTerminal(models.Model):
    point_x = models.FloatField()
    point_y = models.FloatField()
    nama_obyek = models.CharField(max_length=254)
    kls_obyek = models.CharField(max_length=254)
    kode = models.CharField(max_length=254)
    no_foto = models.CharField(max_length=254)
    tgl_survey = models.CharField(max_length=254)
    geom = models.MultiPointField(srid=32651)

    def __str__(self):
        return self.nama_obyek

    class Meta:
        verbose_name_plural = "Terminal Transportasi"

    class Meta:
        verbose_name = "Terminal"

class TrLampu(models.Model):
    geom = models.MultiPointField(srid=32651)

    class Meta:
        verbose_name_plural = "Lampu Lalu Lintas"

    class Meta:
        verbose_name = "Lampu Lalu Lintas"

class TrJembatan(models.Model):
    oid_field = models.IntegerField()
    name = models.CharField(max_length=254)
    base = models.FloatField()
    snippet = models.CharField(max_length=254)
    labelid = models.IntegerField()
    folder_pat = models.CharField(max_length=50)
    symbol_id = models.CharField(max_length=50)
    alt_mode = models.CharField(max_length=50)
    pop_up_inf = models.CharField(max_length=50)
    hsl_tabel = models.CharField(max_length=50)
    geom = models.MultiPointField(srid=32651)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Jembatan"

    class Meta:
        verbose_name = "Jembatan"

class TrTrayek(models.Model):
    panjang_km = models.FloatField()
    nama_traye = models.CharField(max_length=254)
    kode_traye = models.CharField(max_length=254)
    rute = models.CharField(max_length=254)
    geom = models.MultiLineStringField(srid=32651)

    def __str__(self):
            return self.nama_traye

    class Meta:
          verbose_name_plural = "Trayek"

    class Meta:
          verbose_name = "Trayek"

class Telekomunikasi(models.Model):
    no = models.FloatField()
    menara = models.CharField(max_length=254)
    longitude = models.FloatField()
    lattitude = models.FloatField()
    antena_hei = models.FloatField()
    site_categ = models.CharField(max_length=254)
    desa = models.CharField(max_length=254)
    kecamatan = models.CharField(max_length=254)
    kabupaten = models.CharField(max_length=254)
    geom = models.MultiPointField(srid=32651)

    def __str__(self):
        return self.menara

    class Meta:
        verbose_name_plural = "BTS Telekomunikasi"

    class Meta:
        verbose_name = "BTS Telekomunikasi"

class SmpJalan(models.Model):
    point_x = models.FloatField()
    point_y = models.FloatField()
    nama_obyek = models.CharField(max_length=254)
    kls_obyek = models.CharField(max_length=254)
    kode = models.CharField(max_length=254)
    no_foto = models.CharField(max_length=254)
    tgl_surv = models.CharField(max_length=254)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=32651)

    def __str__(self):
        return self.nama_obyek

    class Meta:
        verbose_name_plural = "Sempadan Jalan"

    class Meta:
        verbose_name = "Sempadan Jalan"

class SmpSungai(models.Model):
    point_x = models.FloatField()
    point_y = models.FloatField()
    nama_obyek = models.CharField(max_length=254)
    kls_obyek = models.CharField(max_length=254)
    kode = models.CharField(max_length=254)
    no_foto = models.CharField(max_length=254)
    tgl_surv = models.CharField(max_length=254)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=32651)

    def __str__(self):
        return self.nama_obyek

    class Meta:
        verbose_name_plural = "Sempadan Sungai"

    class Meta:
        verbose_name = "Sempadan Sungai"

class Sanitasi(models.Model):
    fid_field = models.IntegerField()
    name = models.CharField(max_length=254)
    descript = models.CharField(max_length=254)
    type = models.CharField(max_length=254)
    comment = models.CharField(max_length=254)
    symbol = models.CharField(max_length=254)
    datetimes = models.CharField(max_length=24)
    elevation = models.FloatField()
    keterangan = models.CharField(max_length=254)
    geom = models.MultiPointField(srid=32651)

    def __str__(self):
        return self.keterangan

    class Meta:
        verbose_name_plural = "Sanitasi"

    class Meta:
        verbose_name = "Sanitasi"

class Cctv(models.Model):
    lokasi = models.CharField(max_length=50)
    geom = models.MultiPointField(srid=32651)
