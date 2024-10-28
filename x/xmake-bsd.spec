%global _name xmake

Name:           xmake-bsd
Version:        1.06
Release:        2.1
Summary:        Powerful project making make program
License:        GPL
Group:          Development/Other
Source0:        %{_name}-%{version}.tar.bz2
URL:            https://apollo.backplane.com/xmake/

%description
XMAKE is similar to other make's out there, but is specifically designed to
allow you to easily construct multiple complex dependencies without getting
screwed by default rulesets. XMake contains a number of features specifically
designed to trivialize the construction of compilation rules.

%prep
%setup -q -n %{_name}

%build
make
perl -pi -e "s#-g -O2 -Wall -Wstrict-prototypes#$RPM_OPT_FLAGS#g" XMakefile
./%{_name}

%install
rm -rf $RPM_BUILD_ROOT
install obj/%{_name} -D $RPM_BUILD_ROOT%{_bindir}/%{name}
install %{_name}.1 -D $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%files 
%doc README RELEASE_NOTES
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Fri May 10 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 1.06
- Rebuilt for Fedora
* Fri Feb 17 2017 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1.06-10
- (2b23943) MassBuild#1257: Increase release tag
