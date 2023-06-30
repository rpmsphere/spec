Name:           asclock
BuildRequires:  libX11-devel, libXpm-devel, libXext-devel, imake
License:        GPL v2 or later
Group:          Amusements/Toys/Clocks
Version:        2.0.12
Release:        596.1
Summary:        AfterStep digital clock
URL:            https://www.tigr.net/afterstep/
Source:         asclock-%{version}.tar.bz2
Patch:          asclock-gcc4.diff

%description
A swallowable applet shows clock and calendar. Supports themes for
different looks.

%prep
%setup -q
%patch
sed -i 's|gcc|gcc -Wl,--allow-multiple-definition|' Imakefile

%build
rm -f languages/english/*~
./configure <<EOF
shaped
1
EOF
make

%install
make DESTDIR=$RPM_BUILD_ROOT install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/asclock
cp -ar themes languages $RPM_BUILD_ROOT%{_datadir}/asclock

%files
%{_bindir}/asclock
%{_datadir}/asclock

%changelog
* Thu Sep 22 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.12
- Rebuilt for Fedora

* Sat Sep 17 2011 jengelh@medozas.de
- Remove redundant tags/sections from specfile
- Use %%_smp_mflags for parallel build

* Fri Aug  4 2006 schwab@suse.de
- New package.
