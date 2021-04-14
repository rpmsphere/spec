Name: spigot
Summary: Exact real calculator
Version: 20180306
Release: 4.1
Group: math
License: Free Software
URL: http://www.chiark.greenend.org.uk/~sgtatham/spigot/
Source0: https://www.chiark.greenend.org.uk/~sgtatham/spigot/%{name}-%{version}.fe8a7a4.tar.gz
BuildRequires: gmp-devel
BuildRequires: ncurses-devel

%description
spigot is an exact real calculator: that is, you give it a
mathematical expression to evaluate, and it computes it to any
desired precision, by default simply printing digits to standard
output until it is interrupted.

%prep
%setup -q -n %{name}-%{version}.fe8a7a4

%build
%configure
make

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/%{name}
%{_datadir}/doc/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Wed Mar 07 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 20180306
- Rebuilt for Fedora
