DEFAULT_LIMIT = 100
DIRECT_PROPERTIES = ["length", "digits", "dashes"];
SCORE_PROPERTIES = ["english", "spanish", "french", "german",
					"prefix", "suffix"];
TLD_SCORES = {
	net: 5, org: 5, biz: 3, info: 3, mobi: 3, name: 3, tel: 3,
	at: 1, be: 1, ca: 1, de: 1, es: 1, eu: 2, fm: 2,
	"in": 1, is: 1, it: 1, li: 1, ly: 2, ru: 1, se: 1,
	to: 1, tv: 2, us: 1,
};
SEARCH_LENGTHS = [7, 6, 8, 5, 9, 4, 10, 3, 11, 12];
TLD_SUPPORTED = {
	"godaddy.com": " ag am asia at be biz bz ca cc com de es eu fm gs in info it jobs jp me mobi ms mx net nl nu org tc tk tv tw us vg ws ",
}

function force_number(text) {
	var number = parseInt(text);
	if (isNaN(number)) return 0;
	return number;
}

function force_micro(text) {
	return force_number(text) / 1000000;
}

function form_weights() {
	return {length: 12 * force_number($("input[name=len]:checked").val()),
			digits: force_number($("input[name=digits]:checked").val()),
			dashes: force_number($("input[name=dashes]:checked").val()),
			english: force_micro($("input[name=english]:checked").val()),
			spanish: force_micro($("input[name=spanish]:checked").val()),
			french: force_micro($("input[name=french]:checked").val()),
			german: force_micro($("input[name=german]:checked").val()),
			prefix: force_micro($("input[name=prefix]:checked").val()),
			suffix: force_micro($("input[name=suffix]:checked").val())};
}

function priority_changed() {
	var weights = {
		len: "positive", digits: "important", dashes: "critical",
		english: "important", spanish: "positive", french: "positive",
		german: "positive", prefix: "positive", suffix: "positive",
	}
	if ($("input#id_priority_0").attr("checked")) {
		weights["len"] = "critical";
		weights["digits"] = "neutral";
		weights["dashes"] = "neutral";
	}
	if ($("input#id_priority_1").attr("checked")) {
		weights["len"] = "important";
		weights["digits"] = "critical";
		weights["dashes"] = "critical";
	}
	if ($("input#id_priority_0").attr("checked") ||
		$("input#id_priority_1").attr("checked")) {
		weights["english"] = "positive";
		weights["spanish"] = "neutral";
		weights["french"] = "neutral";
		weights["german"] = "neutral";
	}
	if ($("input#id_priority_3").attr("checked")) {
		weights["prefix"] = "important";
		weights["suffix"] = "important";
	}
	if ($("input#id_priority_4").attr("checked")) {
		weights["prefix"] = "critical";
		weights["suffix"] = "critical";
	}
	for (var key in weights) {
		$("input#id_" + key + "_" + weights[key]).attr("checked", true);
	}
	update_scores();
}

function muldiv(weight, score) {
	if (weight >= 0) return weight * score;
	if (score == 0) return -weight;
	return -weight / score;
}

function domain_score(domain, weights) {
	var score = 0;
	for (var attr in weights)
		score += muldiv(weights[attr], domain[attr]);
	return score;
}

function mouse_down_track(one, two, three, four) {
	var path = '/' + one + '/';
	if (two) path += two + '/';
	if (three) path += three + '/';
	if (four) path += four + '/';
	var javascript = "ga_track('" + path + "');";
	return 'onMouseDown="' + javascript + '"';
}

function affiliate_link(name, tld) {
	var html = '<a href="';
	if ($.registrar == 'godaddy.com') {
		html += "http://www.anrdoezrs.net/interactive";
		html += "?domainToCheck=" + name + "&tld=." + tld.toUpperCase();
		html += "&checkAvail=1";
		html += "&aid=10390987&pid=3770298";
		html += "&url=http://www.godaddy.com/gdshop/registrar/search.asp";
		html += "?isc=0000000000";
	} else if ($.registrar == 'dotster.com') {
		html += "http://www.tkqlhce.com/interactive";
		html += "?DomainName=" + name + "." + tld + "&siteid=4798";
		html += "&aid=10275199&pid=3770298";
		html += "&url=https://secure.registerapi.com/dds2/index.php";
	} else if ($.registrar == '1and1.com') {
		html += "http://www.dpbolvw.net/interactive";
		html += "?domain=" + name + "&tld=" + tld;
		html += "&aid=10376103&pid=3770298";
		html += "&url=http://order.1and1.com/dcjump";
		html += "?ac=OM.US.US469K02463T2103a";
	} else if ($.registrar == 'namecheap.com') {
		html += "http://www.namecheap.com/domain-name-search.asp";
		html += "?formtype=domain&sld=" + name + "&tld=" + tld;
		html += "&aff=5799";
	} else { // moniker.com
		html += "http://affiliates.moniker.com/pub/Affiliates";
		html += "?affiliate_id=3154&landingpage=domaincheck&domain=";
		html += name + "." + tld;
	}
	html += '" title="Click here to check if ' + name + '.' + tld +
		' is available on ' + $.registrar + '" ';
	html += mouse_down_track('outgoing', $.registrar, tld, name.length);
	html += ' target="_blank">';
	if (tld == 'com') html += name + '.';
	html += tld + '</a>';
	return html;
}

function domain_link(name, tld) {
	return '<a href="http://' + name + '.' + tld + '/" ' +
		mouse_down_track('outgoing', 'website', tld, name.length) +
		' target="_blank">' + tld + '</a>';
}

function google_link(name) {
	return '<a href="http://www.google.com/search?q=' + name + '" ' +
		mouse_down_track('outgoing', 'google', name.length) +
		' target="_blank">' + name + '</a>';
}

function bar(attr, domain, highest, value) {
	var score = muldiv($.weights[attr], domain[attr]);
	var pixels = Math.round(400 * score / highest);
	if (pixels <= 0) return '';
	var html = '';
	html += '<div class="bar color-' + attr + '"';
	html += ' style="width: ' + pixels + 'px">';
	if (!value) value = score;
	if (typeof value == "number") value = value.toFixed(0);
	html += value + '</div>\n';
	return html;
}

function domain_row(domain, highest) {
	html = '';
	html += bar('length', domain, highest, domain.length);
	html += bar('english', domain, highest, domain.english / 10000);
	html += bar('spanish', domain, highest, domain.spanish / 10000);
	html += bar('french', domain, highest, domain.french / 10000);
	html += bar('german', domain, highest, domain.german / 10000);
	html += bar('prefix', domain, highest,
				domain.key.substr(0, domain.pl));
	html += bar('suffix', domain, highest,
				domain.key.substr(-domain.sl));
	var name = domain.key;
	html += affiliate_link(name, 'com');
	for (var tld in TLD_SCORES) {
		if (domain[tld]) {
			var title = 'Taken: ' + name + '.' + tld + ' uses name server';
			var color = 'taken';
			if (domain[tld].indexOf('parking') >= 0 ||
				domain[tld].indexOf('parked') >= 0 ||
				domain[tld].indexOf('.hitfarm.com') >= 0 ||
				domain[tld].indexOf('.fastpark.net') >= 0 ||
				domain[tld].indexOf('.name-services.com') >= 0 ||
				domain[tld].indexOf('.above.com') >= 0 ||
				domain[tld].indexOf('.domaincontrol.com') >= 0 ||
				domain[tld].indexOf('.dsredirection.com') >= 0 ||
				domain[tld].indexOf('.buydomains.com') >= 0) {
				title = 'Parking: ' + name + '.' + tld + ' uses name server';
				color = 'parking';
			}
			if (domain[tld].substr(0, 7) == 'status=' ||
				domain[tld].substr(0, 8) == 'timeout=') {
				title = 'DNS error: ' + name + '.' + tld + ' returned';
				color = 'status';
			}
			html += ' <span class="tld ' + color + '" title="' +
				title + ' ' + domain[tld] + '">';
			html += domain_link(domain.key, tld);
			html += '</span>';
		}
	}
	html += '<br />';
	return html;
}

function p_html(start, end) {
	if ($.keys.length == 0) return '';
	var highest = $.domains[$.keys[0]].score;
	var html = '';
	if (end > $.keys.length) end = $.keys.length;
	for (var index = start; index < end; index++) {
		var domain = $.domains[$.keys[index]];
		html += domain_row(domain, highest);
	}
	return html;
}

function update_html() {
	if ($.ajax_search.left + $.ajax_search.right == '') {
		$("div#results_div").hide();
		$("div#results_loading").hide();
		$("div#results_empty").hide();
		$("div#feedback").hide();
		$("div#welcome").show();
		return;
	}
	$.keys = [];
	for (var key in $.domains) $.keys.push(key);
	$.keys.sort(function(a, b) {
		return $.domains[b].score - $.domains[a].score });
	$.ajax_search.showing = DEFAULT_LIMIT;
	var html = p_html(0, DEFAULT_LIMIT);
	$("div#welcome").hide();
	if ($.keys.length == 0) {
		$("div#results_div").hide();
		if ($.ajax_search.start) {
			$("#results_empty").hide();
			$("#results_loading").show();
		} else {
			$("#results_loading").hide();
			$("#results_empty").show();
		}
	} else {
		$("#results_empty").hide();
		$("#results_loading").hide();
		$("#results_p").html(html);
		$("#results_div").show();
		$("div#feedback").show();
		if ($.keys.length > DEFAULT_LIMIT && !$.ajax_search.start)
			$("#results_more").show();
		else
			$("#results_more").hide();
		if ($.keys.length <= DEFAULT_LIMIT / 2 && !$.ajax_search.start)
			$("#results_few").show();
		else
			$("#results_few").hide();
	}
}

function show_more() {
	var start = $.ajax_search.showing;
	$.ajax_search.showing += DEFAULT_LIMIT;
	var html = p_html(start, $.ajax_search.showing);
	$("#results_p").append(html);
	if ($.ajax_search.showing >= $.keys.length)
		$("#results_more").hide();
	ga_track("/more/" + start + "/");
}

function array_unchanged(a, b) {
	for (var index in a) if (a[index] != b[index]) return false;
	for (var index in b) if (a[index] != b[index]) return false;
	return true;
}

function update_registrar() {
	$.registrar = this.value;
	$.changed = true;
}

function update_scores() {
	var weights = form_weights();
	if (array_unchanged($.weights, weights)) return;
	$.weights = weights;
	for (var key in $.domains) {
		var domain = $.domains[key];
		domain.score = domain_score(domain, weights);
	}
	update_html();
	$.changed = false;
}

function keyword_match(left, right, name) {
	if (left && name.substr(0, left.length) != left) return false;
	if (right && name.substr(-right.length) != right) return false;
	return true;
}

function delete_domains(left, right) {
	for (var key in $.domains)
		if (!keyword_match(left, right, key)) {
			delete $.domains[key];
			$.changed = true;
		}
}

function ajax_result(json, status) {
	var left = jQuery.trim($("input#id_left").val()).toLowerCase();
	var right = jQuery.trim($("input#id_right").val()).toLowerCase();
	var weights = form_weights();
	var length = 0;
	for (var key in json) {
		domain = json[key];
		if (domain.com) continue;
		domain.key = key;
		domain.length = key.length;
		domain.score = domain_score(domain, weights);
		if (keyword_match(left, right, key)) {
			$.domains[key] = domain;
			$.changed = true;
		}
		length = key.length;
	}
	$.ajax_search.xhr[length] = false;
}

function ga_track(path) {
	if ($.ga && window.location.host == "www.nxdom.com") {
		$.ga.trackPageview(path);
	}
}

function gwo_track(path) {
	return; // Disabled on 2010-02-21.
	if (_gat && window.location.host == "www.nxdom.com") {
		var gwoTracker = _gat._getTracker("UA-939486-5");
		gwoTracker._trackPageview(path);
	}
}

function ajax_start() {
	var now = new Date();
	$.ajax_search.start = now.getTime();
}

function ajax_stop() {
	$("img#loading").hide();
	var now = new Date();
	var milliseconds = now.getTime() - $.ajax_search.start;
	var seconds = (milliseconds / 1000).toFixed(1);
	if ($.ajax_search.left || $.ajax_search.right) {
		ga_track('/search/' +
				 $.ajax_search.left.length + '/' +
				 $.ajax_search.right.length + '/' +
				 seconds + '/');
		$.ajax_search.counter++;
		// if ($.ajax_search.counter == 1) {
		//     gwo_track("/3251202061/goal");
		// }
	}
	$.ajax_search.start = false;
	$.changed = true;
}

function ajax_search(left, right) {
	left = jQuery.trim(left).toLowerCase();
	right = jQuery.trim(right).toLowerCase();
	if ($.ajax_search.left == left && $.ajax_search.right == right) return;
	if (left || right) {
		$("img#loading").show();
	} else {
		$("img#loading").hide();
		$.changed = true;
	}
	var now = new Date();
	$.ajax_search.start = now.getTime();
	$.ajax_search.left = left;
	$.ajax_search.right = right;
	delete_domains(left, right);
	for (var index in SEARCH_LENGTHS) {
		var length = SEARCH_LENGTHS[index];
		if ($.ajax_search.xhr[length]) {
			$.ajax_search.xhr[length].abort();
			$.ajax_search.xhr[length] = false;
		}
		if (left.length > length || right.length > length)
			continue;
		var data = 'left=' + left + '&right=' + right +
			'&length=' + length + '&version=' + $.json_version;
		$.ajax_search.xhr[length] = $.ajax({
				type: "GET",
				url: "/search/json/",
				data: data,
				dataType: "json",
				cache: true,
				success: ajax_result,
			});
	}
}

function keyword_keypress(e) {
	if (e.altKey || e.ctrlKey || e.metaKey) return;
	if ((e.which != 45) &&
		(e.which < 48 || e.which > 57) &&
		(e.which < 97 || e.which > 122)) return;
	var left = $("input#id_left").val();
	var right = $("input#id_right").val();
	var updated =
		this.value.substr(0, this.selectionStart) +
		String.fromCharCode(e.which) +
		this.value.substr(this.selectionEnd);
	if (this.name == 'left') left = updated;
	else if (this.name == 'right') right = updated;
	ajax_search(left, right);
}

function update_if_changed(i) {
	var left = $("input#id_left").val();
	var right = $("input#id_right").val();
	ajax_search(left, right);
	if ($.changed) update_html();
	$.changed = false;
}

function show_weights() {
	$("div#priority").hide();
	$("div#weights").show();
    $("div.three").css("top", 606);
    $("div.four").css("top", 678);
	$("div#left").css("height", 759);
}

function show_priority() {
	$("div#weights").hide();
	$("div#priority").show();
    $("div.three").css("top", 438);
    $("div.four").css("top", 510);
	$("div#left").css("height", 591);
}

function document_ready() {
	$.domains = {};
	$.keys = [];
	$.weights = form_weights();
	$.ajax_search = {};
	$.ajax_search.xhr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
	$.ajax_search.start = false;
	$.ajax_search.left = '*';
	$.ajax_search.right = '*';
	$.ajax_search.counter = 0;
	$.ajax_search.showing = 0;
	$.changed = false;
    $("img#loading").ajaxStart(ajax_start).ajaxStop(ajax_stop);
}

$(document).ready(document_ready);
