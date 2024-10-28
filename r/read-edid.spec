Summary:        Get monitor details
Name:           read-edid
Version:        3.0.2
Release:        1
URL:            https://www.polypux.org/projects/read-edid/
Source0:        https://www.polypux.org/projects/read-edid/%{name}-%{version}.tar.gz
License:        GPLv2
Group:          System/Configuration/Other
BuildRequires:  libx86-devel
BuildRequires:  cmake

%description
This package will try to read the monitor details directly from the
monitor. The program get-edid asks a VBE BIOS for the EDID data. The
program parse-edid parses the data and prints out a human readable
summary.

%prep
%setup -q
cp LICENSE COPYING

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%cmake
%cmake_build

%install
%cmake_install

%files
%{_docdir}/%{name}/*
%{_mandir}/man1/get-edid.1.*
%{_bindir}/*-edid*

%changelog
* Sun Apr 9 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0.2
- Rebuilt for Fedora
* Mon Apr 28 2014 Denis Silakov <denis.silakov@rosalab.ru> 3.0.1-1
+ Revision: b7fc005
- Drop unneeded patches
