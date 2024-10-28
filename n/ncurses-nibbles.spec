%undefine _debugsource_packages

Summary: NCurses based nibbles game
Name: ncurses-nibbles
Version: 0.0.4
Release: 12.1
License: GPL
Group: Games/Arcade
Source0: https://www.earth.li/projectpurple/files/nibbles-v%version.tar.gz
Patch0: nibbles-Makefile.patch
Patch1: nibbles-window.patch
Patch2: nibbles-score.patch
URL: https://www.earth.li/projectpurple/progs/nibbles.html
BuildRequires: ncurses-devel

%description
Nibbles is a remake of the classic Snake/Nibbles game in ncurses. I am
sure that better nibbles games exist, but I thought that I'd write an
ncurses one to learn how.

%prep
%setup -q -n nibbles-v%version
%patch 0 -p1
%patch 1 -p1
%patch 2 -p1

%build
export LDFLAGS=-Wl,--allow-multiple-definition
make DATADIR=%{_datadir}

%install
rm -rf %{buildroot}
install -Dm755 nibbles %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_datadir}/nibbles
touch %{buildroot}%{_datadir}/nibbles/nibbles.score
cp -a nibbles.levels %{buildroot}%{_datadir}/nibbles

%files
%{_bindir}/%{name}
%config(noreplace) %{_datadir}/nibbles/nibbles.score
%{_datadir}/nibbles/nibbles.levels
%doc README TODO HISTORY CREDITS example.nibblerc

%changelog
* Sun Dec 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.4
- Rebuilt for Fedora
* Thu Feb 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.0.4-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * vendor-tag for nibbles
  * postclean-05-filetriggers for spec file
* Wed Dec 16 2009 Fr. Br. George <george@altlinux.ru> 0.0.4-alt1
- Initial build from PLD
