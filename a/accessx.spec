%undefine _debugsource_packages

Name:           accessx
Version:        0.951
Release:        7.1
Summary:        Open source utility to set and display all of the XKEYBOARD

Group:          User Interface/X
License:        GPLv2+
URL:            https://cita.disability.uiuc.edu/software/accessx/freewareaccessx.php
Source0:        https://cita.disability.uiuc.edu/software/accessx/files/%{name}0951.tar.gz

#The makefile is totally hadwriten, we had to make sure that it is sane.
#A mail with the patches sent to the upstream
Patch0:         accessx-make_fix.patch
Patch1:         accessx-header_fix.patch

#Buildfix for  F14
Patch2:         accessx-buildfix.patch
BuildRequires:  gcc-c++, libX11-devel, libXext-devel
Requires:       tk

%description
An open source utility to set and display all of the XKEYBOARD 
(XKB) AccessX features. It is designed to mimic the interface 
provided by the Sun and DEC "accessx" tool.

%prep
%setup -q -n accessx
%patch 0 -p1
%patch 1 -p1
%patch 2 -p1

%build
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT 

%files
%{_bindir}/ax
%{_bindir}/accessx
%doc README

%changelog
* Thu Feb 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.951
- Rebuilt for Fedora

* Sun May 30 2010 Kushal Das <kushal@fedoraproject.org> 0.951-2
- fixed changelog section

* Sat May 29 2010 Kushal Das <kushal@fedoraproject.org> 0.951-1
- Initial packaging
