%global debug_package %{nil}

Summary: Split a multi-routine Fortran file into individual files
Name: fsplit
Version: 5.5
Release: 10.1
License: BSD
Group: Development/Other
Source0: fsplit.tar.bz2

%description
Fsplit takes as input either a file or standard input containing Fortran source
code.  It attempts to split the input into separate routine files of the form
name.f, where name is the name of the program unit (e.g.  function, subroutine,
block data or program).

%prep
%setup -q -n %{name}

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_bindir}
install -d $RPM_BUILD_ROOT/%{_mandir}/man1
install -m 755 fsplit $RPM_BUILD_ROOT/%{_bindir}
install -m 644 fsplit.1 $RPM_BUILD_ROOT/%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/fsplit
%{_mandir}/man1/fsplit.1*

%changelog
* Sun Apr 14 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 5.5
- Rebuild for Fedora
* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 5.5-6mdv2009.0
+ Revision: 245429
- rebuild
* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 5.5-4mdv2008.1
+ Revision: 136423
- restore BuildRoot
  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
* Tue Aug 21 2007 Olivier Thauvin <nanardon@mandriva.org> 5.5-4mdv2008.0
+ Revision: 68534
- rebuild
* Sun Aug 06 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/06/06 12:17:02 (53428)
- rebuild
* Sun Aug 06 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/06/06 12:14:01 (53427)
Import fsplit
* Sat Mar 04 2006 Olivier Thauvin <nanardon@mandriva.org> 5.5-2mdk
- rebuild
* Fri Feb 18 2005 Olivier Thauvin <thauvin@aerov.jussieu.fr>  5.5-1mdk
- initial mdk spec
* Thu May 13 2004 Jan Iven <jan.iven@cern.ch>
- small change to cope with compressed manpage, move to macros for pathes
