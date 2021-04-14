%undefine _debugsource_packages

Name:          input-utils
Version:       1.2
Release:       4.1
Summary:       Utilities for the input layer of the Linux kernel
Group:         System/Kernel and Hardware
URL:           https://www.kraxel.org/releases/input/
Source:        https://www.kraxel.org/releases/input/input-%{version}.tar.gz
License:       GPLv2

%description
This is a collection of utilities which are useful when working with the
input layer of the Linux kernel (version 2.6 and later). Included are
utilities to list the input devices known to the kernel, show the input
events that are received by a device, and query or modify keyboard maps.

%prep
%setup -q -n input-%{version}

%build
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/input-events
%{_bindir}/input-kbd
%{_bindir}/input-recv
%{_bindir}/input-send
%{_bindir}/lsinput
%{_mandir}/man8/input-events.8.gz
%{_mandir}/man8/input-kbd.8.gz
%{_mandir}/man8/lsinput.8.gz
%doc COPYING README

%changelog
* Tue Dec 06 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2
- Rebuilt for Fedora
* Tue Feb 17 2009 Silvan Calarco <silvan.calarco@mambasoft.it> 20081014.101501-1mamba
- update to 20081014.101501
* Sat Sep 09 2006 Silvan Calarco <silvan.calarco@mambasoft.it> 143821-1qilnx
- package created by autospec
