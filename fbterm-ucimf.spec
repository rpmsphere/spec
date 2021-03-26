Name:           fbterm-ucimf
Version:        0.2.9
Release:        2.1
Summary:        Bridge of ucimf as input module for fbterm
Group:          Applications/System
License:        GPL
URL:            http://code.google.com/p/ucimf/
Source0:        http://ucimf.googlecode.com/files/fbterm_ucimf-%{version}.tar.gz
BuildRequires:  gcc-c++, ucimf-devel
Requires:       fbterm, ucimf

%description
Bridge of ucimf as input module for fbterm.

%prep
%setup -q -n fbterm_ucimf-%{version}

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/*
%{_datadir}/man/man1/*

%changelog
* Thu Apr 14 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.9
- Rebuild for Fedora
