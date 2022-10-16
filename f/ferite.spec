%global __os_install_post %{nil}

Summary: The ferite programming language and engine
Name: ferite
Version: 1.1.17
Release: 1
License: BSD
Group: Development/Languages
Source0: https://sourceforge.net/projects/ferite/files/ferite/1.1/%{name}-%{version}.tar.gz
URL: https://ferite.sourceforge.net/

%description
ferite is a modern, lighweight, portable, threadsafe scripting engine with
a language that is very easy to pick up and leverage for any task. It\'s been
designed for rapid deployment in other programs as well as stand alone use.

%prep
%setup -q
sed -i 's|lib/ferite|%{_lib}/ferite|' configure*
sed -i 's|pcre_info( rgx->compiled_re, NULL, NULL )|pcre_fullinfo( rgx->compiled_re, NULL, NULL, NULL )|' modules/regexp/regexp.fec modules/regexp/regexp_Regexp.c

%build
%configure
%make_build

%install
%make_install
#mv %{buildroot}/usr/lib/%{name} %{buildroot}%{_libdir}
cp TODO ROADMAP RELEASE.NOTES README LICENSE DEVELOPERS ChangeLog AUTHORS ABOUT %{buildroot}%{_docdir}/%{name}

%files 
%{_docdir}/%{name}
%{_bindir}/*
%{_includedir}/*
%{_libdir}/%{name}
%{_libdir}/lib%{name}*
%{_datadir}/aclocal/%{name}.m4
%{_datadir}/%{name}
%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Oct 09 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.17
- Rebuilt for Fedora
