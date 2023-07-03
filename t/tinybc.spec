%undefine _debugsource_packages

Summary: Tiny BASIC for Curses
Name: tinybc
Version: 0.8.6
Release: 3.1
License: LGPL
Group: Development/Language
URL: https://tinybc.sourceforge.net/
Source: https://sourceforge.net/projects/tinybc/files/%{name}-%{version}.zip

%description
tinybc is a BASIC interpreter for the curses character screen handling library,
which fully corresponds to the Tiny BASIC specification. The engine is thread-
safe and can be embedded into other code. Can be used as a game or a minimalist
challenge.

%prep
%setup -q
sed -i 's|-lcurses|-lcurses -Wl,--allow-multiple-definition|' Makefile

%build
make clean
make

%install
install -Dm755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dm644 %{name}.1.gz $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1.gz

%files
%doc README LICENSE *.bas tinybctut.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Wed Jan 31 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.6
- Rebuilt for Fedora
