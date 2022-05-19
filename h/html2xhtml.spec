Summary:   A free-software converter from HTML to XHTML 
Name:      html2xhtml
Version:   1.3
Release:   1
License:   GPL v2
Group:     Development/Tools
Source0:   http://www.it.uc3m.es/jaf/html2xhtml/downloads/%{name}-%{version}.tar.gz 
URL:       http://www.it.uc3m.es/jaf/html2xhtml/

%description
html2xhtml converts HTML files into XHTML. It can fix many common errors in HTML files (e.g. missing end tags,
elements with incorrect content model, non-standard elements or attributes, etc.)
It can also handle invalid or non well-formed XHTML input, and clean it to produce a well-formed and valid XHTML
output. The output document type can be selected among several XHTML DTDs (1.0, 1.1, Basic, etc.)

%prep
%setup -q

%build
autoreconf -ifv
./configure --prefix=/usr
make

%install
rm -rf %{buildroot}
DESTDIR=$RPM_BUILD_ROOT make install

%clean
rm -rf %{buildroot}

%files
%{_bindir}/dtdquery
%{_bindir}/html2xhtml
%{_datadir}/man/man1/html2xhtml.1.gz

%changelog
* Sun May 8 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3
- Rebuilt for Fedora
* Wed Mar 31 2010 Gene <gene.hsu@ossii.com.tw>
- build the program
