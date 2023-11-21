%undefine _auto_set_build_flags

Name:           mined
Version:        2022.27
Release:        7
Summary:        Powerful Text Editor with Extensive Unicode and CJK Support
Summary(fr):    Puissant éditeur de texte avec Unicode Extensible et support de CJK
License:        GPLv3
URL:            https://towo.net/mined/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:         fix-timestmp-gcc-command.patch
Patch1:         fix-armv7hl-build-in-configure-script.patch
BuildRequires:  gcc
BuildRequires:  desktop-file-utils
BuildRequires:  ncurses-devel

%description
Mined is the first text editor that provided Unicode support in a plain-text
terminal. It now has both extensive Unicode and CJK support offering
many specific features and covering special cases that other editors
are not aware of (like auto-detection features and automatic handling of
terminal variations or Han character information). Basically, it is an
editor tailored to efficient editing of plain text documents and
programs with features and interactive behavior designed for this
purpose.

%description -l fr
Mined est le premier éditeur de texte qui fourni le support Unicode dans un
terminal en texte brut. Il possède maintenant à la fois l'Unicode extensible
et le support de CJK offrant beaucoup de traits spécifiques et couvre les
cas spéciaux que les autres éditeurs n'ont pas conscience (comme
l'auto-détection des caractéristiques et la manipulation des variations entre
les terminaux ou l'information de caractères Han). Fondamentalement, c'est
un éditeur taillé pour l'édition efficace de document en texte brut et
programmes avec des caractéristiques et des comportements interactifs conçus
à cet effet.

%package -n xmined
Summary:        Graphical interface using Xterm of Mined text editor
Summary(fr):    Interface graphique utilisant Xterm pour éditeur de texte Mined
Requires:       xterm
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n xmined
Mined is the first text editor that provided Unicode support in a plain-text
terminal. It now has both extensive Unicode and CJK support offering
many specific features and covering special cases that other editors
are not aware of (like auto-detection features and automatic handling of
terminal variations or Han character information). Basically, it is an
editor tailored to efficient editing of plain text documents and
programs with features and interactive behavior designed for this
purpose.

%description -n xmined -l fr
Mined est le premier éditeur de texte qui fourni le support Unicode dans un
terminal en texte brut. Il possède maintenant à la fois l'Unicode extensible
et le support de CJK offrant beaucoup de traits spécifiques et couvre les
cas spéciaux que les autres éditeurs n'ont pas conscience (comme
l'auto-détection des caractéristiques et la manipulation des variations entre
les terminaux ou l'information de caractères Han). Fondamentalement, c'est
un éditeur taillé pour l'édition efficace de document en texte brut et
programmes avec des caractéristiques et des comportements interactifs conçus
à cet effet.

%prep
%setup -q
# Delete file for Windows :
rm -f ./usrshare/bin/wined.bat
# For rpmlint warning "dangling-relative-symlink" in mined package :
# Symlinks are: CHANGES -> usrshare/package_doc/CHANGES -> usrshare/doc_user/changes.html
rm -f ./CHANGES
cp -p ./usrshare/doc_user/changes.html ./CHANGES
# Convert to UTF8 mined.1.gz and CHANGES :
for f in CHANGES man/%{name}.1; do
  iconv -f iso-8859-1 -t utf8 $f >$f.tmp && \
  touch -r $f $f.tmp && \
  mv $f.tmp $f
done
# Fix desktop-file-validate warning: remove .xpm suffix from icon filename :
sed -i "s/mined.xpm/mined/" ./usrshare/setup_install/mined.desktop
# Fix desktop-file-validate warning: semicolon missing for Categories key :
sed -i s/Utility/Utility\;/ ./usrshare/setup_install/mined.desktop
%patch0 -p0
#patch1 -p0

%build
#./configure
# Optflag isn't applied by default :
make OPT='%{optflags} -fPIE' USRLIBDIR=%{_libdir} ROOTLIBDIR=/%{_lib} %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
# Install mined.desktop and fix desktop-file-validate warning :
desktop-file-install --remove-key Encoding                      \
                     --dir=%{buildroot}%{_datadir}/applications \
%{buildroot}%{_datadir}/%{name}/setup_install/%{name}.desktop
# Remove files for Windows but needed for build
# and useless directory (package_doc, doc_user) :
rm -fr %{buildroot}%{_datadir}/%{name}/{bin,setup_install,conf_user,package_doc,doc_user}

%files
%doc ./usrshare/package_doc/README ./usrshare/doc_user DESCR CHANGES LICENCE.GPL VERSION
%{_bindir}/%{name}
%{_bindir}/minmacs
%{_bindir}/mpico
%{_bindir}/mstar
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/minmacs.1*
%{_mandir}/man1/mpico.1*
%{_mandir}/man1/mstar.1*
%{_datadir}/%{name}/

%files -n xmined
%{_bindir}/umined
%{_bindir}/uterm
%{_bindir}/xmined
%{_mandir}/man1/umined.1*
%{_mandir}/man1/uterm.1*
%{_mandir}/man1/xmined.1*
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/applications/%{name}.desktop

%changelog
* Sun Nov 12 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 2022.27
- Rebuilt for Fedora
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2015.25-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild
* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2015.25-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2015.25-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild
* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2015.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild
* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2015.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild
* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2015.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild
* Thu Jun 01 2017 Matthieu Saulnier <fantom@fedoraproject.org> - 2015.25-1
- Update to 2015.25
 - Upstream moved sources on sourceforge.net
 - Fix timestmp.c gcc compilation flags in makefile (Patch0)
 - Fix ./configure for armv7hl arches (Patch1)
- Fix french translation
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2013.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2013.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013.23-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2013.23-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Mon Sep 09 2013 Dan Horák <dan[at]danny.cz> - 2013.23-2
- fix build on non-x86 64-bit arches
* Sun Aug 18 2013 Matthieu Saulnier <fantom@fedoraproject.org> - 2013.23-1
- Update to 2013.23 version
- Update %%doc macro
- Fix desktop-file-validate warning in %%prep section
- Fix spelling error in Summary(fr) tag and %%description section
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Thu Aug 16 2012 Matthieu Saulnier <fantom@fedoraproject.org> - 2012.22-4
- Fix incomplete French translation
- Fix incomplete removing Group tags
* Thu Aug 16 2012 Matthieu Saulnier <fantom@fedoraproject.org> - 2012.22-3
- Add French translation in spec file
- Remove Group tag in spec file
* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Thu May 10 2012 Matthieu Saulnier <fantom@fedoraproject.org> - 2012.22-1
- update to 2012.22
- fix man page compression in %%files section
* Wed Mar 14 2012 Matthieu Saulnier <fantom@fedoraproject.org> - 2012.21-1
- update to 2012.21 version
* Sun Jan 29 2012 Matthieu Saulnier <fantom@fedoraproject.org> - 2012.20-1
- update to 2012.20 version
* Sun Jan 15 2012 Matthieu Saulnier <fantom@fedoraproject.org> - 2011.19.2-1
- update to 2011.19.2 version
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2011.19-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Wed Nov 23 2011 Matthieu Saulnier <casper.le.fantom@gmail.com> 2011.19-3.1
- add "ncurses-devel" in BuildRequires to fix koji build in el6 branch
* Tue Nov 22 2011 Matthieu Saulnier <casper.le.fantom@gmail.com> 2011.19-3
- remove the dependency on xterm arch specific
* Mon Nov 21 2011 Matthieu Saulnier <casper.le.fantom@gmail.com> 2011.19-2
- add "usrshare/package_doc/README" doc file
- convert to UTF8 the manpage and doc file CHANGES
- add "optflags" in make
- fix help function (F1) doesn't work because file mined.hlp was missing
- move HTML documentation in doc directory
- add xmined subpackage
- remove .xpm suffix from the icon filename in mined.desktop by sed
* Wed Nov 16 2011 Matthieu Saulnier <casper.le.fantom@gmail.com> 2011.19-1
- upgrade to 2011.19 version
* Mon Aug 22 2011 Matthieu Saulnier <casper.le.fantom@gmail.com> 2011.17-1
- remove files for Windows
* Tue Aug 9 2011 Matthieu Saulnier <casper.le.fantom@gmail.com> 2011.17-1
- initial RPM
