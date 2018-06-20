function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function(){
    // $('.popup_con').fadeIn('fast');
    // $('.popup_con').fadeOut('fast');
    allInfo();
});

// 渲染页面 区域 area  // 渲染页面的 设施
function allInfo() {
    $.get('/house/area_facility/', function (data) {
        console.log(data);
        for (var i = 0; i < data.data.areas.length; i += 1) {
            var name = data.data.areas[i].name;
            var id = data.data.areas[i].id;

            var option = $('<option>').attr('value', id).text(name);

            $('#area-id').append(option);
        };

        for (var i = 0; i < data.data.facilities.length; i += 1) {
            var name = data.data.facilities[i].name;
            var id = data.data.facilities[i].id;

            var input = $('<input>').attr('type', 'checkbox').attr('name', 'facility').attr('value', id);
            var label = $('<label>').append(input).append(name);
            var div = $('<div>').addClass('checkbox').append(label);
            var li = $('<li>').append(div);

            $('.house-facility-list').append(li)
        };

    });
};



