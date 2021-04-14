Name: python3-periphery
Summary: A pure Python 2/3 library for peripheral I/O
Version: 1.1.1
Release: 2.1
Group: python
License: MIT
URL: https://github.com/vsergeev/python-periphery
Source0: https://github.com/vsergeev/python-periphery/archive/v%{version}.tar.gz#/python-periphery-%{version}.tar.gz
BuildRequires: python3-devel
BuildArch: noarch

%description
python-periphery is a pure Python library for GPIO, LED, PWM, SPI, I2C, MMIO,
and Serial peripheral I/O interface access in userspace Linux. It is useful
in embedded Linux environments (including Raspberry Pi, BeagleBone, etc.
platforms) for interfacing with external peripherals.

%prep
%setup -q -n python-periphery-%{version}

%build
%py3_build

%install
%py3_install

%files
%doc *.md LICENSE
#{_bindir}/*
%{python3_sitelib}/*

%changelog
* Fri Aug 24 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.1
- Rebuilt for Fedora
