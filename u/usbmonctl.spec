%undefine _debugsource_packages

Name:           usbmonctl
Version:        1.2
Release:        3.1
License:        GPLv2
Summary:        USB HID Monitor control utility
URL:            https://www.rainbow-software.org/linux
Group:          Hardware/Mobile
Source:         https://www.rainbow-software.org/linux_files/%{name}_%{version}.tar.gz
BuildRequires:  libusb1-devel

%description
Controls higher-end monitors with USB port that comply with USB Monitor
Control Class Specification. Tested with Samsung SyncMaster 757DFX and 765MB
(replacement for Samsung MouScreen utility for Windows). Should also work
with Apple Cinema Displays as a replacement for acdcontrol and acdctl
utilities that are not developed anymore.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
rm -f -r $RPM_BUILD_ROOT
%{__mkdir} -pv $RPM_BUILD_ROOT/etc/udev/rules.d/
%{__mkdir} -pv $RPM_BUILD_ROOT%{_bindir}
%{__cp} -r %{name} $RPM_BUILD_ROOT%{_bindir}
%{__cp} -r 95-%{name}-monitor.rules $RPM_BUILD_ROOT/etc/udev/rules.d/

%files
%doc ChangeLog COPYING README
%config /etc/udev/rules.d/95-usbmonctl-monitor.rules
%{_bindir}/usbmonctl

%changelog
* Thu Mar 15 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2
- Rebuilt for Fedora
* Wed Jan 25 2012 i@marguerite.su
- initial package 1.1
