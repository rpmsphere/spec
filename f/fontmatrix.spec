Name: fontmatrix
Summary: A fonts manager
Version: 0.9.100
Release: 1
License: GPLv2+
Source0: %{name}-%{version}.tar.gz
Patch0: bug_564904_fix-missing-DSO-icuuc.patch 
Patch1: fontmatrix-0.9.99-arm.patch
Patch2: fontmatrix-0.9.99-rh893080-move-fonts-config-file.patch
Patch3: fontmatrix-0.9.99-format-security-flag.patch
Patch4: fontmatrix-0.9.99-adapt-to-icu-56.patch
BuildRequires: qt5-qtbase-devel freetype-devel qt5-qtwebkit-devel
BuildRequires: desktop-file-utils cmake python2-devel
BuildRequires: openssl-devel podofo-devel libicu-devel
Requires:      fontforge

%description
A powerful and well designed fonts manager.

%prep
%setup -q
%patch 0 -p0
#patch1 -p0
#patch2 -p1
#patch3 -p1
#patch4 -p1

# Though I don't see this is installed but lets remove non-free icon files
rm -f src/icons/application-fontmatrix-*-vectors.svg

%build
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"
%cmake
#cmake -DWANT_HARFBUZZ:bool=true -DWANT_ICU:bool=true -DWANT_PYTHONQT:bool=true -DWANT_PODOFO:bool=true
%cmake_build

%install
%cmake_install

#rpmlint complains Zero-length file
rm -f $RPM_BUILD_ROOT%{_datadir}/fontmatrix/help/en/what_fonts_are.html

desktop-file-install --delete-original  \
    --dir=$RPM_BUILD_ROOT%{_datadir}/applications/ \
    $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See https://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com>-->
<!--
BugReportURL: https://gna.org/bugs/?22101
SentUpstream: 2014-09-18
-->
<application>
  <id type="desktop">fontmatrix.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Manage fonts installed on your system</summary>
  <description>
    <p>
      Font Matrix is an advanced font manager that allows you to view and organise the fonts
      installed on your system. It provides a wide range of information about the fonts installed
      on your system, and allows you to tag them into groups, perform searches on your fonts based
      on font metadata, and easily compare glyphs of fonts.
    </p>
  </description>
  <url type="homepage">https://fontmatrix.be/node/21</url>
  <screenshots>
    <screenshot type="default">https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/fontmatrix/a.png</screenshot>
    <screenshot>https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/fontmatrix/b.png</screenshot>
  </screenshots>
</application>
EOF

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%doc COPYING TODO INSTALL
%{_bindir}/fontmatrix
%{_datadir}/fontmatrix
%{_mandir}/man1/*
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/48x48/apps/fontmatrix.png

%changelog
* Sun Oct 23 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.100
- Rebuilt for Fedora
* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.99-30.r1218
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild
* Thu Feb 02 2017 Sandro Mani <manisandro@gmail.com> - 0.9.99-29.r1218
- Rebuild (podofo)
* Fri Sep 23 2016 Jon Ciesla <limburgher@gmail.com> - 0.9.99-28.r1218
- podofo rebuild
* Wed Aug 10 2016 Parag Nemade <pnemade AT redhat DOT com> - 0.9.99-27.r1218
- Resolves:rh#1295169 - fontmatrix included non-free content
* Fri Apr 15 2016 David Tardon <dtardon@redhat.com> - 0.9.99-26.r1218
- rebuild for ICU 57.1
* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.99-25.r1218
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Thu Oct 29 2015 Eike Rathke <erack@redhat.com> - 0.9.99-24.r1218
- adapt to ICU 56.1 LEFontInstance::getFontTable()
* Wed Oct 28 2015 David Tardon <dtardon@redhat.com> - 0.9.99-23.r1218
- rebuild for ICU 56.1
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.99-22.r1218
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.9.99-21.r1218
- Rebuilt for GCC 5 C++11 ABI change
* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.9.99-20.r1218
- Add an AppData file for the software center
* Mon Jan 26 2015 David Tardon <dtardon@redhat.com> - 0.9.99-19.r1218
- rebuild for ICU 54.1
* Tue Aug 26 2014 David Tardon <dtardon@redhat.com> - 0.9.99-18.r1218
- rebuild for ICU 53.1
* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.99-17.r1218
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.99-16.r1218
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Fri Feb 14 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.9.99-15.r1218
- rebuild for icu 52
* Wed Dec 04 2013 Parag Nemade <pnemade AT redhat DOT com>- 0.9.99-14.r1218
- Shame format-security feature owner not provided any patch (rh#1037066)
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.99-13.r1218
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Mon Jul 22 2013 David Tardon <dtardon@redhat.com> - 0.9.99-12.r1218
- rebuild for ICU ABI break
* Mon May 13 2013 Jon Ciesla <limburgher@gmail.com> - 0.9.99-11.r1218
- Drop desktop vendor tag.
* Fri Feb 08 2013 Parag Nemade <pnemade AT redhat DOT com>- 0.9.99-10.r1218
- Remove vendor tag as per https://fedorahosted.org/fesco/ticket/1077
* Tue Jan 29 2013 Parag Nemade <pnemade AT redhat DOT com> - 0.9.99-9.r1218
- rebuild for icu 50
* Sun Jan 20 2013 Parag Nemade <pnemade AT redhat DOT com> - 0.9.99-8.r1218
- Resolves:rh#893080-Fontmatrix creates a deprecated $HOME/.fonts.conf file
* Wed Sep 19 2012 Jon Ciesla <limburgher@gmail.com> - 0.9.99-7.r1218
- Fix FTBFS on ARM.
* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.99-6.r1218
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Thu May 10 2012 Parag Nemade <pnemade AT redhat DOT com> - 0.9.99-5.r1218
- Commented dead upstream URL.
* Mon Apr 23 2012 Parag Nemade <pnemade AT redhat DOT com> - 0.9.99-4.r1218
- rebuild for icu 49
* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.99-3.r1218
- Rebuilt for c++ ABI breakage
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.99-2.r1218
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Mon Oct 03 2011 Parag Nemade <pnemade AT redhat DOT com> - 0.9.99-1.r1218
- update to latest upstream commit 1218
* Sun Sep 11 2011 Parag Nemade <pnemade AT redhat DOT com> - 0.6.99-16.r1073
- Rebuild against icu 4.8
* Wed May 04 2011 Dan Horák <dan@danny.cz> - 0.6.99-15.r1073
- rebuilt against podofo 0.9.1
* Thu Apr 14 2011 Dan Horák <dan@danny.cz> - 0.6.99-14.r1073
- rebuilt against podofo 0.9.0
* Mon Mar 07 2011 Caolán McNamara <caolanm@redhat.com> - 0.6.99-13.r1073
- rebuild for icu 4.6
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.99-12.r1073
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Tue Nov 02 2010 Dan Horák <dan@danny.cz> - 0.6.99-11.r1073
- rebuilt against podofo 0.8.4
* Fri Oct 22 2010 Dan Horák <dan@danny.cz> - 0.6.99-10.r1073
- rebuilt against podofo 0.8.3
* Tue Jul 27 2010 David Malcolm <dmalcolm@redhat.com> - 0.6.99-9.r1073
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild
* Tue Jun 08 2010 Dan Horák <dan@danny.cz> - 0.6.99-8.r1073
- rebuilt with podofo 0.8.1
* Tue Jun 01 2010 Parag Nemade <pnemade AT redhat.com> - 0.6.99-7.r1073
- qt-devel no longer provides qt-webkit-devel; so add it as BR
* Mon May 03 2010 Parag Nemade <pnemade AT redhat.com> - 0.6.99-6.r1073
- rebuild for podofo-0.8.0-1.fc14
* Fri Apr 02 2010 Caolán McNamara <caolanm@redhat.com> - 0.6.99-5.r1073
- rebuild for icu 4.4
* Tue Feb 16 2010 Parag <pnemade AT redhat.com> - 0.6.99-4.r1073
- Resolves: rh#561044,rh#532882:- Remove broken fontmatrix shaper
- Resolves: rh#564904:-ImplicitDSOLinking 
* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 0.6.99-3.r1073
- rebuilt with new openssl
* Tue Aug 11 2009 Parag <pnemade@redhat.com> - 0.6.99-2.r1073
- update to svn revision 1073
- Fix Source Audit 2009-08-10
* Tue Aug 04 2009 Parag <pnemade@redhat.com> - 0.6.99-1.r1072
- update to svn revision 1072
* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3.r1063
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Mon Jul 13 2009 Parag <pnemade@redhat.com> - 0.6.0-2.r1063
- Add missing BRs:python-devel podofo-devel libicu-devel
* Mon Jul 13 2009 Parag <pnemade@redhat.com> - 0.6.0-1.r1063
- update to svn revision 1063
* Fri Apr 24 2009 Parag <pnemade@redhat.com> - 0.5.0-2.r931
- update to svn revision 931
* Fri Mar 20 2009 Parag <pnemade@redhat.com> - 0.5.0-1.r900
- update to svn revision 900
* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Fri Jan 16 2009 Tomas Mraz <tmraz@redhat.com> - 0.4.2-3
- rebuild with new openssl
* Tue Jun 10 2008 Parag <pnemade@redhat.com> - 0.4.2-2
- Resolves: rh#449406:FTBFS fontmatrix-0.4.2-1.fc9
* Tue Apr 08 2008 Parag <pnemade@redhat.com> - 0.4.2-1.fc9
- Update to 0.4.2
* Mon Apr 07 2008 Parag <pnemade@redhat.com> - 0.4.0-2.fc9
- Add support for Shaper functionality.
* Fri Apr 04 2008 Parag <pnemade@redhat.com> - 0.4.0-1.fc9
- Update to 0.4.0
* Mon Feb 11 2008 Parag <pnemade@redhat.com> - 0.3.1-2
- Rebuild for gcc 4.3
* Wed Jan 23 2008 Parag <pnemade@redhat.com> - 0.3.1-1
- Update to 0.3.1
* Mon Jan 14 2008 Parag <pnemade@redhat.com> - 0.3.0-4.r289
- update to svn revision 289(Stable release of 0.3.0 version)
* Thu Dec 27 2007 Parag <pnemade@redhat.com> - 0.3.0-3.r270
- update to svn revision 270
- Added Requires:fontforge
* Thu Dec 27 2007 Parag <pnemade@redhat.com> - 0.3.0-3.r270
- update to svn revision 270
* Fri Dec 21 2007 Parag <pnemade@redhat.com> - 0.3.0-3.r263
- Fixed license tag
- update to new svn checkout
- drop unnecessary BR: qt4-x11
* Tue Dec 18 2007 Parag <pnemade@redhat.com> - 0.3.0-2.r253
- Added BR:cmake
* Mon Dec 17 2007 Parag <pnemade@redhat.com> - 0.3.0-1.r253
- New upstream svn checkout
* Fri Dec 14 2007 Parag <pnemade@redhat.com> - 0.2-14.3.fc8
- Some spec cleanup
* Fri Dec 14 2007 Parag <pnemade@redhat.com> - 0.2-14.2.fc8
- Initial spec for Fedora.
* Mon Nov 26 2007 <mrdocs@scribus.info> - 0.2-14.1
- Initial upstream spec.
