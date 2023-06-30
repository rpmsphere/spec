Name:         ffe
Summary:      Flat-File Extractor
URL:          https://ff-extractor.sourceforge.net/
Group:        ShellUtils
License:      GPL
Version:      0.3.9a
Release:      1
Source0:      https://sourceforge.net/projects/ff-extractor/files/%{name}/%{version}/%{name}-%{version}.tar.gz

%description
Flat-File Extractor (FFE) can be used for parsing different flat
file structures and printing them in different formats. FFE is a
command line tool which provides: extracting particular fields
or records from a flat file; converting data from one format to
an other, e.g. from CSV to fixed length; verifying a flat file
structure; testing tool for flat file development; displaying flat
file content in human readable form.

%prep
%setup -q

%build
%configure
%{__make} %{_smp_mflags -O}

%install
%{__make} %{_smp_mflags} install AM_MAKEFLAGS="DESTDIR=$RPM_BUILD_ROOT"
rm %{buildroot}%{_infodir}/dir

%files
%{_bindir}/ffe
%{_docdir}/ffe/ffe.html
%{_infodir}/ffe.info.gz
%{_mandir}/man1/ffe.1.gz

%changelog
* Sun Oct 16 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.9a
- Rebuilt for Fedora
