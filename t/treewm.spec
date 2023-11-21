%undefine _debugsource_packages
%undefine _auto_set_build_flags

Name: treewm
Summary: Window Manager that arranges the windows in a tree
Version: 0.4.5
Release: 1
Group: x11
License: Free Software
Source0: %{name}-%{version}.tar.gz
BuildRequires: libXxf86vm-devel

%description
 treewm is a window manager that tries to implement a new concept. In addition to
 the client windows the user can create desktops which can themselves contain
 windows and desktops. By arranging the windows in such a tree the user is able
 to manage his tasks efficiently.

%prep
%setup -q
sed -i 's|/usr/local|/usr|' Makefile
sed -i '20i #include <cstring>' src/global.h

%build
make %{?_smp_mflags}

%install
make install ROOT=%{buildroot}

%files
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/doc/%{name}

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.5
- Rebuilt for Fedora
