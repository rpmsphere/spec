Name: vyqchat
Version: 0.2.9test
Release: 31.4
Summary: A real-time, text-based, serverless chat program dedicated to LANs
License: GPL
Group: Networking/Chat
URL: http://freecode.com/projects/vyqchat
Source: %name-%version.tar.gz
Source1: %name.desktop
Source2: %name.xpm
Patch1: %name-0.2.9-acinclude.patch
Patch2: %name-0.2.8-Makefile.patch
Requires: sound_handler
BuildRequires: fontconfig freetype-devel gcc-c++ glib2-devel
BuildRequires: libao-devel qt3-devel
BuildRequires: libsndfile-devel openssl-devel libstdc++-devel
BuildRequires: pkgconfig libX11-devel

%description
VyQChat runs on Linux using Qt/X11 library. It is almost 100%%
compatible with Vypress Chat(TM) for Windows. It allows you to chat with
friends on public or private channels, send and recieve messages etc.
The GUI is meant to be user-friendly and lets you to do most things with
mouse. There is also optional sound support.

%prep
%setup -q -n %{name}-0.2.9
%patch1 -p0
%patch2 -p0
sed -i '77,81d' configure.in
sed -i -e 's|@QT_CXXFLAGS@|-I%{_libdir}/qt-3.3/include -DQT_THREAD_SUPPORT|' -e 's|@QT_DIR@|%{_libdir}/qt-3.3|' -e 's|@QT_LIBS@|-L%{_libdir}/qt-3.3/lib -lqt-mt -lSM -lICE  -lX11 -lXext -lXt|' -e 's|@QT_MOC@|%{_libdir}/qt-3.3/bin/moc|' -e 's|@QT_UIC@|%{_libdir}/qt-3.3/bin/uic|' Makefile.in */Makefile.in */*/Makefile.in

%build
autoconf
./configure --with-arts --with-libao --with-Qt-dir=%{_libdir}/qt-3.3
make

%install
%makeinstall
%__install -pD -m644 %SOURCE1 %buildroot%_datadir/applications/%name.desktop
%__install -pD -m644 %SOURCE2 %buildroot%_datadir/pixmaps/%name.xpm

%files
%doc AUTHORS ChangeLog NEWS README THANKS TODO FAQ README-KEYS
%_bindir/%name
%_datadir/%name
%_datadir/pixmaps/%name.xpm
%_datadir/applications/%name.desktop

%changelog
* Sun Jun 02 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.9
- Rebuilt for Fedora
* Thu May 18 2006 Eugene V. Horohorin <genix@altlinux.ru> 0.2.9-alt0.1
- new (test) version 0.2.9test
- gcc4.1 compatible
- acinclude.m4 patch updated
* Fri Apr 28 2006 Eugene V. Horohorin <genix@altlinux.ru> 0.2.8-alt3
- fixes required for ld --as-needed:
  + Makefile.am patch
  + acinclude.m4 patch
- #8577 fix (new URL)
- #8646 fix
- #9162 fix (x86_64 support)
* Sat Dec 17 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.2.8-alt2
- add patch hotkey
* Wed Jul 27 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.2.8-alt1
- 0.2.8
* Sat Jan 08 2005 Andrey Semenov <mitrofan@altlinux.ru> 0.2.7-alt1
- 0.2.7
* Sat Jun 5 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.2.6-alt4
- fixed confirm exit bug
* Sun May 30 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.2.6-alt3
- rebuild with libao
- small bugs fixed, thanks to Eugene V. Horohorin
* Wed May 26 2004 Eugene V. Horohorin <genix@altlinux.ru> 0.2.6-alt2
- arts-server support added
- soundwrapper'ed playing sound
* Tue May 4 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.2.6-alt1
- 0.2.6
- fixed small bug with recieving messages
- added history window (Edit->Commands history)
- added Save option for channel context menu
- UTF-8 character encoding support
* Mon Jan 12 2004 Andrey Semenov <mitrofan@altlinux.ru> 0.2.5-alt1
- 0.2.5
- fixed small bug with packet id (thanks to Mindaugas Janu鈴itis for pointing it)
- "leave" option in channel menu works for private channels now, too
- added nick box for easy nick change
- added history for chat line
- added .def file for buildpkg package system
- small cleanups and improvements in settings handling
* Sun Dec 28 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.2.4-alt1
- 0.2.4
- new option, "character encoding"
- added context menu with "leave" action for channels
- keyboard shortcuts for "Send" buttons
- small code cleanups
- improved Makefile.am to handle 'make dist' correctly
* Fri Dec 19 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.2.3-alt1
- 0.2.3
- added slider for chat window and users list
- fixed configure script to fail when Qt is not installed
* Mon Nov 17 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.2.2-alt1
- 0.2.2
- ability to show/hide toolbar and users list added (new menu option: "View")
- tabs have now different icons to indicate activity on channels
- fixed bug with "#" not appended to channels list in user info
- minor code cleanups in settings handling code
- updated bnv_have_qt configure macro (v1.3)
* Wed Nov 12 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.2.1-alt1
- 0.2.1
- improved protocol compatibility
- "Chat" button in received message window
- new action, "Say nick:" in user list context menu
- support for Mass Messages
- icons for "Message" and "Mass Message" actions
* Sun Oct 26 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.1.2-alt1
- 0.1.2
- fixed bug that caused crash when changing the nick
- fixed bug with wrong nick in message ack
- support for character encodings other than ISO-8859-1
- new, better settings dialog; sounds can be set now
- added an option to use external command for playing sounds
* Mon Oct 6 2003 Andrey Semenov <mitrofan@altlinux.ru> 0.1.1-alt1
- First version of RPM package
