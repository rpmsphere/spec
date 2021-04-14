%define _name liquid_feedback_frontend

Name:		liquidfeedback-frontend
Version:	2.2.2
Release:	1
Summary:	Interactive Democracy Frontend
License:	MIT/X11
Group:		Productivity/Networking
Source0:	http://www.public-software-group.org/pub/projects/liquid_feedback/frontend/v%{version}/%{_name}-v%{version}.tar.gz
Source1:	liquidfeedback.conf
Source2:	myconfig.lua
Requires:	liquidfeedback-core
Requires:	lua
Requires:	webmcp
BuildRequires:  postgresql-devel
BuildRequires:	rocketwiki-lqfb
URL:		http://liquidfeedback.org/

%description
LiquidFeedback is an open-source software, powering internet platforms for
proposition development and decision making.

Our frontend reference is being implemented in Lua using our web application
framework WebMCP.

%prep
%setup -q -n %{_name}-v%{version}
sed -i 's|liquid_feedback_testing/app|%{_name}|' fastpath/getpic.c

%build
make -C fastpath
LANG=en_US.UTF-8 make -C locale

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}/opt/%{_name}
%__cp -a * %{buildroot}/opt/%{_name}
%__mkdir_p %{buildroot}/etc/lighttpd/conf.d
%__install -m644 %{SOURCE1} %{buildroot}/etc/lighttpd/conf.d
%__install -m644 %{SOURCE2} %{buildroot}/opt/%{_name}/config

%post
chown lighttpd.lighttpd /opt/%{_name}/tmp
echo 'include "conf.d/liquidfeedback.conf"' >> /etc/lighttpd/modules.conf

%postun
sed -i '/liquidfeedback/d' /etc/lighttpd/modules.conf

%clean
%__rm -rf %{buildroot}

%files
%doc LICENSE README
/opt/%{_name}
/etc/lighttpd/conf.d/liquidfeedback.conf

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2.2
- Rebuilt for Fedora
