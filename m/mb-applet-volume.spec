%undefine _debugsource_packages
Summary: 	Volume control for the Matchbox Desktop
Name: 		mb-applet-volume
Version: 	0.2
Release: 	1
URL: 		http://matchbox-project.org
License: 	GPLv2+
Group: 		Graphical desktop/Other
Source: 	http://matchbox-project.org/sources/%name/%version/%{name}-%{version}.tar.bz2
BuildRequires:	gtk2-devel libmatchbox-devel libxsettings-client-devel

%description
Volume for the Matchbox Desktop.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=%{buildroot} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS TODO 
%_bindir/mb-applet-volume
%_datadir/applications/*
%_datadir/pixmaps/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuilt for Fedora
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2-5mdv2011.0
+ Revision: 620304
- the mass rebuild of 2010.0 packages
* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.2-4mdv2010.0
+ Revision: 429992
- rebuild
* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.2-3mdv2009.0
+ Revision: 252097
- rebuild
- fix no-buildroot-tag
- kill re-definition of %%buildroot on Pixel's request
* Tue Nov 06 2007 Funda Wang <fwang@mandriva.org> 0.2-1mdv2008.1
+ Revision: 106281
- New version 0.2
- import mb-applet-volume
* Tue Jul 27 2004 Austin Acton <austin@mandrake.org> 0.1-1mdk
- initial package
