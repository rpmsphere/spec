Name: scheme48
Version: 1.9.2
Release: 6.1
License: BSD-3-Clause
Summary: An implementation of Scheme
URL: https://www.s48.org
Group: Development/Languages/Scheme
Source: %url/%version/%name-%version.tgz
Patch1: no-env-trampoline.diff
Patch2: debian-user-name.diff
Patch3: man-properly-escape-minuses.diff
Patch4: security-tmpfile.patch

%description
Scheme 48 is an implementation of Scheme written by Richard Kelsey and Jonathan
Rees. It is based on a byte-code interpreter and is designed to be used as a
testbed for experiments in implementation techniques and as an expository tool.

%prep
%setup -q
%patch 1 -p1
%patch 2 -p1
%patch 3 -p1
%patch 4 -p1
iconv -f iso88591 -t utf8 README > README.utf8
mv README.utf8 README

%build
#add_optflags -Wall -Wno-return-type
%configure --docdir=%{_docdir}/%{name}
%make_build LIB=%{_libdir}/%{name} SHARE=%{_datadir}/%{name}

%install
%make_install LIB=%{_libdir}/%{name} SHARE=%{_datadir}/%{name}
ln -s %{name} %{buildroot}%{_bindir}/s48
ln -s %{name}.1 %{buildroot}%{_mandir}/man1/s48.1
install README %{buildroot}%{_docdir}/%{name}
# for scsh
mkdir %{buildroot}/usr/lib
ln -s %{_libdir}/%{name} %{buildroot}/usr/lib/%{name}-%{version}

%files
%doc %{_docdir}/%{name}
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_mandir}/man1/*
%{_datadir}/%{name}
/usr/lib/%{name}-%{version}

%changelog
* Mon Aug 27 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.9.2
- Rebuilt for Fedora
* Mon Oct  6 2014 Led <ledest@gmail.com> 1.9.2-3
- add some debian patches
* Mon Oct  6 2014 Led <ledest@gmail.com> 1.9.2-2
- add optflags: -Wall -Wno-return-type
* Sun Oct  5 2014 Led <ledest@gmail.com> 1.9.2-1
- initial build
