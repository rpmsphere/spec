Name:           js-jquery-lightbox
URL:            https://lokeshdhakar.com/projects/lightbox2/
Summary:        Javascript used to overlay images on a web page
Version:        2.51
Release:        2.1
License:        Creative Commons Attribution 2.5
Group:          Productivity/Networking/Web/Utilities
Source:         https://lokeshdhakar.com/projects/lightbox2/releases/lightbox%{version}.zip
BuildArch:      noarch
BuildRequires:  web-assets-devel
Requires:       js-jquery1
Requires:       web-assets-filesystem

%description 
Lightbox is a simple, unobtrusive script used to overlay images on
the current page. It's a snap to setup and works on all modern
browsers.

%prep
%setup -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/javascript/jquery-lightbox
cp -a . $RPM_BUILD_ROOT%{_datadir}/javascript/jquery-lightbox

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/javascript/jquery-lightbox

%changelog
* Sun Sep 02 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.51
- Rebuilt for Fedora
* Tue Aug 11 2009 Ludwig Nussel <lnussel@suse.de>
- initial package version 2.04 with patches
