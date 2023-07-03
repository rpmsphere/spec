Name:         uniutils
Summary:      Unicode Utilities
URL:          https://billposer.org/Software/unidesc.html
Group:        Charset
License:      GPL
Version:      2.27
Release:      4.1
Source0:      https://billposer.org/Software/Downloads/uniutils-%{version}.tar.gz

%description
This package consists of a set of programs for manipulating and
analyzing Unicode text. The analysis utilities are useful when
working with Unicode files when one doesn't know the writing
system, doesn't have the necessary font, needs to inspect invisible
characters, needs to find out whether characters have been combined
or in what order they occur, or needs statistics on which characters
occur.

%prep
%setup -q

%build
./configure \
    --prefix=%{_prefix} \
    --mandir=%{_mandir}
%{__make} %{_smp_mflags -O}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} %{_smp_mflags} install AM_MAKEFLAGS="DESTDIR=$RPM_BUILD_ROOT"

%files
%{_bindir}/*
%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.27
- Rebuilt for Fedora
