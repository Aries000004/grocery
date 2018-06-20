$(document).ready(function(){
    $(".auth-warn").show();
});

// 验证用户是否已近实名认证, 已近实名认证展示房源信息
$.get('/user/auths/', function (msg) {
    if (msg.code == 200) {
        if (!msg.data.id_name || !msg.data.id_card) {
            $('#houses-list').hide();
        } else {
            $('#authicate').hide();
        }
    };
});

// 展示所有房源信息
function all_houses () {
    $.get('/house/all_houses/', function (data) {
        console.log(data)
    });
};