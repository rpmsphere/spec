Summary: Galago desktop presence daemon
Name: galago-daemon
Version: 0.5.1
Release: 6.1
Source0: http://www.galago-project.org/files/releases/source/galago-daemon/%{name}-%{version}.tar.bz2
License: GPL
Group: System/Servers
URL: http://www.galago-project.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: galago-devel >= 0.5.2
BuildRequires: dbus-glib-devel

%description
This is the daemon of the Galago desktop presence framework.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc NEWS AUTHORS ChangeLog
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/galago-daemon.conf
%{_libexecdir}/galago-daemon
%{_datadir}/dbus-1/services/org.freedesktop.Galago.service

%changelog
* Sun Sep 02 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.1
- Rebuild for Fedora
* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.5.1-3mdv2009.0
+ Revision: 245618
- rebuild
* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.5.1-1mdv2008.1
+ Revision: 140733
- restore BuildRoot
  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %$RPM_BUILD_ROOT on Pixel's request
* Fri Jan 05 2007 Götz Waschk <waschk@mandriva.org> 0.5.1-1mdv2007.0
+ Revision: 104441
- new version
- bump deps
- Import galago-daemon
* Fri Jan 05 2007 Götz Waschk <waschk@mandriva.org> 0.5.0-4mdv2007.1
- Rebuild
* Thu Aug 03 2006 Frederic Crozat <fcrozat@mandriva.com> 0.5.0-3mdv2007.0
- Rebuild with latest dbus
* Fri Jul 21 2006 Götz Waschk <waschk@mandriva.org> 0.5.0-2mdk
- Rebuild
* Sat Apr 22 2006 Götz Waschk <waschk@mandriva.org> 0.5.0-1mdk
- bump deps
- New release 0.5.0
- use mkrel
* Fri Jan 27 2006 Frederic Crozat <fcrozat@mandriva.com> 0.3.4-3mdk
- rebuild for new dbus
* Thu Oct 27 2005 Götz Waschk <waschk@mandriva.org> 0.3.4-2mdk
- rebuild for new dbus
* Wed Oct 26 2005 Götz Waschk <waschk@mandriva.org> 0.3.4-1mdk
- update file list
- bump deps
- new URL
- new version
* Fri Jun 17 2005 Götz Waschk <waschk@mandriva.org> 0.3.3-1mdk
- initial package
