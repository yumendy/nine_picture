# 九图

### 将一张图片切割为九张小图片，用于微信朋友圈。

### 依赖

Python 2.7

PIL: pip install pillow

### 说明

<del>输入图片若不是方形将会根据较小边对较大边进行居中裁切。</del>

支持两种模式，第一种为居中裁剪，第二种为白色填充。

### 使用方法

命令行：

```bash
python main.py C image_path # 居中裁剪

python main.py F image_path # 白色填充
```


也可以将这个类作为一个模块导入自己的项目：

```python
from main import NinePictures

app = NinePictures(image_path, image_mode)
image_list = app.process()
```
返回的`image_list`是一个`PIL.Image`的对象列表，为处理好的九张图片。

示例：

`python main.py C header.png`

原图：

![header.png](header.png)

结果：

<table>
	<tr>
		<td><img src="1.png" alt=""></td>
		<td><img src="2.png" alt=""></td>
		<td><img src="3.png" alt=""></td>
	</tr>
	<tr>
		<td><img src="4.png" alt=""></td>
		<td><img src="5.png" alt=""></td>
		<td><img src="6.png" alt=""></td>
	</tr><tr>
		<td><img src="7.png" alt=""></td>
		<td><img src="8.png" alt=""></td>
		<td><img src="9.png" alt=""></td>
	</tr>
</table>

|  |  | |
|:-------------:|:-------------:|:-----:|
|![1.png](1.png)|![2.png](2.png)|![3.png](3.png)|
|![4.png](4.png)|![5.png](5.png)|![6.png](6.png)|
|![7.png](7.png)|![8.png](8.png)|![9.png](9.png)|