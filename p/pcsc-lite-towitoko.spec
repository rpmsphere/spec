Name:           pcsc-lite-towitoko
BuildRequires:  libusb-devel
BuildRequires:  pcsc-lite-devel
Version:        2.0.8
Release:        1
URL:            https://github.com/cprados/towitoko-linux
Summary:        Towitoko Smartcard Readers Driver
License:        LGPL-2.1
Group:          Productivity/Security
Source0:        https://codeload.github.com/cprados/towitoko-linux/tar.gz/refs/tags/v%{version}#/towitoko-linux-%{version}.tar.gz

%description
This package contains a driver for the smart card readers produced by Towitoko.

%prep
%setup -q -n towitoko-linux-%{version}

%build
%configure --enable-usb-bundle --with-pcsc-lite-dir=%{buildroot}%{_libdir}/pcsc
%make_build

%install
%make_install
mv %{buildroot}%{_bindir}/tester %{buildroot}%{_bindir}/towitoko-tester
install -Dm644 doc/reader.conf %{buildroot}/etc/reader.conf.d/libtowitoko

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc ChangeLog README THANKS COPYING AUTHORS NEWS
%{_bindir}/towitoko-tester
%{_includedir}/*.h
%{_libdir}/libtowitoko.*
%{_mandir}/man3/*
%{_libdir}/pcsc/drivers/towitoko.bundle
%{_sysconfdir}/reader.conf.d/libtowitoko

%changelog
* Sun May 2 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.8
- Rebuilt for Fedora
