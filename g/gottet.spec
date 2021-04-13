%global debug_package %{nil}

Name:           gottet
Version:        1.1.9
Release:        1
Summary:        Falling blocks game
Group:          Amusements/Games
License:        GPLv3+
URL:            http://gottcode.org/%{name}/
Source:         http://gottcode.org/%{name}/%{name}-%{version}-src.tar.bz2
BuildRequires:  gcc-c++ hicolor-icon-theme
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-linguist

%description
A tetris clone using the Qt GUI toolkit.

%prep
%setup -q

%build
qmake-qt5 PREFIX=/usr
make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_mandir}/man6/gottet.6.*
%{_datadir}/metainfo/gottet.appdata.xml

%postun
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%changelog
* Sun Apr 04 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.9
- Rebuild for Fedora
* Mon Dec 05 2011 graeme@gottcode.org 1.0.4-4
- Update GNOME icon cache
* Fri Nov 11 2011 graeme@gottcode.org 1.0.4-3
- Improve spec file
* Sat Apr 02 2011 graeme@gottcode.org 1.0.4-2
- Add dependency on hicolor-icon-theme
* Sat Oct 02 2010 graeme@gottcode.org 1.0.4-1
- New upstream release
* Tue Sep 21 2010 graeme@gottcode.org 1.0.3-1
- Initial package
