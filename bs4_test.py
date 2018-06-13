from bs4 import BeautifulSoup

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

	<!-- <div class="zhushi"> This is div with class name </div> -->

</body>
</html>
'''

bsp = BeautifulSoup(page_text, 'lxml')

# 获得 title 元素
# print( bsp.title )
# print( type(bsp.title) )

# 获得 title 元素文本
# print( bsp.title.text )
# print( type(bsp.title.text) )
# print( bsp.title.string )
# print( type(bsp.title.string) )

# 获得第一个 div 元素
# print( bsp.div )

# 获得所有 div 元素
# print( bsp.find_all("div") )
# print( bsp.select("div") )


# 所有拥有id属性的 div 元素集合列表
# print( bsp.select("div[id]") )

# 所有 class 属性为 div_classname 的所有元素
# print( bsp.select(".div_classname") )
# print( bsp.select("div[class='div_classname']") )

# 所有 id 属性为 divid 的所有元素
# print( bsp.select("#divid") )

# 最后一个 div 元素
# print( bsp.select("div")[-1] )

# 倒数第2个 div 元素，类型列表
# print( bsp.select("div")[-2] )

# 位置为最前面 2 个的div元素
# print( bsp.select("div")[0:2] )

# 第一个 a 元素的 href 属性
# print( bsp.a.get("href") )
# print( bsp.a.attrs['href'] )

# 第二个 a 元素的所有属性
# print( bsp.select("a")[1].attrs )

# id = divid 的 div 元素下一层的 a 元素
# print( bsp.select("#divid > a") )
# print( bsp.select("div[id='divid'] > a") )
# print( bsp.select("div[id=divid] > a") )

# id = divid 的 div 元素下所有层的 a 元素
# print( bsp.select("div[id=divid] a") )

# id = divid 的 div 标签下第1个 span 的 id 属性值
# print( bsp.select("div[id=divid] span")[0].get('id') )
# print( bsp.select("div[id=divid]")[0].span.get('id') )
# print( bsp.select("div[id=divid] span", limit=1)[0].get('id') )

# 踢除最后一个 div 元素的所有 div
# print( bsp.select("div")[:-1] )

# 获得所有 a 元素的 href 属性集合
# print( [a.get('href') for a in bsp.select("a")] )
# print( [a.attrs['href'] for a in bsp.select("a")] )

# 所有属性 非空 的 div 元素集合列表
# print( [div for div in bsp.select("div") if div.attrs] )

# 所有属性为 空 的 div 元素集合列表
# print( [div for div in bsp.select("div") if not div.attrs] )

