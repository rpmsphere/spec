Name:           js-jquery-ui
URL:            http://jqueryui.com/
Summary:        jQuery User Interface
Version:        1.11.3
Release:        4.1
License:        MIT or GPLv2+
Group:          Productivity/Networking/Web/Utilities
Source:         https://github.com/downloads/jquery/jquery-ui/jquery-ui-%{version}.zip
BuildArch:      noarch
BuildRequires:  web-assets-devel
Requires:       js-jquery1
Requires:       web-assets-filesystem

%description 
jQuery UI is a curated set of user interface interactions, effects, widgets,
and themes built on top of the jQuery JavaScript Library. Whether you're
building highly interactive web applications or you just need to add a date
picker to a form control, jQuery UI is the perfect choice.

%prep
%setup -q -n jquery-ui-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/javascript/jquery-ui
cp -a * $RPM_BUILD_ROOT%{_datadir}/javascript/jquery-ui

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/javascript/jquery-ui

%changelog
* Fri Feb 13 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.11.3
- Rebuild for Fedora
