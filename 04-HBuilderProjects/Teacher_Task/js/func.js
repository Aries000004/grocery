
var cache = {}; //性能略微优化   cache  缓存  方便获取已经获取过的元素                 // 缓存 : 优化一般都是优化时间   牺牲空间来获取时间   
function $(id) {
	if(!cache[id]) {
		cache[id] = document.getElementById(id);
	}
	return cache[id];
}

/**
 * 绑定事件回调函数
 * @param {HTMLElement} elem
 * @param {event} en
 * @param {function} fn
 */
function bind(elem, en, fn) {
	if(elem.addEventListener) {                // 第三个参数表示事件处理的方式     默认为 false (bubble)
		elem.addEventListener(en, fn);  //false 事件冒泡(bubble), true 事件捕获(capture)
	} else {
		elem.attachEvent('on' + en, fn);
	}
}

// IE 兼容   获取元素的只读样式
// 三元条件运算     
function getStyle(elem) {
	return window.getComputedStyle ? window.getComputedStyle(elem) : elem.currentStyle
}
//	if (window.getComputedStyle) {
//				return window.getComputedStyle(elem);
//			} else {
//				return elem.currentStyle;

/**
 * 让固定定位元素变成可拖拽的元素
 * @param {HTMLElement} elem
 */
function makeDraggable(elem) {
	bind(elem, 'mousedown', function(evt) {
		evt = evt || window.event;
		elem.isMouseDown = true;
		var divStyle = getStyle(elem); //得到div的可读样式
		elem.originLeft = parseInt(divStyle.left); //得到div的位置
		elem.originTop = parseInt(divStyle.top);
		elem.mouseX = evt.clientX;
		elem.mouseY = evt.clientY;
	});
	bind(elem, 'mouseup', function() {
		elem.isMouseDown = false;
	});
	bind(elem, 'mousemove', function(evt) {
		if(!elem.isMouseDown) return;
		evt = evt || window.event;
		var dx = evt.clientX - elem.mouseX;
		var dy = evt.clientY - elem.mouseY;
		elem.style.left = (elem.originLeft + dx) + 'px';
		elem.style.top = (elem.originTop + dy) + 'px';
	});
};

/**
 * 阻止事件的默认行为
 * @param {Object} evt
 */
function prevDefault(evt) {
	if (evt.preventDefault) {
		evt.preventDefault();
	} else {
		evt.returnValue = false;
	}
}

/**
 * 处理事件对象 解决兼容性问题  修改 prevDefault
 * @param {Object} evt
 */
function handleEvent(evt) {
	evt = evt || event;
	evt.preventDefault = evt.preventDefault || function () {
		//没有属性绑定函数
		this.returnValue = false;
	};
	evt.stopPropagation = evt.stopPropagation || function () {
		this.cancelBubble = false;
	};
	return evt;
		
		
