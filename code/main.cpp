#include <bits/stdc++.h>
#include "window.cpp"

using namespace std;

int main() {
    cout << "Creating Window\n";
    window* pWindow = new window;
    bool running = true;

    while(running){
        if(!pWindow -> ProcessMessages()){
            cout << "Closing Window\n";
            running = false;
        }
        Sleep(10);
    }
    delete pWindow;
    
    return 0;
}