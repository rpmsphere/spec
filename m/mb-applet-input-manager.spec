%undefine _debugsource_packages
Summary:        Input manager for the Matchbox Desktop
Name:           mb-applet-input-manager
Version:        0.6
Release:        1
URL:            https://matchbox-project.org/
License:        GPLv2+
Group:          Graphical desktop/Other
Source:         https://matchbox-project.org/sources/%name/%version/%{name}-%{version}.tar.bz2
BuildRequires:  pango-devel libX11-devel libjpeg-devel libpng-devel libxsettings-client-devel libmatchbox-devel

%description
Input manager for the Matchbox Desktop.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=%{buildroot} install

%files
%doc AUTHORS README 
%_bindir/mbinputmgr
%_datadir/applications/*
%_datadir/pixmaps/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6
- Rebuilt for Fedora
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6-6mdv2011.0
+ Revision: 620303
- the mass rebuild of 2010.0 packages
* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.6-5mdv2010.0
+ Revision: 429985
- rebuild
* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.6-4mdv2009.0
+ Revision: 252074
- rebuild
- fix no-buildroot-tag
- kill re-definition of %%buildroot on Pixel's request
* Tue Nov 06 2007 Funda Wang <fwang@mandriva.org> 0.6-2mdv2008.1
+ Revision: 106289
- BR matchbox-devel
- Rebuild
- import mb-applet-input-manager
* Mon Jan 10 2005 Austin Acton <austin@mandrake.org> 0.6-1mdk
- 0.6
* Tue Jul 27 2004 Austin Acton <austin@mandrake.org> 0.5-1mdk
- initial package
