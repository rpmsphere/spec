%undefine _debugsource_packages

Name:           gtkdialogs
Version:        2.2
Release:        11.1
Source:         %{name}-%{version}.tar.bz2
Patch0:         gtkdialogs-2.2-fix-str-fmt.patch
License:        GPL
Summary:        Ready-to-use GTK+ dialog boxes
Provides:       gchooser gmessage xtest
Group:          System/Configuration/Packaging
BuildRequires:  gtk2-devel

%description
Ready-to-use GTK+ dialog boxes:
- xtest lets you test if X is running or not
- gmessage show a message and some buttons, it returns with the number of the
  pressed button
- gchooser presents a list of entries from which the user can choose
- gfilechooser helps choosing a filename or dirname

%prep
%setup -q -n %{name}
%patch 0 -p0

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT install

%files
%{_bindir}/*

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2
- Rebuilt for Fedora
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.2-8mdv2011.0
+ Revision: 664950
- mass rebuild
* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2-7mdv2011.0
+ Revision: 605508
- rebuild
* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2-6mdv2010.1
+ Revision: 522780
- rebuilt for 2010.1
* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.2-5mdv2010.0
+ Revision: 425076
- rebuild
* Tue Apr 07 2009 Funda Wang <fwang@mandriva.org> 2.2-4mdv2009.1
+ Revision: 365032
- fix str fmt
* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.2-4mdv2009.0
+ Revision: 221112
- rebuild
* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 2.2-3mdv2008.1
+ Revision: 150246
- rebuild
- kill re-definition of %%buildroot on Pixel's request
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
* Thu Jul 05 2007 Adam Williamson <awilliamson@mandriva.org> 2.2-2mdv2008.0
+ Revision: 48481
- rebuild for 2008
* Mon Aug 28 2006 Pixel <pixel@mandriva.com>
+ 2006-08-28 14:05:25 (58305)
- move from /usr/X11R6/bin to /usr/bin
* Mon Aug 28 2006 Pixel <pixel@mandriva.com>
+ 2006-08-28 13:57:21 (58300)
- Import gtkdialogs
* Sun Jun 18 2006 Stefan van der Eijk <stefan@eijk.nu.lurtspam> 2.1-3
- rebuild for png
- %%mkrel
* Thu Oct 13 2005 Pixel <pixel@mandriva.com> 2.1-2mdk
- rebuild
* Mon Feb 09 2004 Guillaume Cottenceau <gc@mandrakesoft.com> 2.1-1mdk
- add gfilechooser
- gmessage: allow to have a comma in buttons, when it's backslashed
