%define _name acsccid

Name:           pcsc-lite-acsccid
Version:        1.0.8
Release:        2.1
Summary:        ACS USB CCID smart card reader driver
Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://acsccid.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{_name}/%{_name}-%{version}.tar.bz2
BuildRequires:  libusb-devel
BuildRequires:  pcsc-lite-devel
BuildRequires:  flex
Requires(post): systemd-units
Requires(postun): systemd-units
Provides:       pcsc-ifd-handler
Obsoletes:      pcsc-lite-acr38

%description
ACS USB CCID (Chip/Smart Card Interface Devices) driver for use with the
PC/SC Lite daemon.

%prep
%setup -q -n %{_name}-%{version}
cp -a src/openct/LICENSE LICENSE.openct
cp -a src/towitoko/README README.towitoko

%build
%configure --enable-composite-as-multislot
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
/bin/systemctl try-restart pcscd.service >/dev/null 2>&1 || :

%postun
/bin/systemctl try-restart pcscd.service >/dev/null 2>&1 || :

%files
%doc AUTHORS ChangeLog COPYING LICENSE.openct README README.towitoko
%{_libdir}/pcsc/drivers/ifd-acsccid.bundle

%changelog
* Mon Dec 15 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.8
- Rebuild for Fedora
* Fri Jul  4 2014 Godfrey Chung <godfrey.chung@acs.com.hk> - 1.0.8-1
- Updated to version 1.0.8.
* Tue Jun 17 2014 Godfrey Chung <godfrey.chung@acs.com.hk> - 1.0.7-1
- Updated to version 1.0.7.
* Thu Apr 24 2014 Godfrey Chung <godfrey.chung@acs.com.hk> - 1.0.6-1
- Updated to version 1.0.6.
* Wed Sep  4 2013 Godfrey Chung <godfrey.chung@acs.com.hk> - 1.0.5-1
- Updated to version 1.0.5.
* Tue Jun 26 2012 Godfrey Chung <godfrey.chung@acs.com.hk> - 1.0.4-1
- Updated to version 1.0.4.
* Fri Jan 13 2012 Godfrey Chung <godfrey.chung@acs.com.hk> - 1.0.3-1
- Updated to version 1.0.3.
- Removed pcsc-lite-1_7_3.patch.
- Included ChangeLog from upstream.
* Thu Jan 12 2012 Godfrey Chung <godfrey.chung@acs.com.hk> - 1.0.2-1
- Created package.
- Based on pcsc-lite-ccid.spec.
