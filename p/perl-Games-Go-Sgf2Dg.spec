%define cpan_name Games-Go-Sgf2Dg

Name:           perl-%{cpan_name}
Version:        4.221
#Version:        4.252
Release:        8.1
Summary:        Sgf2dg (Replaces Sgf2tex) Converts Smart Go Format (Sgf) Files to Go Dia[cut]
License:        CHECK(GPL-1.0+ or Artistic-1.0)
Group:          Development/Libraries/Perl
URL:            http://search.cpan.org/dist/Games-Go-Sgf2Dg/
Source0:        http://www.cpan.org/authors/id/R/RE/REID/%{cpan_name}-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl-File-Slurp

%description
sgf2dg (replaces sgf2tex) converts Smart Go Format (SGF) files to Go diagrams -
includes the GOOE TeX fonts.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" <<< q
%{__make} %{?_smp_mflags}

%install
%make_install

%files
%doc Changes COPYING figure*.eps genan-shuwa.sgf INSTALL.DOS manual.tex README sgf2dg UPGRADE
%{_bindir}/*
%{_libdir}/perl5/vendor_perl/Games/Go/*
%{_libdir}/perl5/vendor_perl/auto/Games/Go/Sgf2Dg
%{_mandir}/man?/*
%exclude %{_libdir}/perl5/perllocal.pod

%changelog
* Tue Jul 17 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 4.221
- Rebuilt for Fedora
