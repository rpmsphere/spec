Summary:        OSSII pdf viewer(oxular)
Epoch:          1
Version:        0.8.4
Release:        5
Name:           oxular
Group:          Applications/Multimedia
License:        GPLv2
URL:            http://www.ossii.com.tw/
Source0:       %{name}-%{version}.tar.gz
Source1:	    ossiiui.tar.gz
BuildRequires: 	gettext
BuildRequires:  cmake 
BuildRequires:  kdelibs4, kdelibs4-devel, kde-filesystem, kdelibs-common, kde-settings
BuildRequires:  chmlib-devel
BuildRequires:  djvulibre-devel
BuildRequires:  ebook-tools-devel
BuildRequires:  exiv2-devel
#BuildRequires:  giflib-devel
BuildRequires:  lcms-devel

#%ifnarch s390 s390x
#%if 0%{?fedora} > 9
#BuildRequires:  libgphoto2-devel
#%else
#BuildRequires:  gphoto2-devel
#%endif
#BuildRequires:  sane-backends-devel
#%endif

BuildRequires:  libspectre-devel
#BuildRequires:  libtiff-devel
#BuildRequires:  libXxf86vm-devel
#BuildRequires:  pcre-devel
BuildRequires:  poppler-qt4-devel
#BuildRequires:  qca2-devel
BuildRequires:  qimageblitz-devel
#BuildRequires:  soprano-devel


%{?_kde4_macros_api:Requires: kde4-macros(api) = %{_kde4_macros_api} }
Requires: kdelibs
#Requires: %{name}-libs = %{?epoch:%{epoch}:}%{version}-%{release}
# used by okular
#Requires: kio_msits = %{?epoch:%{epoch}:}%{version}-%{release}

%description
Oxular, a document viewer; support different kinds of documents.
Oxular is based on Okular 0.8.3

%prep
%setup -q -n %{name}-%{version} -a 1

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
cmake ..
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
rm -rf %{buildroot}
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%clean
rm -rf %{buildroot}


%post
touch --no-create %{_kde4_iconsdir}/hicolor &> /dev/null || :

%posttrans
gtk-update-icon-cache %{_kde4_iconsdir}/hicolor &> /dev/null || :
update-desktop-database -q &> /dev/null ||:

%postun
if [ $1 -eq 0 ] ; then
touch --no-create %{_kde4_iconsdir}/hicolor &> /dev/null || :
gtk-update-icon-cache %{_kde4_iconsdir}/hicolor &> /dev/null || :
update-desktop-database -q &> /dev/null ||:
fi


%files
%defattr(-,root,root,-)
%doc COPYING README
%{_kde4_bindir}/*
%{_kde4_appsdir}/oxular/
%{_kde4_configdir}/*
%{_kde4_datadir}/applications/kde4/*
%{_kde4_datadir}/config.kcfg/*
%{_kde4_datadir}/kde4/services/*.desktop
%{_kde4_datadir}/kde4/servicetypes/oxularGenerator.desktop
%{_kde4_libdir}/kde4/oxularGenerator_*.so
%{_kde4_libdir}/kde4/oxularpart.so
%{_kde4_iconsdir}/hicolor/*/apps/oxular.*
%{_kde4_libdir}/liboxularcore.so.1*
%{_libdir}/liboxularcore.so

#%{_kde4_libdir}/kde4/kio_msits.so
#%{_kde4_datadir}/kde4/services/msits.protocol

%defattr(-,root,root)
%lang(zh_TW) %{_datadir}/locale/zh_TW/LC_MESSAGES/*


%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuilt for Fedora
* Thu Oct 13 2011 Wind <yc.yan@ossii.com.tw> - 0.8.4-5
- refit icon size to 60%.

* Wed Sep 14 2011 Wind <yc.yan@ossii.com.tw> - 0.8.4-4
- Add font-family style for default. (shell.cpp)

* Fri Sep  9 2011 Wind <yc.yan@ossii.com.tw> - 0.8.4-3
- Add TextHinting for poppler font rendering.

* Thu Sep  8 2011 Wind <yc.yan@ossii.com.tw> - 0.8.4-2
- Always open annot. edit.

* Thu Aug 25 2011 Wind <yc.yan@ossii.com.tw> - 0.8.4-1
- Always open topic window even if no topic.

* Wed Aug 24 2011 Wind <yc.yan@ossii.com.tw> - 0.8.3-16
- New feature added: Delete all notes from current page.
- l10n po files added.

* Thu Aug  4 2011 Wind <yc.yan@ossii.com.tw> - 0.8.3-15
- Bug fixes.

* Wed Aug  3 2011 Wind <yc.yan@ossii.com.tw> - 0.8.3-14
- Bug fixes.

* Tue Aug  2 2011 Wind <yc.yan@ossii.com.tw> - 0.8.3-13
- Bug fixes.

* Wed Jul 13 2011 Wind <yc.yan@ossii.com.tw> - 0.8.3-12
- hide some icons.

* Fri Jun 24 2011 Chih-Chun Tu <vincent.tu@ossii.com.tw> - 0.8.3-11
- Add BuildRequires: cmake, kdelibs, kdelibs-devel, kde-filesystem, kdelibs-common, kde-settings

* Wed Jul 15 2009 Wind <yc.yan@ossii.com.tw> - 0.0.1-3
- Build for ossii.

* Sun May 03 2009 Than Ngo <than@redhat.com> - 4.2.3-1
- 4.2.3

* Mon Apr 27 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.2-5
- kio_msits subpkg, help avoid kchmviewer conflicts (#484861)

* Wed Apr 22 2009 Than Ngo <than@redhat.com> - 4.2.2-4
- fix build issue on s390(x)

* Fri Apr 03 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.2.2-3
- work around Kolourpaint crash with Qt 4.5 (kde#183850)

* Wed Apr 01 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.2-2
- optimize scriptlets

* Tue Mar 31 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.2.2-1
- KDE 4.2.2

* Mon Mar 09 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.1-3
- gwenview-fix-version.diff

* Sun Mar 08 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.1-2
- missing dependency on kipiplugin.desktop (#489218)

* Fri Feb 27 2009 Than Ngo <than@redhat.com> - 4.2.1-1
- 4.2.1

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7:4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 31 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.0-2
- unowned dirs (#483317)

* Thu Jan 22 2009 Than Ngo <than@redhat.com> - 4.2.0-1
- 4.2.0

* Sat Jan 17 2009 Rakesh Pandit <rakesh@fedoraproject.org> - 4.1.96-2
- Updated with new djvulibre

* Wed Jan 07 2009 Than Ngo <than@redhat.com> - 4.1.96-1
- 4.2rc1

* Mon Dec 22 2008 Rex Dieter <rdieter@fedoraproject.org> - 4.1.85-4
- -devel: Provides: libkipi-devel = 0.3.0

* Thu Dec 18 2008 Rex Dieter <rdieter@fedoraproject.org> - 4.1.85-3 
- respin (eviv2)

* Mon Dec 15 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.85-2
- BR: ebook-tools-devel

* Fri Dec 12 2008 Than Ngo <than@redhat.com> 4.1.85-1
- 4.2beta2
- BR: soprano-devel

* Mon Dec 01 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.80-3
- Obsoletes: libkdcraw libkexiv2 libkipi (F10+)
- cleanup Obsoletes: kdegraphics-extras

* Thu Nov 20 2008 Than Ngo <than@redhat.com> 4.1.80-2
- merged

* Thu Nov 20 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 7:4.1.72-1
- 4.1.80
- BR cmake >= 2.6.2
- make install/fast

* Wed Nov 12 2008 Than Ngo <than@redhat.com> 4.1.3-1
- 4.1.3

* Wed Oct 29 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.2-4
- respin libkexiv2/libkdcraw backport patches

* Mon Oct 06 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.2-3
- respun tarball
- backport latest libkexiv2 and libkdcraw from trunk

* Mon Sep 29 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.2-2
- make VERBOSE=1
- respin against new(er) kde-filesystem

* Fri Sep 26 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.2-1
- 4.1.2

* Fri Aug 29 2008 Than Ngo <than@redhat.com> 4.1.1-1
- 4.1.1

* Thu Aug 21 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.0-6
- f10+: Obsoletes/Provides: libkdcraw-devel, libkexiv2-devel, libkipi-devel

* Wed Aug 20 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.0-5
- fix "last page is not printed" (kde #160860)

* Tue Aug 12 2008 Than Ngo <than@redhat.com> 4.1.0-4
- fix crash in printing review in okular
- update all the configuration each time a document is open in okular

* Tue Jul 29 2008 Than Ngo <than@redhat.com> 4.1.0-3
- respun

* Fri Jul 25 2008 Than Ngo <than@redhat.com> 4.1.0-2
- respun

* Wed Jul 23 2008 Than Ngo <than@redhat.com> 4.1.0-1
- 4.1.0

* Mon Jul 21 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.99-2
- omit conflicting lib{kexiv2,kdcraw,kipi}-devel bits in F-9 builds (#452392)

* Fri Jul 18 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.99-1
- 4.0.99

* Fri Jul 11 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.98-1
- 4.0.98

* Sun Jul 06 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.85-1
- 4.0.85

* Fri Jun 27 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.84-1
- 4.0.84

* Wed Jun 25 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.83-2
- respin for exiv2

* Thu Jun 19 2008 Than Ngo <than@redhat.com> 4.0.83-1
- 4.0.83 (beta2)

* Sun Jun 15 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.82-1
- 4.0.82

* Mon May 26 2008 Than Ngo <than@redhat.com> 4.0.80-1
- 4.1 beta1

* Sat May 10 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.72-2
- add BR qca2-devel (for encrypted ODF documents in Okular)

* Sat May 10 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.72-1
- update to 4.0.72
- drop backported system-libspectre patch

* Thu Apr 03 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-3
- rebuild (again) for the fixed %%{_kde4_buildtype}

* Mon Mar 31 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-2
- rebuild for NDEBUG and _kde4_libexecdir

* Fri Mar 28 2008 Than Ngo <than@redhat.com> 4.0.3-1
- 4.0.3
- drop kdegraphics-4.0.2-poppler07.patch, it's included in 4.0.3

* Thu Mar 20 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.2-4
- backport patch to support poppler 0.7 from KDE 4.0.3

* Wed Mar 19 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.2-3
- respin (poppler)

* Sat Mar 01 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.2-2
- package new FindOkular.cmake (in -devel)

* Thu Feb 28 2008 Than Ngo <than@redhat.com> 4.0.2-1
- 4.0.2

* Fri Feb 01 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.1-2
- build against system libspectre (backported from KDE 4.1)

* Thu Jan 31 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.1-1
- kde-4.0.1

* Tue Jan 08 2008 Rex Dieter <rdieter[AT]fedoraproject.org> 4.0.0-1
- kde-4.0.0

* Fri Dec 14 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.97.0-7
- License: GPLv2
- Obsoletes: -extras(-libs)
- cleanup BR's, scriptlets
- omit devel symlink hacks

* Tue Dec 11 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.97.0-4
- rebuild for changed _kde4_includedir

* Fri Dec 07 2007 Than Ngo <than@redhat.com> 3.97.0-3
- get rid of useless define for F9

* Thu Dec 06 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.97.0-2
- don't hardcode %%fedora
- Requires: lpr (provided by cups) for printing in Okular

* Thu Dec 06 2007 Than Ngo <than@redhat.com> 3.97.0-1
- 3.97.0

* Fri Nov 30 2007 Sebastian Vahl <fedora@deadbabylon.de> 7:3.96.2-1
- kde-3.96.2

* Wed Nov 21 2007 Sebastian Vahl <fedora@deadbabylon.de> 7:3.96.1-1
- kde-3.96.1
- also use epoch in changelog (also backwards)

* Wed Nov 21 2007 Sebastian Vahl <fedora@deadbabylon.de> 7:3.96.0-9
- libs subpkg

* Wed Nov 21 2007 Sebastian Vahl <fedora@deadbabylon.de> 7:3.96.0-8
- %%description updated
- sorted %%BuildRequires
- sorted  %%files

* Mon Nov 19 2007 Sebastian Vahl <fedora@deadbabylon.de> 7:3.96.0-7
- BR: kde-filesystem >= 4
- License is GPLv2+

* Mon Nov 19 2007 Sebastian Vahl <fedora@deadbabylon.de> 7:3.96.0-6
- re-work the "%%if's"

* Mon Nov 19 2007 Sebastian Vahl <fedora@deadbabylon.de> 7:3.96.0-5
- BR: libXcomposite-devel
- BR: libXdamage-devel
- BR: libxkbfile-devel
- BR: libXv-devel
- BR: libXxf86misc-devel
- BR: libXScrnSaver-devel

* Sun Nov 18 2007 Sebastian Vahl <fedora@deadbabylon.de> 7:3.96.0-4
- explicit require on kdebase-runtime (for icons)
- fix copy&paste errors in devel package

* Sat Nov 17 2007 Sebastian Vahl <fedora@deadbabylon.de> 7:3.96.0-3
- name kdegraphics4 on fedora <= 9
- remove all but okular on fedora <= 9
- +BR: kde4-macros(api)
- remove unneeded require for kdepimlibs
- add defattr to devel package

* Thu Nov 15 2007 Sebastian Vahl <fedora@deadbabylon.de> 7:3.96.0-2
- re-added epoch (from kdegraphics3)
- move libspectreOkular.so from devel to normal package

* Thu Nov 15 2007 Sebastian Vahl <fedora@deadbabylon.de> 7:3.96.0-1
- Initial version for Fedora
