%undefine _debugsource_packages
%define real_name base

BuildArch:	noarch
Name:           base4snort
Group:          Applications/Publishing
BuildRequires:  httpd-devel, fedora-logos-httpd
Requires:       httpd, php >= 4.3.0, php-mysql, mysql, curl, php-gd, php-pear
Requires:       perl-IP-Country, perl-NetPacket
Requires:       php-pecl-geoip
Version:        1.4.5
Release:        21.1
%define apxs    /usr/bin/apxs
%define	apache_libexecdir	%(%{apxs} -q LIBEXECDIR)
%define	apache_sysconfdir	%(%{apxs} -q SYSCONFDIR)
%define base_dir /var/www/base
%define real_name base
URL:            https://base.secureideas.net/
Summary:        BASE is the Basic Analysis and Security Engine
License:        GPLv2
Source0:        https://sourceforge.net/projects/secureideas/files/BASE/%{real_name}-%{version}/%{real_name}-%{version}.tar.gz
Source1:        %{name}.conf.default
Source2:        %{name}.conf.vhost
Source3:        %{name}.conf.nonsuse

%description
BASE is the Basic Analysis and Security Engine. It is based on the code from
the Analysis Console for Intrusion Databases (ACID) project. This application
provides a web front-end to query and analyze the alerts coming from a SNORT
IDS system.

%prep
%setup -q -n %{real_name}-%{version}
find . -type d -name CVS -prune -exec rm -rf {} \;
find . -type f -exec sed -i 's|Net::Packet|NetPacket|g' {} \;

%install
mkdir -p $RPM_BUILD_ROOT/%{apache_sysconfdir}/../conf.d
cp -avL %{S:3} $RPM_BUILD_ROOT/%{apache_sysconfdir}/../conf.d/base.conf
mkdir -p $RPM_BUILD_ROOT/%{base_dir}
cp -avL * $RPM_BUILD_ROOT/%{base_dir}/
rm -rf $RPM_BUILD_ROOT/%{base_dir}/docs
find $RPM_BUILD_ROOT%{base_dir} -type d | \
sed "s@$RPM_BUILD_ROOT@%dir @" > files.base
find $RPM_BUILD_ROOT%{base_dir} -type f | \
sed "s@$RPM_BUILD_ROOT@@;/\/templates\/\|\.conf$/s@^@%config (noreplace) @" >> files.base

%files -f files.base
%dir %{apache_sysconfdir}/../conf.d
%config (noreplace) %{apache_sysconfdir}/../conf.d/base.conf
%doc docs/*

%changelog
* Fri Jul 27 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.5
- Rebuilt for Fedora
* Wed Oct 27 2010 joop.boonen@opensuse.org
- Build version 1.4.5
