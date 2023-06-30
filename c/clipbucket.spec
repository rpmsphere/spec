Name:		clipbucket
Version:	2.6.r738.p3
Release:	1
URL:		https://clip-bucket.com/
Summary:	A way to broadcast yourself
License:	Open Source
Group:		Productivity/Networking
Source0:	https://sourceforge.net/projects/clipbucket/files/ClipBucket%20v2/clipbucket-2.6-r738-security-fixed-p3.zip
Source1:	zh_TW.lang
BuildArch:	noarch
Requires:	httpd php mysql-server gd ffmpeg gpac gpac-libs flvtool2

%description
ClipBucket is an OpenSource Multimedia Management Script Provided Free to the
Community.This script comes with all the bells & whistles required to start
your own Video Sharing website like Youtube, Metacafe, Veoh, Hulu or any other
top video distribution application in matter of minutes. ClipBucket is fastest
growing script which was first started as Youtube Clone but now its advance
features & enhancements makes it the most versatile, reliable & scalable media
distribution platform with latest social networking features, while staying
light on your pockets. Whether you are a small fan club or a big Multi Tier
Network operator, Clipbucket will fulfill your video management needs.

%prep
%setup -q -c
sed -i -e "5i 'zh_TW'	=>	'中文 (繁體)'," -e "s|cn_ZH|zh_CN|" upload/includes/languages.php
cp %{SOURCE1} upload/includes/langs

%build

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}/var/www/html/%{name}
%__cp -a upload/* %{buildroot}/var/www/html/%{name}

%clean
%__rm -rf %{buildroot}

%files
 %defattr(-,apache,apache)
%doc CHANGELOG README.txt "do not upload/admin_change_pass.php"
/var/www/html/%{name}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.6.r738.p3
- Rebuilt for Fedora
