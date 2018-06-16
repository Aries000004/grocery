function $(id) {
	return document.getElementById(id);
}

function bind(elem, en, fn) {
	if(elem.addEventListener) {
		elem.addEventListener(en, fn);
	} else {
		elem.attachEvent('on' + en, fn); //ie 浏览器
	}
}

function unbind(elem, en, fn) {
	if(elem.removeEventListener) {
		elem.removeEventListener(en, fn);
	} else {
		elem.detachEvent('on' + en, fn);  //ie浏览器
	}
}




//'back': function(num) {
//					if(this.state && this.room + num < 100) {
//						this.room += num;
//						alert(hotel.room)
//					} else {
//						alert('退房失败')
//						alert('房间数' + this.room)
//					}
//
//				}

//'close': function() {
//					this.state = false;
//					alert('停止营业')
//				},