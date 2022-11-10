%undefine _debugsource_packages

Name:           ascii-patrol
Version:        1.7
Release:        1
Summary:        Text based Moon Patrol clone
License:        GPL-3.0-only
Group:          Amusements/Games/Action/Arcade
URL:            http://ascii-patrol.com/
Source:         https://github.com/msokalski/ascii-patrol/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(libpulse)
Requires:       curl

%description
Ascii Patrol is an ASCII game project.
It was mainly inspired by "Moon Patrol".

%prep
%autosetup -p1

%build
%make_build

%install
install -D asciipat %{buildroot}%{_bindir}/asciipat

%files
%license LICENSE
%doc README.md
%{_bindir}/asciipat

%changelog
* Sun Oct 23 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.7
- Rebuilt for Fedora
* Wed Dec 30 2020 Matthias Mailänder <mailaender@opensuse.org>
- initial packaging of version 1.7
