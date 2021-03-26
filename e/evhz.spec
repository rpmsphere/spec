%global debug_package %{nil}

Name: evhz
Version: 2014
Release: 3.1
Summary: Measure mouse polling rate
Group: System/Configuration/Hardware
License: Public domain
URL: https://wiki.archlinux.org/index.php/Mouse_Polling_Rate
Source: %name-master.zip

%description
A tool named evhz that can display the current mouse refresh rate -- useful
when checking that your customised polling settings have been applied.

You will have root permissions to /dev/input/event*

Inspired by code written by Alan Kivlin.

%prep
%setup -q -n %{name}-master

%build
gcc -o %name %name.c

%install
install %name -D %buildroot%_sbindir/%name

%files
%_sbindir/%name

%changelog
* Mon Mar 02 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 2014
- Rebuild for Fedora
* Sat Dec 22 2012 Vitaly Lipatov <lav@altlinux.ru> 2012-alt1
- full rewrite original code and set appropriate license
* Fri Apr 06 2012 Vitaly Lipatov <lav@altlinux.ru> 2006-alt1
- initial build for ALT Linux Sisyphus
