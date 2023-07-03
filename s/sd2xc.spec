Summary: CursorXP to X11 Mouse Theme Converter
Name:    sd2xc
Version: 2.5
Release: 4.1
Source0: %{name}-%{version}.pl.bz2
URL: https://gtk-apps.org/content/show.php/CursorXP+to+X11+Mouse+Theme+Converter?content=104659
License: MIT
Group: Graphics
Requires: perl-Image-Magick
Requires: perl-Config-IniFiles
BuildArch: noarch

%description
Converts StarDock CursorXP themes (https://www.wincustomize.com/) to
XCursor themes compatible with XFree86 4.2.99 and higher.

%prep

%build

%install
mkdir -p %buildroot%_bindir
bzip2 -dc %{SOURCE0} > %buildroot%_bindir/%name

%files
%attr(755,root,root) %_bindir/%name

%changelog
* Tue Aug 02 2011 Götz Waschk <waschk@mandriva.org> 0.0.4-0.RC1.5mdv2012.0
+ Revision: 692732
- rebuild
* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0.0.4-0.RC1.4mdv2011.0
+ Revision: 140782
- restore BuildRoot
  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
* Wed Aug 01 2007 Götz Waschk <waschk@mandriva.org> 0.0.4-0.RC1.4mdv2008.0
+ Revision: 57446
- Import sd2xc
* Mon Jul 31 2006 Götz Waschk <waschk@mandriva.org> 0.0.4-0.RC1.4mdv2007.0
- Rebuild
* Tue Mar 14 2006 Götz Waschk <waschk@mandriva.org> 0.0.4-0.RC1.3mdk
- fix URL
* Sun Mar 13 2005 Götz Waschk <waschk@linux-mandrake.com> 0.0.4-0.RC1.2mdk
- rebuild
* Fri Feb 27 2004 Götz Waschk <waschk@linux-mandrake.com> 0.0.4-0.RC1.1mdk
- drop prefix
- newer version
* Mon Mar  3 2003 Götz Waschk <waschk@linux-mandrake.com> 0.0.3-1mdk
- initial package
