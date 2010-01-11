DIRECT_PROPERTIES = ["length", "digits", "dashes"];
SCORE_PROPERTIES = ["english", "spanish", "french", "german",
					"prefix", "suffix"];
TLD_SCORES = {
	com: 10, net: 5, org: 5, biz: 3, info: 3,
	mobi: 3, name: 3, tel: 3, travel: 3,
	at: 1, be: 1, ch: 1, de: 1, es: 1, eu: 2, fm: 2,
	"in": 1, is: 1, it: 1, la: 1, li: 1, ly: 2, ru: 1, se: 1,
	to: 1, tv: 2, us: 1,
};
SEARCH_LENGTHS = [7, 6, 8, 5, 9, 4, 10, 3, 11, 12];

function force_number(text) {
	var number = parseInt(text);
	if (isNaN(number)) return 0;
	return number;
}

function force_million(text) {
	return force_number(text) / 1000000;
}

function form_weights() {
	return {length: force_number($("input[name=len]:checked").val()),
			digits: force_number($("input[name=digits]:checked").val()),
			dashes: force_number($("input[name=dashes]:checked").val()),
			english: force_million($("input[name=english]:checked").val()),
			spanish: force_million($("input[name=spanish]:checked").val()),
			french: force_million($("input[name=french]:checked").val()),
			german: force_million($("input[name=german]:checked").val()),
			prefix: force_million($("input[name=prefix]:checked").val()),
			suffix: force_million($("input[name=suffix]:checked").val())}
}

function domain_score(domain, weights) {
	var score = 0.0;
	for (var attr in weights)
		score += domain[attr] * weights[attr];
	for (var tld in TLD_SCORES)
		if (!domain[tld]) score += TLD_SCORES[tld];
	return score;
}

function mouse_down_track(one, two, three) {
	var path = '/' + one + '/';
	if (two) path += two + '/';
	if (three) path += three + '/';
	var javascript = "$.ga.trackPageview('" + path + "');";
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
	html += '" title="Check availability on ' + $.registrar + '" ';
	html += mouse_down_track('outgoing', $.registrar, tld);
	html += '>' + tld + '</a>';
	return html;
}

function domain_link(name, tld) {
	return '<a href="http://' + name + '.' + tld + '/" ' +
		mouse_down_track('outgoing', 'website', tld) + '>' + tld + '</a>';
}

function google_link(name) {
	return '<a href="http://www.google.com/search?q=' + name + '" ' +
		mouse_down_track('outgoing', 'google') + '>' + name + '</a>';
}

function table_row(domain, row) {
	var html = '<tr class="row' + row + '">';
	html += '<td>' + domain.length + '</td>';
	html += '<td title="Web search">' + google_link(domain.key) + '</td>';
	for (var tld in TLD_SCORES) {
		if (domain[tld]) {
			var color = 'taken';
			if (domain[tld].indexOf('parking') >= 0 ||
				domain[tld].indexOf('parked') >= 0 ||
				domain[tld].indexOf('hitfarm.com') >= 0 ||
				domain[tld].indexOf('fastpark.net') >= 0 ||
				domain[tld].indexOf('buydomains.com') >= 0)
				color = 'parking';
			if (domain[tld].substr(0, 7) == 'status=' ||
				domain[tld].substr(0, 8) == 'timeout=')
				color = 'status';
			html += '<td class="' + color + '" title="' + domain[tld] + '">';
			html += domain_link(domain.key, tld);
			html += '</td>';
		} else {
			html += '<td>';
			html += affiliate_link(domain.key, tld);
			html += '</td>';
		}
	}
	html += '<td>' + domain.score.toFixed(1) + '</td>';
	html += '</tr>';
	return html;
}

function activate_ruler() {
	$("table.ruler tbody tr").hover(
		function() { $(this).addClass("hover"); },
		function() { $(this).removeClass("hover"); });
}

function update_html() {
	var html = '';
	var row = 1;
	var keys = [];
	for (var key in $.domains) keys.push(key);
	keys.sort(function(a,b) {
		return $.domains[b].score - $.domains[a].score });
	keys.length = 100;
	for (var index in keys) {
		domain = $.domains[keys[index]];
		html += table_row(domain, row);
		row = (row % 2) + 1;
	}
	$("tbody#results").html(html);
	activate_ruler();
	$.changed = false;
}

function array_unchanged(a, b) {
	for (var index in a)
		if (a[index] != b[index])
			return false;
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
	var left = jQuery.trim($("input#id_left").val());
	var right = jQuery.trim($("input#id_right").val());
	var weights = form_weights();
	var length = 0;
	for (var key in json) {
		domain = json[key];
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

function ajax_search(left, right) {
	left = jQuery.trim(left);
	right = jQuery.trim(right);
	if ($.ajax_search.left == left && $.ajax_search.right == right) return;
	$.ajax_search.left = left;
	$.ajax_search.right = right;
	delete_domains(left, right);
	for (var index in SEARCH_LENGTHS) {
		var length = SEARCH_LENGTHS[index];
		if ($.ajax_search.xhr[length])
			$.ajax_search.xhr[length].abort();
		if (left.length > length || right.length > length)
			continue;
		$.ajax_search.xhr[length] = $.ajax({
				type: "GET",
				url: "/search/json/",
				data: {left: left, right: right, length: length,
					   version: $.json_version},
				dataType: "json",
				cache: true,
				success: ajax_result,
			});
	}
}

function keyword_keypress(e) {
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

function keyword_keyup() {
	var left = $("input#id_left").val();
	var right = $("input#id_right").val();
	ajax_search(left, right);
}

function update_if_changed(i) {
	$(this).html(i);
	if (!$.changed) return;
	update_html();
}

function document_ready() {
	$.domains = {};
	$.weights = form_weights();
	$.ajax_search = {};
	$.ajax_search.xhr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
	$.ajax_search.left = '*';
	$.ajax_search.right = '*';
	$.changed = false;
	activate_ruler();
}

$(document).ready(document_ready);
