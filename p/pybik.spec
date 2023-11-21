%global __python3 /usr/bin/python3.10

Name:           pybik
Version:        3.0
Release:        13.1
License:        GPLv3+
Summary:        Rubik's cube game
Group:          Games/Puzzles
URL:            https://launchpad.net/pybik/
Source:         https://launchpad.net/pybik/trunk/%{version}/+download/pybik-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3-setuptools
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(gl)
BuildRequires:  freeglut-devel
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  help2man
BuildRequires:  desktop-file-utils
BuildRequires:  ImageMagick
BuildRequires:  qt5-qtbase-devel
BuildRequires:  python3-docutils
BuildRequires:  python3.10
Requires:  python3.10
Requires:  python3-qt5
Requires:  python3-pyicu

%description
Pybik is a 3D puzzle game about the cube invented by Ernő Rubik.
* Different 3D puzzles - up to 10x10x10:
  cubes, towers, bricks, tetrahedra and prisms
* Solvers for some puzzles
* Pretty patterns
* Editor for move sequences
* Changeable colors and images

%prep
%setup -q
sed -i 's|self, args, nargs, NULL|self, args, nargs|' csrc/*
sed -i 's|tstate->exc_|tstate->curexc_|' csrc/_qt_qtwogl.cpp csrc/_qtexec_.cpp

%build
%py3_build ||:
sed -i '/tp_print = 0/d' build/temp.linux-*/pybiklib/ext/_qt_qtwogl.cpp
%py3_build

%install
%py3_install
cp -R build/share/models %{buildroot}%{_datadir}/pybik/models
cp -a build/share/locale %{buildroot}%{_datadir}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
  data/app-meta/pybik.desktop 
rm -fr %{buildroot}%{_datadir}/pixmaps
for size in 256 128 64 48 32 24 22 14 ; do
    install -dm 0755 \
        %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps
    install -m 644 build/share/icons/$size/pybik.png \
        %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/%{name}.png
done
#chmod 755 %{buildroot}%{python3_sitearch}/pybiklib/{model,pybik,modelcommon}.py
#chmod 755 %{buildroot}%{python3_sitearch}/pybiktest/{runner,utils}.py
sed -i 's|%{buildroot}||' %{buildroot}%{python3_sitearch}/pybiklib/config.py
%find_lang pybik

%files -f %{name}.lang
%doc COPYING README NEWS
%{_bindir}/pybik
%{python3_sitearch}/*
%{_datadir}/pybik
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/pybik.desktop

%changelog
* Sun Apr 9 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0
- Rebuilt for Fedora
* Thu Mar 02 2017 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2.1-3
- (8ea10d4) MassBuild#1273: Increase release tag
