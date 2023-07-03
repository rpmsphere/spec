%undefine _debugsource_packages

Name: xcockroach
Version: 0.4
Release: 14.1
Summary: Displays cockroaches on your desktop
License: GPL
Group: Toys
URL: https://xcockroach.free.fr/
Source0: %{name}-%{version}.tar.bz2
Patch0: xcockroach-0.4-flags.patch
BuildRequires: libX11-devel
BuildRequires: libXpm-devel

%description
xcockroach displays cockroaches on your root window,
they will look for windows and hide themselves under them.
It is a GPL clone of xroach, with many enhancements.

%prep
%setup -q
%patch0 -p0 -b .flags

%build
autoreconf -fi
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS ChangeLog COPYING TODO
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuilt for Fedora
* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 0.4-10mdv2011.0
+ Revision: 634890
- drop libpath patch (I don't know why this patch exist)
- correctly using system build flags
- simplify BR
* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.4-9mdv2010.0
+ Revision: 445915
- rebuild
* Wed Mar 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.4-8mdv2009.1
+ Revision: 348660
- fix build
- fix files list
* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 0.4-7mdv2009.0
+ Revision: 262280
- rebuild
* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.4-6mdv2009.0
+ Revision: 256675
- rebuild
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
* Thu Dec 20 2007 Thierry Vignaud <tv@mandriva.org> 0.4-4mdv2008.1
+ Revision: 135640
- adajust file list
- fix & simplify file list
- kill re-definition of %%buildroot on Pixel's request
- do not hardcode man pages extension
- import xcockroach
* Wed Jan 18 2006 Olivier Blin <oblin@mandriva.com> 0.4-4mdk
- build with -fPIC
* Wed Sep 28 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.4-3mdk
- Rebuild
* Thu Jun 02 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.4-2mdk
- Rebuild
* Tue Apr 13 2004 Olivier Blin <blino@mandrake.org> 0.4-1mdk
- Patch0: put plugins in libdir
- new version
* Fri Feb  6 2004 Olivier Blin <blino@mandrake.org> 0.2.2-1mdk
- initial release
