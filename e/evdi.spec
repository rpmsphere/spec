%undefine _debugsource_packages

Name:		evdi
Version:	1.10.1
Release:	1
Summary:	DisplayLink VGA/HDMI driver for DL-6xxx, DL-5xxx, DL-41xx and DL-3xxx adapters
Group:		User Interface/X Hardware Support
License:	GPL v2.0, LGPL v2.1 and Proprietary
URL:		https://github.com/DisplayLink/evdi
Source0:	https://github.com/DisplayLink/evdi/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:	libdrm-devel
Requires:	%{name}-dkms

%description
This adds support for HDMI/VGA adapters built upon the DisplayLink DL-6xxx,
DL-5xxx, DL-41xx and DL-3xxx series of chipsets. This includes numerous
docking stations, USB monitors, and USB adapters.

%package devel
Summary:	Development files for package %{name}
Requires:	%{name}

%description devel
Libraries and header files for DisplayLink VGA/HDMI driver.

%package dkms
Summary:	DKMS files for package %{name}
Requires:	kernel-devel
Requires:	dkms
BuildArch:	noarch

%description dkms
DKMS and source files for DisplayLink VGA/HDMI driver.

%prep
%setup -q
sed -i 's/\r//' README.md

%build
cd library
make %{?_smp_mflags}

%install
# Kernel driver sources
mkdir -p $RPM_BUILD_ROOT/usr/src/evdi-%{version}
cp -a module/* $RPM_BUILD_ROOT/usr/src/evdi-%{version}

mkdir -p $RPM_BUILD_ROOT/etc/modules-load.d
echo evdi > $RPM_BUILD_ROOT/etc/modules-load.d/evdi.conf
mkdir -p $RPM_BUILD_ROOT/etc/modprobe.d
echo options evdi initial_device_count=4 > $RPM_BUILD_ROOT/etc/modprobe.d/evdi.conf

# Library
install -Dm755 library/libevdi.so.%{version} %{buildroot}%{_libdir}/libevdi.so.%{version}
ln -sf libevdi.so.%{version} %{buildroot}%{_libdir}/libevdi.so.0
ln -sf libevdi.so.0 %{buildroot}%{_libdir}/libevdi.so
install -Dm644 library/evdi_lib.h %{buildroot}%{_includedir}/evdi_lib.h

%post dkms
dkms install evdi/%{version}

%preun dkms
dkms remove evdi/%{version} --all

%files
%doc README.md library/LICENSE
/etc/modules-load.d/evdi.conf
/etc/modprobe.d/evdi.conf
%{_libdir}/libevdi.so.*

%files devel
%{_includedir}/evdi_lib.h
%{_libdir}/libevdi.so

%files dkms
/usr/src/evdi-%{version}

%changelog
* Sun Mar 27 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.10.1
- Rebuild package
* Sun Feb 19 2017 Richard Hofer <rofer@rofer.me> 1.3.52
- Bump downloaded version to 1.3.52
- Note support for DL-6xxx devices
* Tue Oct 11 2016 Aaron Aichlmayr <waterfoul@gmail.com> 1.2.64
- Bump downloaded version to 1.2.64
* Tue Oct 04 2016 Victor Rehorst <victor@chuma.org> 1.2.55-2
- Fix systemd-sleep support for DisplayLink driver 1.2.58 (which is now current for v1.2)
* Thu Sep 22 2016 Santiago Saavedra <ssaavedra@gpul.org> 1.2.55-1
- Bump upstream version for both evdi and DisplayLink driver
* Mon May 30 2016 Santiago Saavedra <ssaavedra@gpul.org> 1.1.65-5
- Add systemd-sleep support
* Tue May 24 2016 Bastien Nocera <bnocera@redhat.com> 1.1.65-4
- Really copy the libevdi.so from the sources
* Sun May 22 2016 Bastien Nocera <bnocera@redhat.com> 1.1.65-3
- Add missing libdrm-devel BR
* Tue May 17 2016 Bastien Nocera <bnocera@redhat.com> 1.1.65-2
- Update to daemon 1.1.62 (with a zip file called 1.1.68, sigh)
* Tue May 17 2016 Bastien Nocera <bnocera@redhat.com> 1.1.65-1
- Update to 1.1.65
* Tue May 10 2016 Bastien Nocera <bnocera@redhat.com> 1.1.61-1
- Update to 1.1.61
* Thu Apr 28 2016 Bastien Nocera <bnocera@redhat.com> 1.0.453-1
- Update to 1.0.453
- Compile the library from source
* Mon Dec 14 2015 Bastien Nocera <bnocera@redhat.com> 1.0.335-1
- Update to 1.0.335
* Mon Sep 07 2015 Bastien Nocera <bnocera@redhat.com> 1.0.138-4
- Disable debuginfo subpackage creation
* Mon Sep 07 2015 Bastien Nocera <bnocera@redhat.com> 1.0.138-3
- Create RPM directly from downloaded zip file
- Add LICENSE
- Create i386 RPM
* Sun Sep 6  2015 Eric Nothen <enothen@gmail.com> - 1.0.138-2
- Modified installed kernels detection section to be more precise
* Wed Sep 2  2015 Eric Nothen <enothen@gmail.com> - 1.0.138-1
- Updated driver to version 1.0.138, as published by DisplayLink
* Wed Aug 19 2015 Eric Nothen <enothen@gmail.com> - 1.0.68-2
- Changed udev rule to detect devices based on vendor rather than model
* Thu Aug 13 2015 Eric Nothen <enothen@gmail.com> - 1.0.68-1
- Initial package based on module version 1.0.68 available at http://www.displaylink.com/downloads/ubuntu.php
