%define		pkgname	SASM

Name:		sasm
Version:	3.10.1
Release:	1
Summary:	IDE for assembly languages
URL:		http://dman95.github.io/SASM/
License:	GPLv3
Source0:	%{pkgname}-%{version}.tar.gz
Group:		Development/Other
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	nasm
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xcb-render)
BuildRequires:	pkgconfig(xcb-icccm)
Requires:	fasm
Requires:	nasm
Requires:	gdb

%description
SASM - simple crossplatform IDE for NASM, MASM, GAS
and FASM assembly languages

%prep
%setup -qn %{pkgname}-%{version}

%build
%qmake_qt5 PREFIX=%{buildroot}/usr
%make_build

%install
%make_install
install -d %{buildroot}%{_docdir}/%{name}
install -m644 README* COPYING* %{buildroot}%{_docdir}/%{name}

%files
%{_docdir}/%{name}
%{_bindir}/%{name}
%exclude %{_bindir}/fasm
%exclude %{_bindir}/listing
%{_datadir}/applications/sasm.desktop
%{_datadir}/%{name}/NASM/macro.c
%{_datadir}/%{name}/Projects/*
%{_datadir}/%{name}/keys.ini
%{_datadir}/%{name}/%{name}.png
%{_datadir}/%{name}/include/io.inc
%{_datadir}/%{name}/include/io64.inc

%changelog
* Thu Sep 05 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 3.10.1
- Rebuilt for Fedora
* Wed Jul 11 2018 User <user@mail.net> 3.9.0-1
- (06ec9cf) Update deps


