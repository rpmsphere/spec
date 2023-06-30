Name:         kochi-substitute-fonts
License:      distributable
Group:        System/X11/Fonts
Conflicts:    ttf-kochi-gothic, ttf-kochi-mincho
Version:      20030809
Release:      7.1
URL:          https://sourceforge.jp/projects/efont/files/
Source0:      https://downloads.sourceforge.jp/efont/5411/kochi-substitute-20030809.tar.bz2
Source1:      fonts.scale.kochi-substitute
Source100:    https://prdownloads.sourceforge.jp/efont/5411/substkit-20030809.tar.bz2
BuildArch:    noarch
Summary:      kochi-substitute fonts

%description
kochi-substitute font.

%prep
%setup -q -n kochi-substitute-20030809

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/fonts/kochi-substitute
install -c -m 644 kochi-mincho-subst.ttf $RPM_BUILD_ROOT%{_datadir}/fonts/kochi-substitute/kochi-mincho.ttf
install -c -m 644 kochi-gothic-subst.ttf $RPM_BUILD_ROOT%{_datadir}/fonts/kochi-substitute/kochi-gothic.ttf
install -c -m 644 $RPM_SOURCE_DIR/fonts.scale.kochi-substitute \
                  $RPM_BUILD_ROOT%{_datadir}/fonts/kochi-substitute/

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%doc COPYING README* docs
%{_datadir}/fonts/kochi-substitute

%changelog
* Fri Jul 27 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 20030809
- Rebuilt for Fedora
* Mon Aug 11 2003 - mfabian@suse.de
- add correct substkit-20030809.tar.bz2, last one was broken.
* Mon Aug 11 2003 - mfabian@suse.de
- update to version 20030809. Together with the patches to
  gs_ttf.ps in Ghostscript, this update makes vertical printing
  work.
* Thu Jul 17 2003 - mfabian@suse.de
- make file names of substitute fonts exactly the same as the
  file names of the original Kochi fonts for better compatibility,
  especially for CJK-LaTeX.
* Thu Jul 17 2003 - mfabian@suse.de
- fix fonts.scale.*
* Wed Jul 16 2003 - mfabian@suse.de
- new package: version 20030628
