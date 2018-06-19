function logout() {
    $.get("/api/logout", function(data){
        if (0 == data.errno) {
            location.href = "/";
        }
    })
}

$(document).ready(function(){
    UserInfo()
});

// 获取用户信息功能函数
function UserInfo() {
     $.ajax({
        url: '/user/user_info/',
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            console.log(data);
            $('#user-name').html(data.name);
            $('#user-mobile').html(data.phone);
            var avatar_path = '/static/'+data.avatar;
            $('#user-avatar').attr('src', avatar_path);
            alert(avatar_path)
        },
        error: function (msg) {
            alert('请求失败')
        },
    });
};