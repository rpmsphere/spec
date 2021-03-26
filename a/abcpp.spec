%global debug_package %{nil}

Name:      abcpp
Version:   1.4.5
Release:   5.1
Summary:   An ABC file preprocessor
License:   GPL
URL:       http://abcplus.sourceforge.net
Group:     Applications/File
Source:    http://abcplus.sourceforge.net/%{name}-%{version}.tar.gz

%description
abcpp is a simple yet powerful preprocessor designed for, but not limited
to, ABC music files. It allows the user to write portable ABC files, change
the syntax, extract parts, etc.

%prep
%setup -q

%build
make # CFLAGS="$RPM_OPT_FLAGS -Wall"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/abcpp
%{_bindir}/install -m 755 abcpp $RPM_BUILD_ROOT%{_bindir}
%{_bindir}/install -m 644 fancyheader.abp $RPM_BUILD_ROOT%{_datadir}/abcpp
%{_bindir}/install -m 644 italiano.abp $RPM_BUILD_ROOT%{_datadir}/abcpp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING INSTALL LEGGIMI README docs
%doc examples
%{_bindir}/*
%{_datadir}/abcpp

%changelog
* Mon Mar 30 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.5
- Rebuild for Fedora
* Fri May 06 2005 Guido Gonzato
- updated to 1.3.2
* Mon Dec 31 2001 José Romildo Malaquias <romildo@iceb.ufop.br> 1.1.1-2
- More use of macros in spec file
- Use $RPM_OPT_FLAGS at compilation
- A small fix in the %files section
- Include the examples in the documentation
