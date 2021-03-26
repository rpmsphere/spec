Name:         solarium
Summary:      PHP Solr Client Library
URL:          http://www.solarium-project.org/
Group:        Web
License:      BSD
Version:      3.2.0rc1
Release:      2.1
Source0:      %{name}-3.2.0-RC1.tar.gz
BuildArch:    noarch

%description
Solarium is a Solr client library for PHP applications. By offering
an API for common Solr functionality you no longer need to compose
complex query strings and parameters manually, greatly reducing
development time and complexity.

%prep
%setup -q -n %{name}-3.2.0-RC1

%build

%install
mkdir -p -m 755 \
    $RPM_BUILD_ROOT%{_prefix}/lib/php
cp -rp library/* $RPM_BUILD_ROOT%{_prefix}/lib/php/

%files
%{_prefix}/lib/php/*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 3.2.0rc1
- Rebuild for Fedora
