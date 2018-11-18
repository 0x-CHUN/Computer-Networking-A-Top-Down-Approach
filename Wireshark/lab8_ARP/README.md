# ICMP

## 实验步骤

1. 打开 Wireshark 启动捕获
2. 访问 <http://gaia.cs.umass.edu/wireshark-labs/HTTP-ethereal-lab-file3.html>
3. 接下来停止 Wireshark数据包捕获


## Answer

1. Source: 94:db:da:3e:8f:cf
2. Destination: 34:97:f6:e2:8a:f0。gaia.cs.umass.edu 的地址。
3. 0x0800 代表上层协议是 IPV4
4. 55 Byte
5. 源地址：94:db:da:3e:8f:cf，是我的计算机的地址
6. 目的地址：34:97:f6:e2:8a:f0，是gaia.cs.umass.edu 的地址。
7. 0x0800 代表上层协议是 IPV4
8. 68字节
9. 如下
    ```
    接口: 169.254.147.186 --- 0x9//不同的网卡
    Internet 地址         物理地址              类型
     169.254.255.255       ff-ff-ff-ff-ff-ff     静态 //广播地址
     239.255.255.250       01-00-5e-7f-ff-fa     静态 //组播地址
     255.255.255.255       ff-ff-ff-ff-ff-ff     静态

    接口: 192.168.56.1 --- 0xb
      Internet 地址         物理地址              类型
      192.168.56.255        ff-ff-ff-ff-ff-ff     静态
      239.255.255.250       01-00-5e-7f-ff-fa     静态

    ```
10. 00:d0:59:a9:3d:68 目的地址：ff:ff:ff:ff:ff:ff
11. ARP 协议，16 进制值 806
12. a)21Byte

    b)操作码值 1

    c)包含

    d)从操作码看出
13. a)21Byte
 
    b)操作码值 2
 
    c)从操作码看出
14. 源地址：作者路由地址 00:d0:59:a9:3d:68
 
    目的地址：作者电脑地址 00:06:25:da:af:73
15. 因为 ARP 广播信息是广播的，所有该网段内所有的电脑均可收到，而 ARP 广播回的 复是单播的，只有请求的那台电脑才能收到，因此抓不到另外一台电脑的 ARP 请求。