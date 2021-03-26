Name: scan3d
Summary: To acquire the three dimensional shape of a real-world object
Version: 0.1
Release: 20.1
Group: Applications/Engineering
License: GPL
URL: http://scan3d.sourceforge.net/
Source0: http://sourceforge.net/projects/scan3d/files/scan3d/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires: ImageMagick-c++-devel

%description
With Scan3D you can scan a real object and reconstruct its three-dimensional
surface. You need only to take set of photographs of the object and you'll
be able to obtain a file in VRML or other 3d graphic formats.

%prep
%setup -q
sed -i 's|Data::add_data|add_data|' src/data.h
sed -i '1i #include <cstdlib>\n#include <cassert>' src/common.h
sed -i "146s|0x80|'\x80'|" src/data.cpp

%build
%configure
sed -i 's|-O2|-I/usr/include/ImageMagick-6 -O2|' src/Makefile
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc AUTHORS COPYING TODO
%{_bindir}/s3d-*

%changelog
* Sun May 12 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuild for Fedora
