%undefine _debugsource_packages

Name: gswiss
Version: 0.1a
Release: 3.1
Summary: A chess tournament management software
License: GPLv2
Group: Games
Source0: https://sourceforge.net/projects/gswiss/files/gswiss-src/gswiss-src_0.1a.tar.gz/gswiss-src_0.1a.tar.gz
URL: https://sourceforge.net/projects/gswiss/

%description
It's a tool to allot the pairings of a chess tournament using the usual
"swiss" pairing system. It is basically desinged to handle a large number
of players.

%prep
%setup -q -n %{name}

%build
make

%install
rm -rf %{buildroot}
install -Dm755 bin/%{name} %{buildroot}%{_bindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%doc README.* COPYING
%{_bindir}/%{name}

%changelog
* Wed May 11 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1a
- Rebuilt for Fedora
