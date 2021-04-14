%undefine _debugsource_packages
%define name gromit
%define cvs 20041213
%define version 0.20041213
%define release 1

Summary: Paint annotations on top of the X screen
Name: %{name}
Version: 0.%{cvs}
Release: %{release}
Source0: http://www.home.unix-ag.org/simon/gromit/%{name}-%{cvs}.tar.bz2
Source1: %{name}.desktop
Patch0: gromit_20041213-4.diff.gz
License: GPL
Group: System/X11
URL: http://www.home.unix-ag.org/simon/gromit/
BuildRequires: gtk2-devel

%description
Gromit (GRaphics Over MIscellaneous Things) is a small tool to make
annotations on the screen.

It is useful for recording presentations with xvidcap.

%prep
%setup -q -n %{name}-%cvs
%patch0 -p1
sed -i 's|-Wall|-Wall -lX11 -lm|' Makefile

%build
%{__make}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__install} -D -m 755 %{name} %buildroot%_bindir/%{name}
%{__install} -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
%{__install} -D -m 644 debian/%{name}.xpm %{buildroot}%{_datadir}/pixmaps/%{name}.xpm
%{__install} -D -m 644 gromitrc %{buildroot}%{_sysconfdir}/%{name}/gromitrc

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS ChangeLog README debian/changelog debian/copyright
%_bindir/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_sysconfdir}/%{name}/gromitrc

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0-20041213.2
- Rebuilt for Fedora
* Wed Jul 25 2007 Götz Waschk <waschk@mandriva.org> 0-20041213.2mdv2008.0
+ Revision: 55231
- Import gromit
* Thu Jul 20 2006 Götz Waschk <waschk@mandriva.org> 0-20041213.2mdv2007.0
- Rebuild
* Mon Apr 17 2006 Götz Waschk <waschk@mandriva.org> 0-20041213.1mdk
- rebuild
* Tue Apr 12 2005 Götz Waschk <waschk@linux-mandrake.com> 0-0.20041213.1mdk
- initial package
