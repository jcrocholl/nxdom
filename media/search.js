DIRECT_PROPERTIES = ["name", "length", "digits", "dashes"];
SCORE_PROPERTIES = ["english", "spanish", "french", "german",
					"prefix", "suffix"];
TLD_PROPERTIES = ["com", "net", "org", "biz", "info"];

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

function ajax_result(json, status) {
	$.ajax_search.xhr = false;
	var html = '';
    var row = 1;
    var weights = form_weights();
    for (name in json) {
		domain = json[name];
		domain.name = name;
		domain.length = name.length;
		domain.score = domain_score(domain, weights);
		html += table_row(domain, row);
		row = (row % 2) + 1;
    }
    $("tbody#results").html(html);
    $("tbody tr").hover(function() { $(this).addClass("hover"); },
						function() { $(this).removeClass("hover"); });
}

function ajax_search(left, right) {
	if ($.ajax_search.left == left && $.ajax_search.right == right) return;
	$.ajax_search.left = left;
	$.ajax_search.right = right;
	if ($.ajax_search.xhr) $.ajax_search.xhr.abort();
	data = {"left": left, "right": right};
	$.ajax_search.xhr = $.getJSON("/search/json/", data, ajax_result);
}

function keyword_keypress(e) {
	if ((e.which != 45) &&
		(e.which < 48 || e.which > 57) &&
		(e.which < 97 || e.which > 122)) return;
	var keywords = {
		"left": $("input#id_left").val(),
		"right": $("input#id_right").val()};
	keywords[this.name] =
		this.value.substr(0, this.selectionStart) +
		String.fromCharCode(e.which) +
		this.value.substr(this.selectionEnd);
	ajax_search(keywords["left"], keywords["right"]);
}

function keyword_keyup() {
	var left = $("input#id_left").val();
	var right = $("input#id_right").val();
	ajax_search(left, right);
}

function document_ready() {
    $.ajax_search = Object();
	$.ajax_search.xhr = false;
	$.ajax_search.left = $("input#id_left").val();
	$.ajax_search.right = $("input#id_right").val();
	$("input.keyword").keypress(keyword_keypress);
	$("input.keyword").keyup(keyword_keyup);
}

$(document).ready(document_ready);
