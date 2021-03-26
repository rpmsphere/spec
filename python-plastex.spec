%define _name plasTeX

Summary:  LaTeX Document Processing Framework
Name:     python-plastex
Version:  0.9.3.20120721
Release:  6.1
Source0:  %{_name}-%{version}.tar.bz2
Patch0:   %{_name}-Config.py.patch
Patch1:   %{_name}-Logging-MAXWIDTH.patch
License:  Freely Distributable
Group:    Development/Libraries/Python
URL:      http://plastex.sourceforge.net/
BuildRequires: dos2unix unzip
BuildRequires: python2-devel
BuildRequires: python2-setuptools >= 0.6
BuildArch: noarch

%description
plasTeX is a LaTeX document processing framework written entirely in
Python. It currently comes bundled with an XHTML renderer (including
multiple themes), as well as a way to simply dump the document to a
generic form of XML. Other renderers can be added as well and are
planned for future releases.

%prep
%setup -q -n %{_name}-%{version}
%patch0
%patch1 -p1
find %{_name} -name \*.py | xargs chmod -x
for i in plasTeX/Packages/listings.py plasTeX/Imagers/pdftoppm.py; do
dos2unix $i
done

%build
%{__python} setup.py build

%install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
%{__python} setup.py install \
   --root=$RPM_BUILD_ROOT \
   --prefix=%{_prefix}
cp plasTeX/plasTeXrc $RPM_BUILD_ROOT%{_sysconfdir}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%config %{_sysconfdir}/plasTeXrc
%doc README PKG-INFO LICENSE INSTALL
%{_bindir}/*
%{python_sitelib}/*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.3.20120721
- Rebuild for Fedora
* Sat Jul 21 2012 toms@opensuse.org
- Updated to 20120721
  * Replaced parse.tokens: DEBUG -> ERROR (plasTexrc)
  * Fixed typo nextok -> nexttok (Base/TeX/Primitives.py)
  * Added XML namespace http://plastex.sf.net for XML debugging
output (DOM/__init__.py)
  * Added option --exact, --no-font to dvisvgm (Imagers/dvisvgm.py)
  * Added pdfbookmark, currentpdfbookmark, subpdfbookmark, belowpdfbook
(Packages/hyperref.py)
  * Added separator between author and dates (Packages/natbib.py)
  * Fixed Renderers/DocBook/:
  - label -> id (Floats.zpts)
  - Added missing tal:content in <ulink> inserted (hyperref.zpts)
  - Added verbatimtab, phrase -> literal (Verbatim.zpts)
* Thu Jun 23 2011 toms@suse.de
- Updated to 20110623, bugs fixed
  * \prime
  * Fixed XML dump
  * Fixed url: contains now arg=url:url
  * Fixed <ulink/> in DocBook renderer
  * Corrected encoding in plastex
* Sat Apr 16 2011 toms@suse.de
- Updated to 20110416, bugs fixed:
  * #3048651: plastex 0.9.2 says it is 0.9.1
  * #3048584: plasTeX has no __version__
  * #3048683: unittests/FuncionalTests.py can use wrong Python
  * #3119470: Parsing documents using html.sty fails
- SPEC: Playing with python-bytecode-inconsistent-mtime warning,
  added filter in rpmlintrc file for the time being
* Sat Jan 22 2011 toms@suse.de
- Updated to 20110122
- Removed patch plasTeX-issection.patch
- Inserted missing "import os" in plasTeX-Logging-MAXWIDTH.patch
* Sun Jan  9 2011 toms@suse.de
- Added patch plasTeX-issection.patch:
  Typo in function issection
* Sat Jan  8 2011 toms@suse.de
- Updated to CVS version from 20110107
- Integrated patch plasTeX-Logging-MAXWIDTH.patch to set MAX_WIDTH
  of logging character from console width
  Function get_terminal_width() taken from
  https://bitbucket.org/birkenfeld/sphinx/src/tip/sphinx/util/console.py
- Renamed patch: plasTeX.patch -> plasTeX-Config.py.patch
* Fri Jan  7 2011 toms@suse.de
- CVS Update 20110107
* Fri Oct  1 2010 toms@suse.de
- Corrected broken tar ball as some important files are missing
- Incorporate config file from /etc
* Fri Sep 24 2010 toms@suse.de
- Update to 0.9.3
- SPEC file changes:
  . Use dos2unix for some files with wrong line endings
* Wed May  5 2010 toms@suse.de
- Initial release
