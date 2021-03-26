%global debug_package %{nil}

Name:           xbattbar-acpi
Version:        0.4.0
Release:        3.1
Summary:        Battery status indicator
Group:          Applications/System
License:        GPLv2+
URL:            http://mirrors.kernel.org/ubuntu/pool/universe/x/xbattbar-acpi/
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  libacpi-devel
BuildRequires:  xosd-devel

%description
Laptop battery status indicator for X11.

%prep
%setup -q

%build
make

%install
rm -rf %{buildroot}
install -d -m 775 %{buildroot}/usr/bin
install -d -m 775 %{buildroot}/usr/share/man/man1
install -m 755 xbattbar-acpi %{buildroot}/usr/bin
install -m 644 xbattbar-acpi.1 %{buildroot}/usr/share/man/man1

%clean
rm -rf %{buildroot}

%files
%{_bindir}/xbattbar-acpi
%{_mandir}/man1/xbattbar-acpi.1.*

%changelog
* Mon Mar 02 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.0
- Rebuild for Fedora
* Tue Feb 19 2013 Shintaro Shinozaki <taro@yadokari-linux.org> - 0.4.0-1
- initial rpm release
