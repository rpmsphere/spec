Name:           scrcpy
Version:        1.22
Release:        1
Summary:        Display and control your Android device
License:        Apache-2.0
Group:          Hardware/Mobile
URL:            https://github.com/Genymobile/scrcpy
Source0:        %{name}-%{version}.tar.gz
Source1:        https://github.com/Genymobile/scrcpy/releases/download/v1.4/scrcpy-server-v1.4.jar
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:	pkgconfig(sdl2)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)

%description
This application provides display and control of Android devices connected
on USB. It does not require any root access

%prep
%setup -q

%build
%meson -Dprebuilt_server=%{SOURCE1}
%meson_build

%install
%meson_install

%files
%doc README.md DEVELOP.md FAQ.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.*
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

%changelog
* Sun Mar 20 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.22
- Rebuilt for Fedora
* Tue Nov 13 2018 pousaduarte@gmail.com
- Update to version 1.5fixversion~git20181113:
  * Move drag&drop features in README
* Mon Nov 12 2018 pousaduarte@gmail.com
- Update to version 1.5fixversion~git20181112:
  * Fix read_packet() return value on error or EOF
  * Configure version at meson project level
  * Update links to v1.5-fixversion
  * Bump version to 1.5
  * Update links to v1.5 in README and BUILD
  * Improve features presentation in README
  * Do not queue invalid PTS
  * Store queue of PTS for pending frames
  * Send frame meta only if recording is enabled
  * Rename --output-file to --record
  * Wrap receiver state into separate struct
  * Avoid partial header reads
  * Move buffer reader functions to buffer_util.h
  * Support AVStream.codec for old FFmpeg versions
  * recorder: use av_oformat_next to support older FFmpeg
  * Reenable custom SDL signal handlers
  * Do not transmit MediaCodec flags
  * Assign PTS to the right frame
  * Decode and push frame before recording
  * Only set valid PTS/DTS
  * Add recorder
  * Enable video output file, with pts set by server
  * Fix SDL 2.0.9 for Windows
  * Update SDL (2.0.9) for Windows
* Sun Nov 11 2018 pousaduarte@gmail.com
- Update to version 1.4~git20181111:
  * Extract bit operations to buffer_util.h
  * Explain how to install up-to-date meson
* Sat Nov 10 2018 pousaduarte@gmail.com
- Update to version 1.4~git20181110:
  * Add feature test macro to declare kill()
  * Fix memory leak on error
* Thu Nov  1 2018 pousaduarte@gmail.com
- Update to version 1.4~git20181101:
  * Replace Ctrl by Meta for volume shortcuts on MacOS
  * Refactor to support Meta in shortcuts
* Tue Oct 30 2018 pousaduarte@gmail.com
- Update to version 1.4~git20181027:
  * input_manager: fix potential memory leak on text
* Thu Oct 25 2018 pousaduarte@gmail.com
- Update to version 1.4~git20181024:
  * Capture Alt and Meta keys
* Mon Oct 22 2018 pousaduarte@gmail.com
- Update to version 1.4~git20181021:
  * Factorize Windows command building
* Wed Oct 10 2018 pousaduarte@gmail.com
- Update to version 1.4~git20181009:
  * Work around Os.write() not updating position
* Fri Oct  5 2018 pousaduarte@gmail.com
- Update to version 1.4~git20181004:
  * Support paths containing spaces on Windows
  * Declare fun(void) functions with no parameters
  * Update links to v1.4 in README and BUILD
  * Update platform-tools (28.0.1) for Windows
  * Bump version to 1.4
  * Handle alpha and space chars as raw events
  * prevent closing console right after process error in windows
  * Fix header guard name
  * Use specific error for missing binary on Windows
  * Avoid additional buffer copy in userspace
  * Present fullscreen option in README
  * Add option to start in fullscreen
  * Do not handle system-specific values in command.c
  * Notify adb missing
  * Update FFmpeg (4.0.2) for Windows
  * Update platform-tools (28.0.0) for Windows
  * Add missing include for lock_util.h
  * Separate multi-words filenames by '_'
  * Document "push file" feature
  * Make request_queue functions static
  * Simplify SDL_assert() calls
  * Add missing include config.h
  * Support drag&drop a file to transfer it to device
  * installer -> file_handler
* Thu Sep 20 2018 pousaduarte@gmail.com
- Update to version 1.3~git20180919:
  * Add link to Gentoo Ebuild in README
* Tue Aug 21 2018 pousaduarte@gmail.com
- Update to version 1.3~git20180820:
  * Add link to FLAG_SECURE in FAQ
* Fri Aug 17 2018 pousaduarte@gmail.com
- Update to version 1.3~git20180817:
  * Explain how to install adb on Mac OS
  * Separate build instructions from README
* Thu Aug 16 2018 pousaduarte@gmail.com
- Update to version 1.3~git20180815:
  * Reset current installer process
  * Return non-zero value on connection loss
  * Remove AINPUT_SOURCE_ANY value
  * Replace Uint32 by int to fix warnings in tinyxpm
  * Explicitly use ISO C11
* Sun Aug 12 2018 pousaduarte@gmail.com
- Update to version 1.3~git20180812:
  * Destroy mutex if strdup failed
  * remove redundant semicolon
* Fri Aug 10 2018 pousaduarte@gmail.com
- Update to version 1.3~git20180809:
  * Update links to v1.3 in README
  * Bump version to 1.3
  * Add crop feature
  * Move annotation comment
  * Extract video size computation
  * Increase "adb forward" connection attempts
  * Do not call deprecated av_register_all()
* Tue Jul 17 2018 pousaduarte@gmail.com
- Update to version 1.2~git20180716:
  * Simplify README for Windows users
* Mon Jun 25 2018 pousaduarte@gmail.com
- Update to version 1.2~git20180624:
  * Forward repeated volume events
  * Send separate DOWN/UP key events
  * Improve English comment
* Sat Jun 23 2018 pousaduarte@gmail.com
- Update to version 1.2~git20180622:
  * Prevent killing unexpected process
  * Fix missing installer initialization
* Fri Jun  8 2018 pousaduarte@gmail.com
- Update to version 1.2~git20180608:
  * Fix meson error: ‘for’ loop initial declarations are only allowed in C99 mode.
  * Use a meson option to crossbuild for Windows
  * Fix clean recipe in cross Makefile
  * Upgrade gradle
* Tue May 29 2018 pousaduarte@gmail.com
- Update to version 1.2~git20180528:
  * Update links to v1.2 in README
  * Bump version to 1.2
  * Rename SHA256SUM to SHA256SUMS
  * Make CreateProcess() flags depend on "noconsole"
  * Update README and FAQ for the new Windows releases
  * Also build "noconsole" binary for Windows
  * Add cross-compilation scripts for Windows
  * Indicate that libs are included for Windows
  * Indicate that scrcpy also works over TCP/IP
  * Document APK drag & drop
  * Quote apk path on Windows
  * Drag and drop to install apk files from computer
  * Fix net_send_all() warning
  * Fix proc_show_touches warning
  * Release controller lock while processing events
  * Fix leak on server start error
  * Add missing includes
  * Change volume shortcuts
  * Improve startup time when show_touches is enabled
  * Disable "show touches" once window is closed
  * Add an option to enable "show touches"
  * Group scrcpy options into a struct
  * Swap MENU and APP_SWITCH shortcuts
  * Rename "shake" to "menu"
  * Add support for CTRL+S to send hardware "shake" to device w/readme
* Tue Apr 10 2018 pousaduarte@gmail.com
- Update to version 1.1~git20180408:
  * Map numpad ENTER key
* Thu Apr  5 2018 pousaduarte@gmail.com
- Update to version 1.1~git20180405:
  * Add FAQ section about KWin crash
* Wed Apr  4 2018 pousaduarte@gmail.com
- Update to version 1.1~git20180404:
  * Avoid pointer arithmetic on "void *"
  * Use const pointers when possible
* Sat Mar 31 2018 pousaduarte@gmail.com
- Update to version 1.1~git20180331:
  * Document 32 bits packages Windows in README
* Thu Mar 29 2018 pousaduarte@gmail.com
- Update to version 1.1~git20180328:
  * Make checkstyle happy
  * Install on macOS via Homebrew in README
* Wed Mar 28 2018 pousaduarte@gmail.com
- Update to version 1.1~git20180328:
  * Document how to make a portable build on Windows
* Tue Mar 27 2018 pousaduarte@gmail.com
- Update to version 1.1~git20180327:
  * Factorize texture creation
* Mon Mar 26 2018 pousaduarte@gmail.com
- Update to version 1.1~git20180326:
  * Forward double-click events
* Sun Mar 25 2018 pousaduarte@gmail.com
- Update to version 1.1~git20180325:
  * Add instructions to install Java 8 on macOS
  * Update README.md
  * Add instructions to run via Docker
* Sat Mar 24 2018 pousaduarte@gmail.com
- Update to version 1.1~git20180324:
  * Change links to wikipedia
  * Add links to FFmpeg and LibSDL2 dependencies
  * Process the last video frame
  * Unref last packet on exit
  * Clarify adb requirements
  * Describe workaround to get output on Windows
* Wed Mar 21 2018 opensuse-packaging@opensuse.org
- Update to version 1.1~git20180321:
  * Disable custom SDL signal handlers
  * Remove useless blocks in switch/case
* Wed Mar 21 2018 opensuse-packaging@opensuse.org
- Update to version 1.1~git20180320:
  * Include source root directory
* Sun Mar 18 2018 pousaduarte@gmail.com
- Update to version 1.1~git20180318:
  * Document the step to clone the project
  * Increase the number of connection attempts
  * Fix win32 build
  * Remove useless cast
  * Fix warning message
  * Fix switch/case code style
* Thu Mar 15 2018 pousaduarte@gmail.com
- Update to version 1.1~git20180315:
  * Add FAQ section about mouse clicks
* Wed Mar 14 2018 pousaduarte@gmail.com
- Update to version 1.1~git20180314:
  * Add link to the article for v1.1 in README
  * Update FAQ after v1.1 release
  * Update links to v1.1 in README
  * Bump version to 1.1
  * Remove useless argument
  * Immediately close the server socket on the device
  * Workaround continuous resizing on Windows/MacOS
  * Remove black borders on double-click
  * Make it work over tcpip
  * Store serial in server instance
  * Always use the best render scale quality available
  * Fix mouse clicks on LG devices
  * Support screens with dimensions not divisible by 8
  * Map middle-click to HOME
  * Map right-click to BACK if screen is on
  * Fix text input event segfault
* Tue Mar 13 2018 pousaduarte@gmail.com
- Update to version 1.0~git20180313:
  * Disable stdout/stderr buffering on Windows
* Mon Mar 12 2018 pousaduarte@gmail.com
- Update to version 1.0~git20180312:
  * Add links to AUR packages in README
  * Reverse horizontal scrolling behavior
  * Use one subsection by distribution in README
  * Document how to install on Fedora
  * Improve dependencies in README
  * Add a FAQ for common issues
  * Add empty lines around code blocks
  * removed "$" and changed Mac OS ---> MacOS
  * added "$" in front of terminal commands
  * Unref the packet on error
