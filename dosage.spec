%global debug_package %{nil}
Name:    dosage
Version: 2.15
Release: 6.1
Summary: A commandline webcomic downloader and archiver
License: MIT
URL:     https://github.com/wummel/dosage
BuildArch: noarch
Source0: %name-%version.tar
BuildRequires: python2-devel

%description
Dosage is designed to keep a local copy of specific webcomics
and other picture-based content such as Picture of the Day sites.
With the dosage commandline script you can get the latest strip
of webcomic, or catch-up to the last strip downloaded, or
download a strip for a particular date/index (except if the
webcomic's site layout makes this impossible).

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install --root=%{buildroot} --prefix=%{_prefix}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%files
%doc doc/changelog.txt doc/dosage.txt doc/README.txt
%_bindir/%name
%_mandir/man1/*
%python2_sitelib/%{name}lib*
%python2_sitelib/*egg-info
%python2_sitelib/_dosage*

%changelog
* Tue Apr 19 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.15
- Rebuild for Fedora
* Wed Sep 10 2014 Nikolay A. Fetisov <naf@altlinux.ru> 2.15-alt1
- New version 2.15
* Wed Feb 26 2014 Nikolay A. Fetisov <naf@altlinux.ru> 2.12-alt1
- New version 2.12
* Sun Dec 01 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.7-alt1
- New version 2.7
* Sat Aug 10 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.5-alt1
- New version 2.5
* Sat Jun 29 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.4-alt1
- New version 2.4
* Sun Jun 09 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.3-alt1
- New version 2.3
* Sun May 19 2013 Nikolay A. Fetisov <naf@altlinux.ru> 2.2-alt1
- New version 2.2
* Fri Jan 04 2013 Nikolay A. Fetisov <naf@altlinux.ru> 1.8-alt1
- Initial build for ALT Linux Sisyphus
