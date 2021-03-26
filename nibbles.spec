%global debug_package %{nil}

Summary: Curses game ala snake
Name: nibbles
Version: 1.4
Release: 6.1
License: Public Domain
Group: Games/Arcade
Source0: http://www.alge.no/projects/apps/%{name}-%{version}.tar.gz
URL: http://www.alge.no/index.php/C_Programming
BuildRequires: ncurses-devel

%description
Updated Dec. 28, 2007: Added modes and length.
A not so simple game based on Nibbles! 1.2 by Nils Magnus Englund
Code modified and in parts completly rewritten during May/June 2005.

%prep
%setup -q
sed -i 's|-lcurses|-lncurses|' Makefile
sed -i 's|curses\.h|ncurses.h|' *.c

%build
make

%install
rm -rf %{buildroot}
install -Dm755 nibbles %{buildroot}%{_bindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%doc README CHANGES
%{_bindir}/nibbles

%changelog
* Sun Dec 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4
- Rebuild for Fedora
