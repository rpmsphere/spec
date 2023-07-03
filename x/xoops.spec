Name:		xoops
Version:	2.5.5
Release:	1
Summary:	Easy to use dynamic web content management system written in PHP
License:	GPL
URL:		https://www.xoops.org/
Group:		Productivity/Networking
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	httpd php

%description
XOOPS is a web application platform written in PHP for the MySQL database.
Its object orientation makes it an ideal tool for developing small or large
community websites, intra company and corporate portals, weblogs and much more.

%prep
%setup -q -c

%build

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}/var/www/html
%__cp -a %{name} %{buildroot}/var/www/html

%clean
%__rm -rf %{buildroot}

%files
 %defattr(-,apache,apache)
/var/www/html/%{name}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.5.5
- Rebuilt for Fedora
