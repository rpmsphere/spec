%undefine _debugsource_packages

BuildArch:      noarch
Name:           coppermine
Group:          Applications/Publishing
BuildRequires:  httpd-devel, fedora-logos-httpd
Requires:       php >= 4.2.0 httpd php-mysql mysql ImageMagick
Version:        1.5.24
Release:        5.1
%define apache_libexecdir       %{_libdir}/httpd/modules
%define apache_sysconfdir       /etc/httpd/conf
%define coppermine_dir /var/www/%{name}
URL:            https://coppermine-gallery.net/
Summary:        Multi-purpose fully-featured and integrated web picture gallery
License:        GPLv2+
Source0:        https://sourceforge.net/projects/coppermine/files/Coppermine/1.5.x/cpg%{version}.zip
Source1:        %{name}.conf.default
Source2:        %{name}.conf.vhost
Source3:        %{name}.conf.nonsuse

%description
Coppermine Photo Gallery is an advanced, user-friendly, picture gallery script
with built-in support for other multi-media/data files. The gallery can be private,
accessible to registered users only, and/or open to all visitors to your site.

%prep
%setup -q  -n cpg15x

%build

%install
mkdir -p $RPM_BUILD_ROOT%{apache_sysconfdir}/../conf.d
cp -avL %{S:3} $RPM_BUILD_ROOT%{apache_sysconfdir}/../conf.d/coppermine.conf
mkdir -p $RPM_BUILD_ROOT%{coppermine_dir}
cp -avL * $RPM_BUILD_ROOT%{coppermine_dir}/
chmod 755 $RPM_BUILD_ROOT%{coppermine_dir}/include
chmod 755 $RPM_BUILD_ROOT%{coppermine_dir}/albums
chmod 755 $RPM_BUILD_ROOT%{coppermine_dir}/albums/userpics
chmod 755 $RPM_BUILD_ROOT%{coppermine_dir}/albums/edit

%files
%dir %{apache_sysconfdir}/../conf.d
%config (noreplace) %{apache_sysconfdir}/../conf.d/coppermine.conf
%attr(-,apache,apache) %{coppermine_dir}

%changelog
* Tue Nov 05 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5.24
- Rebuilt for Fedora
* Mon Jun 28 2010 joop.boonen@opensuse.org
- build version 1.5.6
* Sun Feb 14 2010 joop.boonen@opensuse.org
- build version 1.4.26
* Fri Jul 3 2009 joop.boonen@opensuse.org
- build version 1.4.25
* Fri Jun 19 2009 joop.boonen@opensuse.org
- build version 1.4.24
* Fri Apr 3 2009 joop.boonen@opensuse.org
- build version 1.4.21
* Sun Nov 2 2008 joop.boonen@opensuse.org
- set the config directories correctly for non suse distros
* Sat Nov 1 2008 joop.boonen@opensuse.org
- experimenting to get it more distro compliant
* Sun Oct 18 2008 joop.boonen@opensuse.org
- changes the multi distro a bit
* Sat Oct 11 2008 joop.boonen@opensuse.org
- Last vhost framework wasn't good enough perfected it
- It can now either be used in the default and/or vhost
* Tue Oct 7 2008 joop.boonen@opensuse.org
- Added framework for vhost in coppermine.conf
* Mon Oct 6 2008 joop.boonen@opensuse.org
- Added the authentication possibility via .htaccess in the directory in coppermine.conf
* Mon Sep 1 2008 joop.boonen@opensuse.org
- First coppermine rpm build
- Used viewvc.spec as a base
