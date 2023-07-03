Name:           qmetro
Version:        0.7.1
Release:        1
License:        GPL-2.0+
Summary:        Map of the Transport System for Many City Subways
URL:            https://sourceforge.net/projects/qmetro/
Group:          Productivity/Other
Source0:        https://sourceforge.net/projects/qmetro/files/source/%{name}-%{version}.zip
BuildRequires:  gcc-c++ qt4-devel hicolor-icon-theme
BuildRequires:  ghostscript ImageMagick
Requires:       pmetro-maps

%description
Vector metro (subway) map for calculating route and getting information
about transport nodes. It's GPL project for creating analog of pMetro
(Muradov B.) and it's using PMZ format. Maps have an open format and can
easily be edited or created.

%prep
%setup -q
sed -i 's/\r$//' AUTHORS LICENSE README

%build
`pkg-config --variable=exec_prefix QtCore`/bin/qmake \
    QMAKE_CFLAGS+="%{optflags}" \
    QMAKE_CXXFLAGS+="%{optflags}" \
    QMAKE_STRIP="" \
    LIBS+=-lz
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make INSTALL_ROOT=$RPM_BUILD_ROOT install
for size in 48x48 32x32 22x22 16x16 ; do
    install -dm 0755 \
        $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${size}/apps
    convert -resize ${size} rc/icons/hicolor/64x64/apps/%{name}.png \
        $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${size}/apps/%{name}.png
done
mv %{buildroot}/tmp/qMetro %{buildroot}%{_datadir}/%{name}
rm -rf %{buildroot}%{_datadir}/%{name}/map
ln -s ../pmetro-maps %{buildroot}%{_datadir}/%{name}/map

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS LICENSE README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.*

%changelog
* Sun Apr 04 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.1
- Rebuilt for Fedora
* Fri May 18 2012 lazy.kent@opensuse.org
- Split off maps packages.
* Wed May  2 2012 lazy.kent@opensuse.org
- Updated maps:
  * Baku
* Fri Mar 30 2012 lazy.kent@opensuse.org
- Update to 0.5.5.
  * Time table.
  * New graphics.
  * Better map render.
  * Fixes.
- Updated maps:
  * Moscow
  * Novosibirsk
  * Samara
- Use pkgconfig(*) as build dependencies.
* Sun Mar  4 2012 lazy.kent@opensuse.org
- Updated maps:
  * Moscow
  * Ekaterinburg
  * Nizhny Novgorod
  * Minsk
  * Saint Petersburg
  * Kiev
- Removed check for unsupported openSUSE versions.
* Fri Dec 16 2011 lazy.kent@opensuse.org
- Updated maps:
  * Moscow
  * Saint Petersburg
  * Ekaterinburg
  * Volgograd
  * Italy (Milan)
  * Denmark (Copenhagen)
- Added Kazakhstan (Almaty) map.
- Added cities lists in descriptions for every country package.
* Fri Nov 25 2011 lazy.kent@opensuse.org
- Updated Moscow and Saint Petersburg maps.
* Wed Nov  2 2011 lazy.kent@opensuse.org
- Updated Moscow map.
* Tue Nov  1 2011 lazy.kent@opensuse.org
- Initial package created - 0.5.2.
