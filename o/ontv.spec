Name:			ontv
Version:		3.2.0
Release:		9.1
Summary:	TV listings for the GNOME panel
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		ftp://ftp.gnome.org/pub/GNOME/sources/ontv
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/ontv/3.0/%{name}-%{version}.tar.bz2
Patch0:		ontv-3.0.0-assistant.patch
BuildRequires:	GConf2
BuildRequires:	perl-XML-Parser
BuildRequires:	pygtk2-devel
BuildRequires:	gnome-python2-devel
BuildRequires:	gnome-python2-extras
BuildRequires:	notify-python
BuildRequires:	vte-devel
#BuildRequires:	libgnome-window-settings-devel
BuildRequires:	intltool
BuildRequires:	notification-daemon
BuildRequires:	udisks2
BuildArch:	noarch

%description
OnTV is a GNOME Applet which uses XMLTV files to monitor current and upcoming
TV programs.

%prep
%setup -q

%build
export PYTHON=/usr/bin/python2
%configure --disable-schemas-install
make
										
%install
rm -rf %{buildroot}
%make_install
%find_lang %{name}
%define schemas %{name}

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_libexecdir}/*
sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*
sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%doc AUTHORS FAQ README NEWS THANKS TODO
%{_sysconfdir}/gconf/schemas/*
%{_libdir}/bonobo/servers/*
%{_bindir}/*
%{_libexecdir}/ontv-applet
%{python2_sitelib}/%name
%{_datadir}/%{name}
%{_datadir}/gnome-2.0/ui/*.xml
%{_datadir}/applications/ontv.desktop
#{_datadir}/gnome-control-center/keybindings/90-%{name}.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%changelog
* Fri Feb 13 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 3.2.0
- Rebuilt for Fedora
* Sun Nov 21 2010 Jani Välimaa <wally@mandriva.org> 3.2.0-3mdv2011.0
+ Revision: 599593
- don't own icon dirs
* Mon Nov 01 2010 Jani Välimaa <wally@mandriva.org> 3.2.0-2mdv2011.0
+ Revision: 591697
- rebuild for python 2.7
* Sun Aug 22 2010 Funda Wang <fwang@mandriva.org> 3.2.0-1mdv2011.0
+ Revision: 571827
- BR intltool
- New version 3.2.0
* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 3.0.0-7mdv2010.1
+ Revision: 440368
- rebuild
* Mon Jan 12 2009 Guillaume Bedot <littletux@mandriva.org> 3.0.0-6mdv2009.1
+ Revision: 328526
- Fix license
- Fix requires
- Fix python interpreter for 2009 Spring
* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 3.0.0-5mdv2009.1
+ Revision: 325782
- rebuild
* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 3.0.0-4mdv2009.0
+ Revision: 268348
- rebuild early 2009.0 package (before pixel changes)
* Wed Apr 23 2008 Guillaume Bedot <littletux@mandriva.org> 3.0.0-3mdv2009.0
+ Revision: 197036
- enable keybindings
* Wed Apr 23 2008 Guillaume Bedot <littletux@mandriva.org> 3.0.0-2mdv2009.0
+ Revision: 196959
- fixes bug #40203
* Tue Mar 04 2008 Guillaume Bedot <littletux@mandriva.org> 3.0.0-1mdv2008.1
+ Revision: 178825
- 3.0.0 + some spec cleanup
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
* Wed Dec 12 2007 Guillaume Bedot <littletux@mandriva.org> 2.8.0-4mdv2008.1
+ Revision: 117781
- fix buildreq again
* Wed Dec 12 2007 Guillaume Bedot <littletux@mandriva.org> 2.8.0-3mdv2008.1
+ Revision: 117692
- fix buildreqs, reqs and update hicolor icon cache
* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.8.0-2mdv2008.0
+ Revision: 90014
- rebuild
* Sat Aug 18 2007 Funda Wang <fwang@mandriva.org> 2.8.0-1mdv2008.0
+ Revision: 65458
- new version 2.8.0
