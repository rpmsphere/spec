%undefine _debugsource_packages

Name: mgt
Summary: Game record display/editor for the oriental game of go
Version: 2.31
Release: 3.1
Group: games
License: Free Software
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: ncurses-devel

%description
Mgt allows the user to examine Go game tree files in the SmartGo format.
Mgt also has basic Go game tree editing capabilities and may be used
to create or edit game tree files.

Mailgo is a utility which manages E-mail Go games using mgt as the Go
board editor.  It is included in the mgt package.

%prep
%setup -q
sed -i 's|games/mgt|mgt|' Makefile

%build
make %{?_smp_mflags}

%install
install -d %{buildroot}%{_bindir}
install -m755 mailgo mgt mgt2short wrapmgt %{buildroot}%{_bindir}
install -d %{buildroot}/usr/lib/mgt
install -m644 Rules Sample.01 Sample.02 %{buildroot}/usr/lib/mgt
install -d %{buildroot}%{_mandir}/man6
install -m644 *.6 %{buildroot}%{_mandir}/man6

%files
%doc Prop.lst README Smart-Go.def Spec.io
%{_bindir}/*
/usr/lib/%{name}
%{_mandir}/man6/*

%changelog
* Thu Jul 19 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.31
- Rebuilt for Fedora
