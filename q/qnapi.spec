%undefine _debugsource_packages

Name:           qnapi
Version:        0.2.3
Release:        1.1
Summary:        A NapiProjekt client
Summary(pl):    Klient NapiProjekt
License:        GPL-2.0+
Group:          Productivity/Multimedia/Other
URL:            http://qnapi.github.io/
Source0:        https://github.com/QNapi/qnapi/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  libmediainfo-devel
Requires:       p7zip

%description
QNapi is unofficial clone of NapiProjekt program (http://napiprojekt.pl)
written using Qt5. It's focused to be functional on GNU/Linux and other
Unix-like systems, for which NapiProjekt is not available.

%description -l pl
QNapi jest nieoficjalnym klonem programu NapiProjekt (http://napiprojekt.pl)
napisanym w bibliotece Qt5 z myślą o użytkownikach Linuksa oraz innych
systemów, pod które oryginalny NapiProjekt nie jest dostępny.

%prep
%setup -q
### Fix paths specific for openSUSE
#sed -i 's|doc.path = $${INSTALL_PREFIX}/share/doc/$${TARGET}|doc.path = $${INSTALL_PREFIX}/share/doc/packages/$${TARGET}|' qnapi.pro
sed -i '19i #include <QIcon>' gui/src/forms/subdatawidget.h

%build
%{_qt5_qmake}
%make_build QMAKE=%{_qt5_qmake} PREFIX=%{_prefix}

%install
make INSTALL_ROOT=%{buildroot} install %{?_smp_mflags}
# Add service menu
install -m 644 -D doc/qnapi-download.desktop %{buildroot}%{_datadir}/kde4/services/ServiceMenus/qnapi-download.desktop
install -m 644 -D doc/qnapi-scan.desktop %{buildroot}%{_datadir}/kde4/services/ServiceMenus/qnapi-scan.desktop

## Fix for "wrong-file-end-of-line-encoding" doc/ChangeLog file
sed -i 's/\r//' doc/ChangeLog

%files
%{_bindir}/%{name}
%{_datadir}/icons/*
%{_datadir}/applications/%{name}.desktop
%attr(644,root,root) %{_mandir}/man1/*
%attr(644,root,root) %{_mandir}/*/man1/*
%dir %{_datadir}/kde4
%dir %{_datadir}/kde4/services
%dir %{_datadir}/kde4/services/ServiceMenus
%{_datadir}/kde4/services/ServiceMenus/qnapi-download.desktop
%{_datadir}/kde4/services/ServiceMenus/qnapi-scan.desktop
%{_docdir}/%{name}

%changelog
* Thu Jan 03 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.3
- Rebuilt for Fedora
* Wed Dec 06 2017 Sérgio Basto <sergio@serjux.com> - 0.2.3-1
- Update to 0.2.3
* Tue Jul 19 2016 Sérgio Basto <sergio@serjux.com> - 0.2.1-1
- Update to 0.2.1
* Wed Mar 04 2009 Mariusz Fik <fisiu82@gmail.com> - 0.1.6rc2
- upstream version
* Sat Dec 27 2008 Mariusz Fik <fisiu82@gmail.com> - 0.1.5
- added service menus for KDE4
* Mon Apr 07 2008 Piotr Pacholak <obi.gts@gmail.com>
- 0.1.4
* Sat Mar 01 2008 Piotr Pacholak <obi.gts@gmail.com>
- 0.1.3
* Wed Feb 20 2008 Piotr Pacholak <obi.gts@gmail.com>
- 0.1.2
* Sat Feb 16 2008 Piotr Pacholak <obi.gts@gmail.com>
- 0.1.1
