var ip = location.host;
ip = ip.split(":");
var urlpng = "http://"+ip[0]+"/dataGIS/images/frontend/";
var urltiles = "http://"+ip[0]+"/dataGIS/Other/Bapelitbang_tiles/";

document.getElementById("header").src = "http://"+ip[0]+"/dataGIS/images/frontend/header.png";

$("#pop").click(function() {
	alert("test");
	//$('#imagepreview').attr('src', $('#imageresource').attr('src')); // here asign the image to the modal when the user click the enlarge link
	//$('#imagemodal').modal('show'); // imagemodal is the id attribute assigned to the bootstrap modal, then i use the show function
});

function formatRibuan(value) {
	var val = (value/1).toFixed(0).replace('.', ',')
	return val.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".")
}

var _nopjson;

function getEpajak() {
	var xhttp = new XMLHttpRequest();
		xhttp.open("POST", "http://epajak.manadokota.go.id/index.php/c_public/jsonpajak");
		xhttp.setRequestHeader("Content-type", "application/json");
		xhttp.send("pass=epajakjson");

	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			if (this.responseText != null) {
				_nopjson = (JSON.parse(this.responseText));
			} else {
				console.log("ePajak tidak terhubung...!!");
			}
		}
	}
}

function findObjectByKey(array, key, value) {
	if (value != "") {
		for (var i = 0; i < array.length; i++) {
			if (array[i][key] == value) {
				return array[i];
			}
		}
	}
	return [];
}

getEpajak();

// Global Default Color
function getDefaultColor(stat)
{
	switch(stat){
	
		case 'bidang':
			return {
				color: "#ffffff",
				weight: 1,
				opacity: 0.65,
				fillOpacity: 0,
			};
		case 'sungai':
			return {
				fillOpacity: 0,
				opacity: 0,
				weight: 0,
			};
		case 'umum':
			return {
				color: "#ffffff",
				fillOpacity: 1,
				opacity: 0.65,
				weight: 1,
			};
		case 'no_nop':
			return {
				color: "#ffffff",
				fillOpacity: 1,
				opacity: 0.65,
				weight: 1,
			};
		case 'sekolah':
			return {
				color: "#ffffff",
				fillOpacity: 1,
				opacity: 0.65,
				weight: 1,
			};
		case 'gereja':
			return {
				color: "#ffffff",
				fillOpacity: 1,
				opacity: 0.65,
				weight: 1,
			};
	}
}

// Global Status Color
function getStatusColor(arr,feature)
{
	if ( arr.status_kelunasan == "Lunas"){
		return ["#00ff00", 0.2];
	
	} else if (feature.properties.nop == "unknown" && feature.properties.stat == "bidang") {
		return ["#ff00f0", 0.6];
		
	} else if (feature.properties.stat == "sungai") {
		return ["#0000ff", 0];
		
	} else if (feature.properties.stat == "umum") {
		return ["#ffa500", 0.5];

	} else if (feature.properties.stat == "no_nop") {
		return ["#00fffc", 0.5];

	} else if (feature.properties.stat == "sekolah") {
		return ["#fff600", 0.5];

	} else if (feature.properties.stat == "gereja") {
		return ["#73491c", 0.5];

	} else if (feature.properties.stat == "masjid") {
		return ["#73491c", 0.5];

	} else if (feature.properties.stat == "tempat_ibadah") {
		return ["#73491c", 0.5];

	} else if (feature.properties.stat == "hotel") {
		return ["#73491c", 0.5];

	} else if (feature.properties.stat == "pemukiman") {
		return ["#73491c", 0.5];

	} else if (feature.properties.stat == "wisma") {
		return ["#73491c", 0.5];

	} else if (feature.properties.stat == "tni_polri") {
		return ["#73491c", 0.5];

	} else if (feature.properties.stat == "militer") {
		return ["#73491c", 0.5];

	} else if (feature.properties.stat == "kantor") {
		return ["#73491c", 0.5];

	} else if (feature.properties.stat == "pemerintahan") {
		return ["#73491c", 0.5];

	} else if (feature.properties.stat == "perdagangan") {
		return ["#73491c", 0.5];

	} else {
		return ["#ff0000", 0.1];
		
	}
}


// Global Path Foto Bidang
function getPathFoto(feature)
{
	var path_foto = "";
	var pf = feature.properties.path_foto;
	
	switch(pf)
	{
		case null:
			path_foto = '"http://www.bsmc.net.au/wp-content/uploads/No-image-available.jpg"'; break;
		case "":
			path_foto = '"http://www.bsmc.net.au/wp-content/uploads/No-image-available.jpg"'; break;
		case "unknown":
			path_foto = '"http://www.bsmc.net.au/wp-content/uploads/No-image-available.jpg"'; break;
		default:
			path_foto = '"http://'+ip[0]+'/dataGIS/'+pf+'"'; break;
	}
	return path_foto;
}

// Global Layer Popup
function getPopup(feature,arr)
{
	var path_foto = getPathFoto(feature);
	popup 	= '';
	style	= 'style="height : 170px; width : 100%;"';

	rowx	= "No. Rumah"; 			isix 	= feature.properties.no_rumah;
	row0	= "TAHUN"; 				isi0 	= arr.tahun;
	row1	= "NIK"; 				isi1 	= arr.nik;
	row2	= "NOP ePajak"; 		isi2 	= arr.nop;
	row2_1	= "NOP Bidang"; 		isi2_1	= feature.properties.nop;
	row3	= "NAMA"; 				isi3	= arr.nama;
	row4	= "ALAMAT"; 			isi4	= arr.alamat;
	row4_1	= "KELUHARAN"; 			isi4_1	= arr.nama_kelurahan;
	row5	= "NAMA USAHA"; 		isi5	= arr.nama_usaha;
	row6	= "ALAMAT USAHA"; 		isi6	= arr.alamat_usaha;
	row6_1	= "TGL USAHA"; 			isi6_1	= arr.tgl_usaha;
	row6_2	= "SITU"; 				isi6_2	= arr.situ;
	row7	= "No.HP"; 				isi7	= arr.no_hp;
	row8	= "EMAIL"; 				isi8	= arr.email;
	row9	= "No.NPWPD (LAMA)";	isi9	= arr.npwpd_lama;
	row10	= "No.NPWPD"; 			isi10	= arr.no_npwpd;
	row11	= "TGL PERMOHONAN"; 	isi11	= arr.tgl_permohonan;
	row12	= "TGL KETETAPAN"; 		isi12	= arr.tanggal_ketetapan;
	row13	= "TGL PEMBAYARAN"; 	isi13	= arr.tanggal_pembayaran;
	row14	= "No.BUKTI LUNAS"; 	isi14	= arr.no_bukti_lunas;
	row15	= "No.URUT"; 			isi15	= arr.no_urut;
	row16	= "No.URUT ABT"; 		isi16	= arr.no_urut_abt;
	row16	= "No.URUT KEBERSIHAN";	isi16	= arr.no_urut_kebersihan;
	row17	= "STATUS";				isi17	= arr.status;
	row18	= "TOTAL KEBERSIHAN";	isi18	= formatRibuan(arr.total_kebersihan);
	row19	= "TOTAL REKLAME";		isi19	= formatRibuan(arr.total_reklame);
	row20	= "TOTAL AIR";			isi20	= formatRibuan(arr.total_air);
	row21	= "TOTAL";				isi21	= formatRibuan(arr.total);
	row22	= "KUBIK AIR";			isi22	= formatRibuan(arr.kubik_air);
	row23	= "BUKTI PAM";			isi23	= arr.bukti_pam;
	row98	= "STATUS"; 			isi98	= arr.status;
	row99	= "STATUS BAYAR"; 		isi99	= arr.status_kelunasan;

	popup	+= '<div class="" style="overflow-y:auto; overflow-x:hidden; height:60vh; width:100%;">';
	popup	+= '<table class="table table-bordered">';
	popup	+= '<tbody>';

	popup	+= '<tr><td class="text-right" style="width:30%;" colspan="2"><a href="#" id="pop">';
	popup	+= '<img id="imageresource" '+style+' src='+path_foto+'/></a></td></tr>';
	popup	+= '<tr><td class="text-right" style="width:30%;">'+rowx+'</td><td class="text-left" style="width:70%;">'+isix+'</td></tr>';
	popup	+= '<tr><td class="text-right" style="width:30%;">'+row0+'</td><td class="text-left" style="width:70%;">'+isi0+'</td></tr>';
	popup	+= '<tr><td class="text-right" style="width:30%;">'+row1+'</td><td class="text-left" style="width:70%;">'+isi1+'</td></tr>';
	popup	+= '<tr><td class="text-right" style="width:30%;">'+row2+'</td><td class="text-left" style="width:70%;">'+isi2+'</td></tr>';
	popup	+= '<tr><td class="text-right" style="width:30%;">'+row2_1+'</td><td class="text-left" style="width:70%;">'+isi2_1+'</td></tr>';
	popup	+= '<tr><td class="text-right" style="width:30%;">'+row3+'</td><td class="text-left" style="width:70%;">'+isi3+'</td></tr>';
	popup	+= '<tr><td class="text-right" style="width:30%;">'+row4+'</td><td class="text-left" style="width:70%;">'+isi4+'</td></tr>';
	popup	+= '<tr><td class="text-right" style="width:30%;">'+row4_1+'</td><td class="text-left" style="width:70%;">'+isi4_1+'</td></tr>';
	popup	+= '<tr><td class="text-right" style="width:30%;">'+row5+'</td><td class="text-left" style="width:70%;">'+isi5+'</td></tr>';
	popup	+= '<tr><td class="text-right" style="width:30%;">'+row6+'</td><td class="text-left" style="width:70%;">'+isi6+'</td></tr>';
	popup	+= '<tr><td class="text-right" style="width:30%;">'+row6_1+'</td><td class="text-left" style="width:70%;">'+isi6_1+'</td></tr>';
	popup	+= '<tr><td class="text-right" style="width:30%;">'+row6_2+'</td><td class="text-left" style="width:70%;">'+isi6_2+'</td></tr>';
	popup	+= '<tr><td class="text-right" style="width:30%;">'+row7+'</td><td class="text-left" style="width:70%;">'+isi7+'</td></tr>';
	popup	+= '<tr><td class="text-right" style="width:30%;">'+row8+'</td><td class="text-left" style="width:70%;">'+isi8+'</td></tr>';
	popup	+= '<tr><td class="text-right" style="width:30%;">'+row9+'</td><td class="text-left" style="width:70%;">'+isi9+'</td></tr>';
	popup	+= '<tr><td class="text-right" style="width:30%;">'+row10+'</td><td class="text-left" style="width:70%;">'+isi10+'</td></tr>';
	popup	+= '<tr><td class="text-right" style="width:30%;">'+row11+'</td><td class="text-left" style="width:70%;">'+isi11+'</td></tr>';
	popup	+= '<tr><td class="text-right" style="width:30%;">'+row12+'</td><td class="text-left" style="width:70%;">'+isi12+'</td></tr>';
	popup	+= '<tr><td class="text-right" style="width:30%;">'+row13+'</td><td class="text-left" style="width:70%;">'+isi13+'</td></tr>';
	popup	+= '<tr><td class="text-right" style="width:30%;">'+row14+'</td><td class="text-left" style="width:70%;">'+isi14+'</td></tr>';
	popup	+= '<tr><td class="text-right" style="width:30%;">'+row15+'</td><td class="text-left" style="width:70%;">'+isi15+'</td></tr>';
	popup	+= '<tr><td class="text-right" style="width:30%;">'+row16+'</td><td class="text-left" style="width:70%;">'+isi16+'</td></tr>';
	popup	+= '<tr><td class="text-right" style="width:30%;">'+row17+'</td><td class="text-left" style="width:70%;">'+isi17+'</td></tr>';
	popup	+= '<tr><td class="text-right" style="width:30%;">'+row18+'</td><td class="text-left" style="width:70%;">'+isi18+'</td></tr>';
	popup	+= '<tr><td class="text-right" style="width:30%;">'+row19+'</td><td class="text-left" style="width:70%;">'+isi19+'</td></tr>';
	popup	+= '<tr><td class="text-right" style="width:30%;">'+row20+'</td><td class="text-left" style="width:70%;">'+isi20+'</td></tr>';
	popup	+= '<tr><td class="text-right" style="width:30%;">'+row21+'</td><td class="text-left" style="width:70%;">'+isi21+'</td></tr>';
	popup	+= '<tr><td class="text-right" style="width:30%;">'+row22+'</td><td class="text-left" style="width:70%;">'+isi22+'</td></tr>';
	popup	+= '<tr><td class="text-right" style="width:30%;">'+row23+'</td><td class="text-left" style="width:70%;">'+isi23+'</td></tr>';
	popup	+= '<tr><td class="text-right" style="width:30%;">'+row98+'</td><td class="text-left" style="width:70%;">'+isi98+'</td></tr>';
	popup	+= '<tr><td class="text-right" style="width:30%;">'+row99+'</td><td class="text-left" style="width:70%;">'+isi99+'</td></tr>';

	popup	+= '</tbody>';
	popup	+= '</table>';
	popup	+= '</div>';
	
	return popup;
}

// Global View Detail Bidang
function viewDetailBidang(feature,arr)
{
	var popup = getPopup(feature,arr);
	$('#bnba').html(popup);
	
	var stat = $('#toolbar').hasClass("open");
	if ( !stat ){
		$('#toolbar .hamburger').parent().toggleClass('open');
	}
}

function debug(prop)
{
	// console.log(prop.stat);
}

$('#toolbar .hamburger').on('click', function() {
  $(this).parent().toggleClass('open');
});


function getIconTelekomunikasi(feature)
{
	var myIcon = L.icon({
		iconUrl: "http://"+ip[0]+"/dataGIS/images/frontend/towerValid.png",
		iconSize: [50, 50],
		iconAnchor: [25, 40],
		popupAnchor:  [1, -40]
	});
	return myIcon;
}

function getIconSwalayan(feature)
{
	var myIcon = L.icon({
		iconUrl: "http://"+ip[0]+"/dataGIS/images/frontend/" + feature.properties.minimarket + ".png",
		iconSize: [50, 50],
		iconAnchor: [25, 40],
		popupAnchor:  [1, -40],
		shadowUrl: "http://"+ip[0]+"/dataGIS/images/frontend/minimarketshadow.png",
		shadowSize: [50, 50]
	});
	return myIcon;
}

// Global Style Bidang
function _style(feature)
{
	return getDefaultColor(feature.properties.stat);
}

// Global Feature Bidang
function _onEachFeature(feature,layer)
{
	var arr = findObjectByKey(_nopjson, 'nop', feature.properties.nop);
	var statusColor = getStatusColor(arr,feature);
	layer.setStyle({
		fillColor: statusColor[0],
		fillOpacity: statusColor[1]
	});
	debug(feature.properties);
}

// Global Detail Bidang
function _clickBidang(e)
{
	var arr = findObjectByKey(_nopjson, 'nop', e.layer.feature.properties.nop);
	viewDetailBidang(e.layer.feature,arr);
}

// Global Function BNBA
function _layer2(url)
{
	return (new L.GeoJSON.AJAX(url,
	{style:_style, onEachFeature:_onEachFeature}))
	.on('click', _clickBidang);
}
