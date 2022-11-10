Name:           acpi_call
Version:        1.1.0
Release:        1
Summary:        Call ACPI methods by writing to /proc
License:        GPL3+
URL:            https://github.com/mkottman/acpi_call
Source0:        https://github.com/mkottman/acpi_call/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        dkms.conf
Patch1:         linux-acpi-h.patch
Requires:       dkms kernel-headers kernel-devel
BuildArch:      noarch

%description
A kernel simple module that enables you to call ACPI methods by writing the
method name followed by arguments to /proc/acpi/call.

This module is to be considered a proof-of-concept and has been superseeded by
projects like bbswitch. It allows you to tamper with your system and should be
used with caution.

%prep
%autosetup

%install
mkdir -p $RPM_BUILD_ROOT/usr/src/%{name}-%{version}
cp -rf * $RPM_BUILD_ROOT/usr/src/%{name}-%{version}
cp %{SOURCE1} $RPM_BUILD_ROOT/usr/src/%{name}-%{version}

%files
%{_usrsrc}/%{name}-%{version}

%post
dkms add -m %{name} -v %{version} --rpm_safe_upgrade
dkms build -m %{name} -v %{version}
dkms install -m %{name} -v %{version}

%preun
dkms remove -m %{module} -v %{version} --all --rpm_safe_upgrade

%changelog
* Sun Oct 23 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.0
- Rebuilt for Fedora
* Sat Jul 23 2016 Martin Ueding <dev@martin-ueding.de> 1.1.0-1
- Initial packaging
