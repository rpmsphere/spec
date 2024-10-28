Summary:        Gtk-based front-end for Esetroot
Name:           gsetroot
Version:        1.1
Release:        18.1
Source0:        https://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
License:        GPLv2
Group:          Graphical desktop/GNOME
URL:            https://gsetroot.sf.net
BuildRequires:  gtk2-devel
Requires:       eterm

%description
Use it to configure root window under a Window Manager like FluxBox,
Enlightenment, WindowMaker, NextStep, BlackBox..

%prep
%setup -q

%build
%configure
make CFLAGS+="-DHAVE_STPCPY -DHAVE_MEMPCPY"

%install
rm -rf %{buildroot}
%makeinstall
rm -rf %{buildroot}/usr/doc/* %{buildroot}%{_datadir}/locale/locale.alias

%files
%doc AUTHORS README ChangeLog
%{_bindir}/%{name}

%changelog
* Tue Apr 19 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuilt for Fedora
* Mon Apr 25 2011 Jani Välimaa <wally@mandriva.org> 1.1-1mdv2011.0
+ Revision: 659049
- new version 1.1
* Mon Apr 25 2011 Jani Välimaa <wally@mandriva.org> 1.0-7
+ Revision: 658719
- require lowercase eterm
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-6mdv2011.0
+ Revision: 619259
- the mass rebuild of 2010.0 packages
* Mon Sep 07 2009 Thierry Vignaud <tv@mandriva.org> 1.0-5mdv2010.0
+ Revision: 432712
- use %%configure2_5x
- rebuild
* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.0-4mdv2009.0
+ Revision: 246656
- rebuild
* Thu Feb 14 2008 Thierry Vignaud <tv@mandriva.org> 1.0-2mdv2008.1
+ Revision: 168497
- rebuild
- fix summary
- fix no-buildroot-tag
* Tue Dec 18 2007 Thierry Vignaud <tv@mandriva.org> 1.0-1mdv2008.1
+ Revision: 131749
- BR gtk2-devel
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- fix summary-ended-with-dot
- import gsetroot
* Wed Dec 28 2005 Samir Bellabes <sbellabes@mandriva.com> 1.0-1mdk
- first release.
