%global debug_package %{nil}
%undefine _missing_build_ids_terminate_build

Name:          pcsc-lite-ezusb
Version:       1.5.3
Release:       1.bin
Summary:       PCSC driver for EZUSB
Group:         System/Libraries
URL:           https://www.castlestech.com/zh-hant/%E6%AA%94%E6%A1%88%E4%B8%8B%E8%BC%89/#1471668869492-81bb3b92-514e
Source0:       EZUSB_Linux_x86_64_v%{version}.zip
License:       Commercial, freeware
BuildRequires: pcsc-lite-devel

%description
PC/SC Lite Driver for EZ100PU/EZMINI driver Smartcard reader series.

%prep
%setup -q -n EZUSB_Linux_x86_64_v%{version}
sed -i 's|/usr/local/include|/usr/include/PCSC|' mifdtest/Makefile
sed -i 's|LPSCARD_READERSTATE_A|LPSCARD_READERSTATE|' mifdtest/mifdtest.c

%build
make -C mifdtest

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/pcsc/drivers/ezusb.bundle/Contents/Linux
cd driver_ezusb_v%{version}_for_64_bit
install -m644 drivers/Info.plist $RPM_BUILD_ROOT%{_libdir}/pcsc/drivers/ezusb.bundle/Contents
install -m644 drivers/ezusb.so $RPM_BUILD_ROOT%{_libdir}/pcsc/drivers/ezusb.bundle/Contents/Linux
install -Dm755 ../mifdtest/mifdtest $RPM_BUILD_ROOT%{_bindir}/mifdtest

%post
systemctl try-restart pcscd.service >/dev/null 2>&1 || :

%postun
systemctl try-restart pcscd.service >/dev/null 2>&1 || :

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/mifdtest
%{_libdir}/pcsc/drivers/ezusb.bundle
%doc driver_ezusb_v%{version}_for_64_bit/*.txt

%changelog
* Thu Jul 02 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5.3
- Initial package
