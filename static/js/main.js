$(document).ready(function () {
//    $('#user_button').click();
    $(".comment-content").keypress(function (event) {
        if (event.which == 13) {
            event.preventDefault();
            $(".comment-form").submit();
        }
    });
})

$(document).ready(function () {
    $(".reply-form").hide();
    $(".reply-button").click(function () {
        var id = $(this).data('comment');
//        var id = $(this).attr('data-comment');
        $("#form_reply_" + id).toggle();
    });
})

$(document).ready(function(){

		$('#back-top a').click(function () {
			$('body,html').animate({
				scrollTop: 0
			}, 800);
			return false;
		});
});