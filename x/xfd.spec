Name:           xfd
Version:        1.1.3
Release:        3
Summary:        Display all the characters in an X font
Group:          Development/X11
Source:         https://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:        MIT
BuildRequires: pkgconfig(fontconfig)
BuildRequires: freetype-devel
BuildRequires: pkgconfig(xkbfile)
BuildRequires: pkgconfig(xft)
BuildRequires: pkgconfig(xt)
BuildRequires: pkgconfig(xaw7)
BuildRequires: xorg-x11-util-macros

%description
The xfd utility creates a window containing the name of the font being
displayed, a row of command buttons, several lines of text for 
displaying character metrics, and a grid containing one glyph per cell.
The characters are shown in increasing order from left to right, top
to bottom.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/xfd
%{_datadir}/X11/app-defaults/Xfd
%{_mandir}/man1/xfd.1*

%changelog
* Sun Nov 27 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.3
- Rebuilt for Fedora
* Thu Mar 31 2022 umeabot <umeabot> 1.1.3-3.mga9
+ Revision: 1836001
- Mageia 9 Mass Rebuild
* Sat Feb 15 2020 umeabot <umeabot> 1.1.3-2.mga8
+ Revision: 1523598
- Mageia 8 Mass Rebuild
+ wally <wally>
- replace deprecated %%configure2_5x
- replace deprecated %%makeinstall_std
* Mon Mar 11 2019 tv <tv> 1.1.3-1.mga7
+ Revision: 1374217
- BR pkgconfig(xkbfile)
- new release
* Sun Sep 23 2018 umeabot <umeabot> 1.1.2-6.mga7
+ Revision: 1301894
- Mageia 7 Mass Rebuild
* Fri Feb 05 2016 umeabot <umeabot> 1.1.2-5.mga6
+ Revision: 936380
- Mageia 6 Mass Rebuild
* Wed Oct 15 2014 umeabot <umeabot> 1.1.2-4.mga5
+ Revision: 750243
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 1.1.2-3.mga5
+ Revision: 690644
- Mageia 5 Mass Rebuild
* Sat Oct 19 2013 umeabot <umeabot> 1.1.2-2.mga4
+ Revision: 530194
- Mageia 4 Mass Rebuild
* Sat Jul 20 2013 luigiwalser <luigiwalser> 1.1.2-1.mga4
+ Revision: 456611
- 1.1.2
* Mon Jan 14 2013 umeabot <umeabot> 1.1.1-2.mga3
+ Revision: 386890
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Thu Feb 16 2012 tv <tv> 1.1.1-1.mga2
+ Revision: 209654
- new release
* Fri Jan 21 2011 ennael <ennael> 1.1.0-1.mga1
+ Revision: 27745
- imported package xfd
* Thu Oct 21 2010 Thierry Vignaud <tv@mandriva.org> 1.1.0-1mdv2011.0
+ Revision: 587076
- new release
* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-10mdv2010.1
+ Revision: 524440
- rebuilt for 2010.1
* Mon Apr 13 2009 Funda Wang <fwang@mandriva.org> 1.0.1-9mdv2009.1
+ Revision: 366633
- no more autoconf needed
  + Antoine Ginies <aginies@mandriva.com>
    - rebuild
* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-8mdv2009.0
+ Revision: 226035
- rebuild
  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert to use upstream tarball, build requires and remove non mandatory local patches.
* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.1-7mdv2008.1
+ Revision: 154753
- Updated BuildRequires and resubmit package.
- Choose default Xaw from xaw.m4 unless configure explicitly told otherwise.
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
* Fri Aug 31 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.1-6mdv2008.0
+ Revision: 76524
- rebuild for 2008
- wrap description
- slight spec clean
  + Thierry Vignaud <tv@mandriva.org>
    - do not hardcode lzma extension!!!
* Fri Sep 01 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-09-01 21:18:27 (59537)
- rebuild to fix libXaw.so.8 dependency
* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading
* Tue May 30 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-30 20:41:44 (31752)
- rebuild against new libXaw package
* Tue May 30 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-30 16:15:56 (31710)
- fill in a few more missing descriptions
* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway
* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release
* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository
