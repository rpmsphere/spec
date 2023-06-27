Name:           wxEphe
Version:        1.8
Release:        1
Summary:        Astronomical ephemeris for the Sun, Moon and solar system planets
License:        GPL-3.0
Group:          Productivity/Scientific/Astronomy
URL:            https://www.jpmr.org/
Source:         https://sourceforge.net/projects/wxephe/files/wxEphe-%version/wxEphe-%version.tar.xz
BuildRequires:  libtool
BuildRequires:  gcc-c++
BuildRequires:  wxGTK3-devel

%description
wxEphe displays astronomical ephemeris for the Sun, the Moon and
solar system planets, given the date and observer's location.

%prep
%setup -q

%build
autoreconf -fi
%configure --with-wx-config=wx-config-3.2
make %{?_smp_mflags}

%install
%make_install
%find_lang %name

%files -f %name.lang
%doc COPYING
%{_bindir}/wxEphe
%{_datadir}/applications/wxEphe.desktop
%{_datadir}/pixmaps/wxEpheIcon.png

%changelog
* Sun May 21 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.8
- Rebuilt for Fedora
* Sat Aug 12 2017 jengelh@inai.de
- Update to new upstream release 1.4
- An unspecified set of fixes was applied.
* Wed Dec 23 2015 jengelh@inai.de
- Initial package (version 1.3) for build.opensuse.org
