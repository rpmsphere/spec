Name: achilles
Summary: An artificial life and evolution simulator
Version: 2
Release: 8
Group: science
License: Free Software
Source0: %{name}-%{version}.tar.gz
BuildRequires: desktop-file-utils
BuildRequires: libpng-devel
#Requires: libgl1-mesa-glx
#Requires: |
#Requires: libgl1,
#Requires: libglu1-mesa
#Requires: |
#Requires: libglu1,
#Requires: libsdl1.2debian
#Requires: libx11-6,
#Requires: zlib1g

%description
Achilles is an artificial life and evolution simulator that uses Hebbian
neural networks and OpenGL/SDL to simulate life in a simplified environment.
It is based on Larry Yaeger's PolyWorld.

%prep
%setup -q
sed -i 's|iostream.h|iostream|' *.cc
sed -i '27i #include <math.h>' gene.cc
sed -i '3i using namespace std;' license.cc
sed -i 's|(png_byte\*)|png_byte*|' screenshot.cc

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc README NEWS COPYING ChangeLog AUTHORS
%{_bindir}/%{name}

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 2
- Rebuilt for Fedora
