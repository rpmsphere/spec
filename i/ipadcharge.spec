%undefine _debugsource_packages

Name:       ipadcharge
Version:	1.1
Release:	5.1
License:	GPLv2
Summary:	An iPad USB Charging Control Utility
URL:		http://www.rainbow-software.org/linux
Group:		Hardware/Mobile
Source:		http://www.rainbow-software.org/linux_files/ipad_charge_%{version}.tar.gz
BuildRequires:	libusb1-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
iPad Charge is used to enable/disable charging of an iPad connected to USB port.

%prep
%setup -q -n ipad_charge-%{version}

%build
make %{?_smp_mflags}

%install
rm -f -r $RPM_BUILD_ROOT
%{__mkdir} -pv $RPM_BUILD_ROOT/etc/udev/rules.d/
%{__mkdir} -pv $RPM_BUILD_ROOT%{_bindir}
%{__cp} -r ipad_charge $RPM_BUILD_ROOT%{_bindir}
%{__cp} -r 95-ipad_charge.rules $RPM_BUILD_ROOT/etc/udev/rules.d/

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%config /etc/udev/rules.d/95-ipad_charge.rules
%{_bindir}/ipad_charge

%changelog
* Thu Mar 15 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuilt for Fedora
* Wed Jan 25 2012 i@marguerite.su
- initial package 1.1
