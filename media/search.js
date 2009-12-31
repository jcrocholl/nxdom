DIRECT_PROPERTIES = ["name", "length", "digits", "dashes"];
SCORE_PROPERTIES = ["english", "spanish", "french", "german",
					"prefix", "suffix"];
TLD_PROPERTIES = ["com", "net", "org", "biz", "info"];
SEARCH_LENGTHS = [7, 8, 6, 9, 5, 10, 4, 11, 3, 12]

function form_weights() {
	return {"length": $("input#id_len").val(),
			"digits": $("input#id_digits").val(),
			"dashes": $("input#id_dashes").val(),
			"english": $("input#id_english").val() / 1000000,
			"spanish": $("input#id_spanish").val() / 1000000,
			"french": $("input#id_french").val() / 1000000,
			"german": $("input#id_german").val() / 1000000,
			"prefix": $("input#id_prefix").val() / 1000000,
			"suffix": $("input#id_suffix").val() / 1000000,
			"com": $("input#id_com").val(),
			"net": $("input#id_net").val(),
			"org": $("input#id_org").val(),
			"biz": $("input#id_biz").val(),
			"info": $("input#id_info").val()}
}

function domain_score(domain, weights) {
	var score = 0.0;
	for (attr in weights)
		score += domain[attr] * weights[attr];
	return score;
}

function table_row(domain, row) {
	var html = '<tr class="row' + row + '">';
	var index;
	for (index in DIRECT_PROPERTIES) {
		html += '<td>' + domain[DIRECT_PROPERTIES[index]] + '</td>';
	}
	for (index in SCORE_PROPERTIES) {
		var score = domain[SCORE_PROPERTIES[index]] / 1000000;
		html += '<td>' + score.toFixed(3) + '</td>';
	}
	for (index in TLD_PROPERTIES) {
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
	for (name in $.domains) names.push(name);
	names.sort(function(a,b) {
		return $.domains[b].score - $.domains[a].score });
	names.length = 100;
	for (index in names) {
		domain = $.domains[names[index]];
		html += table_row(domain, row);
		row = (row % 2) + 1;
	}
	$("tbody#results").html(html);
	$("tbody tr").hover(
		function() { $(this).addClass("hover"); },
		function() { $(this).removeClass("hover"); });
}

function keyword_match(left, right, name) {
	if (left && name.substr(0, left.length) != left) return false;
	if (right && name.substr(-right.length) != right) return false;
	return true;
}

function ajax_result(json, status) {
	var left = $("input#id_left").val();
	var right = $("input#id_right").val();
	var weights = form_weights();
	var length = 0;
	for (name in json) {
		domain = json[name];
		domain.name = name;
		domain.length = name.length;
		domain.score = domain_score(domain, weights);
		if (keyword_match(left, right, name))
			$.domains[name] = domain;
		length = name.length;
	}
	$.ajax_search.xhr[length] = false;
	update_html();
}

function ajax_search(left, right) {
	if ($.ajax_search.left == left && $.ajax_search.right == right) return;
	$.ajax_search.left = left;
	$.ajax_search.right = right;
	for (var index in SEARCH_LENGTHS) {
		var length = SEARCH_LENGTHS[index];
		if ($.ajax_search.xhr[length])
			$.ajax_search.xhr[length].abort();
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
	for (name in $.domains)
		if (!keyword_match(left, right, name))
			delete $.domains[name];
	update_html();
	ajax_search(left, right);
}

function keyword_keyup() {
	var left = $("input#id_left").val();
	var right = $("input#id_right").val();
	ajax_search(left, right);
}

function document_ready() {
	$.domains = {};
	$.ajax_search = {};
	$.ajax_search.xhr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
	$.ajax_search.left = $("input#id_left").val();
	$.ajax_search.right = $("input#id_right").val();
	$("input.keyword").keypress(keyword_keypress);
	$("input.keyword").keyup(keyword_keyup);
}

$(document).ready(document_ready);
