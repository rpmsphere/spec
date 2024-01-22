%global __os_install_post %{nil}
%global debug_package %{nil}
%undefine _missing_build_ids_terminate_build

Name:          pcsc-lite-omnikey
Version:       4.0.5.5
Release:       1.bin
Summary:       PC/SC driver for OMNIKEY
Group:         System/Libraries
URL:           http://www.hidglobal.com/drivers?field_brand_tid=24
Source0:       http://www.hidglobal.com/sites/hidglobal.com/files/drivers/ifdokccid_linux_x86_64-v%{version}.tar.gz
License:       Commercial, freeware

%description
PC/SC Lite Driver for HID Global OMNIKEY CCID driver Smartcard reader series:
3x21, 512x, 532x.

%prep
%setup -q -n ifdokccid_linux_x86_64-v%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/pcsc/drivers
cp -a ifdokccid_linux_x86_64-v%{version}.bundle $RPM_BUILD_ROOT%{_libdir}/pcsc/drivers/ifdokccid.bundle
install -Dm644 omnikey.ini $RPM_BUILD_ROOT%{_sysconfdir}/omnikey.ini
install -Dm644 z98_omnikey.rules $RPM_BUILD_ROOT%{_sysconfdir}/udev/rules.d/10-omnikey.rules
install -Dm755 ok_pcscd_hotplug.sh $RPM_BUILD_ROOT/lib/udev/ok_pcscd_hotplug.sh

%post
systemctl try-restart pcscd.service >/dev/null 2>&1 || :

%postun
systemctl try-restart pcscd.service >/dev/null 2>&1 || :

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_libdir}/pcsc/drivers/ifdokccid.bundle
%{_sysconfdir}/omnikey.ini
%{_sysconfdir}/udev/rules.d/10-omnikey.rules
/lib/udev/ok_pcscd_hotplug.sh
%doc HID_OK_Drivers_EULA README

%changelog
* Mon Dec 15 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 4.0.5.5
- Initial package
