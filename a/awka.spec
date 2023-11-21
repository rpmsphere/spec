Name:          awka
Version:       0.7.5
Release:       19.1
Summary:       Translator of the AWK programming language to ANSI-C
Group:         Applications/Text
URL:           https://awka.sourceforge.net/
Source:        https://awka.sourceforge.net/%{name}-%{version}.tar.gz
Patch0:        awka-%{version}-DESTDIR.patch
License:       GPL

%description
Awka is an open-source implementation of the AWK programming language and is actually two products:
 - the AWK to C translator
 - a library against which the C code is linked

Awka is not an interpreter like Gawk, Mawk or Nawk, but instead it converts the program to ANSI-C,
then compiles this using gcc or a native C compiler to create a binary executable. This means you
must have an ANSI C compiler present on your system for Awka to work.

%prep
%setup -q
%patch0 -p1

%build
export CFLAGS="-O2 -g -pipe -Wall -Wno-format-security -fPIE"
./configure --prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_bindir}/awka
%{_libdir}/libawka.so*
%{_libdir}/libawka.a
%{_includedir}/libawka.h
%{_mandir}/man[15]/*
%doc ACKNOWLEDGEMENTS CHANGELOG.txt PROBLEMS.txt README.txt TODO.txt

%changelog
* Fri Jun 17 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.5
- Rebuilt for Fedora
* Tue Oct 28 2008 Tiziana Ferro <tiziana.ferro@email.it> 0.7.5-2mamba
- rebuild
- update Group in devel package
* Wed Nov 16 2005 Stefano Cotta Ramusino <stefano.cotta@qilinux.it> 0.7.5-1qilnx
- package created by autospec
