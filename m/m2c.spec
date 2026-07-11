Name: m2c
Summary: A Modula-2 (PIM4) to C translator
Version: 0.7.2
Release: 1.0
License: GPLv2+
Group: Development/Languages
URL: https://github.com/gungwald/makarov-m2c/
Source: https://github.com/gungwald/makarov-%{name}/archive/refs/tags/v%{version}.tar.gz
%description
This is a Modula-2 compiler which translates to C. The translator is
based on the language report in the 3rd and 4th editions of Wirth's book
Programming in Modula-2.

%prep
%setup -q -n makarov-%{name}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure +cc=gcc
%{__make} prefix=/usr libdir=%{_libdir}/m2c man1dir=%{_mandir}/man1

%install
%{__mkdir_p} %{buildroot}/usr/{bin,include,%{_lib}/m2c,share/{doc,man/man1}}
%{__make} install prefix=%{buildroot}/usr \
        libdir=%{buildroot}%{_libdir}/%{name} \
        man1dir=%{buildroot}%{_mandir}/man1 \
        includedir=%{buildroot}%{_includedir} \
        docdir=%{buildroot}%{_docdir}/%{name}

%files 
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_mandir}/*
%{_includedir}/*
%{_docdir}/%{name}*

%changelog
* Sat Jul 11 2026 Bill Chatfield github.com/gungwald - 0.7.2
- Update documentation
* Wed Jul 08 2026 Bill Chatfield github.com/gungwald - 0.7.2
- Restore compilation of traditional code with modern gcc
* Wed Jul 08 2026 Bill Chatfield - 0.7.1
- Restore compilation of traditional code with modern gcc
* Wed Oct 24 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7
- Rebuilt for Fedora
* Sun Sep 21 2014  D. E. Evans <sinuhe@gnu.org>
- Here's an initial spec file for x86 Fedora.

