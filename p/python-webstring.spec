%define modname webstring

Summary:   Template Engine That Uses Python as the Template Language
Name:      python-%{modname}
Version:   0.5
Release:   4.1
Source0:   %{modname}-%{version}.tar.bz2
# Remove webstring.tests package
Patch0:    %{name}-setup.py.diff
License:   BSD
Group:     Development/Libraries/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:       http://psilib.sourceforge.net/webstring.html
BuildRequires:  python-devel python-setuptools
BuildRequires:  python-lxml dos2unix
BuildArch: noarch

%description
Webstring is a template engine for programmers whose favorite
template language is Python. webstring can be used to generate
any text format from a template with the additional advantage
of advanced XML and HTML templating using the lxml and
cElementTree libraries.

%prep
%setup -q -n %{modname}-%{version}
%patch0 -p0
%{__chmod} -x README PKG-INFO

%build
%{__python} setup.py build

%install
%{__python} setup.py install \
--optimize 1 \
--prefix=%{_prefix} \
--root=$RPM_BUILD_ROOT

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{python_sitelib}/*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5
- Rebuilt for Fedora
* Sun Mar  7 2010 toms@suse.de
- First release 0.5
