%undefine _debugsource_packages
Name:         python-closure_linter
Summary:      Google Closure Linter
URL:          http://code.google.com/p/closure-linter/
Group:        Language
License:      Apache 2.0
Version:      2.3.11
Release:      5.1
Source0:      http://closure-linter.googlecode.com/files/closure_linter-%{version}.tar.gz
BuildRequires:  python2
BuildArch: noarch

%description
The Closure Linter enforces the guidelines set by the Google JavaScript Style
Guide. The linter handles style issues so that you can focus on the code.

%prep
%setup -q -n closure_linter-%{version}

%build

%install
python2 setup.py install \
    --root=$RPM_BUILD_ROOT \
    --prefix=%{_prefix}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%files
%{_bindir}/*
%{python2_sitelib}/*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3.11
- Rebuilt for Fedora
