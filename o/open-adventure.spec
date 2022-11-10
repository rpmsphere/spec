%define oname   advent

Name:           open-adventure
Version:        1.11
Release:        1
Summary:        Forward-port of Colossal Cave Adventure 2.5 from 1995
Group:          Games/Adventure
License:        BSD-2-Clause
URL:            http://www.catb.org/~esr/open-adventure/
Source0:        http://www.catb.org/~esr/open-adventure/%{oname}-%{version}.tar.gz
BuildRequires:  pkgconfig(libedit)
BuildRequires:  python3
BuildRequires:  python3dist(pyyaml)

%description
Colossal Cave Adventure, the 1995 430-point version.

This is the last descendent of the original 1976 Colossal Cave Adventure
worked on by the original authors - Crowther & Woods.  It has sometimes
been known as Adventure 2.5.  The original PDP-10 name 'advent' is used
for the built program to avoid collision with the BSD Games version (see
'adventure' in the bsd-games package).

%prep
%autosetup -p1 -n %{oname}-%{version}

%build
%set_build_flags
export CCFLAGS="$CFLAGS"
%make_build

%install
install -D -m755 advent %{buildroot}%{_bindir}/advent
ln -s advent %{buildroot}%{_bindir}/%{name}

install -D -m644 advent.6 %{buildroot}%{_mandir}/man6/advent.6
ln -s advent.6 %{buildroot}%{_mandir}/man6/%{name}.6

%files
%doc *.adoc NEWS
%license COPYING
%{_bindir}/advent
%{_bindir}/%{name}
%{_mandir}/man6/advent.6*
%{_mandir}/man6/%{name}.6*

%changelog
* Sun Oct 23 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.11
- Rebuilt for Fedora
* Wed Jun 02 2021 akien <akien> 1.9-1.mga8
+ Revision: 1729400
- Version 1.9
* Fri Feb 14 2020 umeabot <umeabot> 1.0-4.mga8
+ Revision: 1515675
- Mageia 8 Mass Rebuild
+ wally <wally>
- replace deprecated %%setup_compile_flags
* Sun Sep 23 2018 umeabot <umeabot> 1.0-3.mga7
+ Revision: 1299972
- Mageia 7 Mass Rebuild
* Sun Sep 17 2017 cjw <cjw> 1.0-2.mga7
+ Revision: 1154895
- pass optflags to make
* Thu Jun 29 2017 akien <akien> 1.0-1.mga6
+ Revision: 1108654
- Version 1.0
* Sun Jun 04 2017 akien <akien> 1.0-0.0692b8a.1.mga6
+ Revision: 1106517
- New snapshot, future version will be 1.0
* Sun Jun 04 2017 akien <akien> 0-0.mga6
+ Revision: 1106497
- Honor Mageia CCFLAGS and LDFLAGS
- imported package open-adventure
