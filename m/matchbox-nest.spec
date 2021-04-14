Summary: 	X nesting for the Matchbox Desktop
Name: 		matchbox-nest
Version: 	0.3
Release: 	1
URL: 		http://matchbox-project.org
License: 	GPLv2+
Group: 		Graphical desktop/Other
Source: 	http://matchbox-project.org/sources/matchbox-nest/0.3/%{name}-%{version}.tar.bz2
BuildRequires:	libmatchbox-devel libXtst-devel expat-devel

%description
X nesting for the panel from Matchbox.

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
%doc AUTHORS README ChangeLog
%_bindir/*
%_datadir/%name

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuilt for Fedora
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3-6mdv2011.0
+ Revision: 620298
- the mass rebuild of 2010.0 packages
* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.3-5mdv2010.0
+ Revision: 429961
- rebuild
* Mon Jul 28 2008 Thierry Vignaud <tv@mandriva.org> 0.3-4mdv2009.0
+ Revision: 251960
- rebuild
- fix no-buildroot-tag
- kill re-definition of %%buildroot on Pixel's request
* Tue Nov 06 2007 Funda Wang <fwang@mandriva.org> 0.3-2mdv2008.1
+ Revision: 106258
- BR expat
- BR libxtst-devel
- Rebuild
- import matchbox-nest
* Tue Jul 27 2004 Austin Acton <austin@mandrake.org> 0.3-1mdk
- initial package
