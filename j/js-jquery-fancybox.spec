Name:           js-jquery-fancybox
URL:            https://fancybox.net/
Summary:        Javascript tool for displaying images
Version:        1.3.4
Release:        2.1
License:        MIT or GPLv2+
Group:          Productivity/Networking/Web/Utilities
Source:         https://fancybox.googlecode.com/files/jquery.fancybox-%{version}.zip
BuildArch:      noarch
BuildRequires:  web-assets-devel
Requires:       js-jquery1
Requires:       web-assets-filesystem

%description 
FancyBox is a tool for displaying images, html content and multi-media
in a Mac-style "lightbox" that floats overtop of web page.

%prep
%setup -n jquery.fancybox-%version
cd fancybox
find -type f -print0 | xargs -0 chmod 644

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/javascript/jquery-fancybox
cd fancybox
for i in jquery.{easing,fancybox,mousewheel}-{1.3,%version,3.0.4}.{pack.js,css}; do
	test -e "$i" || continue
	sfx=${i##*.}
	pfx=${i%%-*}
	ln -s "$i" "$pfx.$sfx"
done
cp -a * $RPM_BUILD_ROOT%{_datadir}/javascript/jquery-fancybox

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/javascript/jquery-fancybox

%changelog
* Sun Sep 02 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.4
- Rebuilt for Fedora
* Sun Jun  5 2011 Ludwig Nussel <lnussel@suse.de>
- new package version 1.3.4
