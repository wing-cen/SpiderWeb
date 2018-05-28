/**
 * Created by wing on 2017/7/4.
 */
$(function () {
    /*
    * 登录使用
    *
    * */
    $("span").hover(function () {
        var xx = $(this).position().left;
        var yy = $(this).position().top + 250;
        $("#mask").stop().animate({
            left: xx,
            top: yy
        }, 100).fadeIn("fast");
    });
    $("#content").hover(function () {
        $("#mask").css("opacity", "1");
    }, function () {
        $("#mask").fadeOut(500);
    });

    /*
    * 主页使用
    *
    * */
    function showRowLogo(e) {

    }

});
