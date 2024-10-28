Name:           js-jquery-selectBox
URL:            https://github.com/claviska/jquery-selectBox
Summary:        A styleable replacement for SELECT elements
Version:        1.1.4
Release:        3.1
License:        MIT or GPLv2+
Group:          Productivity/Networking/Web/Utilities
Source:         claviska-jquery-selectBox-v1.1.4-0-g1114755.zip
BuildArch:      noarch
BuildRequires:  web-assets-devel
Requires:       js-jquery1
Requires:       web-assets-filesystem

%description 
A jQuery plugin for replacing <select> elements.

%prep
%setup -n claviska-jquery-selectBox-1114755

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/javascript/jquery-selectBox
cp -a * $RPM_BUILD_ROOT%{_datadir}/javascript/jquery-selectBox

%files
%{_datadir}/javascript/jquery-selectBox

%changelog
* Sun Oct 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.4
- Rebuilt for Fedora
