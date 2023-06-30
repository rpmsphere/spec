Name:           m64py
Version:        0.2.5
Release:        2
License:        GPLv3
Source0:        https://sourceforge.net/projects/m64py/files/%{name}-%{version}/%{name}-%{version}.tar.gz
Summary:        A front-end for Mupen64Plus
URL:            https://m64py.sourceforge.net/
BuildArch:      noarch
BuildRequires:  python3
BuildRequires:  python3-qt5-base
BuildRequires:  python3-setuptools
Requires:       python3-qt5-base
Requires:       python3-sdl2

%description
A Qt5 front-end (GUI) for Mupen64Plus, a cross-platform plugin-based Nintendo
64 emulator.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --single-version-externally-managed -O1 --root=%{buildroot} --record=INSTALLED_FILES

%files -f INSTALLED_FILES

%changelog
* Sun Nov 27 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.5
- Rebuilt for Fedora
* Tue Dec 29 2020 RPMBuilder - 0.2.5-2
- SPEC modernisation and minor cleanups
* Tue May 12 2020 RPMBuilder - 0.2.5-1
- Initial release
