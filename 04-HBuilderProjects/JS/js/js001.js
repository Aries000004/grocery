function foo() {
	//定义变量 var 
	var name = window.prompt('输入名字!')
	//在控制台生成日志  保留
	//console.log(typeof(name))
	if(name && name != 'null') {
		window.alert('你好' + name + '!')
	} else {
		window.alert('名字呢?')
		window.alert('你好!');
	}
}

