Name:           uif2iso
Version:        0.1.4
Release:        7.1
License:        GPL
BuildRequires:  cmake zlib-devel openssl-devel
Group:          System/Utilities
Summary:        Tool for converting the UIF files to ISO
Source0:	uif2iso.c
Source1:	CMakeLists.txt

%description
Tool for converting the UIF files (Universal Image Format, used by MagicISO) to ISO.

%prep
cp %{SOURCE0} .
cp %{SOURCE1} .
cat /etc/fstab

%build
%cmake
make

%install
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%{_bindir}/%{name}

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.4
- Rebuild for Fedora
* Mon Sep  7 2009 crrodriguez@suse.de
- fix build
* Tue Dec 25 2007 crrodriguez@suse.de
- initial version
