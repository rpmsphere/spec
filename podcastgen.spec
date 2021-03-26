%global __os_install_post %{nil}

Name:           podcastgen
Version:        1.4
Release:        1
Summary:        Open Source Podcast Publishing Solution
Group:          Applications/Publishing
License:        GPL
URL:            http://podcastgen.sourceforge.net/
Source0:        ftp://ite.ceag.kh.edu.tw/podcastgen/%{name}_%{version}.tar.bz2
Requires:       httpd, php
BuildArch:	noarch

%description
Podcast Generator is a free web based podcast publishing script written in PHP:
upload media files (audio-video) via a web form along with episode information
and automatically create podcast w3c-compliant feed including iTunes specific tags.
It also features a comprehensive web administration.

%prep
%setup -q -n %{name}
rm -rf .svn

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_var}/www/html/%{name}
cp -a * $RPM_BUILD_ROOT%{_var}/www/html/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_var}/www/html/%{name}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4
- Rebuild for Fedora
