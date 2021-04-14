Summary: 	Shared files for the Matchbox Desktop
Name: 		matchbox-common
Version: 	0.9.1
Release: 	10.1
URL: 		http://matchbox.handhelds.org/
License: 	GPLv2+
Group: 		Graphical desktop/Other
Source0: 	http://matchbox-project.org/sources/%{name}/0.9/%{name}-%{version}.tar.bz2
Source1:    matchbox.desktop
BuildRequires:	pkgconfig libmatchbox-devel
BuildArch:	noarch

%description
Matchbox is a base environment for the X Window System running on non-desktop
embedded platforms such as handhelds, set-top boxes, kiosks and anything else
for which screen space, input mechanisms or system resources are limited.

This package contains graphics and scripts required by Matchbox.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%make_install
install -Dm 644 %{SOURCE1} %{buildroot}%{_datadir}/xsessions/matchbox.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc ChangeLog
%{_bindir}/matchbox-session
%{_datadir}/matchbox
%{_datadir}/pixmaps/*
%{_datadir}/icons/blondie
%{_datadir}/xsessions/matchbox.desktop

%changelog
* Fri Feb 20 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.1
- Rebuilt for Fedora
* Fri Oct 18 2013 umeabot <umeabot> 0.9.1-7.mga4
+ Revision: 507718
- Mageia 4 Mass Rebuild
* Sat Jan 12 2013 umeabot <umeabot> 0.9.1-6.mga3
+ Revision: 359422
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Sun Apr 10 2011 dmorgan <dmorgan> 0.9.1-5.mga1
+ Revision: 82825
- imported package matchbox-common
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.9.1-5mdv2010.0
+ Revision: 429958
- rebuild
* Mon Jul 28 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.9.1-4mdv2009.0
+ Revision: 251939
- rebuild
- fix no-buildroot-tag
- kill re-definition of %%buildroot on Pixel's request
* Mon Nov 05 2007 Funda Wang <fundawang@mandriva.org> 0.9.1-2mdv2008.1
+ Revision: 105981
- Rebuild
- import matchbox-common
* Mon Jan 24 2005 Austin Acton <austin@mandrake.org> 0.9.1-1mdk
- 0.9.1
* Tue Jan 4 2005 Austin Acton <austin@mandrake.org> 0.9-1mdk
- 0.9
* Mon Jul 20 2004 Austin Acton <austin@mandrake.org> 0.8-1mdk
- 0.8
