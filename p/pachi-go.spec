%undefine _debugsource_packages

Name: pachi-go
Summary: Engine for the game of go/weiqi/baduk
Version: 12.80
Release: 1
Group: Games
License: GPLv2
URL: https://pachi.or.cz/
Source0: https://github.com/pasky/pachi/archive/pachi-pachi-%{version}.tar.gz
Source1: pachi-data-extra.zip
BuildRequires: boost-devel
Requires: pachi-go-data

%description
Pachi is a reasonably strong engine for the ancient game of go.
(https://senseis.xmp.net/?Go)

The default engine plays by Chinese rules and should be about 7d KGS
strength on 9x9. On 19x19 it can hold a solid KGS 2d rank on modest
hardware (Raspberry Pi 3, dcnn) or faster machine (e.g. six-way Intel
i7) without dcnn. When using a large cluster (64 machines, 20 cores each),
it maintains KGS 3d to 4d and has won e.g. a 7-stone handicap game against
Zhou Junxun 9p.

By default, Pachi currently uses the UCT engine that combines Monte Carlo
approach with tree search; UCB1AMAF tree policy using the RAVE method is
used for tree search, while the Moggy playout policy using 3×3 patterns
and various tactical checks is used for the semi-random Monte Carlo
playouts. Large-scale board patterns and dcnn are used in the tree
search. Technical information (only slightly dated) about Pachi's
architecture and algorithms can be found in Petr Baudis' Master's Thesis:
https://pachi.or.cz/

%package data
Summary: Pachi go engine data files
BuildArch: noarch

%description data
This package contains data files required by Pachi. They include
large patterns, opening book and dcnn.

%prep
%setup -q -n pachi-pachi-%{version} -a 1
mkdir -p .git
touch .git/HEAD .git/index

%build
make %{?_smp_mflags} DCNN=0 DATADIR=/usr/share/%{name}

%install
make install install-data PREFIX=%{buildroot}/usr DATADIR=%{buildroot}%{_datadir}/%{name}
mv %{buildroot}%{_bindir}/pachi %{buildroot}%{_bindir}/%{name}

%files
%doc COPYING CREDITS HACKING README.md TODO
%{_bindir}/%{name}

%files data
%{_datadir}/%{name}

%changelog
* Sun Jun 11 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 12.80
- Rebuilt for Fedora
