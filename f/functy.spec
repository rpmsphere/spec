Name: functy
Summary: 3D graph drawing package
Version: 0.38.0
Release: 1
Group: math
License: Free Software
Source0: %{name}-%{version}.tar.gz
BuildRequires: gdk-pixbuf2-devel
BuildRequires: gtk2-devel
BuildRequires: libpng-devel

%description
Functy is a 3D graph drawing package. The emphasis for the
application is to allow Cartesian and spherical functions to be
plotted and altered quickly and easily. This immediacy and the vivid
results are intended to promote fun exploration of 3D functions.

%prep
%setup -q
sed -i 's|glee||' configure*

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/%{name}
%{_datadir}/doc/%{name}
%{_datadir}/%{name}

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.38
- Rebuilt for Fedora
