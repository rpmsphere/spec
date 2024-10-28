%define fontdir %{_datadir}/fonts/mikachan

Name:           mikachan-fonts
Version:        9.1.2006.08.09
Release:        174.1
Summary:        Handwriting Japanese Fonts
License:        SUSE-Permissive
Group:          System/X11/Fonts
URL:            https://mikachan.sourceforge.jp/
#Source0:        https://mikachan.sourceforge.jp/mikachanALL.lzh
Source0:        mikachan-fonts.tar.bz2
Source1:        https://mikachan.sourceforge.jp/dl.html
Source2:        %name.COPYING
BuildRequires:  convmv
BuildArch:      noarch
Requires(post): fontconfig

%description
This package contains free Japanese fonts in "handwriting" style by Mika-Chan.

%prep
%setup -n %{name}
cp %{SOURCE1} .
cp %{SOURCE2} COPYING
convmv -f shift_jis -t utf-8 --notest *.ttf

%build

%install
mkdir -p %{buildroot}%{fontdir}
install -c -m 644 *.ttf %{buildroot}%{fontdir}

%post
/usr/bin/fc-cache 2> /dev/null

%postun
/usr/bin/fc-cache 2> /dev/null

%files
%doc COPYING *.html
%{fontdir}

%changelog
* Wed Jan 08 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 9.1.2006.08.09
- Rebuilt for Fedora
* Wed Jul  4 2012 pgajdos@suse.cz
- amend spec file to reflect new font packaging scheme
  (see openFATE#313536);
* Thu May 17 2012 pgajdos@suse.com
- call spec-cleaner
* Fri Apr 27 2012 pgajdos@suse.com
- SUSE-Permissive license (see COPYING)
* Thu Apr  8 2010 tiwai@suse.de
- remove unnecessary buildrequires for too old distros
* Tue Dec  2 2008 mfabian@suse.de
- Add inofficial translation of the license in
  https://mikachan.sourceforge.jp/dl.html
* Wed Aug  9 2006 mfabian@suse.de
- move fonts to /usr/share/fonts/truetype
  (openSUSE 10.2 will use X11R7).
- update to 9.1.2006.08.09.
* Wed Mar  1 2006 mfabian@suse.de
- add "Provides: locale(ja)".
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Fri Dec  3 2004 mfabian@suse.de
- use new macro "%%run_suseconfig_fonts -c"
* Mon Sep 13 2004 mfabian@suse.de
- Bugzilla #45156: add "Provides: scalable-font-ja".
* Fri Mar 19 2004 mfabian@suse.de
- use %%suseconfig_fonts_prereq
* Fri Feb 27 2004 mfabian@suse.de
- update to 9.0.2004.02.08
- run SuSEconfig.fonts and SuSEconfig.pango in %%post and %%postun
* Tue Feb  3 2004 hmacht@suse.de
- added option # norootforbuild in specfile
* Sun Aug 24 2003 mfabian@suse.de
- new package: mikachan-fonts, Version 8.9.2003.08.11
