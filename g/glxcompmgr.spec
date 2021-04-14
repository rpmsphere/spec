Name: glxcompmgr
Version: 20080416
Release: 20.1
Summary: OpenGL compositing manager
Group: Development/X11
# git-archive --format=tar --prefix=glxcompmgr/ master | bzip2 > glxcompmgr.tar.bz2
Source: glxcompmgr.tar.bz2
Patch0: glxcompmgr-fix-link.patch
Patch1: glxcompmgr-makefile.am.patch
License: MIT
BuildRequires: libpng12-devel
BuildRequires: mesa-libGL-devel
BuildRequires: GConf2-devel cairo-devel
BuildRequires: libXcomposite-devel libXfixes-devel libXdamage-devel

%description
glxcompmgr is an OpenGL compositing manager that use GLX_MESA_render_texture
for binding redirected top-level windows to texture objects. It has a flexible
plug-in system and it is designed to run well on most graphics hardware. 

%package devel
Summary: Development files of glxcompmgr

%description devel
Development files of OpenGL compositing manager.

%prep
%setup -q -n %{name}
%patch0 -p0 -b .link
%patch1

%build
autoreconf -fi
%configure
sed -i 's|-lpng1.|-lpng12|' Makefile src/Makefile
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/glxcompmgr
%{_libdir}/glxcomp/*.so
%{_datadir}/glxcomp

%files devel
%{_includedir}/glxcomp            
%{_libdir}/glxcomp/*.a
%exclude %{_libdir}/glxcomp/*.la
%{_libdir}/pkgconfig/glxcomp.pc   

%changelog
* Tue Aug 02 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 20080416
- Rebuilt for Fedora
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 20080416-4mdv2011.0
+ Revision: 610869
- rebuild
* Thu Feb 18 2010 Funda Wang <fwang@mandriva.org> 20080416-3mdv2010.1
+ Revision: 507779
- fix linking
  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild early 2009.0 package (before pixel changes)
* Wed Apr 16 2008 Paulo Andrade <pcpa@mandriva.com.br> 20080416-1mdv2009.0
+ Revision: 195005
- glxcompmgr is an OpenGL compositing manager that use GLX_MESA_render_texture
  for binding redirected top-level windows to texture objects. It has a flexible
  plug-in system and it is designed to run well on most graphics hardware.
- glxcompmgr package.
