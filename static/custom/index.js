var ip = location.host;
ip = ip.split(":");
var urlpng = "http://"+ip[0]+"/dataGIS/images/frontend/";
var urltiles = "http://"+ip[0]+"/dataGIS/Other/Bapelitbang_tiles/";

document.getElementById("header").src = "http://"+ip[0]+"/dataGIS/images/frontend/header.png";

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
	var arrPopup = [];
	arrPopup.push({label: "No. Rumah", 			value: feature.properties.no_rumah});
	arrPopup.push({label: "TAHUN", 				value: arr.tahun});
	arrPopup.push({label: "NIK", 				value: arr.nik});
	arrPopup.push({label: "NOP ePajak", 		value: arr.nop});
	arrPopup.push({label: "NOP Bidang", 		value: feature.properties.nop});
	arrPopup.push({label: "NAMA", 				value: arr.nama});
	arrPopup.push({label: "ALAMAT", 			value: arr.alamat});
	arrPopup.push({label: "KELUHARAN", 			value: arr.nama_kelurahan});
	arrPopup.push({label: "NAMA USAHA", 		value: arr.nama_usaha});
	arrPopup.push({label: "ALAMAT USAHA", 		value: arr.alamat_usaha});
	arrPopup.push({label: "TGL USAHA", 			value: arr.tgl_usaha});
	arrPopup.push({label: "SITU", 				value: arr.situ});
	arrPopup.push({label: "No.HP", 				value: arr.no_hp});
	arrPopup.push({label: "EMAIL", 				value: arr.email});
	arrPopup.push({label: "No.NPWPD (LAMA)",	value: arr.npwpd_lama});
	arrPopup.push({label: "No.NPWPD", 			value: arr.no_npwpd});
	arrPopup.push({label: "TGL PERMOHONAN", 	value: arr.tgl_permohonan});
	arrPopup.push({label: "TGL KETETAPAN", 		value: arr.tanggal_ketetapan});
	arrPopup.push({label: "TGL PEMBAYARAN", 	value: arr.tanggal_pembayaran});
	arrPopup.push({label: "No.BUKTI LUNAS", 	value: arr.no_bukti_lunas});
	arrPopup.push({label: "No.URUT", 			value: arr.no_urut});
	arrPopup.push({label: "No.URUT ABT", 		value: arr.no_urut_abt});
	arrPopup.push({label: "No.URUT KEBERSIHAN",	value: arr.no_urut_kebersihan});
	arrPopup.push({label: "STATUS", 			value: arr.status});
	arrPopup.push({label: "TOTAL KEBERSIHAN", 	value: formatRibuan(arr.total_kebersihan)});
	arrPopup.push({label: "TOTAL REKLAME", 		value: formatRibuan(arr.total_reklame)});
	arrPopup.push({label: "TOTAL AIR", 			value: formatRibuan(arr.total_air)});
	arrPopup.push({label: "TOTAL", 				value: formatRibuan(arr.total)});
	arrPopup.push({label: "KUBIK AIR", 			value: formatRibuan(arr.kubik_air)});
	arrPopup.push({label: "BUKTI PAM", 			value: arr.bukti_pam});
	arrPopup.push({label: "STATUS", 			value: arr.status});
	arrPopup.push({label: "STATUS BAYAR", 		value: arr.status_kelunasan});

	var popup 	= '';
	popup	+= '<div class="" style="overflow-y:auto; overflow-x:hidden; height:60vh; width:100%;">';
	popup	+= '<table class="table table-bordered">';
	popup	+= '<tbody>';
	popup	+= '<tr><td class="text-center" colspan="2"><a href="#">';
	
	style	= 'style="height : 170px; width : auto;"';
	popup	+= '<img id="imageresource" '+style+' src='+getPathFoto(feature)+'/></a></td></tr>';
	
	for (var row of arrPopup){
		popup	+= '<tr><td class="text-right" style="width:30%;">'+row.label+'</td>';
		popup	+= '<td class="text-left" style="width:70%;">'+row.value+'</td></tr>';
	}

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



// Global Function Layer Bidang
function _layer2(url)
{
	return (new L.GeoJSON.AJAX(url,	{
		style:_style, onEachFeature:_onEachFeature
	})).on('click', _clickBidang);
}

// Global Style Bidang
function _style(feature)
{
	return getDefaultColor(feature.properties.stat);
}

// Global eachFeature Bidang
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

// Global Detail Click Bidang
function _clickBidang(e)
{
	var arr = findObjectByKey(_nopjson, 'nop', e.layer.feature.properties.nop);
	viewDetailBidang(e.layer.feature,arr);
}



// Global Function Layer Point
function _layer1(url)
{
	var _url = url.split("'");
	_url = _url[0].split("/");
	_url = _url[1].split("_");
	
	var jenis = _url[0];
	return (new L.GeoJSON.AJAX(url, {
		pointToLayer: function(feature, latlng) {
			var myIcon = getIcon(feature, jenis);
			return L.marker(latlng, {icon: myIcon});
		},
		onEachFeature:function(feature,layer){
			var popup = getLayer1Popup(jenis, feature);
			if (jenis != "trlampu"){
				layer.bindPopup(popup);
			}
		}
	}));
}


function getLayer1Popup(jenis, feature)
{
	var popup = "";
	switch(jenis)
	{
		case "swalayan"			: popup = '<center>'+feature.properties.nama+'</center>'; break;
		case "trjembatan"		: popup = '<center>'+feature.properties.name+'</center>'; break;
		case "trterminal"		: popup = '<center>'+feature.properties.nama_obyek+'</center>'; break;
		case "trtrayek"			: popup = '<center>'+feature.properties.nama_traye+'</center>'; break;
		case "telekomunikasi"	: popup = '<center>'+feature.properties.menara+'</center>'; break;
		case "sanitasi"			: popup = '<center>'+feature.properties.keterangan+'</center>'; break;
		case "cctv"	:	
			var popup = '<div class="pb-video">';
				popup += '<video class="video-js vjs-default-skin pb-video-frame" ';
				popup += 'poster="http://vjs.zencdn.net/v/oceans.png" controls preload="auto" width="250px" height="250px" data-setup="{}">';
				popup += '<source src="" type="rtmp/mp4">';
				popup += '</video><label class="form-control text-center" style="font-size:10px;">'+feature.properties.lokasi+'</label></div>';
			break;
	}
	
	return popup;
}


// Icon marker
function getIcon(feature, jenis)
{
	var _iconUrl = "http://"+ip[0]+"/dataGIS/images/frontend/";
	var _shadowUrl = _iconUrl;
	
	switch (jenis)
	{
		case "telekomunikasi" : 
			_iconUrl += "towerValid.png"; 
			_shadowUrl += "";
			break;
			
		case "swalayan" : 
			_iconUrl += feature.properties.minimarket + ".png"; 
			_shadowUrl += "minimarketshadow.png";
			break;
			
		case "trlampu" : 
			_iconUrl += "TrafficLight.png"; 
			_shadowUrl += "TrafficLightShadow.png";
			break;
			
		case "infralampu" : 
			_iconUrl += "RoadLight" + feature.properties.keterangan + ".png"; 
			_shadowUrl += "RoadLightShadow.png";
			break;
			
		case "sanitasi" : 
			if (feature.properties.keterangan == "TPSS") {
				_iconUrl += "tpss.png"; 
			} 
			else if (feature.properties.keterangan == "MCK KOMUNAL") {
				_iconUrl += "mck.png"; 
			} 
			else if (feature.properties.keterangan == "IPAL KOMUNAL") {
				_iconUrl += "ipal.png"; 
			} 
			else {
				_iconUrl += "mckipal.png";
			} 
			
			_shadowUrl += "tpssmckipalshadow.png";
			break;
			
		default :
			_iconUrl += "default.png"; 
			_shadowUrl += "RoadLightShadow.png";
			break;
			
	}
	
	var myIcon = L.icon({
		iconUrl: _iconUrl,
		iconSize: [50, 50],
		iconAnchor: [25, 40],
		popupAnchor:  [1, -40],
		shadowUrl: _shadowUrl,
		shadowSize: [50, 50]
	});
	return myIcon;
}
