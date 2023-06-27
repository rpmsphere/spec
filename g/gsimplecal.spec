Name:           gsimplecal
Version:        2.4.1
Release:        1
License:        BSD-3-Clause
Summary:        Lightweight gui calendar applet
URL:            https://github.com/dmedvinsky/gsimplecal
Group:          System/X11/Utilities
Source:         https://gsimplecal.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++ gtk3-devel

%description
Gsimplecal is a lightweight calendar application written in C++ using GTK2.

%prep
%setup -q

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
%make_install

%clean
rm -fr %{buildroot}

%files
%{_bindir}/%{name}
%{_mandir}/man*/*
%doc ChangeLog README COPYING AUTHORS

%changelog
* Sun Jun 11 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 2.4.1
- Rebuilt for Fedora
* Fri Mar 22 2013 build for openSUSE
- Initial package created - 1.6
