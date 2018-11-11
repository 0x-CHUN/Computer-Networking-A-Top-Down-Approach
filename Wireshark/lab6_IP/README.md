# IP

## 实验步骤

1. 安装pingplotter
2. 打开 wireshark 抓包，并且 pingplotter 设置 Edit->Options->Default->Settings->Engine 包大小设置为 56Byte 。
3. 然后打开gaia.cs.umass.edu的跟踪，大约跟踪3次.
4. 将大小设置 2000Byte 以及 3500Byte，重复 2-3 步。
5. 关闭 wireshark

## Answer

1. 我的IP地址192.168.1.102
2. Protocol: ICMP (1)。上层协议是ICMP，值为1.
3. Total Length: 56，.... 0101 = Header Length: 20 bytes (5)。可以得出IP header有20bytes，IP datagram有（56-20）36bytes。IP datatgram = Total Length - Header Length。
4. 
    ```
    Flags: 0x0000
    0... .... .... .... = Reserved bit: Not set
    .0.. .... .... .... = Don't fragment: Not set
    ..0. .... .... .... = More fragments: Not set
    ...0 0000 0000 0000 = Fragment offset: 0
    ```
    从上可以看出没有被分段
5. Identification、Time to live（TTL）、Header checksum在变化。
6. IP Version、 Header Length、Differentiated Services Field、Protocol不会变。
7. 
    ```
    Internet Control Message Protocol
    Type: 8 (Echo (ping) request)
    Code: 0
    Checksum: 0x346c [correct]
    [Checksum Status: Good]
    Identifier (BE): 1 (0x0001)
    Identifier (LE): 256 (0x0100)
    Sequence number (BE): 465 (0x01d1)
    Sequence number (LE): 53505 (0xd101)
    [No response seen]
    Data (28 bytes)
    ----------------------------------------------
    Internet Control Message Protocol
    Type: 8 (Echo (ping) request)
    Code: 0
    Checksum: 0x346b [correct]
    [Checksum Status: Good]
    Identifier (BE): 1 (0x0001)
    Identifier (LE): 256 (0x0100)
    Sequence number (BE): 466 (0x01d2)
    Sequence number (LE): 53761 (0xd201)
    [No response seen]
    Data (28 bytes)

    ```
    从上可以看出IP 数据段就是 ICMP 协议，根据 ICMP 协议的数据报格式，他的识别代码和校验码一定会改变，且是每次递增的关系。
8. Time to live: 1；Identification: 0x58ed (22765)；  
    从上可以看出TTL=1，ID字段=22765
9. ID 字段递增，TTL不变。
10. 
    ```
    2 IPv4 Fragments (1980 bytes): #24109(1456), #24110(524)
    ```
    存在分片
11. 
    ```
    Total Length: 1476
    Flags: 0x2000, More fragments
    0... .... .... .... = Reserved bit: Not set
    .0.. .... .... .... = Don't fragment: Not set
    ..1. .... .... .... = More fragments: Set
    ...0 0000 0000 0000 = Fragment offset: 0
    ```
    通过 IP数据头的标志位有个分段标志可以发现已经被分段，通过偏移量发现这是第一个片段，这个数据报有 1476Byte。
12. 
    ```
    Total Length: 44
    Flags: 0x20b9, More fragments
    0... .... .... .... = Reserved bit: Not set
    .0.. .... .... .... = Don't fragment: Not set
    ..1. .... .... .... = More fragments: Set
    ...0 0000 1011 1001 = Fragment offset: 182
    ```
    从Total Leng 和Fragment offset的数值不满足关系，可以得出这不是第一个数据报的片段。
13. IP 头的 ID ，标志位，以及校验码
14. 3 IPv4 Fragments (1980 bytes): #27387(1456), #27388(24), #27386(500)。可以看出3个片段。
15. IP 头的 ID ，标志位，以及校验码