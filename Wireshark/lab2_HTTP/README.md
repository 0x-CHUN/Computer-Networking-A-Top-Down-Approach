# 实验一：基本HTTP GET/response交互
## 实验步骤
1. 打开wireshark，将出现接口列表。双击选择接口，程序将捕获接口的所有数据包。
2. 访问http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file1.html
3. 使用过滤器，过滤除HTTP的协议

结果：

![](img\result.PNG)

输出：

[result.pdf](result\result.pdf)

## Answer：

1. 服务器运行HTTP1.1，本机运行HTTP1.1
2. zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2（q为权重）
3.  gaia.cs.umass.edu的IP地址为：128.119.245.12 本机IP为：10.173.185.180
4. 服务器返回状态码：200
5. 最后一次修改时间：Last-Modified: Fri, 05 Oct 2018 05:59:01 GMT
6. 返回了128bytes
7. 无

# 实验二：HTTP条件Get/response交互
## 实验步骤
1. 重启浏览器，清除缓存
2. 访问http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file2.html，刷新

结果：

![](img\result2.PNG)

输出：

[result2.pdf](result\result2.pdf)

## Answer：
8. 第一次访问无
9. 显示返回内容
10. 能，If-Modified-Since是标准的HTTP请求头标签，在发送HTTP请求时，把浏览器端缓存页面的最后修改时间一起发到服务器去，服务器会把这个时间与服务器上实际文件的最后修改时间进行比较。
11. 状态码：304 短语：Not Modified。因为第二次访问时本地有缓存，直接调用即可。

# 实验三：检索长文件
## 实验步骤
1. 重启浏览器，清除缓存
2. 访问http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file3.html

结果：

![](img\result3.PNG)

输出：

[result3.pdf](result\result3.pdf)

## Answer：
12. 发送了3个HTTP GET请求消息，第144个数据包含有美国权利法案的消息。
13. 第131、148、151 包含响应HTTP GET请求的状态码和短语。
14. 有两种状态码：200 404 .两种短语：OK、Not　Found。
15. 需要4个包含数据的TCP段来执行单个HTTP响应和权利法案文本。

# 实验四：具有嵌入对象的HTML文档
## 实验步骤
1. 重启浏览器，清除缓存
2. 访问http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file4.html

结果：

![](img\result4.PNG)

输出：

[result4.pdf](result\result4.pdf)

## Answer：
16. 浏览器发送了3个HTTP GET请求消息，这些GET请求发送到128.119.245.12。
17. 串行下载了两幅图片。因为它的发包顺序有时间差。

# 实验五：HTTP认证
## 实验步骤
1. 重启浏览器，清除缓存
2. 访问http://gaia.cs.umass.edu/wireshark-labs/HTTP-wireshark-file5.html

结果：

![](img\result5.PNG)

输出：

[result5.pdf](result\result5.pdf)
## Answer：
18. 初始响应的状态码：401  短语：Unauthorized
19. 新包含了：Authorization: Basic Y2h1bjoxMjM0NTY=\r\n
    从Base64转换为ASCII可得：Credentials: chun:123456