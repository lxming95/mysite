当django2.0使用xadmin点击用户出现render() got an unexpected keyword argument 'renderer'错误

修改xadmin下的boundfield.py中的def as_widget方法

89行：

源代码如下
``` python
return widget.render(
   name=self.html_initial_name if only_initial else self.html_name,
   value=self.value(),
   attrs=attrs,
   renderer=self.form.renderer,
)

#修改为：
return widget.render(
   name=self.html_initial_name if only_initial else self.html_name,
   value=self.value(),
   attrs=attrs,
   # renderer=self.form.renderer,
)
return force_text(html)
``` 

