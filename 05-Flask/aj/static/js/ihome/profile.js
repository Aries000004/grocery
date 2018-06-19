function showSuccessMsg() {
    $('.popup_con').fadeIn('fast', function() {
        setTimeout(function(){
            $('.popup_con').fadeOut('fast',function(){}); 
        },1000) 
    });
}

function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function () {
    $('#form-avatar').submit(function () {

        var avatar = $('#avatar').val();
        var name = $('.user-name').val();
        // alert(avatar);
        // alert(typeof(avatar));

        $.ajax({
            url: '/user/profile/',
            type: 'PATCH',
            dataType: 'json',
            data: {'avatar': avatar},
            success: function (data) {
                console.log(data)
            },
            error: function () {
                alert('请求失败')
            }
        });

    });
    // 更换用户名
    $('#form-name').submit(function () {

        var name = $('#user-name').val();
        // alert(name)
        $.ajax({
            url: '/user/profile/',
            type: 'PATCH',
            dataType: 'json',
            data: {'name': name},
            success: function (data) {
                console.log(data);
            },
            error: function () {
                alert('请求失败')
            }
        });

    });
});
