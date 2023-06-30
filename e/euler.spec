%undefine _debugsource_packages

Name:           euler
Summary:        An interactive mathematical programming environment 
License:        GPL v2 or any later version
Group:          Productivity/Scientific/Math
Version:        1.61.0
Release:        20.1
URL:            https://euler.sourceforge.net/
Requires:       xdg-utils
BuildRequires:  gtk2-devel pcre-devel
Source0:        %name-%version.tar.bz2
Patch1:         euler-browser.patch
Patch2:         euler-static.patch
Patch3:         euler-obsolete-CLK_TCK.patch
#Patch4:         euler-docdir.patch
Patch5:         euler-missing_lib.patch
Source1:        %name.desktop

%description
The Euler Mathematical Toolbox is an open software for numerical and symbolic
computations written and maintained by R. Grothmann, professor for mathematics
at the University of Eichstätt.

This is the GTK+ port of euler, a program for quickly and interactively
computing with real and complex numbers and matrices. It features advanced
graphics capabilities and a simple programming language.


Authors:
--------
	Dr. Renee Grothmann <grothm@ku-eichstaett.de>
	Eric Boucharé <bouchare.eric@wanadoo.fr>
	Puji Prasetiyo <aripujiprasetiyo@yahoo.com>


%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
#patch4 -p1
%patch5 -p1

%build
%configure --disable-static
make %{?jobs:-j%jobs} CFLAGS="-Wall -O3 -fPIC"

%install
%makeinstall
install -Dm644 pixmaps/icon.xpm %{buildroot}/%{_datadir}/pixmaps/euler.xpm
install -Dm644 %{SOURCE1} %{buildroot}/%{_datadir}/applications/euler.desktop

%clean
rm -rf %buildroot

%files
%doc %{_defaultdocdir}/%name
%{_bindir}/euler
%{_datadir}/euler
%{_datadir}/applications/%name.desktop
%{_datadir}/pixmaps/euler.xpm

%changelog
* Thu Apr 02 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.61.0
- Rebuilt for Fedora
* Wed Feb 15 2012 lars@linux-schulserver.de
- fix build: include -lm in GTK_LIBS ( euler-missing_lib.patch )
- make rpmlint happy and remove unneeded documentation files
* Mon Sep 22 2008 lars@linux-schulserver.de
- moved to Education base repository
* Thu Sep 11 2008 lars@linux-schulserver.de
- initial version 1.61
