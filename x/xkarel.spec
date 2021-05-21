%undefine _debugsource_packages

Summary: Programming language Karel
Name: xkarel
Version: 2.1.0b1
Release: 30.1
Source: %{name}-%{version}.tar.gz
License: GPL
Group: Games/Other
URL: http://xkarel.sourceforge.net
BuildRequires: gcc-c++ fltk-fluid
BuildRequires: libXinerama-devel libpng-devel libjpeg-devel mesa-libGL-devel mesa-libGLU-devel

%description
Program xKarel can occur as a game or as a simple programming language.
xKarel is definitely great tool how to learn structure programming
especially for children. Creating new procedures force user to 
algorithmization of the problem and to split the problem to the smaller parts.

Program Karel was very popular in the time of 8-bits computers.

%prep
%setup -q
sed -i 's|-Wall|-Wall -fpermissive|' makeinclude.x
sed -i 's|/usr/local|/usr|' makeinclude.x
sed -i '1i #include <cstring>' src/Katalog.h
sed -i 's|return is;|return bool(is);|' src/AtributyKRL.cpp
sed -i 's|fstream.h|fstream|' src/Katalog.cpp
sed -i 's|character(|char_at(|' src/Editorc.cxx
sed -i 's|"FL/Fl_File_Chooser.h"|<FL/Fl_File_Chooser.h>|' src/KatalogUIc.cxx

%build
make INSTALL_DIRECTORY=/usr

%install
rm -f -r $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/lib/menu
mkdir -p $RPM_BUILD_ROOT/usr/share/pixmaps
make INSTALL_DIRECTORY=$RPM_BUILD_ROOT/usr install

%files
%attr(0775,root,root) %{_bindir}/xkarel
%{_datadir}/doc/xkarel-*
%{_datadir}/xkarel
%{_datadir}/locale/*/LC_MESSAGES/*
/usr/lib/menu
%{_datadir}/pixmaps/*

%clean
rm -fr $RPM_BUILD_ROOT

%changelog
* Thu Mar 15 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.0b1
- Rebuilt for Fedora
* Tue Dec 16 2003 Petr Abrahamczik <pabro@users.sourceforge.net> & Radim Dostal <radimdostal@users.sourceforge.net>
- Initial package
