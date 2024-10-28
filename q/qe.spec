Summary: A PE2 alike editor
Name: qe
Version: 0.2.0
Release: 6.1
License: GPL
Group: Applications/Editors
Source: https://ftp.de.debian.org/debian/pool/main/q/qe/%{name}_%{version}.orig.tar.gz
Patch0: https://ftp.de.debian.org/debian/pool/main/q/qe/%{name}_%{version}-4.diff.gz
URL: https://www.cc.ncu.edu.tw/~center5/product/qe/
BuildRequires: gcc-c++, ncurses

%description
Qe is a PE2-like editor for U*nix (Linux/BSD/Solaris... etc),
I name it Qe for the reason that P is followed by Q, hope it
can exceed PE2 :) and useful for people who need a full-screen,
macro capable editor.

%prep
%setup -q
%patch 0 -p1
sed -i 's/color_xterm/xterm-color/' src/main.cc
sed -i '/basename/d' src/misc.h
#msgconv -t UTF-8 -o src/po/zh_TW.UTF-8.po src/po/zh_TW.po
#mv -f src/po/zh_TW.UTF-8.po src/po/zh_TW.po
rm -f src/po/zh_CN.GB2312.po src/po/zh_TW.Big5.po

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall rootdir=$RPM_BUILD_ROOT

%files
%doc COPYING README
%{_bindir}/*
%{_datadir}/qe
%{_datadir}/locale/*/LC_MESSAGES/qe.mo

%changelog
* Mon Apr 25 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.0
- Rebuilt for Fedora

* Mon Apr 23 2001 Jiann-Ching Liu <center5@cc.ncu.edu.tw>
- Fix problem under Redhat Linux 7.x
- Include GNU-style auto configuration feature
