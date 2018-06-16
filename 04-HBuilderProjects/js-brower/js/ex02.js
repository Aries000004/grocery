var cache = {}; //性能略微优化   cache  缓存  方便获取已经获取过的元素
// 缓存 : 优化一般都是优化时间   牺牲空间来获取时间   
function $(id) {
	if(!cache[id]) {
		cache[id] = document.getElementById(id);
	}
	return cache[id];
}

// IE 兼容   去元素的只读样式
// 三元条件运算     
function getStyle(elem) {
	return window.getComputedStyle ? window.getComputedStyle(elem) : elem.currentStyle
}
//	if (window.getComputedStyle) {
//				return window.getComputedStyle(elem);
//			} else {
//				return elem.currentStyle;



function $tag(tag) {
	return document.getElementsByTagName(tag)
}