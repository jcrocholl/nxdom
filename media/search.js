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
	// if (tld == 'com') html += name + '.';
	// html += tld + '</a>';
	html += name + '</a>';
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

function group_row(prefix, keys) {
	var html = '<span class="quiet">' + prefix + '</span>';
	var length = prefix.length;
	for (var index in keys) {
		var key = keys[index];
		var domain = $.domains[key];
		var name = domain.key;
		length += 1 + name.length;
		if (length >= 80) break;
		html += ' ' + affiliate_link(name, 'com');
	}
	html += '<br />';
	return html;
}

function p_html(groups) {
	var prefixes = [];
	for (var prefix in groups) prefixes.push(prefix);
	prefixes.sort(function(a, b) {
			if (a == b) return 0;
			if (a.substr(0, b.length) == b) return -1;
			if (b.substr(0, a.length) == a) return 1;
			if (a < b) return -1;
			if (a > b) return 1;
			return 0; });
	var html = '';
	for (var index in prefixes) {
		var prefix = prefixes[index];
		html += group_row(prefix, groups[prefix]);
	}
	return html;
}

function split_group(groups, old_prefix) {
	// Count all prefixes (old_prefix + one more letter).
	var old_length = old_prefix.length;
	var new_length = old_length + 1;
	var prefixes = {};
	for (var index in groups[old_prefix]) {
		var key = groups[old_prefix][index];
		prefix = key.substr(0, new_length);
		if (prefix in prefixes) prefixes[prefix] += 1;
		else prefixes[prefix] = 1;
	}
	// Find the prefix with the highest count.
	var best_count = 0;
	var best_prefix = '';
	for (var prefix in prefixes) {
		if (prefixes[prefix] > best_count) {
			best_count = prefixes[prefix];
			best_prefix = prefix;
		}
	}
	// Move keys with the best prefix to a new group.
	groups[best_prefix] = [];
	for (var index = groups[old_prefix].length - 1; index >= 0; index--) {
		var key = groups[old_prefix][index];
		if (key.substr(0, new_length) == best_prefix) {
			groups[old_prefix].splice(index, 1);
			groups[best_prefix].push(key);
		}
	}
}

function make_groups(groups, max_count) {
	for (var count = 1; count <= max_count; count++) {
		// Find the largest group.
		var best_count = 0;
		var best_prefix = '';
		for (var prefix in groups) {
			if (groups[prefix].length > best_count) {
				best_count = groups[prefix].length;
				best_prefix = prefix;
			}
		}
		// If the largest group is small enough, we're done.
		if (best_count <= 8) break;
		// Split the largest group into two groups.
		split_group(groups, best_prefix);
	}
	for (var prefix in groups) {
		groups[prefix].sort(function(a, b) {
				return $.domains[b].score - $.domains[a].score });
	}
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
	var keys = [];
	for (var key in $.domains) keys.push(key);
	var results_count = keys.length;
	var groups = {};
	groups[$.ajax_search.left] = keys;
	make_groups(groups, 25);
	var html = p_html(groups);
	$("div#welcome").hide();
	if (results_count == 0) {
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
		if (results_count <= DEFAULT_LIMIT / 2 && !$.ajax_search.start)
			$("#results_few").show();
		else
			$("#results_few").hide();
	}
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
