%global __os_install_post %{nil}
%undefine _debugsource_packages

Name:           glitz
Version:        0.5.6
Release:        1
Summary:        OpenGL image compositing library
Group:          System Environment/Libraries
License:        BSD
URL:            http://www.freedesktop.org/Software/glitz
Source:         http://cairographics.org/snapshots/%{name}-%{version}.tar.gz
BuildRequires:  libX11-devel, libXt-devel, libICE-devel, mesa-libGL-devel

%description
Glitz is an OpenGL image compositing library. Glitz provides Porter/Duff
compositing of images and implicit mask generation for geometric primitives
including trapezoids, triangles, and rectangles.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        glx
Summary:        GLX extensions for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    glx
The %{name}-glx package contains GLX extensions for %{name}.

%package        glx-devel
Summary:        Development files for %{name}-glx
Group:          Development/Libraries
Requires:       %{name}-glx = %{version}-%{release}
Requires:       %{name}-devel = %{version}-%{release}
Requires:       libX11-devel, mesa-libGL-devel, pkgconfig

%description    glx-devel
The %{name}-glx-devel package contains libraries and header files for
developing applications that use %{name}-glx.

%prep
%setup -q

%build
export CFLAGS=-Wno-format-security
%configure --disable-static --enable-glx --disable-agl \
           --disable-egl --disable-wgl
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
install -D -m 644 ./src/glitz.man \
        $RPM_BUILD_ROOT%{_mandir}/man3/glitz.3
install -D -m 644 ./src/glx/glitz-glx.man \
        $RPM_BUILD_ROOT%{_mandir}/man3/glitz-glx.3

%clean
rm -rf $RPM_BUILD_ROOT



%files
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO
%{_libdir}/libglitz.so.*

%files devel
%{_includedir}/glitz.h
%{_libdir}/libglitz.so
%{_libdir}/pkgconfig/glitz.pc
%{_mandir}/man3/glitz.3*

%files glx
%{_libdir}/libglitz-glx.so.*

%files glx-devel
%{_includedir}/glitz-glx.h
%{_libdir}/libglitz-glx.so
%{_libdir}/pkgconfig/glitz-glx.pc
%{_mandir}/man3/glitz-glx.3*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.6
- Rebuilt for Fedora
* Sat Nov 11 2006 Eric Work <work.eric@gmail.com> 0.5.6-5
- bump EVR to assure devel replaces FC6
* Fri Sep 15 2006 Eric Work <work.eric@gmail.com> 0.5.6-4
- bumped version to prepare for FC6
* Wed Jun 07 2006 Eric Work <work.eric@gmail.com> 0.5.6-3
- added missing requires to devel packages
- moved man pages to devel packages
* Mon Jun 05 2006 Eric Work <work.eric@gmail.com> 0.5.6-2
- added configure flags for build consistency
- added man pages for glitz and glitz-glx
- split package into subpackages glitz and glitz-glx
* Wed May 31 2006 Eric Work <work.eric@gmail.com> 0.5.6-1
- initial release
