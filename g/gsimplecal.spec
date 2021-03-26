Name:           gsimplecal
Version:        2.1
Release:        3.1
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
* Thu Dec 18 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1
- Rebuild for Fedora
* Fri Mar 22 2013 build for openSUSE
- Initial package created - 1.6
