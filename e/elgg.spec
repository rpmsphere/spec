Name:           elgg
Version:        1.8.19
Release:        3
Summary:        Social networking platform
License:        GPLv2, MIT
URL:            https://elgg.org/
Group:          Productivity/Networking
Source0:        https://elgg.org/download/%{name}-%{version}.zip
BuildArch:      noarch
Requires:       httpd, mysql, mysql-server
Requires:   php, php-gd, php-mbstring

%description
Elgg is an open source social networking platform developed for LAMP 
(Linux, Apache, MySQL, PHP) which encompasses weblogging, file storage, 
RSS aggregation, personal profiles, FOAF functionality and more.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/var/www/html
cp -a * %{buildroot}/var/www/html
mv %{buildroot}/var/www/html/htaccess_dist %{buildroot}/var/www/html/.htaccess
mkdir -p %{buildroot}/var/www/%{name}-data

%post
#sed -i 's|^SELINUX=.*|SELINUX=disabled|' /etc/sysconfig/selinux
#sed -i 's|^short_open_tag = .*|short_open_tag= On|' /etc/php.ini
#sed -i '/\/var\/www\/html/,/\/Directory/s/^    AllowOverride .*/    AllowOverride All/' /etc/httpd/conf/httpd.conf

%files
 %defattr(-,apache,apache)
/var/www/html/.htaccess
/var/www/html/*
/var/www/%{name}-data

%changelog
* Sat Aug 16 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 1.8.19
- Initial package for Fedora
