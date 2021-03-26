Name:           paragui
Version:        1.0.4
Release:        9.1
Summary:        Graphical User Interface based on SDL
Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://www.bms-austria.com/projects/paragui/
Source0:        http://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.gz
Patch0:         paragui-gcc34-fix.patch
Patch1:         newrpms-paragui-64bit.patch
Patch2:         newrpms-paragui-makefile.patch
Patch3:         paragui-aclocal.patch
Patch4:         paragui-python.patch
Patch5:         paragui-multilib.patch
BuildRequires:  gcc-c++
BuildRequires:  SDL-devel libpng-devel SDL_image-devel libtiff-devel
BuildRequires:  freetype-devel expat-devel physfs-devel libjpeg-devel
BuildRequires:  swig python2-devel python-unversioned-command

%description
ParaGUI is a cross-platform high-level application framework and GUI
(graphical user interface) library. ParaGUI's cross-platform nature is
completely based on the Simple DirectMedia Layer (SDL).

%package devel
Summary:        Headers for developing programs that will use paragui
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       expat-devel SDL_image-devel freetype-devel libstdc++-devel
Requires:       pkgconfig automake

%description devel
This package contains the headers that programmers will need to develop
applications which will use paragui, a GUI on top of SDL.

%package python
Summary:        Python bindings for paragui
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description python
Python bindings for ParaGUI, a cross-platform high-level application framework
and GUI (graphical user interface) library.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
chmod -x include/paragui*.h
# fixup some timestamps to stop autoxxx from rerunning due to our patches
touch aclocal.m4
touch include/stamp-h.in configure `find -name Makefile.in`
touch paraconfig_gnu.h.in
# sdl-config --libs' output includes -L/usr/lib[64] causing multilib pain
sed -i 's|-Wall|-Wall -Wno-narrowing|' configure
sed -i 's|`$SDL_CONFIG $sdlconf_args --libs`|"-lSDL -lpthread"|' configure
sed -i 's|__EXPORT__|PHYSFS_DECL|' src/core/physfsrwops.h

%build
%configure --disable-static --enable-python
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
mkdir -p $RPM_BUILD_ROOT%{python2_sitearch}
mv $RPM_BUILD_ROOT%{_libdir}/python2.7/%{name}* \
  $RPM_BUILD_ROOT%{python2_sitearch}
chmod +x $RPM_BUILD_ROOT%{python2_sitearch}/paraguicmodule.so
rm $RPM_BUILD_ROOT%{_libdir}/lib%{name}.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING README
%{_libdir}/lib%{name}-1.0.so.*
%{_datadir}/%{name}

%files devel
%{_bindir}/paragui-config
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/aclocal/%{name}.m4

%files python
%{python2_sitearch}/%{name}*

%changelog
* Fri Jul 01 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.4
- Rebuild for Fedora
* Sun Oct 21 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.4-6
- Fix paragui-config multilib conflict (bz 342831)
* Tue Aug 28 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.4-5
- Rebuild for new expat 2.0
* Wed Aug 15 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.4-4
- Update License tag for new Licensing Guidelines compliance
* Sat Mar 24 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.4-3
- Fix building of python bindings when paragui isn't installed already,
  for example when building under mock (bz 233140)
* Sat Mar 24 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.4-2
- Various specfile improvements (bz 233140)
* Sun Mar 18 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1.0.4-1
- Initial Fedora Extras package based on specfile by Che (newrpms)
