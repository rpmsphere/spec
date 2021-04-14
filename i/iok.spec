Name:           iok
Version:        2.1.3
Release:        18
Summary:        Indic Onscreen Virtual Keyboard
License:        GPLv2+
URL:            http://pagure.io/iok
Source0:        https://releases.pagure.org/iok/%{name}-%{version}.tar.gz
Source1:        %{name}.appdata.xml
BuildRequires:  desktop-file-utils libXtst-devel
BuildRequires:  gtk3-devel gettext libxml2-devel
BuildRequires:  intltool unique3-devel
BuildRequires:  gcc
Requires:	xkeyboard-config 

%description
iok is Indic Onscreen Keyboard. It provides virtual Keyboard functionality. 
It currently works with Inscript and xkb keymaps for Indian languages. iok
can even try to parse non-inscript keymaps and show them in iok.

%prep
%autosetup

%build
%configure
make CFLAGS="%{optflags}" %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"

mkdir -p %{buildroot}%{_datadir}/appdata
install -m 0644 -p %{SOURCE1} %{buildroot}%{_datadir}/appdata

desktop-file-install \
    --delete-original \
    --copy-generic-name-to-name \
    --dir %{buildroot}/%{_datadir}/applications/ \
     %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog README.old README
%{_bindir}/iok
%{_datadir}/applications/iok.desktop
%{_datadir}/icons/hicolor/16x16/apps/iok.png
%{_datadir}/icons/hicolor/22x22/apps/iok.png
%{_datadir}/icons/hicolor/24x24/apps/iok.png
%{_datadir}/icons/hicolor/32x32/apps/iok.png
%{_datadir}/icons/hicolor/48x48/apps/iok.png
%{_datadir}/icons/hicolor/scalable/apps/iok.svg
%{_mandir}/man1/iok.1.gz
%{_datadir}/appdata/iok.appdata.xml

%changelog
* Mon Jul 20 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.3
- Rebuilt for Fedora

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Parag Nemade <pnemade AT redhat DOT com> - 2.1.3-16
- Add BuildRequires: gcc as per packaging guidelines
- Removed Group tag

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.3-14
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Feb 22 2017 Parag Nemade <pnemade AT redhat DOT com>- 2.1.3-11
- Update project links to pagure.io

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 07 2015 Parag Nemade <pnemade AT redhat DOT com>- 2.1.3-7
- Add appdata file

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 08 2013 Parag Nemade <pnemade AT redhat DOT com>- 2.1.3-2
- Remove vendor tag as per https://fedorahosted.org/fesco/ticket/1077

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 09 2012 Parag Nemade <pnemade AT redhat DOT com>- 2.1.3-1
- Update to 2.1.3 release

* Thu Apr 05 2012 Parag Nemade <pnemade AT redhat DOT com>- 2.1.2-1
- Update to 2.1.2 release

* Wed Mar 28 2012 Parag Nemade <pnemade AT redhat DOT com>- 2.1.1-1
- Update to 2.1.1 release

* Wed Mar 14 2012 Parag Nemade <pnemade AT redhat DOT com>- 2.1.0-2
- Resolves:rh#803227- Fix default locale code set function

* Tue Mar 13 2012 Parag Nemade <pnemade AT redhat DOT com>- 2.1.0-1
- Update to 2.1.0 release

* Fri Mar 02 2012 Parag Nemade <pnemade AT redhat DOT com>- 1.3.13-4
- Resolves:rh#799568 - iok crashed while selecting 'xkb-Malayalam (enhanced Inscript with Rupee Sign)'

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.13-2
- Rebuilt for glibc bug#747377

* Mon Oct 17 2011 Parag Nemade <panemade AT gmail DOT com>- 1.3.13-1
- Update to 1.3.13 release

* Wed Aug 31 2011 Parag Nemade <panemade AT gmail DOT com>- 1.3.12-4
- Resolves: rh#734372 - too many xkb-(null) in the list

* Tue Mar 22 2011 Parag Nemade <panemade AT gmail DOT com>- 1.3.12-3
- Resolves: rh#684652 - iok looks for ~/.m17n not ~/.m17n.d 

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 15 2010 Parag Nemade <panemade AT gmail.com>- 1.3.12-1
- Update to Next release 1.3.12

* Wed Jun 02 2010 Parag Nemade <panemade AT gmail.com>- 1.3.11-1
- Update to Next release 1.3.11

* Mon Mar 08 2010 Parag Nemade <panemade AT gmail.com>- 1.3.10-1
- Update to Next release 1.3.10

* Tue Feb 09 2010 Parag Nemade <panemade@gmail.com>- 1.3.9-1
- Update to Next release 1.3.9

* Mon Oct 26 2009 Parag Nemade <panemade@gmail.com>- 1.3.8-1
- Update to Next release 1.3.8

* Fri Sep 11 2009 Parag Nemade <panemade@gmail.com>- 1.3.7-1
- Update to Next release 1.3.7

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 20 2009 Parag Nemade <panemade@gmail.com>- 1.3.6-1
- Update to Next release 1.3.6
- Add BR:intltool

* Thu Jun 25 2009 Parag Nemade <panemade@gmail.com>- 1.3.5-1
- Update to Next release 1.3.5
- Resolves: rh506623:iok segfaults when changing the language

* Tue Apr 14 2009 Parag Nemade <panemade@gmail.com>- 1.3.4-1
- Update to Next release 1.3.4

* Fri Mar 20 2009 Parag Nemade <panemade@gmail.com>- 1.3.3-1
- Update to Next release 1.3.3

* Fri Mar 06 2009 Parag Nemade <panemade@gmail.com>- 1.3.2-2
- Resolves: rh#488937:iok should show map list as well as switch button in English locale 

* Thu Mar 05 2009 Parag Nemade <panemade@gmail.com>- 1.3.2-1
- Update to Next release 1.3.2

* Thu Feb 26 2009 Parag Nemade <panemade@gmail.com>- 1.3.1-1
- Update to Next release 1.3.1

* Thu Feb 19 2009 Parag Nemade <panemade@gmail.com>- 1.2.1-1
- Update to Next release 1.2.1

* Tue Jan 20 2009 Parag Nemade <panemade@gmail.com>- 1.2.0-2
- Resolves: rh#480289

* Mon Jan 19 2009 Parag Nemade <panemade@gmail.com>- 1.2.0-1
- Update to Next release 1.2.0

* Tue Jan 13 2009 Parag Nemade <panemade@gmail.com>- 1.1.0-1
- Update to Next release 1.1.0

* Wed Dec 17 2008 Parag Nemade <panemade@gmail.com>- 1.0.9-1
- Update to Next release 1.0.9

* Tue Sep 02 2008 Parag Nemade <panemade@gmail.com>- 1.0.8-2
- Added Source URL and modified description 

* Tue Sep 02 2008 Parag Nemade <panemade@gmail.com>- 1.0.8-1
- Update to Next release 1.0.8

* Thu Aug 14 2008 Parag Nemade <panemade@gmail.com>- 1.0.7-3.svn9
- fix directory ownership

* Thu Aug 14 2008 Parag Nemade <panemade@gmail.com>- 1.0.7-2.svn9
- Update to svn snapshot revision 9

* Tue Jun 17 2008 Parag Nemade <panemade@gmail.com>- 1.0.7-1
- Update to Next release 1.0.7

* Thu Jun 12 2008 Parag Nemade <panemade@gmail.com>- 1.0.6-2
- Added missing BR:libXtst-devel

* Fri Apr 25 2008 Parag Nemade <panemade@gmail.com>- 1.0.6-1
- Update to Next release 1.0.6

* Thu Apr 17 2008 Parag Nemade <panemade@gmail.com>- 1.0.2-1
- Update to Next release 1.0.2

* Tue Apr 15 2008 Parag Nemade <panemade@gmail.com>- 1.0.0-1
- Initial specfile for Fedora 
