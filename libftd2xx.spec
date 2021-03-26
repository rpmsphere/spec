%global debug_package %{nil}

Name:		libftd2xx
Version:	1.1.12
Release:	1.bin
Summary:	Library for the FTDI USB controller
Group:		System Environment/Libraries
License:	commercial, freeware
URL:		http://www.ftdichip.com/Drivers/D2XX.htm
Source0:	http://www.ftdichip.com/Drivers/D2XX/Linux/%{name}%{version}.tar.gz

%description
FTDI developed libftd2xx primarily to aid porting Windows applications 
written with D2XX to Linux.  We intend the APIs to behave the same on
Windows and Linux so if you notice any differences, please contact us 
(see http://www.ftdichip.com/FTSupport.htm).

FTDI do not release the source code for libftd2xx.  If you prefer to work
with source code and are starting a project from scratch, consider using
the open-source libFTDI.

%package devel
Summary:	Header files and static libraries for libftd2xx
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and static libraries for libftd2xx.

%prep
%setup -q -n release
echo -e "blacklist ftdi_sio\nblacklist usbserial" > blacklist-%{name}.conf

%build

%install
%ifarch x86_64
install -Dm755 build/x86_64/statictest %{buildroot}%{_bindir}/%{name}-test
%else
install -Dm755 build/i386/statictest %{buildroot}%{_bindir}/%{name}-test
%endif
install -d %{buildroot}%{_libdir}
%ifarch x86_64
install -m755 build/x86_64/%{name}.* %{buildroot}%{_libdir}
%else
install -m755 build/i386/%{name}.* %{buildroot}%{_libdir}
%endif
install -d %{buildroot}%{_includedir}
install -m644 *.h %{buildroot}%{_includedir}
ln -s libftd2xx.so.%{version} %{buildroot}%{_libdir}/libftd2xx.so
install -Dm644 blacklist-%{name}.conf %{buildroot}%{_prefix}/lib/modprobe.d/blacklist-%{name}.conf

%files
%doc ReadMe.txt
%{_libdir}/libftd2xx.so.*
%{_prefix}/lib/modprobe.d/blacklist-%{name}.conf

%files devel
%{_bindir}/libftd2xx-test
%{_libdir}/libftd2xx.so
%{_libdir}/libftd2xx.a
%{_includedir}/*.h

%changelog
* Wed Jun 17 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.12
- Initial package
