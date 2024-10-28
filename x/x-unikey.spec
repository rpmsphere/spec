%undefine _debugsource_packages
%define gtkim /usr/lib/gtk-2.0/2.10.0/immodules
%define gtkim3 /etc/gtk-2.0/i386-redhat-linux-gnu/gtk.immodules
%define gtkim6 /etc/gtk-2.0/i686-redhat-linux-gnu/gtk.immodules

##%define gtketc /etc/gtk-2.0/%{_host}
##%define gtkimfile %{mygtketc}/gtk.immodules
##%define gtkimfilebak %{mygtketc}/gtk.immodules_BAK
%define gtkquerycmd /usr/bin/gtk-query-immodules-2.0-32

Summary: x-unikey - Unikey Input Method for X-Window
Name: x-unikey
Version: 1.0.4
Release: 1
Epoch : 1
License: GPL
Group: System/Internationalization
URL: https://unikey.sourceforge.net
Source0: %{name}-%{version}.tar.bz2
Source1: x-unikey-install.sh
Requires: gtk2 > 2.0

%description
This package contains following components:
- ukxim: Unikey XIM (X Input Method) server
- unikey: GUI for ukxim and unikey-gtk
- unikey-gtk: GTK vietnamese input method module

%prep
%setup -q
sed -i '290s/char/const char/' src/ukengine/mactab.cpp
sed -i '1i #include <cstdio>\n#include <cstring>' src/ukengine/usrkeymap.cpp

%build
cp /usr/share/automake-*/config.guess .
export CFLAGS="$RPM_OPT_FLAGS -Wno-narrowing"
export CXXFLAGS="$RPM_OPT_FLAGS -Wno-narrowing"
./configure --with-unikey-gtk
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{gtkim}

install -m 755 src/xim/ukxim $RPM_BUILD_ROOT%{_bindir}/
install -m 755 src/gui/unikey $RPM_BUILD_ROOT%{_bindir}/
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}-install
install -m 755 src/unikey-gtk/.libs/im-vn.so $RPM_BUILD_ROOT%{gtkim}

strip $RPM_BUILD_ROOT%{_bindir}/{unikey,ukxim}
strip $RPM_BUILD_ROOT%{gtkim}/*.so
find . -name CVS | xargs rm -rf

%post
if [ -e %{gtkim3} ];then
        %{gtkquerycmd} > %{gtkim3}
fi
if [ -e %{gtkim6} ];then
        %{gtkquerycmd} > %{gtkim6}
fi

%postun
if [ -e %{gtkim3} ];then
        %{gtkquerycmd} > %{gtkim3}
fi
if [ -e %{gtkim6} ];then
        %{gtkquerycmd} > %{gtkim6}
fi

%files
%doc AUTHORS ChangeLog README* INSTALL COPYING CREDITS NEWS 
%doc doc/*
%{_bindir}/ukxim
%{_bindir}/unikey
%{_bindir}/x-unikey-install
%{gtkim}/im-vn.so

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.4
- Rebuilt for Fedora
* Sat Jun  9 2007 Nguyen-Dai Quy <vnpenguin@vnoss.org>
- 1st builf for F7
* Sat Jan 20 2007 Nguyen-Dai Quy <vnpenguin@vnoss.org>
- fixed some var in spec
* Sat Oct 21 2006 Nguyen-Dai Quy <vnpenguin@vnoss.org>
- Build for FC-One (FC6 based)
* Sat Apr 15 2006 Nguyen-Dai Quy <vnpenguin @ gmail.com>
- add x-unikey-install.sh script
* Fri Apr 14 2006 Nguyen-Dai Quy <vnpenguin @ gmail.com>
- update to 1.0.4
* Mon Mar 20 2006 Nguyen-Dai Quy <vnpenguin @ gmail.com>
- build for FC5
* Thu Dec  1 2005 Nguyen-Dai Quy <vnpenguin @ gmail.com>
- update to 1.0.3b
* Sun Oct  2 2005 Nguyen-Dai Quy <vnpenguin @ gmail.com>
- update to 1.0.3
* Sun Aug 14 2005 Nguyen-Dai Quy <vnpenguin @ gmail.com>
- update to 1.0.2b
* Sun Aug  7 2005 Nguyen-Dai Quy <vnpenguin @ gmail.com>
- update to 1.0.2
* Sun Jul 24 2005 Nguyen-Dai Quy <vnpenguin @ gmail.com>
- update to 1.0.1
* Sat Jul 16 2005 Nguyen-Dai Quy <vnpenguin @ gmail.com>
- update to 1.0
* Sun Jun 19 2005 Nguyen-Dai Quy <vnpenguin @ gmail.com>
- build for FC4
* Sat Nov 13 2004 Nguyen-Dai Quy <NguyenDaiQuy@yahoo.com>
- build for FC3
- disable shortcuts in telex mode
* Tue Aug  3 2004 Nguyen-Dai Quy <NguyenDaiQuy@yahoo.com>
- update to 0.9.2
* Mon Apr 12 2004 Nguyen-Dai Quy <NguyenDaiQuy@yahoo.com>
- update to 0.9.1d
* Thu Apr  1 2004 Nguyen-Dai Quy <NguyenDaiQuy@yahoo.com>
- build for FC2-test2
* Wed Mar 17 2004 Nguyen-Dai Quy <NguyenDaiQuy@yahoo.com>
- update to 0.9.1c
* Fri Feb  6 2004 Nguyen-Dai Quy <NguyenDaiQuy@yahoo.com>
- update for 0.9.1b
* Tue Feb  3 2004 Nguyen-Dai Quy <NguyenDaiQuy@yahoo.com>
- update for 0.9.1
- add %%postun
 * Fri Jan 30 2004 Nguyen-Dai Quy <NguyenDaiQuy@yahoo.com>
- first build for version 0.9
