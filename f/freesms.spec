%global debug_package %{nil}
%define _name FreeSMS

Name:           freesms
BuildRequires:  httpd-devel, fedora-logos-httpd
BuildRequires:  unzip
Requires:       ImageMagick
Requires:       httpd
Requires:       mysql
Requires:       php >= 4.2.0
Requires:       php-mysql
Version:        2.1.2
Release:        26.1
%define apxs    /usr/bin/apxs
Summary:        Web application for managing an educational facility
License:        PHP-3.01
Group:          Productivity/Networking/Web/Utilities
%define	apache_libexecdir	%(%{apxs} -q LIBEXECDIR)
%define	apache_sysconfdir	%(%{apxs} -q SYSCONFDIR)
%define FreeSMS_src_dir FreeSMS
%define FreeSMS_dir /var/www/FreeSMS
URL:            http://sourceforge.net/projects/freesms/
Source0:        %{_name}_2_1_2.zip
Source1:        %{_name}.conf.default
Source2:        %{_name}.conf.vhost
Source3:        %{_name}.conf.nonsuse
BuildArch:      noarch

%description
FreeSMS (Free Student Management System) is a Web application for managing an
educational facility. It manages teachers and students and provides marketing,
registration, course management, attendance, and a student evaluation system,
and manages courses within a class environment.

%prep
%setup -q  -n %{FreeSMS_src_dir}

%install
mkdir -p $RPM_BUILD_ROOT/%{apache_sysconfdir}/../conf.d
cp -avL %{SOURCE3} $RPM_BUILD_ROOT/%{apache_sysconfdir}/../conf.d/FreeSMS.conf
mkdir -p $RPM_BUILD_ROOT/%{FreeSMS_dir}
cp -avL * $RPM_BUILD_ROOT/%{FreeSMS_dir}/
#
find $RPM_BUILD_ROOT%{FreeSMS_dir} -name "* *"|while read file; do    echo "$file";    mv "$file" "`echo "$file"| awk ' BEGIN {OFS="_"} $1=$1 '`"; done
#
find $RPM_BUILD_ROOT%{FreeSMS_dir} -type d | \
sed "s@$RPM_BUILD_ROOT@%dir @" > files.FreeSMS
find $RPM_BUILD_ROOT%{FreeSMS_dir} -type f | \
sed "s@$RPM_BUILD_ROOT@@;/\/templates\/\|\.conf$/s@^@%config (noreplace) @" >> files.FreeSMS
cat files.FreeSMS

%files -f files.FreeSMS
%dir %{apache_sysconfdir}/../conf.d
%config (noreplace) %{apache_sysconfdir}/../conf.d/FreeSMS.conf

%changelog
* Fri Jul 27 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.2
- Rebuild for Fedora
* Fri Apr  6 2012 joop.boonen@opensuse.org
- Reformated the spec file with spec-cleaner
* Mon Oct 17 2011 joop.boonen@opensuse.org
- Correction in directory is now /srv/www/FreeSMS
* Sat Oct  8 2011 cristeab@gmail.com
- updated FreeSMS to the latest version
- changed installation folder from /srv to /srv/www/htdocs
* Sun Nov  2 2008 joop.boonen@opensuse.org
- set the config directories correctly for non suse distros
* Sat Nov  1 2008 joop.boonen@opensuse.org
- experimenting to get it more distro compliant
* Mon Oct 20 2008 joop.boonen@opensuse.org
- First FreeSMS rpm build
- Used viewvc.spec as a base
