Name:           whatweb
Version:        0.4.5
URL:            http://www.morningstarsecurity.com/research/whatweb
Summary:        Next generation web scanner
Release:        4.1
License:        GPLv2
Group:          Development/Ruby
Source:         %{name}-%{version}.tar.gz
BuildArch:		noarch
Requires:       ruby

%description
Identify content management systems (CMS), blogging platforms, stats/analytics
packages, javascript libraries, servers and more. When you visit a website in 
your browser the transaction includes many unseen hints about how the webserver
is set up and what software is delivering the webpage. Some of these hints
are obvious, eg. "Powered by XYZ" and others are more subtle.
WhatWeb recognises these cues and reports what it finds.

%prep
%setup -q

%build

%install
make install DESTDIR=$RPM_BUILD_ROOT 

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/%{name}

%changelog
* Mon May 16 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.5
- Rebuild for Fedora
* Thu Nov 11 2010 André Guerreiro <andre.guerreiro@caixamagica.pt> 0.4.5-1xcm15
- First CM15 package
