Name:		xwit
Version:	3.4
Release:	4.1
Summary:	Collection of simple routines to call some X11 functions
Source:		ftp://ftp.x.org/contrib/utilities/xwit-%{version}.tar.gz
Patch1:		https://ftp.de.debian.org/debian/pool/main/x/xwit/xwit_3.4-10.diff.gz
Patch2:		xwit-lib_order.patch
Group:		System/X11/Utilities
License:	BSD (revised), Public Domain, MIT/X
BuildRequires:	libX11-devel
BuildRequires:	gcc make glibc-devel

%description
xwit allows to call some X11 functions from the command line or a shell
script.

xwit will resize, iconify, pop, and move windows given by name or id, change
an icon, title or name, set the screen saver going, and change individual key
autorepeat settings, move the mouse cursor, etc.




Authors:
--------
    Mark M Martin <mmm@cetia.fr>
    David DiGiacomo, david@slack.com
    Dima Barsky <dima@debian.org>
    Michael Mauch <michael.mauch@gmx.de>
    Decklin Foster <decklin@red-bean.com>
    Bernhard R. Link <brlink@debian.org>

%prep
%setup -q
%patch1 -p1
%patch2

%build
%__make %{?jobs:-j%{jobs}} CFLAGS="%{optflags}"

%install
%__rm -rf "$RPM_BUILD_ROOT"
%__install -D -m0755 xwit "$RPM_BUILD_ROOT%{_bindir}/xwit"
%__install -D -m0644 xwit.man "$RPM_BUILD_ROOT%{_mandir}/man1/xwit.1"

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%doc README
%{_bindir}/xwit
%doc %{_mandir}/man1/xwit.1*

%changelog
* Mon Sep 26 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 3.4
- Rebuilt for Fedora

* Thu May  1 2008 Pascal Bleser <guru@unixtech.be> 3.4
- new package
