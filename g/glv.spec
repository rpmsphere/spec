%undefine _debugsource_packages

Summary: A small, cross-platform display library for OpenGL
Name: glv
Version: 0.3.1
Release: 7.1
License: MIT
Group: Development/Libraries
Source: libglv-%{version}.tar.gz
URL: https://outguard.sourceforge.net/download.html
BuildRequires: mesa-libGL-devel libXxf86vm-devel

%description
The GLV library provides a small, cross-platform, C interface for creating
a window or fullscreen display with an OpenGL context.

%prep
%setup -q -n libglv-%{version}

%build
make -C x11

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}/GL
install -m 644 x11/*.h $RPM_BUILD_ROOT%{_includedir}/GL
install -m 755 x11/libglv.so.0.3 $RPM_BUILD_ROOT%{_libdir}
ln -s libglv.so.0.3 $RPM_BUILD_ROOT%{_libdir}/libglv.so.0
ln -s libglv.so.0.3 $RPM_BUILD_ROOT%{_libdir}/libglv.so

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc ChangeLog LICENSE README
%{_libdir}/libglv.so
%{_libdir}/libglv.so.0
%{_libdir}/libglv.so.0.3
%{_includedir}/GL/glv.h
%{_includedir}/GL/glv_keys.h

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.1
- Rebuilt for Fedora
* Sat Apr 05 2008 Karl Robillard <wickedsmoke@users.sf.net>
- Initial package release
