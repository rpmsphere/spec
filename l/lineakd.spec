%global __spec_install_post %{nil}
%undefine _debugsource_packages

Name:           lineakd
Version:        0.9
Release:        19.1
Summary:	Control multimedia keys on modern keyboards
License:	GPL
Group:		System/Configuration/Hardware          
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
URL:		http://lineak.sourceforge.net/
BuildRequires:	libX11-devel
BuildRequires:	libXtst-devel
Patch0:		lineakd-0.9.0-gcc43.patch
Patch1:		lineakd-0.9.0-link.patch

%description
Daemon to control the multimedia keys on modern keyboards.

Features X11 support, window manager independence, ability to configure
all keys (via a GUI [found in lineakconfig] & .conf file), volume
control, and sound controls.

%package devel
Summary:	Headers for developing programs using %{name}
Group:		Development/C
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the headers that programmers will need to develop 
applications which will use %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
rm -fr $RPM_BUILD_ROOT/usr/doc

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc TODO README AUTHORS INSTALL ChangeLog COPYING 
%config(noreplace) %{_sysconfdir}/lineakkb.def
%{_bindir}/%{name}
%{_bindir}/xsendkey*
%ifarch x86_64
%{_sbindir}/send_to_keyboard
%endif
%{_libdir}/%{name}
%{_mandir}/*/*
%{_libdir}/*.so.*

%files devel
%{_includedir}/lineak
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/*.so

%changelog
* Sun Apr 2 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9
- Rebuilt for Fedora
* Thu Jan 06 2011 Funda Wang <fwang@mandriva.org> 0.9-4mdv2011.0
+ Revision: 629146
- add patches to fix build
  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers
* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.9-1mdv2008.1
+ Revision: 136572
- restore BuildRoot
  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel
* Fri Dec 08 2006 Olivier Thauvin <nanardon@mandriva.org> 0.9-1mdv2007.0
+ Revision: 93875
- 0.9
* Thu Aug 10 2006 Olivier Thauvin <nanardon@mandriva.org> 0.8.4-2mdv2007.0
+ Revision: 55009
- rebuild
- remove uneed buildrequires
- Import lineakd
* Tue Dec 27 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.8.4-1mdk
- New release 0.8.4
* Thu Apr 07 2005 Olivier Thauvin <nanardon@mandrake.org> 0.8.3-1mdk
- 0.8.3
* Mon Dec 27 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.8.2-1mdk
- 0.8.2
* Tue Nov 09 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.8.1-2mdk
- removed /etc/X11/xinit.d/lineakd, as it doesn work
* Thu Oct 28 2004 Guillaume Rousse <guillomovitch@mandrakesoft.com> 0.8.1-1mdk
- New release
- fixed source URL
* Wed Sep 15 2004 Götz Waschk <waschk@linux-mandrake.com> 0.8-1mdk
- drop patch
- new version
* Sun Sep 05 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.8-0.beta4.1mdk 
- new version
- rpmbuildupdate aware
- tag launch script as config for rpmlint
- spec cleanup
