Name:		marst
Summary:	Algol-to-C translator
Version:	2.7
Release:	1
Source0:	http://www.algol60.org/translators/%{name}-%{version}.tar.gz
URL:		http://www.gnu.org/software/marst/marst.html
Group:		Development/Languages
License:	GPLv3

%description
MARST is an Algol-to-C translator. It automatically translates programs written
in the algorithmic language Algol 60 to the C programming language.

%prep
%setup -q

%build
%configure
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%clean
rm -rf $RPM_BUILD_ROOT 

%files
%doc AUTHORS ChangeLog COPYING README examples
%{_libdir}/libalgol.*
%{_includedir}/algol.h
%{_bindir}/macvt
%{_bindir}/marst

%changelog
* Mon Oct 07 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2.7
- Rebuild for Fedora
* Fri Feb 17 2017 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2.4-10
- (aad859b) MassBuild#1257: Increase release tag
