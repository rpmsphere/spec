Name:         cttl
Summary:      Common Text Transformation Library
URL:          https://cttl.sourceforge.net/
Group:        Development
License:      LGPL
Version:      3.02
Release:      3.1
Source0:      https://sourceforge.net/projects/cttl/files/cttl302.zip
BuildArch:    noarch

%description
Common Text Transformation Library (CTTL) is a library of C++
classes and functions to parse and modify STL strings. CTTL
substring classes may be compared, inserted, replaced, and parsed
with EBNF grammars. Compiled program implements recursive descent
LL(INF) parser.

%prep
%setup -q -n cttl302

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p -m 755 \
    $RPM_BUILD_ROOT%{_includedir}/cttl/lambda
install -c -m 644 \
    cttl/* $RPM_BUILD_ROOT%{_includedir}/cttl/
install -c -m 644 \
    lambda/* $RPM_BUILD_ROOT%{_includedir}/cttl/lambda/

%files
%{_includedir}/cttl

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 3.02
- Rebuilt for Fedora
