%undefine _debugsource_packages

Name:           ogre-hydrax
Version:        0.5.4
Release:        22.1
License:        LGPL-2.0+
Summary:        An add-on for Ogre for render pretty water scenes
URL:            https://modclub.rigsofrods.com/xavi/
Group:          Development/Libraries/C and C++
Source:         libhydrax-%{version}-6.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  ogre-devel

%description
It's fully configurable, all effect, such as water depth effects, smooth
transitions, foam effects, caustics, underwater god rays, ... can be modified
in real-time as well as all options that do not depend of shaders such as
Rtt's texture quality, hydrax geometry and noise modules options, you can
change between different modules(geometry and noise) on-fly, etc...
Hydrax has a modulable interface wich allows any kind of water geometry,
actually there're three modules availables: The infinite ocean module, based on
the projected grid concept, the simple grid module and the radial grid module;
of course, hydrax geometry modules and noise modules can be coded by users.

%package devel
Summary:        It is an add-on for Ogre for render pretty water scenes
Group:          Development/Libraries/C and C++
Requires:       libhydrax = %{version}
Provides:               libhydrax.so

%description devel
It's fully configurable, all effect, such as water depth effects, smooth
transitions, foam effects, caustics, underwater god rays, ... can be modified
in real-time as well as all options that do not depend of shaders such as
Rtt's texture quality, hydrax geometry and noise modules options, you can
change between different modules(geometry and noise) on-fly, etc...
Hydrax has a modulable interface wich allows any kind of water geometry,
actually there're three modules availables: The infinite ocean module, based on
the projected grid concept, the simple grid module and the radial grid module;
of course, hydrax geometry modules and noise modules can be coded by users.

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%prep
%setup -q -n hydrax
sed -i 's|$(PREFIX)/lib|$(LIBDIR)|' makefile
sed -i 's|mMesh(0)|mMesh()|' src/Mesh.cpp
%ifarch aarch64
sed -i 's|-m64||' makefile
%endif

%build
make

%install
make install DESTDIR=%{buildroot} LIBDIR=%{_libdir}
ln -sf libhydrax.so.0.5.? %{buildroot}%{_libdir}/libhydrax.so

%files
%doc Features License.txt README.txt
%{_libdir}/libhydrax.so.*
%{_datadir}/Hydrax

%files devel
%{_libdir}/libhydrax.so
%{_includedir}/Hydrax

%changelog
* Tue Apr 28 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.4
- Rebuilt for Fedora
* Sat Mar  3 2012 joop.boonen@opensuse.org
- Corrected the license
- Adapted the spec file to the openSUSE standard
* Fri Feb 24 2012 virus0025@gmail.com
- initial version
