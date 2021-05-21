Summary:	Checking misspelled words
Name:		codespell
Version:	1.16.0
Release:	1
License: 	GPLv2
Group: 		Development/Tools
Source:		http://git.profusion.mobi/cgit.cgi/lucas/codespell/snapshot/%{name}-%{version}.tar.gz
URL:		http://git.profusion.mobi/cgit.cgi/lucas/codespell/
BuildArch:	noarch

%description
Fix common misspellings in text files. It's designed primarily for checking
misspelled words in source code, but it can be used with other files as well.

%prep
%setup -q

%build
python2 setup.py build

%install
rm -fr $RPM_BUILD_ROOT
python2 setup.py install --prefix=/usr --root=%{buildroot} --skip-build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc TODO COPYING README*
%{_bindir}/%{name}
%{python_sitelib}/%{name}*

%changelog
* Fri Oct 04 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.16.0
- Rebuilt for Fedora
