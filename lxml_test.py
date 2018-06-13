from lxml import etree

page_text = '''
<html>
<title> This is Title </title>
<body>
	<h1> This is h1 </h1>
	<div> This is fisrt div </div>
	<div id="divid">
		<img src="1111.png"/>
		<span id="sp1"> desc 1111.png </span>

		<img src="2222.png"/>
		<span id="sp2"> desc 2222.png </span>

		<p>
			<a href="http://www.xxxxx.com/"> link-of-xxxxxx </a>
		</p>

		<a href="http://www.yyyyyyy.com/"> link-of-yyyyyyyyy </a>
		<br/>
		<a href="http://www.zzzzzzz.com/"> link-of-zzzzzzzzz </a>

	</div>

	<p class="p_classname"> This is p with class name </p>

	<div class="div_classname"> This is div with class name </div>

</body>
</html>
'''

html = etree.HTML(page_text)


# 所有 h1 元素的文字
# print(html.xpath("//h1/text()")[0])

# 所有 div 元素集合列表
# print( html.xpath("//div") )

# 所有拥有id属性的 div 元素集合列表
# print(html.xpath("//div[@id]"))

# 所有 class 属性为 div_classname 的 div 元素集合列表
# print( html.xpath("//div[@class='div_classname']/text()") )

# 所有属性 非空 的 div 元素集合列表
# print( html.xpath("//div[(@*)]") )

# 所有属性为 空 的 div 元素集合列表
# print( html.xpath("//div[not (@*)]/text()") )

# 第一层(个) div 元素列表，注意下标不是 0，而且类型依然是 列表
# print( html.xpath("//div[1]/text()") )

# 最后一个 div 元素，类型列表
# print( html.xpath("//div[last()]/text()") )

# 倒数第2个 div 元素(最后一个减1)，类型列表
# print( html.xpath("//div[last()-1]/text()") )

# 位置为最前面 2 个的div元素
# print( html.xpath("//div[position() < 3]") )

# 所有 标签a 的 href 属性值，列表
# print( html.xpath("//a/@href") )

# 第 2 个 div 标签下一层所有 a 的 href 属性值
# 注意 p 中的 a 没拿到
# print( html.xpath("//div[2]/a/@href") )

# 第 2 个 div 标签以下所有层面 a 的 href 属性值
# print( html.xpath("//div[2]//a/@href") )

# 第 2 个 div 标签下第1个 span 的 id 属性值
# print( html.xpath("//div[2]/span[1]/@id") )

# 查找 div 和 p 的集合
# print( html.xpath("//div | //p") )

# 除了最后一个 div 以外的所有 div
# print( html.xpath("//div")[:-1] )
# print( html.xpath("//div[position() < last()]") )

# 第 2 个 div 下所有每一层的 第1个 a 标签的属性
# print( html.xpath("//div[2]//a[1]/@href") )

# 第 2 个 div 下第一层的 第1个 a 标签的属性
# print( html.xpath("//div[2]/a[1]/@href") )


