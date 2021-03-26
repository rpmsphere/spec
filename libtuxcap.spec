Name:           libtuxcap
Version:        1.4.0
Release:        6.2
URL:            http://sf.net/projects/tuxcap
Summary:        Tux Cap Games Framework
License:        BSD-4-Clause and BSD-3-Clause and MIT
Group:          Development/Libraries/C and C++
Source:         %{name}-%{version}.tar.bz2
Patch0:         %{name}-1.4.0-build.patch
Patch1:         %{name}-1.4.0-imagemagick.patch
Patch2:         %{name}-1.4.0-no-static.patch
Patch3:         %{name}-1.4.0-stdint.patch
BuildRequires:  ImageMagick-devel
BuildRequires:  mesa-libOSMesa-devel
BuildRequires:  SDL-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ImageMagick-c++-devel
BuildRequires:  python-devel

%description
The TuxCap Games Framework is a GNU/Linux and Mac OSX port of the PopCap
Games Framework used for 2D game development. It comes with PyCap Python
bindings, a fast 2D physics engine, a particle engine, widgets and many
documented examples.

%package devel
Summary:        Tux Cap Games Framework
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       gcc-c++ ImageMagick-devel ImageMagick-c++-devel mesa-libOSMesa-devel python-devel SDL-devel SDL_mixer-devel

%description devel
The TuxCap Games Framework is a GNU/Linux and Mac OSX port of the PopCap
Games Framework used for 2D game development. It comes with PyCap Python
bindings, a fast 2D physics engine, a particle engine, widgets and many
documented examples.

%prep
%setup -q
%patch0
%patch1
%patch2
%patch3

%build
cd tuxcap-build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} ..
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
cd tuxcap-build
make DESTDIR=$RPM_BUILD_ROOT install
if [ "%_lib" != "lib" ] ; then
    mv $RPM_BUILD_ROOT%{_prefix}/lib $RPM_BUILD_ROOT%{_libdir}
fi

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS CHANGELOG COPYRIGHT PopCap?Framework?License.txt README TODO
%{_libdir}/libtuxcap.so.4.0

%files devel
%defattr(-,root,root)
%doc doc/*.pdf
%dir %{_includedir}/tuxcap
%{_includedir}/tuxcap/*
%{_libdir}/*.so

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Tue May  8  2012 Simon Sun <simon@ossii.com.tw>
- Rebuild for OSSII
* Sun Feb 19 2012 jengelh@medozas.de
- Update license field to reflect actual license
- Use short URL
- Remove redundant tags/sections from specfile
* Sat Jul  2 2011 jengelh@medozas.de
- Use %%_smp_mflags for parallel building
- Strip %%clean section (not needed on BS)
* Thu Jun 11 2009 prusnak@suse.cz
- updated to 1.4.0
- fix stdint.h issue (stdint.patch)
* Tue May  5 2009 prusnak@suse.cz
- created package (version 1.3.3)
- fix build flags and don't try to build demos (build.patch)
- fix broken ImageMagick detection (imagemagick.patch)
- don't build static library (no-static.patch)
