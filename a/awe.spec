%global debug_package %{nil}

Name: awe
Version: 2012
Release: 12.1
Summary: An Algol W compiler
License: GPLv3
Group: Development/Languages
URL: http://www.algol60.org/15algolwcomp.htm
Source: http://www.algol60.org/translW/awe.tar.gz
BuildRequires: python2
BuildRequires: ocaml
BuildRequires: gc-devel
Obsoletes: aw2c

%description
Awe is a new compiler for the Algol W language. It is intended to to
be a correct and complete implementation of the language described in
the Algol W Language Description, June 1972.

%prep
%setup -q -n %{name}
sed -i 's|/usr/local|/usr|' Makefile
sed -i 's|python |python2 |' Makefile
sed -i "293s|create n|make n ' '|" compiler.ml
sed -i 294d compiler.ml
sed -i '60s|string|bytes|' awe.ml
sed -i 's|-lawe -lm|-Wl,--allow-multiple-definition -lawe -lm|' awe.*

%build
#export OCAMLPARAM="safe-string=0,_"
make build

%install
%make_install
%ifarch x86_64 aarch64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

%files
%doc COPY* README awe.txt
%{_bindir}/%{name}
%{_includedir}/%{name}*
%{_libdir}/libawe.a
%{_mandir}/man?/%{name}*

%changelog
* Thu Oct 18 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2012
- Rebuild for Fedora
