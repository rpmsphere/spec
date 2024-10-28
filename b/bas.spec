Name:               bas
Version:            2.6
Release:            1
Summary:            Classic BASIC interpreter
Source:             https://www.moria.de/~michael/bas/bas-%{version}.tar.gz
URL:                https://www.moria.de/~michael/bas/
Group:              Development/Language
License:            BSD

%description
Bas is an interpreter for the classic dialect of the programming language BASIC.
It is pretty compatible to typical BASIC interpreters of the 1980s. The interpreter
tokenises the source and resolves references to variables and jump targets before
running the program.

%prep
%setup -q

%build
./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm644 lib%{name}.a %{buildroot}%{_libdir}/lib%{name}.a
ranlib %{buildroot}%{_libdir}/lib%{name}.a
install -Dm644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -Dm644 de.mo %{buildroot}%{_datadir}/locale/de/LC_MESSAGES/%{name}.mo

%files
%doc LICENSE NEWS README
%{_bindir}/%{name}
%{_libdir}/lib%{name}.a
%{_mandir}/man1/%{name}.1.*
%{_datadir}/locale/de/LC_MESSAGES/%{name}.mo

%changelog
* Thu Oct 03 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2.6
- Rebuilt for Fedora
