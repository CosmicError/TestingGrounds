// dllmain.cpp : Defines the entry point for the DLL application.

#include "pch.h"

#include <stdio.h>
#include <cstdint>

#include "detours.h"

/*
* VERSION NUMBER:
*   REG LOCATION    Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Respondus
*   SET BY          0x0040367b      LdbRst11.exe      
*/

template < typename T >
inline T rebaseExe(std::uintptr_t rva) {
    return (T)((rva - 0x00400000) + reinterpret_cast<std::uintptr_t>(GetModuleHandle(NULL)));
};

template < typename T >
inline T rebaseDll(std::uintptr_t rva) {
    return (T)((rva - 0x10000000) + reinterpret_cast<std::uintptr_t>(GetModuleHandleA("LockDownBrowser.dll")));
};

using o_LDBCheckHooks = int32_t(__stdcall*)();
o_LDBCheckHooks ldbCheckHooks = nullptr;


using o_keyboardHookCallback = LRESULT(__stdcall*)(int32_t nCode, WPARAM wParam, LPARAM lParam);
o_keyboardHookCallback keyboardHookCallback = nullptr;

using o_keyboardHookCallback_1 = LRESULT(__stdcall*)(int32_t nCode, WPARAM wParam, LPARAM lParam);
o_keyboardHookCallback_1 keyboardHookCallback_1 = nullptr;

using o_keyboardHookCallback_2 = LRESULT(__stdcall*) (int32_t nCode, WPARAM wParam, LPARAM lParam);
o_keyboardHookCallback_2 keyboardHookCallback_2 = nullptr;


using o_mouseHookCallback = LRESULT(__stdcall*) (int32_t nCode, WPARAM wParam, LPARAM lParam);
o_mouseHookCallback mouseHookCallback = nullptr;

using o_mouseHookCallback_1 = LRESULT(__stdcall*) (int32_t nCode, WPARAM wParam, LPARAM lParam);
o_mouseHookCallback_1 mouseHookCallback_1 = nullptr;

using o_mouseHookCallback_2 = LRESULT(__stdcall*) (int32_t nCode, WPARAM wParam, LPARAM lParam);
o_mouseHookCallback_2 mouseHookCallback_2 = nullptr;


using o_shellHookCallback = LRESULT(__stdcall*) (int32_t nCode, WPARAM wParam, LPARAM lParam);
o_shellHookCallback shellHookCallback = nullptr;


HINSTANCE hinstDll;
HHOOK keyboardHook;
HHOOK mouseHook;
HHOOK shellHook;
int32_t currentSystemKeyDown = 0x0;

uint32_t __stdcall ldbCheckHooksHook()
{
    /*
    * 0x400  -> keyboardHook  Ok
    * 0x1000 -> shellHook     Ok
    * 0x800  -> mouseHook     Ok
    * 0x400 + 0x1000 + 0x800 = 0x1c00 -> All Hooks Ok
    */

    // spoof all hooks are ok
    return 0x1c00;
}

//uint32_t __stdcall ldbManageHooksHook()
//{
//    /*
//    * 0x400  -> keyboardHook  Ok
//    * 0x1000 -> shellHook     Ok
//    * 0x800  -> mouseHook     Ok
//    * 0x400 + 0x1000 + 0x800 = 0x1c00 -> All Hooks Ok
//    */
//
//    // spoof all hooks are ok
//    return 0x1c00;
//}

uint32_t __stdcall keyboardHookCallbackHook(int32_t nCode, WPARAM wParam, LPARAM lParam)
{
    // Mem: 0x100012a0
    /* Original keyboardHookCallback_1 blocks the following from working
    *
    * FOLLOWING KEYBOARD ACTION:
    *       VK_LWIN                 0x5b
    *       VK_RWIN                 0x5c
    *       VK_LWIN+H               0x5b+0x48
    *       VK_MENU+VK_TAB          0x12+0x09
    *       VK_CONTROL+K            0x11+0x4b
    *       VK_CONTROL+VK_ESCAPE    0x11+0x1b
    *       VK_F12                  0x7b
    */

    currentSystemKeyDown = 0x0;
    return CallNextHookEx(keyboardHook, nCode, wParam, lParam);
}

uint32_t __stdcall keyboardHookCallback_1Hook(int32_t nCode, WPARAM wParam, LPARAM lParam)
{
    // Mem: 0x100014a0
    /* Original keyboardHookCallback_1 blocks the following from working
    *
    * FOLLOWING KEYBOARD ACTION:
    *       VK_TAB                  0x09
    *       VK_PRINT                0x2a
    *       VK_SNAPSHOT             0x2c
    *       VK_MENU+VK_ANY          0x12+?
    *       VK_CONTROL+VK_ANY       0x11+?
    *       VK_F1-VK_F24            0x70-0x87
    */

    return CallNextHookEx(keyboardHook, nCode, wParam, lParam);
}

uint32_t __stdcall keyboardHookCallback_2Hook(int32_t nCode, WPARAM wParam, LPARAM lParam)
{
    // Mem: 0x10001580
    /* Original keyboardHookCallback_2 blocks the following from working
    *
    * FOLLOWING KEYBOARD ACTION:
    *       VK_LWIN                 0x5b
    *       VK_RWIN                 0x5c
    *       VK_MENU+VK_TAB          0x12+0x09
    *       VK_MENU+VK_ESCAPE       0x12+0x1b
    *       VK_MENU+VK_F4           0x12+0x73
    *       VK_CONTROL+VK_TAB       0x11+x09
    *       VK_CONTROL+K            0x11+0x4b
    *       VK_CONTROL+VK_ESCAPE    0x11+0x1b
    *       VK_F12                  0x7b
    */

    return CallNextHookEx(keyboardHook, nCode, wParam, lParam);
}

// All 3 are basically the same function just each one builds off of the previous one
// Maybe they did this for some reason idk, kinda stupid ngl
uint32_t __stdcall mouseHookCallbackHook(int32_t nCode, WPARAM wParam, LPARAM lParam)
{
    // Mem: 0x10001650
    /* Original mouseHookCallback blocks the following from working
    *
    * FOLLOWING MOUSE ACTION:
    *       WM_MOUSEWHEEL       0x20b
    *       WM_XBUTTONDOWN      0x20c
    *       WM_XBUTTONUP        0x20d
    *
    *       0xAB-0xAD           0xAB-0xAD
    *       0xA3-0xA6           0xA3-0xA6
    */

    return CallNextHookEx(mouseHook, nCode, wParam, lParam);
}

uint32_t __stdcall mouseHookCallback_1Hook(int32_t nCode, WPARAM wParam, LPARAM lParam)
{
    // Mem: 100016e0
    /* Original mouseHookCallback_1 blocks the following from working
    *
    * FOLLOWING MOUSE ACTION:
    *       WM_MOUSEWHEEL       0x20b
    *       WM_XBUTTONDOWN      0x20c
    *       WM_XBUTTONUP        0x20d
    *
    *       0xAB-0xAD           0xAB-0xAD
    *       0xA3-0xA6           0xA3-0xA6
    *
    * CTRL + FOLLOWING MOUSE ACTION:
    *       WM_LBUTTONDOWN      0x201
    *       WM_LBUTTONUP        0x202
    *       WM_LBUTTONDBLCLK    0x203
    */

    return CallNextHookEx(mouseHook, nCode, wParam, lParam);
}

uint32_t __stdcall mouseHookCallback_2Hook(int32_t nCode, WPARAM wParam, LPARAM lParam)
{
    // Mem: 0x100017b0
    /* Original mouseHookCallback_2 blocks the following from working
    *
    * FOLLOWING MOUSE ACTION:
    *       WM_MOUSEWHEEL       0x20b
    *       WM_XBUTTONDOWN      0x20c
    *       WM_XBUTTONUP        0x20d
    *
    *       WM_RBUTTONDOWN      0x204
    *       WM_RBUTTONUP        0x205
    *       WM_RBUTTONDBLCLK    0x206
    *
    *       0xAB-0xAD           0xAB-0xAD
    *       0xA3-0xA6           0xA3-0xA6
    *
    * CTRL + FOLLOWING MOUSE ACTION:
    *       WM_LBUTTONDOWN      0x201
    *       WM_LBUTTONUP        0x202
    *       WM_LBUTTONDBLCLK    0x203
    */

    return CallNextHookEx(mouseHook, nCode, wParam, lParam);
}


uint32_t __stdcall shellHookCallbackHook(int32_t nCode, WPARAM wParam, LPARAM lParam)
{
    // Mem: 0x100018a0
    /* Original shellHookCallback blocks the following from working
    *
    * FOLLOWING SHELL ACTIONS:
    *       HSHELL_TASKMAN      0x7     Taskmanager
    *       HSHELL_APPCOMMAND   0xc     Multimedia Keys
    */

    return CallNextHookEx(shellHook, nCode, wParam, lParam);
}

void attachHook() {
    /*HMODULE hLDBEXE = GetModuleHandle(NULL);
    HMODULE hLDBDLL = GetModuleHandleA("LockDownBrowser.dll");

    if (!hLDBDLL)
    {
        MessageBoxA(NULL, "Failed to get module handle.", "Error", MB_OK | MB_ICONERROR);
        return;
    }*/

    // Cast the address to the function pointer
    keyboardHookCallback = rebaseDll<o_keyboardHookCallback>(0x100012a0);
    keyboardHookCallback_1 = rebaseDll<o_keyboardHookCallback>(0x100014a0);
    keyboardHookCallback_2 = rebaseDll<o_keyboardHookCallback>(0x10001580);

    mouseHookCallback = rebaseDll<o_mouseHookCallback>(0x10001650);
    mouseHookCallback_1 = rebaseDll<o_mouseHookCallback_1>(100016e0);
    mouseHookCallback_2 = rebaseDll<o_mouseHookCallback_2>(0x100017b0);

    shellHookCallback = rebaseDll<o_shellHookCallback>(0x100018a0);

    // Begin the Detours transaction
    DetourTransactionBegin();
    DetourUpdateThread(GetCurrentThread());

    // Attach the hook
    LONG error_kbh = DetourAttach(&(PVOID&)keyboardHookCallback, keyboardHookCallbackHook);
    LONG error_kbh1 = DetourAttach(&(PVOID&)keyboardHookCallback_1, keyboardHookCallback_1Hook);
    LONG error_kbh2 = DetourAttach(&(PVOID&)keyboardHookCallback_2, keyboardHookCallback_2Hook);

    LONG error_mh = DetourAttach(&(PVOID&)mouseHookCallback, mouseHookCallbackHook);
    LONG error_mh1 = DetourAttach(&(PVOID&)mouseHookCallback_1, mouseHookCallback_1Hook);
    LONG error_mh2 = DetourAttach(&(PVOID&)mouseHookCallback_2, mouseHookCallback_2Hook);

    LONG error_sh = DetourAttach(&(PVOID&)shellHookCallback, shellHookCallbackHook);

    // Commit the transaction
    error_kbh = DetourTransactionCommit();
    error_kbh1 = DetourTransactionCommit();
    error_kbh2 = DetourTransactionCommit();

    error_mh = DetourTransactionCommit();
    error_mh1 = DetourTransactionCommit();
    error_mh2 = DetourTransactionCommit();

    error_sh = DetourTransactionCommit();

    /*if (error != NO_ERROR)
    {
        char errorMsg[256];
        sprintf_s(errorMsg, "DetourAttach failed: %ld", error);
        MessageBoxA(NULL, errorMsg, "Error", MB_OK | MB_ICONERROR);
    }
    else
    {
        MessageBoxA(NULL, "Hook attached successfully.", "Success", MB_OK | MB_ICONINFORMATION);
    }*/
}

BOOL APIENTRY DllMain(HMODULE hModule, DWORD  ul_reason_for_call, LPVOID lpReserved)
{


    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
        hinstDll = rebaseDll<HINSTANCE>(0x10015938);
        keyboardHook = rebaseDll<HHOOK>(0x10017000);
        currentSystemKeyDown = rebaseDll<int32_t>(0x1001593c);

        attachHook();
        break;
    case DLL_PROCESS_DETACH:
        // Detach the hook
        DetourTransactionBegin();
        DetourUpdateThread(GetCurrentThread());

        DetourDetach(&(PVOID&)keyboardHookCallback, keyboardHookCallbackHook);
        DetourDetach(&(PVOID&)keyboardHookCallback_1, keyboardHookCallback_1Hook);
        DetourDetach(&(PVOID&)keyboardHookCallback_2, keyboardHookCallback_2Hook);

        DetourDetach(&(PVOID&)mouseHookCallback, mouseHookCallbackHook);
        DetourDetach(&(PVOID&)mouseHookCallback_1, mouseHookCallback_1Hook);
        DetourDetach(&(PVOID&)mouseHookCallback_2, mouseHookCallback_2Hook);

        DetourDetach(&(PVOID&)shellHookCallback, shellHookCallbackHook);

        DetourTransactionCommit();
        break;
    case DLL_THREAD_ATTACH:
    case DLL_THREAD_DETACH:
        break;
    }
    return TRUE;
}
