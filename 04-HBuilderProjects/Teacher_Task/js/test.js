function bind(elem, en, fn) {
	if(elem.addEventListener) {                // 第三个参数表示事件处理的方式     默认为 false (bubble)
		elem.addEventListener(en, fn, true);  //false 事件冒泡(bubble), true 事件捕获(capture)
	} else {
		elem.attachEvent('on' + en, fn);
	}
}

var cache = {}; //性能略微优化   cache  缓存  方便获取已经获取过的元素                 // 缓存 : 优化一般都是优化时间   牺牲空间来获取时间   
function $(id) {
	if(!cache[id]) {
		cache[id] = document.getElementById(id);
	}
	return cache[id];
}