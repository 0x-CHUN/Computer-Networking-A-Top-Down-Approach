# ICMP

## 实验步骤

1. 打开 Wireshark 启动捕获
2. 打开命令提示符使用 ping 命令 ping 其他大陆的服务器 10 次

    ping -n 10 gaia.cs.umass.edu
3. 保存数据包，并且启动下一次捕获
4. 打开命令提示符进行路由跟踪，跟踪 gaia.cs.umass.edu 

    tracert gaia.cs.umass.edu
5. 进行实验数据结果分析

输出一：

[result.pdf](result/result1.pdf)

输出二：

[result.pdf](result/result2.pdf)

## Answer

1. 我的IP地址：10.173.239.177；目的IP地址：128.119.245.12。
2. 因为ICMP协议是网络层的协议，它不需要传输层TCP和UDP承载，直接使用IP报承载，因此不需要源端口号目的端口号，只需要目的地址即可。
3. 请求ICMP数据包：
    ```
    Internet Control Message Protocol
    Type: 8 (Echo (ping) request)
    Code: 0
    Checksum: 0x4d5a [correct]
    [Checksum Status: Good]
    Identifier (BE): 1 (0x0001)
    Identifier (LE): 256 (0x0100)
    Sequence number (BE): 1 (0x0001)
    Sequence number (LE): 256 (0x0100)
    [Response frame: 830]
    Data (32 bytes)
    ```
    ICMP类型是8，代码是0,ICMP数据包还包括校验码，ID值，以及序号。校验和，序列号，标识符都是16个字符，4个字节。
4. 响应ICMP数据包：
    ```
    Internet Control Message Protocol
    Type: 0 (Echo (ping) reply)
    Code: 0
    Checksum: 0x555a [correct]
    [Checksum Status: Good]
    Identifier (BE): 1 (0x0001)
    Identifier (LE): 256 (0x0100)
    Sequence number (BE): 1 (0x0001)
    Sequence number (LE): 256 (0x0100)
    [Request frame: 829]
    [Response time: 352.560 ms]
    Data (32 bytes)
    ```
    ICMP类型是0，代码是0,ICMP数据包还包括校验码，ID值，以及序号。校验和，序列号，标识符都是16个字符，4个字节。
5. 我的IP地址：10.173.239.177；目的IP地址：128.119.245.12。
6. 发送请求路由跟踪的数据包时UDP数据包，因此IP承载上层协议号时17。
7. 路由跟踪的 ICMP 响应数据包（非超时错误数据包）的 ICMP 的 的 TYPE和序列号不同于前半部分 ICMP 的 的 PING 的查询数据包。
8. 多了以下内容
    ```
    Internet Protocol Version 4, Src: 10.173.239.177, Dst: 128.119.245.12
    0100 .... = Version: 4
    .... 0101 = Header Length: 20 bytes (5)
    Differentiated Services Field: 0x00 (DSCP: CS0, ECN: Not-ECT)
    Total Length: 92
    Identification: 0x4e94 (20116)
    Flags: 0x0000
    Time to live: 1
    Protocol: ICMP (1)
    Header checksum: 0xfb2a [validation disabled]
    [Header checksum status: Unverified]
    Source: 10.173.239.177
    Destination: 128.119.245.12
    ```
9. 最后三个 ICMP （响应）数据包是目标主机发送给我ICMP 回应数据增包，因为路由查询是使用逐渐递增 TTL 的 的 ICMP 查询数据包，最后的 ICMP的查询数据包的 TTL 已经大于到达目的主机中间路由跃点数，因此不会被目送 标主机丢弃，发送 ICMP 超时的数据包，所以只会收到 ICMP 响应数据包。
10. 存在
    ```
    通过最多 30 个跃点跟踪
    到 gaia.cs.umass.edu [128.119.245.12] 的路由:
    
     1     1 ms     1 ms     1 ms  10.173.255.254
     2     6 ms     9 ms     4 ms  172.16.255.242
     3     1 ms     1 ms     1 ms  172.16.255.254
     4     2 ms     2 ms     2 ms  124.115.222.145
     5     2 ms     2 ms     2 ms  10.224.67.1
     6     2 ms     2 ms     1 ms  117.36.240.77
     7     *       19 ms    19 ms  202.97.43.185
     8     *       23 ms     *     202.97.48.206
     9     *       25 ms     *     202.97.58.98 //突然增大啦，在中国北京
    10   276 ms   274 ms   264 ms  202.97.52.2  //在美国加利福尼亚州洛杉矶
    11   290 ms   292 ms   290 ms  202.97.49.158
    12   187 ms   178 ms     *     218.30.54.142
    13   293 ms   274 ms     *     cmb-edge-03.inet.qwest.net [67.14.30.158]
    14   383 ms     *      385 ms  65.126.225.186
    15   450 ms   459 ms   447 ms  core1-rt-et-4-3-0.gw.umass.edu [192.80.83.101]
    16   474 ms     *        *     n5-rt-1-1-et-0-0-0.gw.umass.edu [128.119.0.8]
    17   330 ms   335 ms   330 ms  cics-rt-xe-0-0-0.gw.umass.edu [128.119.3.32]
    18     *        *        *     请求超时。
    19   373 ms   366 ms   373 ms  gaia.cs.umass.edu [128.119.245.12]
    ```