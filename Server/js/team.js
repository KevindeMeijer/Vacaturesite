$('.testimonial-pics img').click(function(){
    $(".testimonial-pics img").removeClass("active");
    $(this).addClass("active");

    $(".testimonial").removeClass("active");
    $("#"+$(this).attr("alt")).addClass("active");
});
