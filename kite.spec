Name: kite
Summary: Kite programming language
Version: 1.0.4
Release: 6.1
Group: Development/Languages
License: GPL
URL: http://trac.kite-language.org/
Source0: http://www.kite-language.org/files/%{name}-%{version}.tar.gz
BuildRequires: libgc-devel

%description
Kite is a programming language designed to minimize the required experience
level of the programmer -- quick development and running time and low CPU and
memory usage (the binary is around 250KB stripped on OSX, for instance).

%prep
%setup -q
sed -i '155d' backend/common/kite_vm.c

%build
%configure
make %{?_smp_mflags} CFLAGS+=-Wno-format-security

%install
make install DESTDIR=%{buildroot}

%files
%doc AUTHORS ChangeLog COPYING README NEWS
%{_bindir}/*
%{_libdir}/%{name}
%{_libdir}/lib%{name}*
%{_includedir}/%{name}_*.h
%{_mandir}/man1/*
%{_datadir}/info/%{name}.info.*
%exclude %{_datadir}/info/dir

%changelog
* Sun Jun 02 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.4
- Rebuild for Fedora
