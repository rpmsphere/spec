%define _name webunit

Summary:   Unittest Your Websites With Code That Acts Like a Web Browser
Name:      python2-%{_name}
Version:   1.3.10
Release:   2.1
Source0:   %{_name}-%{version}.tar.gz
License:   BSD
Group:     Development/Libraries/Python
URL:       https://mechanicalcat.net/tech/webunit/
BuildRequires: python2 python2-devel
BuildArch: noarch

%description
Webunit is a framework for unit testing websites:
- Browser-like page fetching including fetching the images and stylesheets
  needed for a page and following redirects
- Cookies stored and trackable (all automatically handled)
- HTTP, HTTPS, GET, POST, basic auth all handled, control over expected
  status codes, ...
- DOM parsing of pages to retrieve and analyse structure, including simple
  form re-posting
- Two-line page-fetch followed by form-submit possible, with error checking
- Ability to register error page content across multiple tests
- Uses python's standard unittest module as the underlying framework
- May also be used to regression-test sites, or ensure their ongoing
  operation once in production (testing login processes work, etc.)

%prep
%setup -qn %{_name}-%{version}

%build
python2 setup.py build

%install
python2 setup.py install \
   --prefix=%{_prefix} \
   --root=$RPM_BUILD_ROOT

%files
%doc *.txt
%{python2_sitelib}/*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.10
- Rebuilt for Fedora
* Tue May 18 2010 toms@suse.de
- Fixed problem in spec file
* Fri Jul 11 2008 toms@suse.de
- Initial release 1.3.9
