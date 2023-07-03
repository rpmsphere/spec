%define _name mathdom

Summary:   Content MathML in Python
Name:      python2-%{_name}
Version:   0.8
Release:   4.1
Source0:   %{_name}-%{version}.tar.bz2
License:   MIT
Group:     Development/Libraries/Python
BuildArch:  noarch
URL:       https://mathdom.sourceforge.net/
BuildRequires:  bzip2 python2-devel
Requires:  python2-lxml pyparsing


%description
MathDOM is a set of Python 2.4 modules (using PyXML or lxml, and pyparsing) that import mathematical terms as a Content MathML DOM. It currently parses MathML and literal infix terms into a DOM or lxml document and writes out MathML and literal infix/prefix/postfix/Python terms. The DOM elements are enhanced by domain specific methods that make using the DOM a little easier. Input parsers and output converters are easily extensible.
Newer versions simplify the portability of code between the PyXML and lxml versions. They also extend the latter with an XSLT-based output filter for Presentational MathML and RelaxNG-based document validation. PyXML does not support any of these.

%prep
%setup -q -n %{_name}-%{version}

%build
python2 setup.py build

%install
python2 setup.py install \
  --root=$RPM_BUILD_ROOT \
  --prefix=%{_prefix}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%doc examples html
%{python2_sitelib}/*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8
- Rebuilt for Fedora
* Fri May 29 2009 toms@suse.de
- Fixed SPEC file
- Updated to version 0.8:
  * works with (and requires) lxml 2.0 or later
  * bug fix for operator qualifiers
* Fri Apr 27 2007 toms@suse.de
- First release 0.7
