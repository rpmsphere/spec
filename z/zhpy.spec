Name:		zhpy
Version:	1.7.4
Release:	3.1
Summary:	Write python language in chinese
Group:		Development/Language
License:	MIT
URL:		http://code.google.com/p/zhpy/
Source0:	http://pypi.python.org/packages/source/z/zhpy/%{name}-%{version}.zip
BuildRequires:	python2-devel, python2-setuptools
BuildArch:	noarch

%description
Zhpy on python is good for Taiwan and China beginners to learn python in our
native language (Currently support Traditional and Simplified chinese).
Zhpy acts like python and play like python, you (chinese users) could use it as
python to educate yourself the program skills plus with your native language.

%prep
%setup -q

%build
python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install --skip-build --root $RPM_BUILD_ROOT

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README.txt PKG-INFO
%{python2_sitelib}/zhpy
%{python2_sitelib}/*egg-info
%{_bindir}/zhpy

%changelog
* Tue Oct 24 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 1.7.4
- Rebuild for Fedora
