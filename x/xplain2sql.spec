%undefine _debugsource_packages

Name:         xplain2sql
Summary:      XPlain to SQL Converter
URL:          https://www.berenddeboer.net/xplain2sql/
Group:        Database
License:      Open Source
Version:      4.0.1
Release:      4.1
Source0:      https://www.berenddeboer.net/xplain2sql/xplain2sql-%{version}-csrc.tar.gz

%description
Xplain is a beautifully orthogonal database manipulation and query
language. Orthogonal means that with Xplain there is usually only
one solution, not dozens like in SQL. Xplain straight-forwardly
supports aggregation and generalization. Or in other words, it
supports HAS-A and IS-A relations, the only possible relations.
Because it supports IS-A relations, it is a very natural component
in an object-oriented environment. Xplain2SQL can convert Xplain
data definition and data manipulation and retrieval statements to
many SQL dialects.

%prep
%setup -q

%build
%{__make} %{_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p -m 755 \
    $RPM_BUILD_ROOT%{_bindir} \
    $RPM_BUILD_ROOT%{_mandir}/man1
install -c -m 755 \
    xplain2sql $RPM_BUILD_ROOT%{_bindir}
install -c -m 644 \
    xplain2sql.1 $RPM_BUILD_ROOT%{_mandir}/man1/

%files
%{_bindir}/*
%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 4.0.1
- Rebuilt for Fedora
