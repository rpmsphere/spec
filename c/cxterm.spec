%undefine _debugsource_packages

Summary: Chinese X-term
Name: cxterm
Version: 5.2.4
Release: 6.1
URL: https://cxterm.sourceforge.net
Source: https://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tgz
License: distributable
Group: X11/Utilities/terms
BuildRequires: libXt-devel, libXmu-devel, libXaw-devel

%description
A terminal emulator for X11, just like "xterm", but with the
capability of displaying and inputting Chinese.
It supports GB, Big5, JIS, and KS encoding.

%package big5
Group: X11/Utilities/terms
Summary: big5 Traditional
%description big5
Chinese X-term for Big5

%package gb
Group: X11/Utilities/terms
Summary: GB Simplified
Requires: cxterm
%description gb
Chinese X-term for GB

%package jis
Group: X11/Utilities/terms
Summary: JIS Japanese
Requires: cxterm
%description jis
Japanese X-term for JIS

%package ks
Group: X11/Utilities/terms
Summary: KS Korean
Requires: cxterm
%description ks
Korean X-term for KS

%package fonts
Group: X11/Utilities/terms
Summary: Fonts
%description fonts
Fonts used by cxterm

%prep
%setup -q

%build
CFLAGS="-Wall -O3" ./configure --prefix=/usr --mandir=/usr/share/man
make

%install
rm -fr $RPM_BUILD_ROOT
DESTDIR=$RPM_BUILD_ROOT make install

mkdir -p $RPM_BUILD_ROOT/usr/lib/X11/fonts/chinese
install -c -m 644 fonts/*.gz fonts/font* $RPM_BUILD_ROOT/usr/lib/X11/fonts/chinese

ln -sf cxterm $RPM_BUILD_ROOT%{_bindir}/cxtermgb
ln -sf cxterm $RPM_BUILD_ROOT%{_bindir}/cxtermb5
ln -sf cxterm $RPM_BUILD_ROOT%{_bindir}/cxtermjis
ln -sf cxterm $RPM_BUILD_ROOT%{_bindir}/cxtermks

%clean
rm -fr $RPM_BUILD_ROOT

%files
%doc Doc README* INSTALL-5.2 ChangeLog cxterm.term* emacs
%dir %{_datadir}/cxterm/dict
%config %{_datadir}/cxterm/cxtermrc
%{_bindir}/cit2tit
%{_bindir}/cxterm
%{_bindir}/cxterm.bin
%{_bindir}/hzimctrl
%{_bindir}/tit2cit
%{_datadir}/man/man1/*.1*

%files big5
%{_bindir}/cxtermb5
%{_datadir}/cxterm/dict/big5

%files gb
%{_bindir}/cxtermgb
%{_datadir}/cxterm/dict/gb

%files jis
%{_bindir}/cxtermjis
%{_datadir}/cxterm/dict/jis

%files ks
%{_bindir}/cxtermks
%{_datadir}/cxterm/dict/ks

%files fonts
/usr/lib/X11/fonts/chinese

%changelog
* Fri Jul 03 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 5.2.4
- Rebuilt for Fedora
* Mon May  5 2003 Hin-Tak Leung <htl10@users.sourceforge.net>
- RPMS packaging since a long while
