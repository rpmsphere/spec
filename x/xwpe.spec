Summary: X Window Programming Environment
Name: xwpe
Version: 1.5.30a
Release: 19.1
License: GPL
URL: http://www.identicalsoftware.com/xwpe
Group: Development/Tools
Source0: http://www.identicalsoftware.com/xwpe/xwpe-%{version}.tar.gz
Source1: xwpe-t.xpm
BuildRequires: ncurses-devel
BuildRequires: gpm-devel
BuildRequires: libX11-devel
BuildRequires: libXt-devel
BuildRequires: xorg-x11-proto-devel
BuildRequires: desktop-file-utils
BuildRequires: cups

%description
XWPE is actually a package of four programs: we, wpe, xwe, and xwpe.
They are different versions of the same basic programmers editor and
development environment. If you have used some of the Microsoft
Windows programming IDE's and longed for an X Window equivalent, this
is what you have been looking for! Also included are the text-mode
equivalents of the X programs, enabling you to use xwpe no matter what
your development environment may be.

%prep
%setup -q
#sed -i '7,10d' unixmakr.h

%build
#patch -p1 < xwpe-conf.patch
#autoconf
./configure --prefix=/usr --mandir=%{_mandir} --with-x
make 

%install
mkdir -p $RPM_BUILD_ROOT/usr
make prefix=$RPM_BUILD_ROOT/usr MANDIR=$RPM_BUILD_ROOT%{_mandir} install
desktop-file-install --vendor="" --dir=%{buildroot}%{_datadir}/applications xwpe.desktop
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/xwpe-t.xpm
echo 'Icon=xwpe-t.xpm' >> %{buildroot}%{_datadir}/applications/xwpe.desktop

%files
%doc README CHANGELOG
/usr/bin/we
/usr/bin/wpe
/usr/lib/xwpe/help.key
/usr/lib/xwpe/help.xwpe
/usr/lib/xwpe/syntax_def
#/usr/lib/xwpe/libxwpe-term.so
%{_mandir}/man1/wpe.1*
%{_mandir}/man1/we.1*
%{_mandir}/man1/xwpe.1*
%{_mandir}/man1/xwe.1*
/usr/bin/xwe
/usr/bin/xwpe
#/usr/lib/xwpe/libxwpe-x11.so
%{_datadir}/applications/xwpe.desktop
%{_datadir}/pixmaps/xwpe-t.xpm

%changelog
* Fri Feb 07 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5.30a
- Rebuild for Fedora
