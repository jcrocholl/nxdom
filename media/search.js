DIRECT_PROPERTIES = ["name", "length", "digits", "dashes"];
SCORE_PROPERTIES = ["english", "spanish", "french", "german",
					"prefix", "suffix"];
TLD_PROPERTIES = ["com", "net", "org", "biz", "info"];
SEARCH_LENGTHS = [7, 8, 6, 9, 5, 10, 4, 11, 3, 12];

function force_number(text) {
	var number = parseFloat(text);
	if (isNaN(number)) return 0;
	return number;
}

function form_weights() {
	return {"length": force_number($("input#id_len").val()),
			"digits": force_number($("input#id_digits").val()),
			"dashes": force_number($("input#id_dashes").val()),
			"english": force_number($("input#id_english").val()) / 1000000,
			"spanish": force_number($("input#id_spanish").val()) / 1000000,
			"french": force_number($("input#id_french").val()) / 1000000,
			"german": force_number($("input#id_german").val()) / 1000000,
			"prefix": force_number($("input#id_prefix").val()) / 1000000,
			"suffix": force_number($("input#id_suffix").val()) / 1000000,
			"com": force_number($("input#id_com").val()),
			"net": force_number($("input#id_net").val()),
			"org": force_number($("input#id_org").val()),
			"biz": force_number($("input#id_biz").val()),
			"info": force_number($("input#id_info").val())}
}

function domain_score(domain, weights) {
	var score = 0.0;
	for (var attr in weights)
		score += domain[attr] * weights[attr];
	return score;
}

function table_row(domain, row) {
	var html = '<tr class="row' + row + '">';
	for (var index in DIRECT_PROPERTIES) {
		html += '<td>' + domain[DIRECT_PROPERTIES[index]] + '</td>';
	}
	for (var index in SCORE_PROPERTIES) {
		var score = domain[SCORE_PROPERTIES[index]] / 1000000;
		html += '<td>' + score.toFixed(3) + '</td>';
	}
	for (var index in TLD_PROPERTIES) {
		if (domain[TLD_PROPERTIES[index]])
			html += '<td class="green">free</td>';
		else
			html += '<td class="red">taken</td>';
	}
	html += '<td>' + domain.score.toFixed(1) + '</td>';
	html += '</tr>';
	return html;
}

function update_html() {
	var html = '';
	var row = 1;
	var names = [];
	for (var name in $.domains) names.push(name);
	names.sort(function(a,b) {
		return $.domains[b].score - $.domains[a].score });
	names.length = 100;
	for (var index in names) {
		domain = $.domains[names[index]];
		html += table_row(domain, row);
		row = (row % 2) + 1;
	}
	$("tbody#results").html(html);
	$("tbody tr").hover(
		function() { $(this).addClass("hover"); },
		function() { $(this).removeClass("hover"); });
}

function array_unchanged(a, b) {
	for (var index in a)
		if (a[index] != b[index])
			return false;
	return true;
}

function update_scores() {
	var weights = form_weights();
	if (array_unchanged($.weights, weights)) return;
	$.weights = weights;
	for (var name in $.domains) {
		var domain = $.domains[name];
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
	for (var name in $.domains)
		if (!keyword_match(left, right, name))
			delete $.domains[name];
	update_html();
}

function ajax_result(json, status) {
	var left = $("input#id_left").val();
	var right = $("input#id_right").val();
	var weights = form_weights();
	var updated = false;
	var length = 0;
	for (name in json) {
		domain = json[name];
		domain.name = name;
		domain.length = name.length;
		domain.score = domain_score(domain, weights);
		if (keyword_match(left, right, name)) {
			$.domains[name] = domain;
			updated = true;
		}
		length = name.length;
	}
	$.ajax_search.xhr[length] = false;
	if (updated) update_html();
}

function ajax_search(left, right) {
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
				data: {left: left, right: right, length: length},
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

function document_ready() {
	$.domains = {};
	$.weights = form_weights();
	$.ajax_search = {};
	$.ajax_search.xhr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
	$.ajax_search.left = $("input#id_left").val();
	$.ajax_search.right = $("input#id_right").val();
	$("input.keyword").keypress(keyword_keypress);
	$("input.keyword").keyup(keyword_keyup);
	$("input.score").keyup(update_scores);
}

$(document).ready(document_ready);
