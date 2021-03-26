#
# spec file for package cutegram
#
# Copyright 2015 Buschmann <buschmann23@opensuse.org>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#

# norootforbuild


Name:               cutegram
Summary:            Telegram Client
Version:            2.3.0
Release:            1.2
License:            GPL-3.0
Group:              System/GUI/KDE
Source0:            http://aseman.co/downloads/cutegram/2/%{name}-src-%{version}.tar.gz
BuildRoot:          %{_tmppath}/%{name}-%{version}-build

Url:                http://aseman.co/en/products/cutegram/

BuildRequires:      qtelegram-devel
BuildRequires:      pkgconfig(openssl)
BuildRequires:      pkgconfig(Qt5Gui)
BuildRequires:      pkgconfig(Qt5Qml)
BuildRequires:      pkgconfig(Qt5Quick)
BuildRequires:      pkgconfig(Qt5Sql)
BuildRequires:      pkgconfig(Qt5DBus)
BuildRequires:      pkgconfig(Qt5Xml)
BuildRequires:      pkgconfig(Qt5Multimedia)
BuildRequires:      pkgconfig(Qt5WebKit)
BuildRequires:      pkgconfig(Qt5WebKitWidgets)
BuildRequires:      pkgconfig(sqlite3)

%description
Cutegram is created to make a better client for Telegram on GNU/Linux
desktops. It has smart and beautiful user interface that supports drag
and drop to send files and delete or forward messages.

%prep
%setup -q -n %{name}-%{version}-src
sed -i 's|qtelegram-ae|qtelegram|' Cutegram/Cutegram.pro

%build
  mkdir build
  pushd build
  qmake-qt5 ..
  make
  popd

  
%install
  pushd build
  %qmake5_install
  popd
  
  %suse_update_desktop_file -r Cutegram Qt KDE Network InstantMessaging
  
# not needed
  rm -rf %{buildroot}%{_datadir}/%{name}/icons
  
  %fdupes $RPM_BUILD_ROOT/%{_datadir}/
  

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
  rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc GPL.txt LICENSE license.txt README.md
%attr(755, root, root) %{_bindir}/%{name}
%{_datadir}/applications/Cutegram.desktop
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/%{name}.png
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/*
%dir %{_datadir}/icons/hicolor/*/apps
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
* Sat May 23 2015 ecsos@opensuse.org
- update to 2.3.0
  * Sticker recieving support
  * Sticker sending support (experimental)
  * Windows version move out from experimental state
  * Many improvement on Windows version look and ui
  * New notification and UI styles on windows 8
  * Many improvement on smooth scroll
  * API Layer 23 support
  * Many other bugfix and improvements
* Sun May 17 2015 ecsos@opensuse.org
- update to 2.2.1
  * Smooth Scroll
  * System tray icon color on configure page
  * Update translations
  * Many bugfixes and improvements
* Thu May  7 2015 buschmann23@opensuse.org
- use BuildRequires libqt5-qtmultimedia-devel instead of pkgconfig(Qt5Multimedia)
  because in some repos there are more than one provider of that
* Thu May  7 2015 buschmann23@opensuse.org
- updated to version 2.2.0
  + Link preview (disabled on trusty, because of some problems)
  + Audio Recorder
  + Audio Player
  + Focus on User messages using click on their messages
  + New messages separator
  + Mention and Hashtag support
  + Add new contact dialog on contact list
  + Better scroll bars
  + An option to disable badges
  + Update and Add new translations
  + Improvement on Secret chat
  + Non-contact chat bugfix
  + Many other improvements and bugfixes
- use libqtelegram-ae Aseman fork instead of libqtelegram
* Sun Mar 29 2015 buschmann23@opensuse.org
- updated to version 2.1.1
  + Smart scroll bar for dialog list
  + Username and Hashtag suggestion
  + Update translations and add Portuguese (Portugal), Spanish and
    Chinese (Taiwan) translations.
  + Master color enabled again.
  + Search selected text on the web.
  + Custom notifications for contact lists.
  + Speed improvement
  + Mac OS X 32bit support.
  + Bugfix on ubuntu packaging.
  + Video thumbnail bugfix on Windows and Mac
  + Many other improvements and Bug fixes
* Thu Mar 12 2015 buschmann23@opensuse.org
- updated to version 2.1.0
  + Theme Support (Master Color feature temporary disabled)
  + Many improvements on user interface
  + Update translations and add French, UK English, Italian, Netherland
    dutch, Brazil Portuguese and Serbian.
  + Many improvements and Bug fixes
* Mon Mar  9 2015 buschmann23@opensuse.org
- added missing requirement: libQt5Sql5-sqlite
* Fri Feb 20 2015 buschmann23@opensuse.org
- added missing requirements: libqt5-qtquickcontrols, libqt5-qtgraphicaleffects,
  libQt5Multimedia5
* Tue Feb 17 2015 buschmann23@opensuse.org
- updated to version 2.0.0
* Thu Feb 12 2015 buschmann23@opensuse.org
- use source service
* Mon Feb  2 2015 buschmann23@opensuse.org
- updated to version 1.0.3
  + add Estonian translations
  + improve on copy action
  + disable visual effects option
  + fix firstname and lastname validator bug
  + fix could not send message to non-contacts users
- removed cutegram-1.0.2-additional-translations.patch, translations
  are now included upstream
- removed lang-de.ts and lang-et.ts files, now included upstream
* Mon Jan 19 2015 buschmann23@opensuse.org
- added estonian translation by sander85
- added german translation by Buschmann
* Mon Jan 19 2015 buschmann23@opensuse.org
- initial package
