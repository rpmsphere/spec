%undefine _debugsource_packages

Summary: A free BASIC to C converter for Unix-based systems
Name: bacon
Version: 4.4
Release: 1
License: MIT
Group: Development
Source: http://www.basic-converter.org/stable/%{name}-%{version}.tar.gz
URL: http://www.basic-converter.org
BuildRequires: gtk3-devel
Requires: enscript

%description
BaCon intends to be a programming aid in creating tools which can be compiled
on different platforms (including 64bit environments). It tries to revive the
days of the good old BASIC. Code converted by BaCon can be compiled by GCC,
the Compaq C Compiler, TCC or the clang/LLVM compiler.

%prep
%setup -q

%build
./configure --prefix=/usr
make

%install
%make_install

%files
%doc README.1ST doc-pak/CHANGES doc-pak/copyright
%{_bindir}/%{name}
%{_bindir}/%{name}gui-gtk
%{_bindir}/%{name}.sh
%{_datadir}/applications/%{name}gui-gtk.desktop
%{_datadir}/enscript/hl/%{name}.st
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/pixmaps/BaCon*
%{_datadir}/BaCon
%{_datadir}/icons/hicolor/scalable/apps/bacon.png

%changelog
* Sun May 8 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 4.4
- Rebuilt for Fedora
* Fri Jun 01 2018 Peter van Eerten <peter@basic-converter.org>
- Initial package
