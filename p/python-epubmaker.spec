%undefine _debugsource_packages
%define module epubmaker

Name:           python-%{module}
Version:        0.3.19
Release:        3.1
Summary:        The Project Gutenberg Epub Maker
Group:          Applications/Publishing
License:        GPLv3
URL:            https://pypi.python.org/pypi/epubmaker/
Source0:        https://e.pypi.python.org/packages/source/e/%{module}/%{module}-%{version}.zip
BuildArch:      noarch
BuildRequires:  python

%description
EpubMaker is the tool used for format conversion at Project Gutenberg.
It builds EPUB2 and Kindle files from HTML. Also it builds HTML4, EPUB2,
Kindle, and PDF files from reST sources.

%prep
%setup -q -n %{module}-%{version}

%build
python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT/usr/CHANGES
mv $RPM_BUILD_ROOT/usr/epubmaker/writers/cover.jpg $RPM_BUILD_ROOT%{python2_sitelib}/%{module}/writers/cover.jpg
mv $RPM_BUILD_ROOT/usr/setup_inc.py $RPM_BUILD_ROOT%{python2_sitelib}/%{module}/setup_inc.py

%files
%doc CHANGES README
%{python2_sitelib}/*

%changelog
* Sun Apr 07 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.19
- Rebuilt for Fedora
