%undefine _debugsource_packages

Name: tetrix
Version: 2.4
Release: 5.1
License: GPL
URL: https://www.catb.org/~esr/tetrix/
Group: Games/Arcade
Summary: An UNIX-hosted, curses-based clone of Tetris
Source: https://www.catb.org/~esr/tetrix/%name-%version.tar.gz
BuildRequires: ncurses-devel xmlto

%description
A clone of the Tetris game. Documentation for the commands is on-screen.
The optional argument is an initial delay loop count between moves; the
game tries to default to a reasonable value.

%prep
%setup -q
rm %name.6

%build
make %name %name.6

%install
install -Dm755 %name %buildroot%_bindir/%name
install -Dm644 %name.6 %buildroot%_mandir/man6/%name.6

%files
%doc README
%_bindir/*
%_mandir/man6/*

%changelog
* Thu May 28 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 2.4
- Rebuilt for Fedora
* Sun Apr 19 2015 Fr. Br. George <george@altlinux.ru> 2.4-alt1
- Autobuild version bump to 2.4
* Tue Aug 23 2011 Fr. Br. George <george@altlinux.ru> 2.3-alt1
- Autobuild version bump to 2.3
- Initial build
* Tue Aug 23 2011 Fr. Br. George <george@altlinux.ru> 0.0-alt1
- Initial 'zero version' commit
