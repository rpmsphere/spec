Name: m2c
Summary: A Modula-2 (PIM4) to C translator
Version: 0.7
Release: 1.1
License: GPLv2+
Group: Development/Languages
URL: https://savannah.nongnu.org/projects/m2c/
Source: http://download.savannah.nongnu.org/releases/%{name}/%{version}/%{name}-%{version}.tar.gz

%description
This is a Modula-2 compiler which translates to C. The translator is
based on the language report in the 3rd and 4th editions of Wirth's book
Programming in Modula-2.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure +cc=gcc
%{__make} prefix=/usr libdir=%{_libdir}/m2c man1dir=%{_mandir}/man1

%install
%{__mkdir_p} %{buildroot}/usr/{bin,include,%{_lib}/m2c,share/{info,man/man1}}
%{__make} install prefix=%{buildroot}/usr \
	libdir=%{buildroot}%{_libdir}/m2c \
	man1dir=%{buildroot}%{_mandir}/man1 \
	includedir=%{buildroot}%{_includedir}
makeinfo doc/modula-2.texinfo
cp modula-2.info %{buildroot}%{_infodir}

%clean
rm -Rf %{buildroot}

%files 
%doc COPYING
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_mandir}/*
%{_includedir}/*
%{_infodir}/*

%changelog
* Wed Oct 24 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7
- Rebuild for Fedora
* Sun Sep 21 2014  D. E. Evans <sinuhe@gnu.org>
- Here's an initial spec file for x86 Fedora.
