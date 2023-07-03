Name: yetris
Summary: Tetris(tm) on console
Version: 2.3.0
Release: 4.1
Group: Amusements/Games
URL: hhttps://sourceforge.net/projects/yetris-yetris/
Source0: https://sourceforge.net/projects/yetris-yetris/files/linux/%{name}-%{version}.tar.gz
License: GPLv3
BuildRequires: ncurses-devel

%description
yetris is a Tetris(tm) clone on the terminal. It has colors and highscore,
along with many features found on modern Tetris(tm) implementations.
It's made with C and runs on (most) Linux terminals.

%prep
%setup -q
sed -i -e 's|games|bin|g' -e 's|-Wall|-Wall -Wno-narrowing|' Makefile

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc BUGS ChangeLog COPYING README.md TODO
%{_bindir}/%{name}
%{_datadir}/man/man6/%{name}*
#/var/games/%{name}

%changelog
* Fri Dec 15 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3.0
- Rebuilt for Fedora
