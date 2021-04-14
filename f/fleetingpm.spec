Name:           fleetingpm
Version:        2.7.1
Release:        4.1
License:        GPL-3.0
Summary:        Fleeting Password Manager
URL:            http://fleetingpm.sourceforge.net/
Group:          Productivity/Security
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  ghostscript-core ImageMagick
BuildRequires:  hicolor-icon-theme
BuildRequires:  gcc-c++ qt4-devel

%description
Fleeting Password Manager is a program that generates pseudo-random
passwords from given master password, URL/ID and user name. The master
password should be common to all passwords and URL/ID should be the url
of the service (e.g. www.facebook.com) or some part of it (e.g.
facebook). Fleeting Password Manager then combines the master password,
URL/ID and the given user name and generates the corresponding login
password.

%prep
%setup -q

%build
qmake-qt4 \
    QMAKE_CFLAGS+="%{optflags}" \
    QMAKE_CXXFLAGS+="%{optflags}" \
    QMAKE_STRIP=""
make %{?_smp_mflags}

%install
make INSTALL_ROOT=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
install -Dm 0644 data/icons/%{name}.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
install -Dm 0644 data/icons/%{name}.svg \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
for size in 48x48 32x32 22x22 16x16 ; do
    install -dm 0755 \
        $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${size}/apps
    convert -resize ${size} data/icons/%{name}.png \
        $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${size}/apps/%{name}.png
done

%files
%doc AUTHORS CHANGELOG COPYING README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.*

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.7.1
- Rebuilt for Fedora
* Tue Mar  6 2012 lazy.kent@opensuse.org
- Update to 2.7.1.
  * Fixed installation (sf#3452640).
* Tue Feb 28 2012 lazy.kent@opensuse.org
- Remove check for unsupported openSUSE versions.
* Tue Dec  6 2011 lazy.kent@opensuse.org
- Update to 2.7.
  * Timeout for master password added.
  * Cosmetic changes.
* Sun Nov  6 2011 lazy.kent@opensuse.org
- Spec clean up.
* Tue Sep 20 2011 lazy.kent@opensuse.org
- Update to 2.6.
  * Stars removed from the main layout.
  * Color change of "Master password" is gradual.
- Remove redundant/obsolete tags/sections from specfile.
- Install icons of various sizes to /usr/share/icons (build
  requires ImageMagick).
* Wed Sep  7 2011 lazy.kent@opensuse.org
- Initial package created - 2.5.
