%global debug_package %{nil}

Name:           qownnotes
BuildRequires:  gcc gcc-c++
BuildRequires:  qt5-qtbase
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-gui
BuildRequires:  qt5-qttools qt5-qttools-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtxmlpatterns-devel
BuildRequires:  desktop-file-utils
Requires:       qt5-qtsvg qt5-qtxmlpatterns
License:        GPL-2.0
Group:          System/GUI/Productivity
Summary:        Note-taking app and todo list manager with ownCloud/Nextcloud integration
URL:            http://www.qownnotes.org/
Version:        19.3.0
Release:        1
Source0:        https://sourceforge.net/projects/qownnotes/files/src/%{name}-%{version}.tar.xz

%description
QOwnNotes is the open source notepad and todo list manager, that works together
with the default notes application of ownCloud. So you are able to write down
your thoughts with QOwnNotes and edit or search for them later from your mobile
device (like with CloudNotes or the ownCloud/Nextcloud web-service.

The notes are stored as plain text files and are synced with ownCloud's/
Nextcloud's file sync functionality. Of course other software, like Dropbox can
be used too. I like the concept of having notes accessible in plain text files,
like it is done in the ownCloud notes app, to gain a maximum of freedom, but I
was not able to find a decent desktop note taking tool or a text editor, that
handles them well. Out of this need QOwnNotes was born.

Author
======
Patrizio Bekerle <patrizio@bekerle.com>

%prep
%setup -q
qmake-qt5 .

%build
make

%install
install -D -m 0755 QOwnNotes $RPM_BUILD_ROOT/%{_prefix}/bin/QOwnNotes
install -D -m 0644 PBE.QOwnNotes.desktop $RPM_BUILD_ROOT/%{_datadir}/applications/PBE.QOwnNotes.desktop
install -D -m 0644 images/icons/128x128/apps/QOwnNotes.png $RPM_BUILD_ROOT/%{_datadir}/pixmaps/QOwnNotes.png
install -D -m 0644 images/icons/16x16/apps/QOwnNotes.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/16x16/apps/QOwnNotes.png
install -D -m 0644 images/icons/24x24/apps/QOwnNotes.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/24x24/apps/QOwnNotes.png
install -D -m 0644 images/icons/32x32/apps/QOwnNotes.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/32x32/apps/QOwnNotes.png
install -D -m 0644 images/icons/48x48/apps/QOwnNotes.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/48x48/apps/QOwnNotes.png
install -D -m 0644 images/icons/64x64/apps/QOwnNotes.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/64x64/apps/QOwnNotes.png
install -D -m 0644 images/icons/96x96/apps/QOwnNotes.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/96x96/apps/QOwnNotes.png
install -D -m 0644 images/icons/128x128/apps/QOwnNotes.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/128x128/apps/QOwnNotes.png
install -D -m 0644 images/icons/256x256/apps/QOwnNotes.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/256x256/apps/QOwnNotes.png
install -D -m 0644 images/icons/512x512/apps/QOwnNotes.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/512x512/apps/QOwnNotes.png
install -D -m 0644 languages/QOwnNotes_en.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_en.qm
install -D -m 0644 languages/QOwnNotes_de.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_de.qm
install -D -m 0644 languages/QOwnNotes_fr.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_fr.qm
install -D -m 0644 languages/QOwnNotes_pl.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_pl.qm
install -D -m 0644 languages/QOwnNotes_zh_CN.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_zh_CN.qm
install -D -m 0644 languages/QOwnNotes_zh_TW.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_zh_TW.qm
install -D -m 0644 languages/QOwnNotes_ru.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_ru.qm
install -D -m 0644 languages/QOwnNotes_pt_BR.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_pt_BR.qm
install -D -m 0644 languages/QOwnNotes_pt_PT.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_pt_PT.qm
install -D -m 0644 languages/QOwnNotes_es.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_es.qm
install -D -m 0644 languages/QOwnNotes_nl.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_nl.qm
install -D -m 0644 languages/QOwnNotes_hu.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_hu.qm
install -D -m 0644 languages/QOwnNotes_ja.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_ja.qm
install -D -m 0644 languages/QOwnNotes_it.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_it.qm
install -D -m 0644 languages/QOwnNotes_ar.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_ar.qm
install -D -m 0644 languages/QOwnNotes_uk.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_uk.qm
install -D -m 0644 languages/QOwnNotes_cs.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_cs.qm
install -D -m 0644 languages/QOwnNotes_hr.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_hr.qm
install -D -m 0644 languages/QOwnNotes_ca.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_ca.qm
install -D -m 0644 languages/QOwnNotes_sv.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_sv.qm
install -D -m 0644 languages/QOwnNotes_id.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_id.qm
install -D -m 0644 languages/QOwnNotes_bn.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_bn.qm
install -D -m 0644 languages/QOwnNotes_tr.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_tr.qm
install -D -m 0644 languages/QOwnNotes_tl.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_tl.qm
install -D -m 0644 languages/QOwnNotes_fil.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_fil.qm
install -D -m 0644 languages/QOwnNotes_ceb.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_ceb.qm
install -D -m 0644 languages/QOwnNotes_hi.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_hi.qm
install -D -m 0644 languages/QOwnNotes_hil.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_hil.qm
install -D -m 0644 languages/QOwnNotes_ur.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_ur.qm

%clean  
rm -rf $RPM_BUILD_ROOT  

%files
%doc LICENSE README.md CHANGELOG.md SHORTCUTS.md
%{_bindir}/QOwnNotes
%{_datadir}/pixmaps/QOwnNotes.png
%{_datadir}/icons/hicolor/16x16/apps/QOwnNotes.png
%{_datadir}/icons/hicolor/24x24/apps/QOwnNotes.png
%{_datadir}/icons/hicolor/32x32/apps/QOwnNotes.png
%{_datadir}/icons/hicolor/48x48/apps/QOwnNotes.png
%{_datadir}/icons/hicolor/64x64/apps/QOwnNotes.png
%{_datadir}/icons/hicolor/96x96/apps/QOwnNotes.png
%{_datadir}/icons/hicolor/128x128/apps/QOwnNotes.png
%{_datadir}/icons/hicolor/256x256/apps/QOwnNotes.png
%{_datadir}/icons/hicolor/512x512/apps/QOwnNotes.png
%{_datadir}/QOwnNotes/languages/QOwnNotes_en.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_de.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_fr.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_pl.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_zh_CN.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_zh_TW.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_ru.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_pt_BR.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_pt_PT.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_es.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_nl.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_hu.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_ja.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_it.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_ar.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_uk.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_cs.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_hr.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_ca.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_sv.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_id.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_bn.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_tr.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_tl.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_fil.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_ceb.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_hi.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_hil.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_ur.qm
%{_datadir}/applications/PBE.QOwnNotes.desktop

%dir %{_datadir}/icons/hicolor/512x512/apps
%dir %{_datadir}/icons/hicolor/256x256/apps
%dir %{_datadir}/icons/hicolor/128x128/apps
%dir %{_datadir}/icons/hicolor/96x96/apps
%dir %{_datadir}/icons/hicolor/64x64/apps
%dir %{_datadir}/icons/hicolor/48x48/apps
%dir %{_datadir}/icons/hicolor/32x32/apps
%dir %{_datadir}/icons/hicolor/24x24/apps
%dir %{_datadir}/icons/hicolor/16x16/apps
%dir %{_datadir}/icons/hicolor/512x512
%dir %{_datadir}/icons/hicolor/256x256
%dir %{_datadir}/icons/hicolor/128x128
%dir %{_datadir}/icons/hicolor/96x96
%dir %{_datadir}/icons/hicolor/64x64
%dir %{_datadir}/icons/hicolor/48x48
%dir %{_datadir}/icons/hicolor/32x32
%dir %{_datadir}/icons/hicolor/24x24
%dir %{_datadir}/icons/hicolor/16x16
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/QOwnNotes/languages
%dir %{_datadir}/QOwnNotes

%changelog
* Thu Sep 05 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 19.3.0
- Rebuilt for Fedora
