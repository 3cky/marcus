$(document).ready(function() {
	$(".likes-link").on('click', function(event) {
		event.preventDefault();
		var el = $(this);
		var replace_target = el.parents('.likes:first');
		$(".likes-heart")
		.on('animationend', function() {
			$.get(el.attr('href'), {}, function(data) {
				replace_target.html(data);
			});
		})
		.toggleClass('likes-heart-clicked');
	});
});
