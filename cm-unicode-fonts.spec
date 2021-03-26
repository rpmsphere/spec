%define _ttfontsdir %{_datadir}/fonts/cm-unicode

Name:           cm-unicode-fonts
Version:        0.7.0
Release:        191.1
Summary:        Unicode Version of the Computer Modern Fonts
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            http://canopus.iacp.dvo.ru/~panov/cm-unicode/
Source0:        ftp://canopus.iacp.dvo.ru/pub/Font/cm_unicode/cm-unicode-0.7.0-otf.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Computer Modern Unicode fonts were converted from metafont sources
using [1] textrace and [2] pfaedit (030404). Their main purpose is to
create free good quality fonts for use in X Window System applications
supporting many languages. Currently the fonts contain glyphs from
Latin1 (Metafont ec, tc), Cyrillic (la, rx) and Greek (cbgreek when
available) code sets.

%prep
%setup -q -n cm-unicode-%{version}

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -c -m 644 *.otf %{buildroot}%{_ttfontsdir}

%files
%defattr(-, root,root)
%doc Changes FAQ FontLog.txt Fontmap.CMU* OFL* README TODO fonts.scale
%{_ttfontsdir}

%changelog
* Thu Feb 28 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.0
- Rebuild for Fedora
* Wed Jul  4 2012 pgajdos@suse.cz
- amend spec file to reflect new font packaging scheme
  (see openFATE#313536);
* Thu May 17 2012 pgajdos@suse.com
- call spec-cleaner
* Thu May 10 2012 pgajdos@suse.com
- updated to 0.7.0 -> OFL-1.1 license
* Wed May  9 2012 cfarrell@suse.com
- license update: SUSE-XFree86-with-font-exception
  This license was added to the spreadsheet linked at license.opensuse.org
  today (SUSE-prefix until spdx.org accepts the license)
* Sun Sep 18 2011 jengelh@medozas.de
- Remove redundant tags/sections from specfile
* Mon Nov  8 2010 coolo@novell.com
- remove support for pre-9.1
* Tue Aug  8 2006 mfabian@suse.de
- move fonts to /usr/share/fonts because of the move to Xorg X11R7.
* Wed Mar  1 2006 mfabian@suse.de
- add "Provides: locale(ru;bg;el)".
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Fri Sep 30 2005 mfabian@suse.de
- update to 0.4.2.
* Fri Dec  3 2004 mfabian@suse.de
- use new macro "%%run_suseconfig_fonts".
* Thu Mar 18 2004 mfabian@suse.de
- use %%suseconfig_fonts_prereq
* Sat Feb 14 2004 mfabian@suse.de
- update to 0.1.2.
- don't build as root
- run SuSEconfig.fonts and SuSEconfig.pango in %%post and %%postun
* Wed Aug 27 2003 mfabian@suse.de
- new package: cm-unicode 0.1.
