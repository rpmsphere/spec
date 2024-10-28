Name:         ucc
Summary:      Your C Compiler
URL:          https://ucc.sourceforge.net/
Group:        Development/Compiler
License:      GPLv2
Version:      1.6.2
Release:      2.1
Source0:      https://sourceforge.net/projects/ucc/files/ucc/1.6/ucc162.zip

%description
UCC is an ANSI C compiler which supports Linux and Windows running on Intel
x86 platform. Its compilation speed is fast and it is suitable for personal
research and instructional use.

%prep
%setup -q -n %{name}

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 driver/ucc %{buildroot}%{_bindir}/ucc
install -Dm755 ucl/ucl %{buildroot}%{_bindir}/ucl
install -Dm644 ucl/assert.o %{buildroot}%{_libdir}/ucl
install -d %{buildroot}%{_includedir}/ucl
install -m644 ucl/linux/include/* %{buildroot}%{_includedir}/ucl

%files
%doc ChangeLog COPYRIGHT GPL.txt REAMDE.txt doc/*
%{_bindir}/ucc
%{_bindir}/ucl
%{_libdir}/ucl
%{_includedir}/ucl

%changelog
* Fri Mar 23 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6.2
- Rebuilt for Fedora
