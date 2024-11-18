Name:         ccide
Summary:      C-Language Decision Table Code Generator
URL:          https://ccide.sourceforge.net/
Group:        Development
License:      GPL
Version:      0.6.6
Release:      20101021.1
Source0:      https://sourceforge.net/projects/ccide/files/%{name}-%{version}.tar.gz
BuildRequires: perl-podlators

%description
ccide reads a source file of C source code containing embedded
decision tables, analyzes it, and expands the tables. This allows
the comfortable and elegant programming of complex state machines.

%prep
%setup -q

%build
%configure
sed -i -e '441i =back' -e '449i =back' -e '/Copyright/d' src/ccide.pod
%{__make} %{_smp_mflags -O}

%install
%{__make} %{_smp_mflags} install AM_MAKEFLAGS="DESTDIR=$RPM_BUILD_ROOT"

%files
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_mandir}/man1/%{name}.1.*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.6
- Rebuilt for Fedora
