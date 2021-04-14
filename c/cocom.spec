Name:         cocom
Summary:      Compiler Creation Toolkit
URL:          http://cocom.sourceforge.net/
Group:        Compiler
License:      GPL/LGPL
Version:      0.996
Release:      10.1
Source0:      http://prdownloads.sourceforge.net/cocom/%{name}-%{version}.tar.gz

%description
COCOM is a set of tools oriented onto the creation of compilers,
cross-compilers, interpreters, and other language processors.
The distribution also contains interpreter of language DINO as
an example of the tool set usage.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}

%description devel
Header files and libraries for the package %{name}.

%prep
%setup -q

%build
./configure \
    --prefix=%{_prefix} \
    --mandir=%{_mandir} \
    --includedir=%{_includedir}/cocom \
    --libdir=%{_libdir}/cocom
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%files
%{_bindir}/*
%{_mandir}/man1/*

%files devel
%{_libdir}/%{name}
%{_includedir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.996
- Rebuilt for Fedora
