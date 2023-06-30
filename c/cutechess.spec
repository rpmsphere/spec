Name: cutechess
Summary: Commandline and graphical interface for playing chess
Version: 1.0.0git
Release: 2.1
Group: Amusements/Games/Board/Chess
License: GPLv3
URL: https://github.com/cutechess/cutechess
Source0: %{name}-master.zip
BuildRequires: qt5-qtbase-devel

%description
Cute Chess is a graphical user interface, command-line interface and a library
for playing chess.

%prep
%setup -q -n %{name}-master

%build
%qmake_qt5
make %{?_smp_mflags}

%install
install -d %{buildroot}%{_bindir}
install -m755 projects/gui/%{name} projects/cli/%{name}-cli %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/applications
install -m644 dist/linux/%{name}.desktop %{buildroot}%{_datadir}/applications
install -d %{buildroot}%{_datadir}/pixmaps
install -m644 projects/gui/res/icons/cutechess_32x32.xpm %{buildroot}%{_datadir}/pixmaps/%{name}.xpm
install -d %{buildroot}%{_mandir}/man5
install -m644 docs/engines.json.5 %{buildroot}%{_mandir}/man5
install -d %{buildroot}%{_mandir}/man6
install -m644 docs/cutechess-cli.6 %{buildroot}%{_mandir}/man6

%files
%doc AUTHORS COPYING README.md TODO
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man5/engines.json.5.*
%{_mandir}/man6/%{name}-cli.6.*
%{_datadir}/pixmaps/%{name}.xpm

%changelog
* Fri Jul 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.0git
- Rebuilt for Fedora
