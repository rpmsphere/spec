%undefine _debugsource_packages

Name:           tetzle
Version:        2.1.6
Release:        1
Summary:        Jigsaw puzzle with tetromino pieces
Group:          Amusements/Games
License:        GPLv3+
URL:            https://gottcode.org/%{name}/
Source:         https://gottcode.org/%{name}/%{name}-%{version}-src.tar.bz2
BuildRequires:  gcc-c++ hicolor-icon-theme
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-linguist

%description
A jigsaw puzzle game that uses tetrominoes for the pieces. Any image can be
imported and used to create puzzles with a wide range of sizes. Games are
saved automatically, and you can select between currently in progress games.

%prep
%setup -q

%build
qmake-qt5 PREFIX=/usr
make %{?_smp_mflags}

%install
make install INSTALL_ROOT=%{buildroot}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man6/%{name}.6.*

%post
update-desktop-database &> /dev/null || :
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%changelog
* Sun Apr 11 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.6
- Rebuilt for Fedora
* Sat May 19 2012 graeme@gottcode.org 2.0.1-1
- New upstream release
* Mon Dec 05 2011 graeme@gottcode.org 2.0.0-4
- Update MIME database and GNOME icon cache
* Fri Nov 11 2011 graeme@gottcode.org 2.0.0-3
- Improve spec file
* Wed May 18 2011 graeme@gottcode.org 2.0.0-2
- Add ownership of data files
* Wed May 18 2011 graeme@gottcode.org 2.0.0-1
- New upstream release
* Sat Apr 02 2011 graeme@gottcode.org 1.2.1-2
- Add dependency on hicolor-icon-theme
* Tue Sep 21 2010 graeme@gottcode.org 1.2.1-1
- Initial package
