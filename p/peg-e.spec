%undefine _debugsource_packages

Name:           peg-e
Version:        1.2.8
Release:        1
Summary:        Peg solitaire game
Group:          Amusements/Games
License:        GPLv3+
URL:            https://gottcode.org/%{name}/
Source:         https://gottcode.org/%{name}/%{name}-%{version}-src.tar.bz2
BuildRequires:  gcc-c++ hicolor-icon-theme
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-linguist

%description
A peg solitaire game in which you jump over pieces in order to remove them from
the board, ultimately trying to eliminate all but one. The boards are randomly
generated, with 100 levels of difficulty. The game auto-saves, and has undo-redo
capability. Pieces can move horizontally, vertically, and diagonally.

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
%{_datadir}/metainfo/%{name}.appdata.xml
%{_mandir}/man6/%{name}.6.*

%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%changelog
* Sun Apr 04 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.8
- Rebuilt for Fedora
* Sun Jun 10 2012 graeme@gottcode.org 1.1.1.1-1
- New upstream release
* Sat Jun 09 2012 graeme@gottcode.org 1.1.1-1
- New upstream release
* Mon Dec 05 2011 graeme@gottcode.org 1.1.0-4
- Update GNOME icon cache
* Fri Nov 11 2011 graeme@gottcode.org 1.1.0-3
- Improve spec file
* Sat Apr 02 2011 graeme@gottcode.org 1.1.0-2
- Add dependency on hicolor-icon-theme
* Tue Sep 21 2010 graeme@gottcode.org 1.1.0-1
- Initial package
