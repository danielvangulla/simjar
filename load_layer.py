import os
from django.contrib.gis.utils import LayerMapping
from .models import Bloklapangan, Umum, PatchSulut, TrTerminal, TrLampu, TrJembatan, TrTrayek, Telekomunikasi, SmpJalan, \
    SmpSungai, Sanitasi, Cctv, Swalayan, BnbaKl, BnbaIstq, BnbaMhkt, BnbaTelb, BnbaTklak, BnbaWngsel, BnbaPin, BnbaWngut, BnbaLwng, \
    BnbaTwut, BnbaTwsel, BnbaCal, BnbaBmib, BnbaMhkb, BnbaSarUt, BnbaRanotana, BnbaSaKobar, BnbaSario, BnbaSarTum, BnbaPerkamil, BnbaKrgwr, \
    BnbaPaal2, BnbaMalendeng, BnbaDenlu, BnbaRanomuut

# Auto-generated `LayerMapping` dictionary for BnbaKl model
bnbakl_mapping = {
    'nop': 'nop',
    'no_rumah': 'no_rumah',
    'lingkungan': 'lingkungan',
    'kode_foto': 'kode_foto',
    'Status': 'Status',
    'path_foto': 'path_foto',
    'geom': 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for Bnbaistq model
bnbaistq_mapping = {
    'nop': 'nop',
    'no_rumah': 'no_rumah',
    'lingkungan': 'lingkungan',
    'kode_foto': 'kode_foto',
    'Status': 'Status',
    'path_foto': 'path_foto',
    'geom': 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for BnbaMhkt model
bnbamhkt_mapping = {
    'nop': 'nop',
    'no_rumah': 'no_rumah',
    'lingkungan': 'lingkungan',
    'kode_foto': 'kode_foto',
    'Status': 'Status',
    'path_foto': 'path_foto',
    'geom': 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for BnbaPin model
bnbapin_mapping = {
    'nop': 'nop',
    'no_rumah': 'no_rumah',
    'lingkungan': 'lingkungan',
    'kode_foto': 'kode_foto',
    'Status': 'Status',
    'path_foto': 'path_foto',
    'geom': 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for BnbaTelb model
bnbatelb_mapping = {
    'nop': 'nop',
    'no_rumah': 'no_rumah',
    'lingkungan': 'lingkungan',
    'kode_foto': 'kode_foto',
    'Status': 'Status',
    'path_foto': 'path_foto',
    'geom': 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for BnbaTklak model
bnbatklak_mapping = {
    'nop': 'nop',
    'no_rumah': 'no_rumah',
    'lingkungan': 'lingkungan',
    'kode_foto': 'kode_foto',
    'Status': 'Status',
    'path_foto': 'path_foto',
    'geom': 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for BnbaWngsel model
bnbawngsel_mapping = {
    'nop': 'nop',
    'no_rumah': 'no_rumah',
    'lingkungan': 'lingkungan',
    'kode_foto': 'kode_foto',
    'Status': 'Status',
    'path_foto': 'path_foto',
    'geom': 'MULTIPOLYGON25D',
}

# Auto-generated `LayerMapping` dictionary for BnbaWngut model
bnbawngut_mapping = {
    'nop': 'nop',
    'no_rumah': 'no_rumah',
    'lingkungan': 'lingkungan',
    'kode_foto': 'kode_foto',
    'stat': 'stat',
    'path_foto': 'path_foto',
    'geom': 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for BnbaLwng model
bnbalwng_mapping = {
    'nop': 'nop',
    'no_rumah': 'no_rumah',
    'lingkungan': 'lingkungan',
    'kode_foto': 'kode_foto',
    'stat': 'stat',
    'path_foto': 'path_foto',
    'geom': 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for BnbaCal model
bnbacal_mapping = {
    'no_rumah': 'no_rumah',
    'nop': 'nop',
    'lingkungan': 'lingkungan',
    'kode_foto': 'kode_foto',
    'stat': 'stat',
    'path_foto': 'path_foto',
    'geom': 'MULTIPOLYGON25D',
}

# Auto-generated `LayerMapping` dictionary for BnbaTwut model
bnbatwut_mapping = {
    'nop': 'nop',
    'no_rumah': 'no_rumah',
    'lingkungan': 'lingkungan',
    'kode_foto': 'kode_foto',
    'stat': 'stat',
    'path_foto': 'path_foto',
    'geom': 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for BnbaTwsel model
bnbatwsel_mapping = {
    'nop': 'nop',
    'no_rumah': 'no_rumah',
    'lingkungan': 'lingkungan',
    'kode_foto': 'kode_foto',
    'stat': 'stat',
    'path_foto': 'path_foto',
    'geom': 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for BnbaBmib model
bnbabmib_mapping = {
    'nop': 'nop',
    'no_rumah': 'no_rumah',
    'lingkungan': 'lingkungan',
    'kode_foto': 'kode_foto',
    'stat': 'stat',
    'path_foto': 'path_foto',
    'trans_id': 'trans_id',
    'kode_kec': 'kode_kec',
    'kode_kel': 'kode_kel',
    'upk': 'upk',
    'geom': 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for BnbaMhkb model
bnbamhkb_mapping = {
    'nop': 'nop',
    'no_rumah': 'no_rumah',
    'lingkungan': 'lingkungan',
    'kode_foto': 'kode_foto',
    'stat': 'stat',
    'path_foto': 'path_foto',
    'trans_id': 'trans_id',
    'kode_kec': 'kode_kec',
    'kode_kel': 'kode_kel',
    'upk': 'upk',
    'geom': 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for BnbaSarut model
bnbasarut_mapping = {
    'nop': 'nop',
    'no_rumah': 'no_rumah',
    'lingkungan': 'lingkungan',
    'kode_foto': 'kode_foto',
    'stat': 'stat',
    'path_foto': 'path_foto',
    'trans_id': 'trans_id',
    'kode_kec': 'kode_kec',
    'kode_kel': 'kode_kel',
    'upk': 'upk',
    'geom': 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for BnbaRanotana model
bnbaranotana_mapping = {
    'nop': 'nop',
    'no_rumah': 'no_rumah',
    'lingkungan': 'lingkungan',
    'kode_foto': 'kode_foto',
    'stat': 'stat',
    'path_foto': 'path_foto',
    'trans_id': 'trans_id',
    'kode_kec': 'kode_kec',
    'kode_kel': 'kode_kel',
    'upk': 'upk',
    'geom': 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for BnbaSaKobar model
bnbasakobar_mapping = {
    'nop': 'nop',
    'no_rumah': 'no_rumah',
    'lingkungan': 'lingkungan',
    'kode_foto': 'kode_foto',
    'stat': 'stat',
    'path_foto': 'path_foto',
    'trans_id': 'trans_id',
    'kode_kec': 'kode_kec',
    'kode_kel': 'kode_kel',
    'upk': 'upk',
    'geom': 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for BnbaSario model
bnbasario_mapping = {
    'nop': 'nop',
    'no_rumah': 'no_rumah',
    'lingkungan': 'lingkungan',
    'kode_foto': 'kode_foto',
    'stat': 'stat',
    'path_foto': 'path_foto',
    'trans_id': 'trans_id',
    'kode_kec': 'kode_kec',
    'kode_kel': 'kode_kel',
    'upk': 'upk',
    'geom': 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for BnbaSarTum model
bnbasartum_mapping = {
    'nop': 'nop',
    'no_rumah': 'no_rumah',
    'lingkungan': 'lingkungan',
    'kode_foto': 'kode_foto',
    'stat': 'stat',
    'path_foto': 'path_foto',
    'trans_id': 'trans_id',
    'kode_kec': 'kode_kec',
    'kode_kel': 'kode_kel',
    'upk': 'upk',
    'geom': 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for BnbaPaal2 model
bnbapaal2_mapping = {
    'nop': 'nop',
    'no_rumah': 'no_rumah',
    'lingkungan': 'lingkungan',
    'kode_foto': 'kode_foto',
    'stat': 'stat',
    'path_foto': 'path_foto',
    'trans_id': 'trans_id',
    'kode_kec': 'kode_kec',
    'kode_kel': 'kode_kel',
    'upk': 'upk',
    'geom': 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for BnbaKrgwr model
bnbakrgwr_mapping = {
    'nop': 'nop',
    'no_rumah': 'no_rumah',
    'lingkungan': 'lingkungan',
    'kode_foto': 'kode_foto',
    'stat': 'stat',
    'path_foto': 'path_foto',
    'trans_id': 'trans_id',
    'kode_kec': 'kode_kec',
    'kode_kel': 'kode_kel',
    'upk': 'upk',
    'geom': 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for BnbaDenlu model
bnbadenlu_mapping = {
    'nop': 'nop',
    'no_rumah': 'no_rumah',
    'lingkungan': 'lingkungan',
    'kode_foto': 'kode_foto',
    'stat': 'stat',
    'path_foto': 'path_foto',
    'trans_id': 'trans_id',
    'kode_kec': 'kode_kec',
    'kode_kel': 'kode_kel',
    'upk': 'upk',
    'geom': 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for BnbaMalendeng model
bnbamalendeng_mapping = {
    'nop': 'nop',
    'no_rumah': 'no_rumah',
    'lingkungan': 'lingkungan',
    'kode_foto': 'kode_foto',
    'stat': 'stat',
    'path_foto': 'path_foto',
    'trans_id': 'trans_id',
    'kode_kec': 'kode_kec',
    'kode_kel': 'kode_kel',
    'upk': 'upk',
    'geom': 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for BnbaPerkamil model
bnbaperkamil_mapping = {
    'nop': 'nop',
    'no_rumah': 'no_rumah',
    'lingkungan': 'lingkungan',
    'kode_foto': 'kode_foto',
    'stat': 'stat',
    'path_foto': 'path_foto',
    'trans_id': 'trans_id',
    'kode_kec': 'kode_kec',
    'kode_kel': 'kode_kel',
    'upk': 'upk',
    'geom': 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for BnbaRanomuut model
bnbaranomuut_mapping = {
    'nop': 'nop',
    'no_rumah': 'no_rumah',
    'lingkungan': 'lingkungan',
    'kode_foto': 'kode_foto',
    'stat': 'stat',
    'path_foto': 'path_foto',
    'trans_id': 'trans_id',
    'kode_kec': 'kode_kec',
    'kode_kel': 'kode_kel',
    'upk': 'upk',
    'geom': 'MULTIPOLYGON',
}

############################################## Batas BNBA ########################################################

# Auto-generated `LayerMapping` dictionary for Swalayan model
swalayan_mapping = {
    'nama': 'nama',
    'keterangan': 'keterangan',
    'geom': 'MULTIPOINT25D',
}

# Auto-generated `LayerMapping` dictionary for Bloklapangan model
bloklapangan_mapping = {
    'nop_field': 'NOP_',
    'd_nop': 'D_NOP',
    'blok': 'BLOK',
    'num': 'NUM',
    'nop': 'NOP',
    'wajibpajak': 'WAJIBPAJAK',
    'nik': 'NIK',
    'alamat': 'ALAMAT',
    'luasbumi': 'LUASBUMI',
    'luasbangun': 'LUASBANGUN',
    'jumlahlant': 'JUMLAHLANT',
    'kondisiata': 'KONDISIATA',
    'kondisidin': 'KONDISIDIN',
    'jenislanta': 'JENISLANTA',
    'keterangan': 'KETERANGAN',
    'penghuni': 'PENGHUNI',
    'pria': 'PRIA',
    'wanita': 'WANITA',
    'difabel': 'DIFABEL',
    'sumberair': 'SUMBERAIR',
    'jamban': 'JAMBAN',
    'sampah': 'SAMPAH',
    'pekerjaan': 'PEKERJAAN',
    'kesehatan': 'KESEHATAN',
    'pendidikan': 'PENDIDIKAN',
    'penguasaan': 'PENGUASAAN',
    'legalitasb': 'LEGALITASB',
    'lahanbng': 'LAHANBNG',
    'geom': 'MULTIPOLYGON25D',
}

# Auto-generated `LayerMapping` dictionary for Umum model
umum_mapping = {
    'num': 'Num',
    'kecamatan': 'KECAMATAN',
    'kelurahan': 'KELURAHAN',
    'lingkungan': 'LINGKUNGAN',
    'jumlah': 'JUMLAH',
    'penduduk_laki_laki': 'L',
    'penduduk_perempuan': 'P',
    'disabilitas': 'DISABILITA',
    'satuan1': 'SATUAN1',
    'pertanian': 'PERTANIAN',
    'perikanan': 'PERIKANAN',
    'tambang': 'TAMBANG',
    'industri': 'INDUSTRI',
    'konstruksi': 'KONSTRUKSI',
    'perdagangan': 'PERDAGANGA',
    'pemerintah': 'PEMERINTAH',
    'dalam_kel': 'DALAMKEL',
    'luar_kel': 'LUARKEL',
    'kota_luar': 'KOTALUAR',
    'tidak_sekolah': 'TIDAKSEKOL',
    'tidak_ada_angg': 'TDKADAANGG',
    'satuan2': 'SATUAN2',
    'luas': 'LUAS',
    'kepadatan_penduduk': 'KEPADATAN',
    'geom': 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for PatchSulut model
patchsulut_mapping = {
    'objectid': 'OBJECTID',
    'area': 'Area',
    'toponym': 'TOPONYM',
    'geom': 'MULTIPOLYGON',
}


# Auto-generated `LayerMapping` dictionary for TrTerminal model
trterminal_mapping = {
    'point_x': 'POINT_X',
    'point_y': 'POINT_Y',
    'nama_obyek': 'Nama_Obyek',
    'kls_obyek': 'Kls_Obyek',
    'kode': 'Kode',
    'no_foto': 'No_Foto',
    'tgl_survey': 'Tgl_Survey',
    'geom': 'MULTIPOINT',
}

# Auto-generated `LayerMapping` dictionary for TrLampu model
trlampu_mapping = {
    'geom': 'MULTIPOINT',
}

# Auto-generated `LayerMapping` dictionary for TrJembatan model
trjembatan_mapping = {
    'oid_field': 'OID_',
    'name': 'Name',
    'base': 'Base',
    'snippet': 'Snippet',
    'labelid': 'LabelID',
    'folder_pat': 'Folder_Pat',
    'symbol_id': 'Symbol_ID',
    'alt_mode': 'Alt_Mode',
    'pop_up_inf': 'Pop_Up_Inf',
    'hsl_tabel': 'Hsl_Tabel',
    'geom': 'MULTIPOINT25D',
}

# Auto-generated `LayerMapping` dictionary for TrTrayek model
trtrayek_mapping = {
    'panjang_km': 'panjang_KM',
    'nama_traye': 'nama_traye',
    'kode_traye': 'kode_traye',
    'rute': 'rute',
    'geom': 'MULTILINESTRING',
}

# Auto-generated `LayerMapping` dictionary for Telekomunikasi model
telekomunikasi_mapping = {
    'no': 'No',
    'menara': 'Menara',
    'longitude': 'Longitude',
    'lattitude': 'Lattitude',
    'antena_hei': 'Antena_Hei',
    'site_categ': 'Site_Categ',
    'desa': 'Desa',
    'kecamatan': 'Kecamatan',
    'kabupaten': 'Kabupaten',
    'geom': 'MULTIPOINT',
}

# Auto-generated `LayerMapping` dictionary for SmpJalan model
smpjalan_mapping = {
    'point_x': 'POINT_X',
    'point_y': 'POINT_Y',
    'nama_obyek': 'Nama_Obyek',
    'kls_obyek': 'Kls_Obyek',
    'kode': 'Kode',
    'no_foto': 'No_Foto',
    'tgl_surv': 'Tgl_Surv',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for SmpSungai model
smpsungai_mapping = {
    'point_x': 'POINT_X',
    'point_y': 'POINT_Y',
    'nama_obyek': 'Nama_Obyek',
    'kls_obyek': 'Kls_Obyek',
    'kode': 'Kode',
    'no_foto': 'No_Foto',
    'tgl_surv': 'Tgl_Surv',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}

# Auto-generated `LayerMapping` dictionary for Sanitasi model
sanitasi_mapping = {
    'fid_field': 'FID_',
    'name': 'Name',
    'descript': 'Descript',
    'type': 'Type',
    'comment': 'Comment',
    'symbol': 'Symbol',
    'datetimes': 'DateTimeS',
    'elevation': 'Elevation',
    'keterangan': 'keterangan',
    'geom': 'MULTIPOINT',
}


# Auto-generated `LayerMapping` dictionary for Cctv model
cctv_mapping = {
    'lokasi': 'Lokasi',
    'geom': 'MULTIPOINT',
}


bloklapangan_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/BLOKLAPANGANMERGE.shp'))
bnbakl_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/komo_luar.shp'))
bnbaistq_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/bidang_tanah_istiqlal.shp'))
bnbamhkt_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/bidang_tanah_mahakeret_timur.shp'))
bnbapin_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/bidang_tanah_pinaesaan.shp'))
bnbatelb_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/bidang_tanah_teling_bawah.shp'))
bnbatklak_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/bidang_tanah_tikala_kumaraka.shp'))
bnbawngsel_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/bidang_tanah_wenang_selatan.shp'))
bnbawngut_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/bidang_tanah_wenang_utara.shp'))
bnbalwng_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/bidang_tanah_lawangirung_fix.shp'))
bnbacal_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/bidang_tanah_calaca.shp'))
bnbatwut_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/bidang_tanah_titiwungen_utara.shp'))
bnbatwsel_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/bidang_tanah_titiwungen_selatan.shp'))
bnbabmib_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/bidang_tanah_bumi_bringin.shp'))
bnbamhkb_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/bidang_tanah_mahakeret_barat.shp'))
bnbasarut_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/bidang_tanah_sario_utara.shp'))
bnbaranotana_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/bidang_tanah_ranotana.shp'))
bnbasakobar_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/bidang_tanah_sakobar.shp'))
bnbasario_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/bidang_tanah_sario.shp'))
bnbasartum_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/bidang_tanah_sario_tumpaan.shp'))
bnbapaal2_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/bidang_tanah_paal_dua.shp'))
bnbakrgwr_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/bidang_tanah_kairagi_weru_fix.shp'))
bnbaperkamil_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/bidang_tanah_perkamil.shp'))
bnbamalendeng_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/bidang_tanah_malendeng.shp'))
bnbadenlu_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/bidang_tanah_dendengan_luar_fix.shp'))
bnbaranomuut_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/bidang_tanah_ranomuut.shp'))


umum_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/MANADOExport_Output.shp'))
patchsulut_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/patch/PatchSulut.shp'))
trterminal_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/geo/transportasi_SHP/terminal_transportasi_SHP/terminal_transportasi.shp'))
trlampu_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/geo/transportasi_SHP/lampu_lalulintas_SHP/lampu_lalulintas.shp'))
trjembatan_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/geo/transportasi_SHP/jembatan_SHP/jembatan.shp'))
trtrayek_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/geo/transportasi_SHP/jalur_trayek_SHP/jalur_trayek.shp'))
telekomunikasi_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/geo/telekomunikasi_SHP/bts.shp'))
smpjalan_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/geo/sempadan_SHP/bang_semp_jalan_SHP/bang_semp_jalan.shp'))
smpsungai_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/geo/sempadan_SHP/bang_semp_sungai_SHP/bang_semp_sungai.shp'))
sanitasi_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/geo/sanitasi_SHP/sanitasi1.shp'))
cctv_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/cctv/CCTV.shp'))
swalayan_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data/infra/swalayan_51N.shp'))

def run(verbose=True):
    lm = LayerMapping(Bloklapangan, bloklapangan_shp, bloklapangan_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runbnbakl(verbose=True):
    lm = LayerMapping(BnbaKl, bnbakl_shp, bnbakl_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runbnbaistq(verbose=True):
    lm = LayerMapping(BnbaIstq, bnbaistq_shp, bnbaistq_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runbnbamhkt(verbose=True):
    lm = LayerMapping(BnbaMhkt, bnbamhkt_shp, bnbamhkt_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runbnbapin(verbose=True):
    lm = LayerMapping(BnbaPin, bnbapin_shp, bnbapin_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runbnbatelb(verbose=True):
    lm = LayerMapping(BnbaTelb, bnbatelb_shp, bnbatelb_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runbnbatklak(verbose=True):
    lm = LayerMapping(BnbaTklak, bnbatklak_shp, bnbatklak_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runbnbawngsel(verbose=True):
    lm = LayerMapping(BnbaWngsel, bnbawngsel_shp, bnbawngsel_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runbnbawngut(verbose=True):
    lm = LayerMapping(BnbaWngut, bnbawngut_shp, bnbawngut_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runbnbalwng(verbose=True):
    lm = LayerMapping(BnbaLwng, bnbalwng_shp, bnbalwng_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runbnbacal(verbose=True):
    lm = LayerMapping(BnbaCal, bnbacal_shp, bnbacal_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runbnbatwut(verbose=True):
    lm = LayerMapping(BnbaTwut, bnbatwut_shp, bnbatwut_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runbnbatwsel(verbose=True):
    lm = LayerMapping(BnbaTwsel, bnbatwsel_shp, bnbatwsel_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runbnbabmib(verbose=True):
    lm = LayerMapping(BnbaBmib, bnbabmib_shp, bnbabmib_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runbnbamhkb(verbose=True):
    lm = LayerMapping(BnbaMhkb, bnbamhkb_shp, bnbamhkb_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runbnbasarut(verbose=True):
    lm = LayerMapping(BnbaSarUt, bnbasarut_shp, bnbasarut_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runbnbaranotana(verbose=True):
    lm = LayerMapping(BnbaRanotana, bnbaranotana_shp, bnbaranotana_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runbnbasakobar(verbose=True):
    lm = LayerMapping(BnbaSaKobar, bnbasakobar_shp, bnbasakobar_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runbnbasario(verbose=True):
    lm = LayerMapping(BnbaSario, bnbasario_shp, bnbasario_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runbnbasartum(verbose=True):
    lm = LayerMapping(BnbaSarTum, bnbasartum_shp, bnbasartum_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runbnbapaal2(verbose=True):
    lm = LayerMapping(BnbaPaal2, bnbapaal2_shp, bnbapaal2_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runbnbakrgwr(verbose=True):
    lm = LayerMapping(BnbaKrgwr, bnbakrgwr_shp, bnbakrgwr_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runbnbaperkamil(verbose=True):
    lm = LayerMapping(BnbaPerkamil, bnbaperkamil_shp, bnbaperkamil_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runbnbamalendeng(verbose=True):
    lm = LayerMapping(BnbaMalendeng, bnbamalendeng_shp, bnbamalendeng_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runbnbadenlu(verbose=True):
    lm = LayerMapping(BnbaDenlu, bnbadenlu_shp, bnbadenlu_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runbnbaranomuut(verbose=True):
    lm = LayerMapping(BnbaRanomuut, bnbaranomuut_shp, bnbaranomuut_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)


################################## Batas BNBA #####################################################################


def runumum(verbose=True):
    lm = LayerMapping(Umum, umum_shp, umum_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runpatchsulut(verbose=True):
    lm = LayerMapping(PatchSulut, patchsulut_shp, patchsulut_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runterminal(verbose=True):
    lm = LayerMapping(TrTerminal, trterminal_shp, trterminal_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runlampu(verbose=True):
    lm = LayerMapping(TrLampu, trlampu_shp, trlampu_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runjembatan(verbose=True):
    lm = LayerMapping(TrJembatan, trjembatan_shp, trjembatan_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runtrayek(verbose=True):
    lm = LayerMapping(TrTrayek, trtrayek_shp, trtrayek_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runtelekomunikasi(verbose=True):
    lm = LayerMapping(Telekomunikasi, telekomunikasi_shp, telekomunikasi_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runsmpjalan(verbose=True):
    lm = LayerMapping(SmpJalan, smpjalan_shp, smpjalan_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runsmpsungai(verbose=True):
    lm = LayerMapping(SmpSungai, smpsungai_shp, smpsungai_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runsanitasi(verbose=True):
    lm = LayerMapping(Sanitasi, sanitasi_shp, sanitasi_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runcctv(verbose=True):
    lm = LayerMapping(Cctv, cctv_shp, cctv_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

def runswalayan(verbose=True):
    lm = LayerMapping(Swalayan, swalayan_shp, swalayan_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

