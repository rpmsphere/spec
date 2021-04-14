Name: xplsprinters
Version: 1.0.1
Release: 12.1
Summary: Shows a list of Xprint printers and it's attributes
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRequires: libX11-devel >= 1.0.0
BuildRequires: libXp-devel >= 1.0.0
BuildRequires: libXprintUtil-devel >= 1.0.1
BuildRequires: xorg-x11-util-macros >= 1.0.1

%description
Xplsprinters is a utility for Xprint, the printing system for the X Window
system.  It can deliver both a list of printers and attributes supported for a
specific list of printers.

%prep
%setup -q

%build
%configure	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}
make

%install
rm -rf %{buildroot}
%make_install

%clean
rm -rf %{buildroot}

%files
%{_bindir}/xplsprinters
%{_mandir}/man1/xplsprinters.1x*

%changelog
* Sun Feb 22 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.1
- Rebuilt for Fedora
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-11mdv2011.0
+ Revision: 615731
- the mass rebuild of 2010.1 packages
* Mon Apr 19 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.1-10mdv2010.1
+ Revision: 536822
- rebuild
* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 1.0.1-9mdv2010.0
+ Revision: 435270
- rebuild
* Mon Aug 04 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-8mdv2009.0
+ Revision: 262700
- rebuild
* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-7mdv2009.0
+ Revision: 257685
- rebuild
  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert to use upstream tarball, build requires and remove non mandatory local patches.
* Thu Jan 17 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.1-5mdv2008.1
+ Revision: 154389
- Updated BuildRequires and resubmit package.
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
* Mon Oct 15 2007 Thierry Vignaud <tv@mandriva.org> 1.0.1-4mdv2008.1
+ Revision: 98668
- fix description
- do not hardcode lzma extension!!!
* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading
* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway
* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release
* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository
