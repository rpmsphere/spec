%global debug_package %{nil}

Name: greed
Version: 4.2
Release: 1
Source: http://www.catb.org/~esr/greed/%name-%version.tar.gz
License: BSD-like
Group: Games/Puzzles
Summary: The board puzzle game of Greed
BuildRequires: ncurses-devel
URL: http://www.catb.org/~esr/greed/

%description
The strategy game of Greed. Try to eat as much as possible of the board
before munching yourself into a corner.

%prep
%setup -q

%build
#make SFILE=%_localstatedir/games/%name.hs
make

%install
#mkdir -p %buildroot%_localstatedir/games
install -Dm755 %name %buildroot%_bindir/%name
install -Dm644 %name.6 %buildroot%_mandir/man6/%name.6

%files
%doc README NEWS COPYING greed.xml greed-logo.png
%_mandir/man6/%name.6*
%_bindir/%name

%changelog
* Wed Sep 04 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 4.2
- Rebuild for Fedora
* Sun Apr 19 2015 Fr. Br. George <george@altlinux.ru> 3.11-alt1
- Autobuild version bump to 3.11
* Tue Jun 03 2014 Fr. Br. George <george@altlinux.ru> 3.10-alt1
- Autobuild version bump to 3.10
* Sun Oct 27 2013 Fr. Br. George <george@altlinux.ru> 3.9-alt1
- Autobuild version bump to 3.9
* Sun Jan 22 2012 Fr. Br. George <george@altlinux.ru> 3.8-alt1
- Autobuild version bump to 3.8
* Fri Jul 01 2011 Fr. Br. George <george@altlinux.ru> 3.7-alt1
- Autobuild version bump to 3.7
* Thu Dec 06 2007 Fr. Br. George <george@altlinux.ru> 3.4-alt1
- Initial build for ALT
