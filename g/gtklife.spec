Summary: Conway's game of life
Name: gtklife
Version: 5.2
Release: 1
License: GPL
Group: Amusements/Games
URL: http://ironphoenix.org/gtklife/
Source: http://ironphoenix.org/gtklife/gtklife-%{version}.tar.gz
BuildRequires: gtk2-devel

%description
GtkLife is a fast and user-friendly implementation of Conway's Life program.
It is something comparable to the venerable XLife in speed, but with a more
modern and featureful GUI. It is not tied to any particular desktop
environment.

%prep
%setup -q

%{__cat} <<EOF >gtklife.desktop
[Desktop Entry]
Name=Conway's Game Of Life
Comment=Create patterns and see them evolve
Icon=gtklife
Exec=gtklife
Terminal=false
Encoding=UTF-8
Type=Application
Categories=GNOME;Application;Game;
EOF

%build
%configure --with-gtk2
make %{?_smp_mflags} CFLAGS+=-Wno-format-security

%install
#make_install
install -d %{buildroot}%{_datadir}/%{name}
cp -a graphics patterns %{buildroot}%{_datadir}/%{name}
install -Dm755 gtklife %{buildroot}%{_bindir}/%{name}
install -Dp -m0644 icon_48x48.png %{buildroot}%{_datadir}/pixmaps/gtklife.png
install -Dp -m0644 gtklife.desktop %{buildroot}%{_datadir}/applications/gtklife.desktop

%clean
rm -rf %{buildroot}

%files
%doc COPYING NEWS README doc/*
%{_bindir}/gtklife
%{_datadir}/applications/gtklife.desktop
%{_datadir}/gtklife
%{_datadir}/pixmaps/gtklife.png

%changelog
* Fri Sep 06 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 5.2
- Rebuilt for Fedora
* Sat Sep 16 2006 Dag Wieers <dag@wieers.com> - 5.1-2
- Use configure and --with-gtk2 if applicable.
* Fri Sep 15 2006 Dag Wieers <dag@wieers.com> - 5.1-1
- Updated to release 5.1.
* Tue Sep 12 2006 Dag Wieers <dag@wieers.com> - 5.0-1
- Updated to release 5.0.
* Sat Jun 04 2005 Dag Wieers <dag@wieers.com> - 4.2-1
- Updated to release 4.2.
* Wed Sep 22 2004 Dag Wieers <dag@wieers.com> - 4.1-1
- Updated to release 4.1.
* Wed Aug 25 2004 Dag Wieers <dag@wieers.com> - 4.0-1
- Updated to release 4.0.
* Sat Apr 10 2004 Dag Wieers <dag@wieers.com> - 2.1-1
- Updated to release 2.1.
* Fri Apr 09 2004 Dag Wieers <dag@wieers.com> - 2.0-2
- Small cosmetic changes.
* Mon Apr 05 2004 Dag Wieers <dag@wieers.com> - 2.0-1
- Initial package. (using DAR)
