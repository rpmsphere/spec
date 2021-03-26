Name: systemc
Summary: SystemC Class Library
Version: 2.3.3
Release: 1
Group: Development/Libraries
License: see docs/License.pdf
URL: https://github.com/systemc
Source0: https://www.accellera.org/images/downloads/standards/systemc/%{name}-%{version}.tar.gz

%description
This version of SystemC contains the "Proof of Concept" simulator for
the IEEE 1666_2011 SystemC standard. Please consult the IEEE 1666_2011
Language Reference Manual for details about the new SystemC standard.

%prep
%setup -q
#sed -i -e '/examples/d' -e 's|$(prefix)|$(prefix)/share/doc/systemc|' Makefile.*
%ifarch %arm
#sed -i '/AX_PTHREAD/d' configure
%endif

%build
%configure
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_datadir}/doc/systemc
%makeinstall
#sed -i '/std::gets/d' %{buildroot}%{_includedir}/systemc.h
mv %{buildroot}/usr/[A-Z]* %{buildroot}/usr/docs/* %{buildroot}/usr/examples %{buildroot}%{_datadir}/doc/systemc
mv %{buildroot}/usr/lib64-linux*64 %{buildroot}%{_libdir}

%files
%{_datadir}/doc/systemc
%{_includedir}/*
%{_libdir}/libsystemc*
%{_libdir}/pkgconfig/*

%changelog
* Tue Nov 05 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3.3
- Rebuild for Fedora
