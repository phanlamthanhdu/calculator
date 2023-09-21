#include <windows.h>
#pragma once

LRESULT CALLBACK WindowProc(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);

class window {
    private:
        HINSTANCE m_hInstance;
        HWND m_hWnd;


    public:
        window();
        window(const window&) = delete;
        window operator =(const window&) = delete;
        ~window();

        bool ProcessMessages();
};